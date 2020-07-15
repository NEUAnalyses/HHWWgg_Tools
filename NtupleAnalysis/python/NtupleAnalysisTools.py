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

def PlotDataMC(dataFiles_,mcFiles_,signalFiles_,dataDirec_,mcDirec_,signalDirec_,drawPads_,Lumi_,SigScale_,ol_,log_,Tags_,VarBatch_,CutsType_,verbose_,noQCD_):
    print"Plotting Data / MC"
    gROOT.ProcessLine("gErrorIgnoreLevel = kError") # kPrint, kInfo, kWarning, kError, kBreak, kSysError, kFatal
    gStyle.SetOptStat(0)    
    gStyle.SetErrorX(0.0001)
    HHWWggTags = []
    for t in Tags_:
        HHWWggTags.append(t)
    cuts, cutNames = GetCuts(CutsType_)
    ##-- if var batch is loose, need separate titles for variables since it will be sum of vars * bools 
    if(VarBatch_ == "Loose"):
        finalStateVars, varNames = GetVars(VarBatch_) # get vars from var batch 
        print"finalStateVars = ",finalStateVars 
        print"varNames = ",varNames
    else: finalStateVars = GetVars(VarBatch_) # get vars from var batch 
    print"cuts:",cuts
    print"cutNames:",cutNames
    if(verbose_): print"vars:",finalStateVars   

    ##-- For each data file (can just be one)
    for dF_ in dataFiles_:
        cutBatchTag_pairs = [] 
        dataNevents_list = []
        MC_names = [] 
        MC_Nevents_lists = []
        MC_Nevents_noweight_lists = []

        ##-- For each category (Ex: HHWWggTag_0, HHWWggTag_1, HHWWggTag_2, combined)
        for itag,HHWWggTag in enumerate(HHWWggTags):
            if(verbose_): 
                print"tag:",HHWWggTag                      
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

            ##-- For each cut 
            for ic,cut in enumerate(cuts):                
                print"Plotting with selection:",cut                  
                cutName = cutNames[ic]
                cutBatchTag = "%s_%s"%(cutName,HHWWggTag)
                cutBatchTag_pairs.append(cutBatchTag)
                dataNevents = -999
                these_MC_Nevents = []
                these_MC_Nevents_noweights = [] 
                outputFolder = "%s/%s"%(ol_,cutName)
                if(not os.path.exists(outputFolder)):
                    os.system('mkdir %s'%(outputFolder))
                    os.system('cp %s/index.php %s'%(ol_,outputFolder))
                MC_CUT += "*(%s)"%(cut)
                DATA_CUT += "*(%s)"%(cut)      
                SIGNAL_CUT += "*(%s)"%(cut) 

                ##-- For each variable 
                for iv,v in enumerate(finalStateVars): 
                    if(VarBatch_ == "Loose"): varTitle = varNames[iv]
                    else: varTitle = GetVarTitle(v)
                    
                    if(verbose_): print"Plotting variable:",varTitle

                    MC_CUT = MC_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
                    DATA_CUT = DATA_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
                    SIGNAL_CUT = SIGNAL_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
                    MC_CUT_NOWEIGHT = MC_WEIGHT.replace(MC_WEIGHT,"(1)")      

                    if(varTitle == "weight"): MC_CUT = MC_CUT.replace(MC_WEIGHT,"(1)") # if you want to plot the "weight" variable, you should not scale it by weight!             
                    
                    if(verbose_): 
                        print"MC_CUT:",MC_CUT         
                        print"DATA_CUT:",DATA_CUT                   
                    legend = TLegend(0.55,0.65,0.89,0.89)
                    legend.SetTextSize(0.025)
                    legend.SetBorderSize(0)
                    legend.SetFillStyle(0)
                    xbins, xmin, xmax = GetBins(varTitle)

                    ##-- Fill histogram with data  
                    Data_h_tmp = TH1F('Data_h_tmp',varTitle,xbins,xmin,xmax)
                    Data_h_tmp.SetTitle("%s"%(varTitle))
                    Data_h_tmp.SetMarkerStyle(8)
                    exec('ch.Draw("%s >> Data_h_tmp","%s")'%(v,DATA_CUT))

                    ##-- Only save number of events for first variable. Should be same for all because same cut is used 
                    if(iv == 0): 
                        dataNevents = Data_h_tmp.GetEntries()
                        dataNevents_list.append(dataNevents)
                    # print"Blinded Data numEvents:",Data_h_tmp.GetEntries()                    
                    DataHist = Data_h_tmp.Clone("DataHist")
                    DataHist.SetDirectory(0)
                    legend.AddEntry(DataHist,"Data","P")

                    ##-- Get histograms with MC Backgrounds 
                    bkgStack = THStack("bkgStack","bkgStack")
                    histos = []
                    histCategories = [] 
                    for i,mcF_ in enumerate(mcFiles_):
                        mcPath = "%s/%s"%(mcDirec_,mcF_)
                        mcFile = TFile.Open(mcPath)
                        treeName = GetMCTreeName(mcF_)
                        MC_Category = GetMCCategory(mcF_)
                        if(verbose_): 
                            # print"Background File:",mcPath
                            print"Background:",MC_Category

                        ##-- If noQCD set to true, skip QCD for Tag_0 and Tag_1 
                        if(MC_Category == "QCD") and (noQCD_) and (HHWWggTag == "HHWWggTag_0" or HHWWggTag == "HHWWggTag_1"): 
                            print"Skipping QCD"
                            these_MC_Nevents_noweights.append(0) # Set yields to 0 for table 
                            these_MC_Nevents.append(0) # Set yields to 0 for table 
                            if(itag == 0 and ic == 0 and iv == 0): 
                                MCname = GetMCName(mcF_)
                                MC_names.append(MCname) # Skipping QCD, but still save name for yields because tag_2 may not be 0                           
                            continue 

                        ##-- Define TChain based on categories 
                        if(HHWWggTag=="combined"):
                            mc_ch = TChain('tagsDumper/trees/%s_13TeV_HHWWggTag_0'%(treeName))
                            mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_0"%(mcPath,treeName))
                            mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_1"%(mcPath,treeName))
                            mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_2"%(mcPath,treeName))
                        else:
                            mc_ch = TChain('tagsDumper/trees/%s_13TeV_%s'%(treeName,HHWWggTag))
                            mc_ch.Add(mcPath)
                        xbins, xmin, xmax = GetBins(varTitle)
                        if(verbose_): 
                            print"tag:",HHWWggTag
                        exec("MC_h_tmp_%s = TH1F('MC_h_tmp_%s',varTitle,xbins,xmin,xmax)"%(i,i))
                        exec("MC_h_tmp_noweight_%s = TH1F('MC_h_tmp_noweight_%s',varTitle,xbins,xmin,xmax)"%(i,i))
                        thisHist = eval("MC_h_tmp_%s"%(i))
                        mcColor = GetMCColor(MC_Category)

                        ##-- If GJet or QCD sample, need to remove prompt-prompt events 
                        if(MC_Category == "GJet" or MC_Category == "QCD"):
                            if(verbose_): print"Remove prompt-prompt"
                            removePromptPromptCut = "(!((Leading_Photon_genMatchType == 1) && (Subleading_Photon_genMatchType == 1)))" # selection: remove events where both photons are prompt
                            original_MC_CUT = "%s"%(MC_CUT)
                            this_MC_CUT = "%s*(%s)"%(original_MC_CUT,removePromptPromptCut)
                            this_MC_CUT_NOWEIGHT = this_MC_CUT.replace(MC_WEIGHT,"(1)")

                        eval("MC_h_tmp_%s.SetFillColor(eval(mcColor))"%(i))
                        eval("MC_h_tmp_%s.SetLineColor(eval(mcColor))"%(i))
                        if(MC_Category == "GJet" or MC_Category == "QCD"): 
                            exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,this_MC_CUT))
                        else: 
                            exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,MC_CUT))                                           

                        eval("MC_h_tmp_%s.Scale(float(Lumi_))"%(i))

                        ##-- MC reweighting for HHWWgg backgrounds (turned off for now)
                        # reWeightVals = ReWeightMC(mcF_)
                        # doReWeight, reWeightScale = reWeightVals[0], reWeightVals[1]
                        # print"doReWeight,reWeightScale:",doReWeight, reWeightScale
                        # if(doReWeight): 
                        #     if(verbose_):
                        #         print"ReWeighting MC"
                        #         print"With scale: ",reWeightScale
                        #     eval("MC_h_tmp_%s.Scale(float(reWeightScale))"%(i))
                        ## 

                        ##-- Only save for 1st variable. Should be same for all variables
                        if(iv == 0): 
                            if(MC_Category == "GJet" or MC_Category == "QCD" ): exec('mc_ch.Draw("%s >> MC_h_tmp_noweight_%s","%s")'%(v,i,this_MC_CUT_NOWEIGHT))
                            else: exec('mc_ch.Draw("%s >> MC_h_tmp_noweight_%s","%s")'%(v,i,MC_CUT_NOWEIGHT))
                            these_MC_Nevents_noweights.append(eval("MC_h_tmp_noweight_%s.Integral()"%(i)))   
                            these_MC_Nevents.append(eval("MC_h_tmp_%s.Integral()"%(i)))
                            
                            ##-- Only need to get MC names once 
                            if(itag == 0 and ic == 0 and iv == 0): 
                                MCname = GetMCName(mcF_)
                                MC_names.append(MCname) # get shorter MC name here

                        newHist = thisHist.Clone("newHist")
                        ##-- Set title based on treeName 
                        newHist.SetTitle(MC_Category)
                        newHist.GetXaxis().SetTitle(mcF_)
                        newHist.SetDirectory(0)
                        histos.append(newHist)
                        histCategories.append(MC_Category)

                    sig_histos = []
                    sig_histCategories = []             

                    ##-- Add Signal to plots 
                    for i,sigF_ in enumerate(signalFiles_):
                        sigPath = "%s/%s"%(signalDirec_,sigF_)
                        sigFile = TFile.Open(sigPath)
                        treeName = GetMCTreeName(sigF_)
                        MC_Category = GetMCCategory(sigF_)
                        if(verbose_):
                            print"Signal File:",sigPath 
                            print"Signal:",MC_Category
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
                        ##-- Style options for signal to distinguish from Data, Background 
                        # eval("MC_h_tmp_%s.SetFillColor(eval(mcColor))"%(i))
                        # eval("MC_h_tmp_%s.SetFillStyle(3004)"%(i))
                        ##-- 
                        eval("MC_h_tmp_%s.SetFillColorAlpha(eval(mcColor),0.1)"%(i))
                        eval("MC_h_tmp_%s.SetLineColor(eval(mcColor))"%(i))
                        exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,SIGNAL_CUT))
                        eval("MC_h_tmp_%s.Scale(float(Lumi_))"%(i)) # should scale to luminosity by default 
                        SigXS_Scale = GetXScale("HHWWgg_v2-6") # how to scale the XS which is by default in flashgg 1fb
                        print("SigXS_Scale: ",SigXS_Scale)
                        eval("MC_h_tmp_%s.Scale(float(SigXS_Scale))"%(i)) # should scale to luminosity by default 
                        newHist = thisHist.Clone("newHist")

                        ##-- Set title based on treeName 
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
                        "WGJJ" : 0,
                        "ttW" : 0
                    }

                    Signals_AddedtoLegend = {
                        "HHWWgg_SM" : 0
                    }

                    ##-- Order histograms by MC category 
                    orderedHistos = OrderHistos(histos,histCategories)
                    sig_orderedHistos = OrderHistos(sig_histos,sig_histCategories)

                    ##-- Add backgrounds to background stack 
                    for h in orderedHistos:
                        bkgStack.Add(h,'hist')
                        bkgName = h.GetTitle()
                        added = MC_AddedtoLegend[bkgName]
                        if(added): continue 
                        else:
                            legend.AddEntry(h,bkgName,"F")
                            MC_AddedtoLegend[bkgName] = 1

                    ##-- By default draw background save background contributions. Later delete if not wanted 
                    outName = "%s/BackgroundsTest_%s.png"%(outputFolder,HHWWggTag)
                    bkgOutName = "%s/BackgroundsPADS_%s_%s.png"%(outputFolder,varTitle,HHWWggTag)
                    SimpleDrawHisto(bkgStack,"PADS",bkgOutName,varTitle)
                    bkgOutName = bkgOutName.replace(".png",".pdf")
                    SimpleDrawHisto(bkgStack,"PADS",bkgOutName,varTitle)  

                    ##-- Add text box with selection type 
                    offset = 0
                    selText = TLatex(0.129,0.85,cutName)
                    selText.SetNDC(1)
                    selText.SetTextSize(0.04)   
                    CatText = TLatex(0.129,0.8,HHWWggTag)
                    CatText.SetNDC(1)
                    CatText.SetTextSize(0.04)                                   
                    stackSum = bkgStack.GetStack().Last() #->Draw(); # for computing ratio 
                    stackSum.Sumw2() 
                    stackSum.SetLineColor(kBlack)
                    stackSum.SetLineStyle(7) # to distinguish from data uncertainty 
                    DataHist.SetLineColor(kBlack)
                    DataHist.Sumw2()
                    xTitle = GetXaxisTitle(varTitle)
                    DataHist.GetXaxis().SetTitle(xTitle)
                    if(log_): 
                        DataHist.SetMinimum(0.01)
                        stackSum.SetMinimum(0.01)
                        bkgStack.SetMinimum(0.01)
                        
                    ##-- Define ratio plot for computing Data / MC ratio 
                    rp = TRatioPlot(DataHist,stackSum)
                    rp.SetH1DrawOpt("P")
                    rp.SetH2DrawOpt("hist")
                    # rp.SetGraphDrawOpt("PE2")
                    dMax = DataHist.GetMaximum()
                    bMax = stackSum.GetMaximum()
                    maxHeight = max(dMax,bMax) 

                    ##-- Create the entire picture: Combine Data, MC, Data / MC ratio and signal in one plot 

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

                        ratioGraph = rp.GetCalculationOutputGraph()
                        ratioGraph.SetMarkerStyle(8)
                        ratioGraph.SetMarkerSize(0.5)

                        # rp.SetGraphDrawOpt("EP")
                        # rp.SetGraphDrawOpt("EPZ2")
                        # rp.GetLowerRefYaxis().SetTitle("Data / MC")

                        rp.GetUpperRefYaxis().SetTitle("Entries")   
                        rp.GetLowerRefYaxis().SetTitle("Data / MC")
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

                            ##-- No user input signal scale 
                            print("user sig scale:",SigScale_)
                            if(SigScale_ == -999): 
                                sigScale = (float(maxHeight)/10.) / float(sigMax) # in order to scale signal to 10th of max of plot 
                                sig_hist.Scale(sigScale)  

                            ##-- User input signal scale 
                            else:
                                sigScale = SigScale_
                                sig_hist.Scale(sigScale) 
                                                        
                            for sig_h in sig_orderedHistos:
                                # sigName = "%s X %d"%(sig_h.GetTitle(),sigScale)
                                sigName = sig_h.GetTitle()
                                added = Signals_AddedtoLegend[sigName]
                                if(added): continue 
                                else:
                                    legend.AddEntry(sig_h,"%s * %.5g"%(sig_h.GetTitle(),sigScale),"FL")
                                    Signals_AddedtoLegend[sigName]                            
                            sig_hist.Draw("samehist")
                        legend.Draw("same")
                        selText.Draw("same")
                        CatText.Draw("same")
                        rp.GetLowerRefGraph().SetMinimum(0.5)
                        rp.GetLowerRefGraph().SetMaximum(1.5)     
                        Npoints = rp.GetLowerRefGraph().GetN()
                        for ip in range(0,Npoints):
                            rp.GetLowerRefGraph().SetPointEXhigh(ip,0)  
                            rp.GetLowerRefGraph().SetPointEXlow(ip,0)  
                        if(log_): 
                            UpperPad.SetLogy()
                            UpperPad.Update() 
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

                MC_Nevents_lists.append(these_MC_Nevents)
                MC_Nevents_noweight_lists.append(these_MC_Nevents_noweights)  

        ##-- Produce table with number of events for each MC, total MC, and data 
        CreateYieldsTables(cutBatchTag_pairs,dataNevents_list,MC_names,MC_Nevents_lists,MC_Nevents_noweight_lists,ol_)