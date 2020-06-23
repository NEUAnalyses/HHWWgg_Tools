###########################################################################################################################
# Abraham Tishelman-Charny
# 13 May 2020
#
# The purpose of this module is to provide variables and definitions for NtupleAnalysis.py 
#
###########################################################################################################################

from ROOT import TCanvas, gROOT, gPad, TH1F, TFile, TChain, TPaveStats, gStyle, THStack, kBlue, kCyan, kRed, kGreen, TLegend, TRatioPlot, kBlack, TLine, kPink, TLatex, kOrange, gErrorIgnoreLevel, kWarning
import os 
import tdrstyle
from MCTools import * 
from VariableTools import * 
from PlotTools import * 
from CutsTools import * 
    
def CalcEff(h_,cut_):
    ##-- return percentage of events that pass cut 
    pctPass_ = 0
    numPass = 0 
    N = h_.GetEntries()
    nBins = h_.GetNbinsX()
    for ix,y in enumerate(h_):
        if ix == 0: continue # skip underflow bin 
        elif ix == nBins + 1: break # skip overflow bin 
        x = h_.GetBinLowEdge(ix)
        if x < cut_: numPass += y # if the x value of the bin is less than the cut, all jets pass 
        elif x >= cut_: break # if the x value of the bin is greater than or equal to the cut, no more jets will pass 
    pctPass_ = float(numPass) / float(N)
    return pctPass_ 

def PlotDataMC(dataFiles_,mcFiles_,signalFiles_,dataDirec_,mcDirec_,signalDirec_,drawPads_,Lumi_,SigScale_,ol_,log_,Tags_,VarBatch_,CutsType_,verbose_):
    print"Plotting Data / MC"
    gROOT.ProcessLine("gErrorIgnoreLevel = kError") # kPrint, kInfo, kWarning, kError, kBreak, kSysError, kFatal
    gStyle.SetOptStat(0)    
    gStyle.SetErrorX(0.0001)
    HHWWggTags = []
    for t in Tags_:
        HHWWggTags.append(t)
    # if(ShortCutsList_): 
        # cuts = ["1"]
        # cutNames = ["PreSelections"]
    cuts, cutNames = GetCuts(CutsType_)
    finalStateVars = GetVars(VarBatch_) # get certain vars based on cut 
    print"cuts:",cuts
    print"cutNames:",cutNames
    if(verbose_): print"vars:",finalStateVars         
    for dF_ in dataFiles_:
        for HHWWggTag in HHWWggTags:
            dPath = "%s/%s"%(dataDirec_,dF_)
            dFile = TFile.Open(dPath)
            if(HHWWggTag=="combined"):
                ch = TChain('tagsDumper/trees/Data_13TeV_HHWWggTag_0')
                ch.Add("%s/tagsDumper/trees/Data_13TeV_HHWWggTag_0"%(dPath))
                ch.Add("%s/tagsDumper/trees/Data_13TeV_HHWWggTag_1"%(dPath))
                ch.Add("%s/tagsDumper/trees/Data_13TeV_HHWWggTag_2"%(dPath))
            else:
                ch = TChain('tagsDumper/trees/Data_13TeV_%s'%(HHWWggTag))
                ch.Add(dPath)
            BLIND_CUT = "(CMS_hgg_mass < 115 || CMS_hgg_mass > 135)"
            MC_WEIGHT = "1*weight"
            ZERO_CUT = "ZERO_CUT"
            MC_CUT = "%s*(%s)*(%s)"%(MC_WEIGHT,BLIND_CUT,ZERO_CUT)
            DATA_CUT = "%s*(%s)"%(BLIND_CUT,ZERO_CUT)       
            SIGNAL_CUT = "%s*(%s)"%(MC_WEIGHT,ZERO_CUT) # no blind cut on signal 

            for ic,cut in enumerate(cuts):
                print"Plotting with selection:",cut 
                cutName = cutNames[ic]
                outputFolder = "%s/%s"%(ol_,cutName)
                if(not os.path.exists(outputFolder)):
                    os.system('mkdir %s'%(outputFolder))
                    os.system('cp %s/index.php %s'%(ol_,outputFolder))
                MC_CUT += "*(%s)"%(cut)
                DATA_CUT += "*(%s)"%(cut)      
                SIGNAL_CUT += "*(%s)"%(cut) 
                for v in finalStateVars: 
                    varTitle = GetVarTitle(v)
                    print"Plotting variable:",varTitle
                    MC_CUT = MC_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
                    DATA_CUT = DATA_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
                    SIGNAL_CUT = SIGNAL_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
                    if(verbose_): 
                        print"MC_CUT:",MC_CUT         
                        print"DATA_CUT:",DATA_CUT                   
                    legend = TLegend(0.55,0.65,0.89,0.89)
                    legend.SetTextSize(0.025)
                    legend.SetBorderSize(0)
                    legend.SetFillStyle(0)
                    xbins, xmin, xmax = GetBins(varTitle)
                    ##-- Get Data 
                    # print"xbins xmin xmax",xbins, xmin, xmax 
                    Data_h_tmp = TH1F('Data_h_tmp',varTitle,xbins,xmin,xmax)
                    Data_h_tmp.SetTitle("%s"%(varTitle))
                    Data_h_tmp.SetMarkerStyle(8)
                    exec('ch.Draw("%s >> Data_h_tmp","%s")'%(v,DATA_CUT))
                    if(verbose_): 
                        print"tag:",HHWWggTag
                        # print"numEvents:",Data_h_tmp.GetEntries()                    
                    DataHist = Data_h_tmp.Clone("DataHist")
                    DataHist.SetDirectory(0)
                    legend.AddEntry(DataHist,"Data","P")

                    ##-- Get MC Backgrounds 
                    bkgStack = THStack("bkgStack","bkgStack")
                    histos = []
                    histCategories = [] 
                    for i,mcF_ in enumerate(mcFiles_):
                        mcPath = "%s/%s"%(mcDirec_,mcF_)
                        mcFile = TFile.Open(mcPath)
                        # print"Background File:",mcPath
                        treeName = GetMCTreeName(mcF_)
                        MC_Category = GetMCCategory(mcF_)
                        if(verbose_): print"Background:",MC_Category
                        ##-- If HHWWgg_bkg, need to multiply by another weight 
                        ##-- MC_WEIGHT = "%s*%s"%(MC_WEIGHT,HHWWgg_MC_Weight)
                        if(HHWWggTag=="combined"):
                            mc_ch = TChain('tagsDumper/trees/%s_13TeV_HHWWggTag_0'%(treeName))
                            mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_0"%(mcPath,treeName))
                            mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_1"%(mcPath,treeName))
                            mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_2"%(mcPath,treeName))
                        else:
                            mc_ch = TChain('tagsDumper/trees/%s_13TeV_%s'%(treeName,HHWWggTag))
                            mc_ch.Add(mcPath)
                        xbins, xmin, xmax = GetBins(varTitle)
                        # print"tag:",HHWWggTag
                        # print"numEvents:",mc_ch.GetEvents()                        
                        # print"xbins xmin xmax",xbins, xmin, xmax 
                        exec("MC_h_tmp_%s = TH1F('MC_h_tmp_%s',varTitle,xbins,xmin,xmax)"%(i,i))
                        thisHist = eval("MC_h_tmp_%s"%(i))
                        mcColor = GetMCColor(MC_Category)
                        # print"mcColor:",mcColor

                        if(MC_Category == "GJet" or MC_Category == "QCD"):
                            # print"Remove prompt-prompt"
                            removePromptPromptCut = "(!((Leading_Photon_genMatchType == 1) && (Subleading_Photon_genMatchType == 1)))" # selection: not true that both photons are prompt
                            removePromptPromptCut += "*(!((Leading_Photon_genMatchType == 0) || (Subleading_Photon_genMatchType == 0)))" # selection: not true that both photons are prompt
                            original_MC_CUT = "%s"%(MC_CUT)
                            this_MC_CUT = "%s*(%s)"%(original_MC_CUT,removePromptPromptCut)
                            # print"this_MC_CUT:",this_MC_CUT                     

                        eval("MC_h_tmp_%s.SetFillColor(eval(mcColor))"%(i))
                        eval("MC_h_tmp_%s.SetLineColor(eval(mcColor))"%(i))
                        if(MC_Category == "GJet" or MC_Category == "QCD"): exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,this_MC_CUT))
                        else: exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,MC_CUT))
                        eval("MC_h_tmp_%s.Scale(float(Lumi_))"%(i))
                        ##-- Check if MC should be reweighted
                        reWeightVals = ReWeightMC(mcF_)
                        doReWeight, reWeightScale = reWeightVals[0], reWeightVals[1]
                        # print"doReWeight,reWeightScale:",doReWeight, reWeightScale
                        if(doReWeight):
                            if(verbose_):
                                print"ReWeighting MC"
                                print"With scale: ",reWeightScale
                            eval("MC_h_tmp_%s.Scale(float(reWeightScale))"%(i))
                        
                        newHist = thisHist.Clone("newHist")
                        # set title based on treeName 
                        newHist.SetTitle(MC_Category)
                        newHist.GetXaxis().SetTitle(mcF_)
                        newHist.SetDirectory(0)
                        histos.append(newHist)
                        histCategories.append(MC_Category)

                    sig_histos = []
                    sig_histCategories = []             

                    ##-- Add Signal 
                    for i,sigF_ in enumerate(signalFiles_):
                        sigPath = "%s/%s"%(signalDirec_,sigF_)
                        sigFile = TFile.Open(sigPath)
                        # print"Signal File:",sigPath
                        treeName = GetMCTreeName(sigF_)
                        MC_Category = GetMCCategory(sigF_)
                        if(verbose_): print"Signal:",MC_Category
                        ##-- If HHWWgg_bkg, need to multiply by another weight 
                        ##-- MC_WEIGHT = "%s*%s"%(MC_WEIGHT,HHWWgg_MC_Weight)
                        if(HHWWggTag=="combined"):
                            mc_ch = TChain('tagsDumper/trees/%s_13TeV_HHWWggTag_0'%(treeName))
                            mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_0"%(sigPath,treeName))
                            mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_1"%(sigPath,treeName))
                            mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_2"%(sigPath,treeName))
                        else:
                            mc_ch = TChain('tagsDumper/trees/%s_13TeV_%s'%(treeName,HHWWggTag))
                            mc_ch.Add(sigPath)
                        xbins, xmin, xmax = GetBins(varTitle)
                        exec("MC_h_tmp_%s = TH1F('MC_h_tmp_%s',v,xbins,xmin,xmax)"%(i,i))
                        thisHist = eval("MC_h_tmp_%s"%(i))
                        mcColor = GetMCColor(MC_Category) 
                        # eval("MC_h_tmp_%s.SetFillColor(eval(mcColor))"%(i))
                        # eval("MC_h_tmp_%s.SetFillStyle(3004)"%(i))
                        eval("MC_h_tmp_%s.SetFillColorAlpha(eval(mcColor),0.1)"%(i))
                        eval("MC_h_tmp_%s.SetLineColor(eval(mcColor))"%(i))
                        exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,SIGNAL_CUT))
                        # eval("MC_h_tmp_%s.Scale(float(Lumi_))"%(i))
                        # eval("MC_h_tmp_%s.Scale(float(SigScale_))"%(i))
                        newHist = thisHist.Clone("newHist")

                        # set title based on treeName 
                        newHist.SetTitle(MC_Category)
                        newHist.GetXaxis().SetTitle(sigF_)
                        newHist.SetLineStyle(1)
                        newHist.SetLineWidth(5)

                        newHist.SetDirectory(0)
                        sig_histos.append(newHist)
                        sig_histCategories.append(MC_Category)              
                        
                    MC_AddedtoLegend = {
                        "QCD" : 0,
                        "SMhgg" : 0,
                        "GJet" : 0,
                        "DiPhoJets" : 0,
                        "DiPhoJetsBox" : 0,
                        # "W1JetsToLNu" : 0,
                        # "W2JetsToLNu" : 0,
                        # "W3JetsToLNu" : 0,
                        # "W4JetsToLNu" : 0,
                        "WJets" : 0,
                        "WW" : 0,
                        "tt" : 0,
                        "DY" : 0,
                        "WGGJets" : 0,
                        "ttW" : 0
                    }

                    Signals_AddedtoLegend = {
                        "HHWWgg_SM" : 0
                    }

                    # order histograms by MC category 
                    orderedHistos = OrderHistos(histos,histCategories)
                    sig_orderedHistos = OrderHistos(sig_histos,sig_histCategories)

                    # for h in histos:
                    for h in orderedHistos:
                        bkgStack.Add(h,'hist')
                        bkgName = h.GetTitle()
                        added = MC_AddedtoLegend[bkgName]
                        if(added): continue 
                        else:
                            legend.AddEntry(h,bkgName,"F")
                            MC_AddedtoLegend[bkgName] = 1

                    for sig_h in sig_orderedHistos:
                        sigName = sig_h.GetTitle()
                        added = Signals_AddedtoLegend[sigName]
                        if(added): continue 
                        else:
                            legend.AddEntry(sig_h,sigName,"FL")
                            Signals_AddedtoLegend[sigName]

                    outName = "%s/BackgroundsTest_%s.png"%(outputFolder,HHWWggTag)
                    bkgOutName = "%s/BackgroundsPADS_%s_%s.png"%(outputFolder,varTitle,HHWWggTag)
                    SimpleDrawHisto(bkgStack,"PADS",bkgOutName,varTitle)
                    bkgOutName = bkgOutName.replace(".png",".pdf")
                    SimpleDrawHisto(bkgStack,"PADS",bkgOutName,varTitle)  
                    ##-- Add text box with selection type 
                    offset = 0
                    # selText = TLatex(0.129+0.03+offset,0.85,cutName)
                    selText = TLatex(0.129,0.85,cutName)
                    selText.SetNDC(1)
                    selText.SetTextSize(0.04)   
                    # combinedText = TLatex(0.129,0.8,"Combined Cats")
                    CatText = TLatex(0.129,0.8,HHWWggTag)
                    CatText.SetNDC(1)
                    CatText.SetTextSize(0.04)                                   
                    # selText.SetTextAlign(33)
                    # selText.SetNDC(1)
                    # selText.SetTextSize(0.045)   
                    stackSum = bkgStack.GetStack().Last() #->Draw(); # for computing ratio 
                    stackSum.SetLineColor(kBlack)
                    stackSum.SetLineStyle(7) # to distinguish from data uncertainty 
                    DataHist.SetLineColor(kBlack)
                    xTitle = GetXaxisTitle(varTitle)
                    DataHist.GetXaxis().SetTitle(xTitle)
                    if(log_): 
                        DataHist.SetMinimum(0.01)
                        stackSum.SetMinimum(0.01)
                        bkgStack.SetMinimum(0.01)
                    rp = TRatioPlot(DataHist,stackSum)
                    rp.SetH1DrawOpt("P")
                    rp.SetH2DrawOpt("hist")
                    # rp.SetGraphDrawOpt("PE2")
                    dMax = DataHist.GetMaximum()
                    bMax = stackSum.GetMaximum()
                    # print'dMax:',dMax
                    # print'bMax:',bMax
                    maxHeight = max(dMax,bMax)

                    for fileType in ["pdf"]:
                        gStyle.SetErrorX(0.0001)
                        # varTitle = GetVarTitle(v)
                        outName = "%s/DataMC_%s_%s.%s"%(outputFolder,varTitle,HHWWggTag,fileType)
                        if(log_): outName = "%s/DataMC_%s_%s_log.%s"%(outputFolder,varTitle,HHWWggTag,fileType)
                        else: outName = "%s/DataMC_%s_%s_nonLog.%s"%(outputFolder,varTitle,HHWWggTag,fileType)                        
                        DataMCRatio_c = TCanvas("DataMCRatio_c","DataMCRatio_c",600,800)
                        rp.Draw("nogrid")
                        rp.GetLowYaxis().SetNdivisions(5)
                        DataMCRatio_c.Update()

                        # yaxis = rp.GetLowerRefGraph().GetYaxis()
                        # print"n divisions:",yaxis.GetNdivisions()
                        # yaxis.SetNdivisions(3)
                        # print"n divisions:",yaxis.GetNdivisions()

                        ratioGraph = rp.GetCalculationOutputGraph()
                        ratioGraph.SetMarkerStyle(8)
                        ratioGraph.SetMarkerSize(0.5)

                        # rp.SetGraphDrawOpt("EP")
                        # rp.SetGraphDrawOpt("EPZ2")
                        # rp.GetLowerRefYaxis().SetTitle("Data / MC")

                        # yaxis.SetNdivisions(2)   
                        # print"offset:",rp.GetLowerRefYaxis().GetTitleOffset()
                        # rp.GetUpperRefYaxis().SetTitleOffset(-0.0000001)
                        # print"offset",rp.GetUpperRefYaxis().GetTitleOffset()
                        rp.GetUpperRefYaxis().SetTitle("Entries")   
                        rp.GetLowerRefYaxis().SetTitle("Data / MC")
                        # rp.GetLowerRefXaxis().SetTitle("testTitle")
                        rp.GetLowerPad().Update()
                        if(log_): rp.GetUpperRefYaxis().SetRangeUser(0.1,maxHeight*100.)   
                        else: rp.GetUpperRefYaxis().SetRangeUser(0,maxHeight*1.3)
                                
                        UpperPad = rp.GetUpperPad()
                        UpperPad.cd()
                        bkgStack.Draw("same")
                        stackSum.Draw("sameE")
                        DataHist.Draw("samePE")
                        for sig_hist in sig_histos:
                            sigMax = sig_hist.GetMaximum()
                            if sigMax == 0: sigMax = 1 
                            sigScale = float(maxHeight) / float(sigMax)
                            sig_hist.Scale(sigScale)
                            sig_hist.Draw("samehist")
                        legend.Draw("same")
                        selText.Draw("same")
                        CatText.Draw("same")
                        rp.GetLowerRefGraph().SetMinimum(0.5)
                        rp.GetLowerRefGraph().SetMaximum(1.5)     
                        # rp.GetLowerRefGraph().GetXaxis().SetTitle("testTitle")                
                        Npoints = rp.GetLowerRefGraph().GetN()
                        for ip in range(0,Npoints):
                            rp.GetLowerRefGraph().SetPointEXhigh(ip,0)  
                            rp.GetLowerRefGraph().SetPointEXlow(ip,0)  
                        if(log_): 
                            UpperPad.SetLogy()
                            UpperPad.Update() 
                            # don't know why this removes Data / MC title   
                        rp.GetLowerPad().cd()
                        lowerPad = rp.GetLowerPad()
                        rp.GetLowerRefYaxis().SetTitle("Data / MC")
                        lineAtOne = TLine(lowerPad.GetUxmin(),1,lowerPad.GetUxmax(),1)
                        lineAtOne.SetLineStyle(3)
                        lineAtOne.Draw("same")
                        rp.GetLowerPad().Update()                        
                        DataMCRatio_c.Update()                
                        DataMCRatio_c.SaveAs(outName) 
                        outName = outName.replace(".pdf",".png")                    
                        DataMCRatio_c.SaveAs(outName)                     
                    if(not drawPads_):
                        bkgOutName = "%s/BackgroundsPADS_%s_%s.png"%(outputFolder,varTitle,HHWWggTag)
                        os.system('rm %s'%(bkgOutName))
                        bkgOutName = bkgOutName.replace(".png",".pdf")
                        os.system('rm %s'%(bkgOutName))
                    MC_CUT = MC_CUT.replace("(%s != 0) && (%s != -999)"%(v,v),"ZERO_CUT")
                    DATA_CUT = DATA_CUT.replace("(%s != 0) && (%s != -999)"%(v,v),"ZERO_CUT")