from ROOT import *
import argparse
from array import array

parser = argparse.ArgumentParser()
parser.add_argument("-p","--plot", action="store_true", default=False, help="Plot", required=False)
parser.add_argument("-n","--norm", action="store_true", default=False, help="normalize plots", required=False)
parser.add_argument("-df","--df", action="store_true", default=False, help="deep flavour b score", required=False)
parser.add_argument("-csv","--dcsv", action="store_true", default=False, help="deep csv b score", required=False)
args = parser.parse_args()

def Draw_Histogram(h_,opt_,fn_):
    c_tmp = TCanvas('c_tmp','c_tmp',1300,800)
    h_.Draw(opt_)
    c_tmp.SaveAs(fn_)
    return 

def MakeEffPlot(tree_, Note_,ol_, Note2_, SL_channel):
    print"Computing efficiency for: %s"%(Note_)
    if(Note_=="SL"): 
        print"Semi-Leptonic channel: ",SL_channel    
    # print"tree:",tree_
    n = 100
    x, y = array( 'd' ), array( 'd' )    
    cuts = [i*0.01 for i in range(1,101)]
    N_tot_Entries = tree_.GetEntries()

    PHOTON_CUTS = "( (Leading_Photon_pt / CMS_hgg_mass) > 0.33 ) && ( (Subleading_Photon_pt / CMS_hgg_mass) > 0.25 )"
    LUMI = "41.5"
    SIGNAL_SCALE = "1"
    CHANNEL_SELECTION = "1"
    if(Note_=="SL"): 
        if(SL_channel=="Electron"): 
            SIGNAL_SCALE = "(31.049*0.00097)*(0.441)" ##-- add lepton flavor selection 
            CHANNEL_SELECTION = "(N_goodElectrons==1)"
        elif(SL_channel=="Muon"): 
            SIGNAL_SCALE = "(31.049*0.00097)*(0.441)"
            CHANNEL_SELECTION = "(N_goodMuons==1)"
        
    if(Note_=="FH"): SIGNAL_SCALE = "(31.049*0.00097)*(0.454)"
    if(Note_=="FL"): SIGNAL_SCALE = "(31.049*0.00097)*(0.107)"

    ##-- Compute integral with all events once for denominator 
    h_tmp_all = TH1F("h_tmp_all","h_tmp_all",20,115,135)
    tree_.Draw("CMS_hgg_mass >> h_tmp_all","1*weight*(%s)*(%s)*(%s)*(%s)"%(LUMI,SIGNAL_SCALE,PHOTON_CUTS,CHANNEL_SELECTION))
    total_weighed_entries = h_tmp_all.Integral()
    print"total_weighed_entries in signal region:",total_weighed_entries

    for icut,cut in enumerate(cuts):
        x.append(cut)
        condition = ""
        maxJets = 5
        h_tmp = TH1F("h_tmp","h_tmp",20,115,135) ##-- signal region 
        for jet_i in range(0,maxJets):
            scoreFormat = "goodJets_%s_bDiscriminator_mini_pfDeepFlavourJetTags_prob"%(jet_i)
            variable = "(%s%s + %s%s + %s%s < %s)"%(scoreFormat,"b",scoreFormat,"bb",scoreFormat,"lepb",cut)
            condition += variable
            if jet_i == maxJets-1: break 
            else: condition += " && "
        
        tree_.Draw("CMS_hgg_mass >> h_tmp","(%s)*weight*(%s)*(%s)*(%s)*(%s)"%(condition,LUMI,SIGNAL_SCALE,PHOTON_CUTS,CHANNEL_SELECTION))
        tmp_integral = h_tmp.Integral()
        N_weighted_entries_pass = tmp_integral
        eff = float(N_weighted_entries_pass) / float(total_weighed_entries)
        y.append(eff)
        del h_tmp 

    eff_g = TGraph(n,x,y)
    eff_g.SetMarkerStyle( 21 )
    eff_g.SetTitle( '%s %s Efficiency vs. b Score Threshold'%(Note2_, Note_) )
    eff_g.GetXaxis().SetTitle( 'b Score Threshold' )
    eff_g.GetYaxis().SetTitle( '%s efficiency'%(Note_) )
    if(Note_=="SL"):
        outputName = ol_ + 'EffVsBthreshold_%s_%s_%s.png'%(Note_,Note2_,SL_channel)
    else:
        outputName = ol_ + 'EffVsBthreshold_%s_%s.png'%(Note_,Note2_)
    Draw_Histogram(eff_g,'ACP',outputName)   
    return eff_g    

def PlotEffVsEffsTogether(g1, g2, g3, ol_):
    c = TCanvas("c","c",800,600)

    g1.SetLineColor(kBlue)
    g1.SetLineWidth(2)
    g1.SetMarkerColor(kBlue)
    g1.SetMarkerStyle( 21 ) 

    g1.SetTitle( 'Sig Eff. vs. ttH Eff' )
    g1.GetXaxis().SetTitle( 'ttH efficiency' )
    g1.GetYaxis().SetTitle( 'signal efficiency' )

    g2.SetLineColor(kGreen+2)
    g2.SetLineWidth(2)
    g2.SetMarkerColor(kGreen+2)
    g2.SetMarkerStyle( 21 )     

    g1.Draw("ACP")
    g2.Draw("CP same")
    l = TLegend(0.5,0.5,0.7,0.7)
    l.AddEntry(g1,"Semi-Leptonic Signal","lp")
    l.AddEntry(g2,"Fully-Hadronic Signal","lp")
    l.Draw("same")
    # c.BuildLegend()
    c.SaveAs("%sEffsTogether.png"%(ol_))

def PlotEffVsEff(sig_g, ttH_g,ol_,Note_):
    nEntries = sig_g.GetN()
    print"sig_g:",sig_g
    print"sig_g.GetPointX(0):",sig_g.GetPointX(0)
    sig_eff_vals_, ttH_eff_vals_ = [], [] 
    for i in range(nEntries):
        bThresh = sig_g.GetPointX(i)
        sigPoint = sig_g.GetPointY(i)
        ttHPoint = ttH_g.GetPointY(i)
        sig_eff_vals_.append(sigPoint)
        ttH_eff_vals_.append(ttHPoint)
        print"bThreshold: %s --- Signal Eff: %s --- ttH Eff: %s"%(bThresh,sigPoint,ttHPoint)
        # print"point:",point
    # for thing in sig_g:
        # print"thing:",thing
    n = 100
    x, y = array( 'd' ), array( 'd' )

    for ientry,entry in enumerate(sig_eff_vals_):
        x_val, y_val = float(ttH_eff_vals_[ientry]), float(sig_eff_vals_[ientry])
        x.append(x_val)
        y.append(y_val)

    effVseff_h = TGraph(n,x,y)
    effVseff_h.SetLineColor( 2 )
    effVseff_h.SetLineWidth( 4 )
    effVseff_h.SetMarkerColor( 4 )
    effVseff_h.SetMarkerStyle( 21 )
    effVseff_h.SetTitle( 'b veto efficiency' )
    effVseff_h.GetXaxis().SetTitle( 'ttH efficiency' )
    effVseff_h.GetYaxis().SetTitle( 'signal efficiency' )
    outputName = ol_ + 'sigEffvsttHeff_%s.png'%(Note_)
    Draw_Histogram(effVseff_h,'ACP',outputName)   
    return effVseff_h

def PlotAllEffs(signal_SL_g_, signal_FH_g_, signal_FL_g_, ol_, Note_, Note2_, titles_):
    c = TCanvas("c","c",800,600)

    signal_SL_g_.SetTitle( '%s Eff. vs. bVeto Threshold'%(titles_) )
    signal_SL_g_.GetXaxis().SetTitle( 'bVeto Threshold' )
    signal_SL_g_.GetYaxis().SetTitle( '%s Efficiency'%(titles_) )
    signal_SL_g_.GetXaxis().SetRangeUser(0,1)
    signal_SL_g_.GetYaxis().SetRangeUser(0,1)

    signal_SL_g_.SetLineColor(kBlue)
    signal_SL_g_.SetLineWidth(2)
    signal_SL_g_.SetMarkerColor(kBlue)
    signal_SL_g_.SetMarkerStyle( 20 ) 

    signal_FH_g_.SetLineColor(kGreen+2)
    signal_FH_g_.SetLineWidth(2)
    signal_FH_g_.SetMarkerColor(kGreen+2)
    signal_FH_g_.SetMarkerStyle( 20 )  

    signal_FL_g_.SetLineColor(kPink+2)
    signal_FL_g_.SetLineWidth(2)
    signal_FL_g_.SetMarkerColor(kPink+2)
    signal_FL_g_.SetMarkerStyle( 20 )      

    ##-- Lines at 3 working points    
    signal_SL_g_.Draw("ACP")
    signal_FH_g_.Draw("CP same")
    signal_FL_g_.Draw("CP same")
    l = TLegend(0.35,0.35,0.6,0.6)
    l.AddEntry(signal_SL_g_,"Semi-Leptonic Tagged %s"%(Note_),"lp")
    l.AddEntry(signal_FH_g_,"Fully-Hadronic Tagged %s"%(Note_),"lp")
    l.AddEntry(signal_FL_g_,"Fully-Leptonic Tagged %s"%(Note_),"lp")
    l.SetBorderSize(0)
    l.Draw("same")
    # c.BuildLegend()
    Loose, Medium, Tight = 0.0494, 0.2770, 0.7264 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X
    c.Update()
    cxmin, cxmax, cymin, cymax = c.GetUxmin(), c.GetUxmax(), c.GetUymin(), c.GetUymax()
    Line_Loose = TLine(Loose, cymin, Loose, cymax)
    Line_Medium = TLine(Medium, cymin, Medium, cymax)
    Line_Tight = TLine(Tight, cymin, Tight, cymax)
    Line_Loose.SetLineStyle(9)
    Line_Medium.SetLineStyle(9)
    Line_Tight.SetLineStyle(9)
    Line_Loose.Draw("same")
    Line_Medium.Draw("same")
    Line_Tight.Draw("same")
    c.SetTickx(1)
    c.SetTicky(1)
    c.SaveAs("%s%s%sEffsTogether.png"%(ol_,Note_,Note2_)) 

def SetGrStyles(gr_, signal_, type_):
    gr_.SetLineWidth(2)
    gr_.SetMarkerSize(0.5)
    
    if(signal_ == "SL"):
        if(type_ == "prev"):
            gr_.SetLineColor(kBlue)
            gr_.SetMarkerColor(kBlue)            
        elif(type_ == "upd"):
            gr_.SetLineColor(kBlue-2)
            gr_.SetMarkerColor(kBlue-2)            
    elif(signal_ == "FH"):
        if(type_ == "prev"):
            gr_.SetLineColor(kGreen+2)
            gr_.SetMarkerColor(kGreen+2)            
        elif(type_ == "upd"):
            gr_.SetLineColor(kGreen-2)
            gr_.SetMarkerColor(kGreen-2)          
    elif(signal_ == "FL"):
        if(type_ == "prev"):
            gr_.SetLineColor(kPink+2)
            gr_.SetMarkerColor(kPink+2)            
        elif(type_ == "upd"):
            gr_.SetLineColor(kPink-2)
            gr_.SetMarkerColor(kPink-2)          

    if(type_ == "prev"):
        gr_.SetMarkerStyle( 20 )       
        gr_.SetLineStyle(2)  
    elif(type_ == "upd"):
        gr_.SetMarkerStyle( 21 )
        gr_.SetLineStyle(1)  

    return gr_ 

# def PlotTwoVars(signal_SL_g_, signal_FH_g_, signal_FL_g_, ol_, Note_, Note2_, titles_):
def PlotTwoVars(signal_g_one, signal_g_two, signal_tag, ol_, Note_):
    c = TCanvas("c","c",800,600)

    # signal_SL_g_.SetTitle( '%s Eff. vs. bVeto Threshold'%(titles_) )
    # signal_SL_g_.GetXaxis().SetTitle( 'bVeto Threshold' )
    # signal_SL_g_.GetYaxis().SetTitle( '%s Efficiency'%(titles_) )
    # signal_SL_g_.GetXaxis().SetRangeUser(0,1)
    # signal_SL_g_.GetYaxis().SetRangeUser(0,1)

    SetGrStyles(signal_g_one, signal_tag, "prev")
    signal_g_one.GetXaxis().SetRangeUser(0,1)
    signal_g_one.GetYaxis().SetRangeUser(0,1)

    SetGrStyles(signal_g_two, signal_tag, "upd")
  
    signal_g_one.Draw("ACP")
    signal_g_two.Draw("CP same")

    if(signal_tag == "SL"):
        SL_channel = Note_.split('-')[-1]
        legendText = "%s %s"%(signal_tag, SL_channel)
    else: 
        legendText = "%s"%(signal_tag)

    l = TLegend(0.35,0.35,0.6,0.6)
    l.AddEntry(signal_g_one,"Previous %s Tagged"%(legendText),"lp")
    l.AddEntry(signal_g_two,"Updated %s Tagged"%(legendText),"lp")
    l.SetBorderSize(0)
    l.Draw("same")
    Loose, Medium, Tight = 0.0494, 0.2770, 0.7264 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X
    c.Update()
    cxmin, cxmax, cymin, cymax = c.GetUxmin(), c.GetUxmax(), c.GetUymin(), c.GetUymax()
    Line_Loose = TLine(Loose, cymin, Loose, cymax)
    Line_Medium = TLine(Medium, cymin, Medium, cymax)
    Line_Tight = TLine(Tight, cymin, Tight, cymax)
    Line_Loose.SetLineStyle(9)
    Line_Medium.SetLineStyle(9)
    Line_Tight.SetLineStyle(9)
    Line_Loose.Draw("same")
    Line_Medium.Draw("same")
    Line_Tight.Draw("same")
    c.SetTickx(1)
    c.SetTicky(1)
    c.SaveAs("%s%s%sEffsTogether.png"%(ol_,signal_tag,Note_))            

def ComputeIntegralRatio(signal_tree, ttH_tree, channel_,ol_,SL_channel, IncludeSFs, FL_channel):
    print"Computing signal / ttH integral in the signal region for %s"%(channel_)
    if(channel_=="SL"): 
        print"Semi-Leptonic channel: ",SL_channel
    # n = 100
    n = 100 ##-- because ratio in 0th bin might be inf.
    x, y = array( 'd' ), array( 'd' )    
    # cuts = [i*0.01 for i in range(0,100)]
    cuts = [i*0.01 for i in range(1,101)]
    # N_tot_Entries = tree_.GetEntries()
    PHOTON_CUTS = "( (Leading_Photon_pt / CMS_hgg_mass) > 0.33 ) && ( (Subleading_Photon_pt / CMS_hgg_mass) > 0.25 )"
    LUMI = "41.5"
    SIGNAL_SCALE = "1"
    CHANNEL_SELECTION = "1"
    if(channel_=="SL"): 
        if(SL_channel=="Electron"): 
            SIGNAL_SCALE = "(31.049*0.00097)*(0.441)" ##-- add lepton flavor selection 
            CHANNEL_SELECTION = "(N_goodElectrons==1)"
        elif(SL_channel=="Muon"): 
            SIGNAL_SCALE = "(31.049*0.00097)*(0.441)*(N_goodMuons==1)"    
            CHANNEL_SELECTION = "(N_goodMuons==1)"
    if(channel_=="FH"): SIGNAL_SCALE = "(31.049*0.00097)*(0.454)"
    if(channel_=="FL"): 
        SIGNAL_SCALE = "(31.049*0.00097)*(0.107)"
        print"****FL_channel = ",FL_channel
        if(FL_channel == "ee"): CHANNEL_SELECTION = "(FL_Lep_Flavor==0)"
        elif(FL_channel == "mumu"): CHANNEL_SELECTION = "(FL_Lep_Flavor==1)"
        elif(FL_channel == "emu"): CHANNEL_SELECTION = "(FL_Lep_Flavor==2)"
        elif(FL_channel == "mue"): CHANNEL_SELECTION = "(FL_Lep_Flavor==3)"
        else: CHANNEL_SELECTION = 1 

    SF_SELECTION = "1"
    if(not IncludeSFs): 
        print"----------Dividing OUT Scale Factors-----------------"
        SF_SELECTION = "(1/centralObjectWeight)"

    ##-- Compute integral with all events once for denominator 
    h_tmp_Signal_all = TH1F("h_tmp_Signal_all","h_tmp_Signal_all",20,115,135)
    h_tmp_ttH_all = TH1F("h_tmp_ttH_all","h_tmp_ttH_all",20,115,135)
    signal_tree.Draw("CMS_hgg_mass >> h_tmp_Signal_all","1*weight*(%s)*(%s)*(%s)*(%s)*(%s)"%(LUMI,SIGNAL_SCALE,PHOTON_CUTS,CHANNEL_SELECTION,SF_SELECTION))
    ttH_tree.Draw("CMS_hgg_mass >> h_tmp_ttH_all","1*weight*(%s)*(%s)*(%s)*(%s)"%(LUMI,PHOTON_CUTS,CHANNEL_SELECTION,SF_SELECTION))
    totalSignal = h_tmp_Signal_all.Integral()
    totalttH = h_tmp_ttH_all.Integral()
    print"Signal Integral in Signal Region no cut:",totalSignal
    print"ttH Integral in Signal Region no cut:",totalttH
    print"Ratio in Signal Region no cut:",float(totalSignal) / float(totalttH)

    for icut,cut in enumerate(cuts):
        # print"icut: ",icut 
        x.append(cut)
        # print"cut value btag < :",cut 
        condition = ""
        maxJets = 5
        h_tmp = TH1F("h_tmp","h_tmp",20,115,135) ##-- signal region 
        h_tmp_ttH = TH1F("h_tmp_ttH","h_tmp_ttH",20,115,135) ##-- ttH in signal region 
        for jet_i in range(0,maxJets):
            scoreFormat = "goodJets_%s_bDiscriminator_mini_pfDeepFlavourJetTags_prob"%(jet_i)
            variable = "(%s%s + %s%s + %s%s < %s)"%(scoreFormat,"b",scoreFormat,"bb",scoreFormat,"lepb",cut)
            condition += variable
            if jet_i == maxJets-1: break 
            else: condition += " && "
        # print "condition = ",condition 

        signal_tree.Draw("CMS_hgg_mass >> h_tmp","(%s)*weight*(%s)*(%s)*(%s)*(%s)"%(condition,LUMI,SIGNAL_SCALE,CHANNEL_SELECTION,SF_SELECTION))
        ttH_tree.Draw("CMS_hgg_mass >> h_tmp_ttH","(%s)*weight*(%s)*(%s)*(%s)"%(condition,LUMI,CHANNEL_SELECTION,SF_SELECTION))
        tmp_integral = h_tmp.Integral()
        tmp_ttH_integral = h_tmp_ttH.Integral()
        sigTottHRatio = float(tmp_integral) / float(tmp_ttH_integral)
        y.append(sigTottHRatio)
        # print"sigTottHRatio",sigTottHRatio
        # N_weighted_entries_pass = tmp_integral
        # eff = float(N_weighted_entries_pass) / float(total_weighed_entries)
        # y.append(eff)
        del h_tmp 
        del h_tmp_ttH

    sigTottHRatio_g = TGraph(n,x,y)
    sigTottHRatio_g.SetMarkerStyle( 21 )
    sigTottHRatio_g.SetTitle( '%s Signal integral / ttH integral in signal region'%(channel_) )
    sigTottHRatio_g.GetXaxis().SetTitle( 'b Score Threshold' )
    sigTottHRatio_g.GetYaxis().SetTitle( '%s / ttH'%(channel_) )
    
    if(channel_=="SL"):
       outputName = ol_ + 'SigOverttHVsBthreshold_%s_%s.png'%(channel_,SL_channel)
    elif(channel_=="FL"):
        outputName = ol_ + 'SigOverttHVsBthreshold_%s_%s.png'%(channel_,FL_channel)
    else:
        outputName = ol_ + 'SigOverttHVsBthreshold_%s.png'%(channel_) 
    Draw_Histogram(sigTottHRatio_g,'ACP',outputName)   
    return sigTottHRatio_g        

def CombineRatioGraphs(SLTottHRatio_g_, FHTottHRatio_g_, FLTottHRatio_g_, ol_):
    c = TCanvas("c","c",800,600)
    c.DrawFrame(-10,-10,10,10)
    c.SetLeftMargin(0.15)
    # c.SetTopMargin(0.8)
    SLTottHRatio_g_.SetTitle( '(Signal / ttH) in signal region')
    SLTottHRatio_g_.GetXaxis().SetTitle( 'bVeto Threshold' )
    SLTottHRatio_g_.GetYaxis().SetTitle( '#int Signal / #int ttH' )
    SLTottHRatio_g_.GetXaxis().SetRangeUser(0,1)
    SLTottHRatio_g_.GetYaxis().SetRangeUser(0,1)

    SLTottHRatio_g_.SetLineColor(kBlue)
    SLTottHRatio_g_.SetLineWidth(2)
    SLTottHRatio_g_.SetMarkerColor(kBlue)
    SLTottHRatio_g_.SetMarkerStyle( 20 ) 

    FHTottHRatio_g_.SetLineColor(kGreen+2)
    FHTottHRatio_g_.SetLineWidth(2)
    FHTottHRatio_g_.SetMarkerColor(kGreen+2)
    FHTottHRatio_g_.SetMarkerStyle( 20 )  

    FLTottHRatio_g_.SetLineColor(kPink+2)
    FLTottHRatio_g_.SetLineWidth(2)
    FLTottHRatio_g_.SetMarkerColor(kPink+2)
    FLTottHRatio_g_.SetMarkerStyle( 20 )      

    ##-- Lines at 3 working points    
    SLTottHRatio_g_.Draw("ACP")
    FHTottHRatio_g_.Draw("CP same")
    FLTottHRatio_g_.Draw("CP same")
    l = TLegend(0.35,0.35,0.6,0.6)
    l.AddEntry(SLTottHRatio_g_,"Semi-Leptonic Tag","lp")
    l.AddEntry(FHTottHRatio_g_,"Fully-Hadronic Tag","lp")
    l.AddEntry(FLTottHRatio_g_,"Fully-Leptonic Tag","lp")
    l.SetBorderSize(0)
    l.Draw("same")
    Loose, Medium, Tight = 0.0494, 0.2770, 0.7264 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X
    c.Update()
    cxmin, cxmax, cymin, cymax = c.GetUxmin(), c.GetUxmax(), c.GetUymin(), c.GetUymax()
    Line_Loose = TLine(Loose, cymin, Loose, cymax)
    Line_Medium = TLine(Medium, cymin, Medium, cymax)
    Line_Tight = TLine(Tight, cymin, Tight, cymax)
    Line_Loose.SetLineStyle(9)
    Line_Medium.SetLineStyle(9)
    Line_Tight.SetLineStyle(9)
    Line_Loose.Draw("same")
    Line_Medium.Draw("same")
    Line_Tight.Draw("same")
    c.SetTickx(1)
    c.SetTicky(1)

    # c.SetLeftMargin(0.5)
    c.SaveAs("%s/SigOverttHRatiosTogether.png"%(ol_))    

# def GetTrees(prefix):
    # #-- LooseElecID_TightMuonIDISO Files 
    # signal_path_SL = "%sSL_SM2017.root"%(prefix) 
    # signal_path_FH = "%sFH_SM2017.root"%(prefix) 
    # signal_path_FL = "%sFL_SM2017.root"%(prefix) 
    # ttH_path = "%sttHJetToGG_2017.root"%(prefix)
    # signal_file_SL = TFile.Open(signal_path_SL)
    # signal_file_FH = TFile.Open(signal_path_FH)
    # signal_file_FL = TFile.Open(signal_path_FL)
    # ttH_file = TFile.Open(ttH_path)

    # SL_tree_ = signal_file_SL.Get("tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0")
    # SL_tree = SL_tree_.CopyTree("")

    # if("MediumMVAElecID" in prefix): FH_tree_ = signal_file_FH.Get("tagsDumper/trees/GluGluToHHTo2G4Q_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8_13TeV_HHWWggTag_1")
    # else: FH_tree_ = signal_file_FH.Get("tagsDumper/trees/GluGluToHHTo2G4Q_node_cHHH1_13TeV_HHWWggTag_1")
    # FL_tree_ = signal_file_FL.Get("tagsDumper/trees/GluGluToHHTo2G2l2nu_node_cHHH1_13TeV_HHWWggTag_2")

    # # SL_tree = SL_tree_.CopyTree("1")
    # # FH_tree = FH_tree_.CopyTree()
    # # FL_tree = FL_tree_.CopyTree()

    # ttH_SL_tree = ttH_file.Get('tagsDumper/trees/tth_125_13TeV_HHWWggTag_0')
    # ttH_FH_tree = ttH_file.Get('tagsDumper/trees/tth_125_13TeV_HHWWggTag_1')
    # ttH_FL_tree = ttH_file.Get('tagsDumper/trees/tth_125_13TeV_HHWWggTag_2')

    # for finalState in ["SL","FH","FL"]:
    #     print"num %s signal entries: "%(finalState)
    #     exec('print eval("%s_tree.GetEntries()")'%(finalState))
        
    #     print"num %s ttH entries: "%(finalState)
    #     exec('print eval("ttH_%s_tree.GetEntries()")'%(finalState))

    # return SL_tree, FH_tree, FL_tree, ttH_SL_tree, ttH_FH_tree, ttH_FL_tree 

if __name__ == '__main__':
    gROOT.SetBatch(1) # Do not output upon draw statement 
    ol = '/eos/user/a/atishelm/www/HHWWgg/Pre-Production-Checks/bVeto/'
    prefix_prev = '/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/Signal_LooseElecID_TightMuonIDISO/hadded/'
    prefix_updated = '/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/Signal_MediumMVAElecID_MediumMuonIDISO/hadded/'

    # prev_SL_tree, prev_FH_tree, prev_FL_tree, prev_ttH_SL_tree, prev_ttH_FH_tree, prev_ttH_FL_tree = GetTrees(prefix_prev)
    # upd_SL_tree, upd_FH_tree, upd_FL_tree, upd_ttH_SL_tree, upd_ttH_FH_tree, upd_ttH_FL_tree = GetTrees(prefix_updated)
        
    ##-- Get Trees 
    signal_path_SL = "%sSL_SM2017.root"%(prefix_prev) 
    signal_path_FH = "%sFH_SM2017.root"%(prefix_prev) 
    signal_path_FL = "%sFL_SM2017.root"%(prefix_prev) 
    ttH_path = "%sttHJetToGG_2017.root"%(prefix_prev)
    signal_file_SL = TFile.Open(signal_path_SL)
    signal_file_FH = TFile.Open(signal_path_FH)
    signal_file_FL = TFile.Open(signal_path_FL)
    ttH_file = TFile.Open(ttH_path)

    prev_SL_tree = signal_file_SL.Get("tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0")
    prev_FH_tree = signal_file_FH.Get("tagsDumper/trees/GluGluToHHTo2G4Q_node_cHHH1_13TeV_HHWWggTag_1")
    prev_FL_tree = signal_file_FL.Get("tagsDumper/trees/GluGluToHHTo2G2l2nu_node_cHHH1_13TeV_HHWWggTag_2")

    prev_ttH_SL_tree = ttH_file.Get('tagsDumper/trees/tth_125_13TeV_HHWWggTag_0')
    prev_ttH_FH_tree = ttH_file.Get('tagsDumper/trees/tth_125_13TeV_HHWWggTag_1')
    prev_ttH_FL_tree = ttH_file.Get('tagsDumper/trees/tth_125_13TeV_HHWWggTag_2')

    for finalState in ["SL","FH","FL"]:
        print"num %s signal entries: "%(finalState)
        exec('print eval("prev_%s_tree.GetEntries()")'%(finalState))
        
        print"num %s ttH entries: "%(finalState)
        exec('print eval("prev_ttH_%s_tree.GetEntries()")'%(finalState))

    print"**********Previous IDs******************"

    # signal_SL_g_prev_elec = MakeEffPlot(prev_SL_tree,"SL",ol,"Prev","Electron")
    # signal_SL_g_prev_muon = MakeEffPlot(prev_SL_tree,"SL",ol,"Prev","Muon")
    # signal_FH_g_prev = MakeEffPlot(prev_FH_tree,"FH",ol,"Prev","")
    # signal_FL_g_prev = MakeEffPlot(prev_FL_tree,"FL",ol,"Prev","")
    PHOTON_CUTS = "( (Leading_Photon_pt / CMS_hgg_mass) > 0.33 ) && ( (Subleading_Photon_pt / CMS_hgg_mass) > 0.25 )"

    prev_goodElectrons_h = TH1F("prev_goodElectrons_h","prev_goodElectrons_h",10,0,10)
    LUMI = "41.5"
    SIGNAL_SCALE = "(31.049*0.00097)*(0.107)"
    prev_FL_tree.Draw("N_goodElectrons >> prev_goodElectrons_h","1")
    prev_goodElectrons_h.SetDirectory(0)

    prev_goodMuons_h = TH1F("prev_goodMuons_h","prev_goodMuons_h",10,0,10)
    LUMI = "41.5"
    SIGNAL_SCALE = "(31.049*0.00097)*(0.107)"
    # prev_FL_tree.Draw("N_goodElectrons >> prev_goodElectrons_h","1*weight*%s*%s"%(LUMI,SIGNAL_SCALE))
    prev_FL_tree.Draw("N_goodMuons >> prev_goodMuons_h","1")
    prev_goodMuons_h.SetDirectory(0)
    # upd_FL_tree.Draw("N_goodElectrons >> upd_goodElectrons_h","1*weight*%s*%s"%(LUMI,SIGNAL_SCALE))    
    print"**********Previous IDs******************"

    # prev_SLTottHRatio_g_elec = ComputeIntegralRatio(prev_SL_tree,prev_ttH_SL_tree,"SL",ol,"Electron",1) ##-- Final argument: IncludeSFs
    # prev_SLTottHRatio_g_muon = ComputeIntegralRatio(prev_SL_tree,prev_ttH_SL_tree,"SL",ol,"Muon",1)
    # prev_FHTottHRatio_g = ComputeIntegralRatio(prev_FH_tree,prev_ttH_FH_tree,"FH",ol,"",1)
    # prev_FLTottHRatio_g = ComputeIntegralRatio(prev_FL_tree,prev_ttH_FL_tree,"FL",ol,"",1,"ee")
    # prev_FLTottHRatio_g = ComputeIntegralRatio(prev_FL_tree,prev_ttH_FL_tree,"FL",ol,"",1,"mumu")
    # prev_FLTottHRatio_g = ComputeIntegralRatio(prev_FL_tree,prev_ttH_FL_tree,"FL",ol,"",1,"emu")
    # prev_FLTottHRatio_g = ComputeIntegralRatio(prev_FL_tree,prev_ttH_FL_tree,"FL",ol,"",1,"mue")

    ##-- Updated IDs and ISOs 
    signal_path_SL = "%sSL_SM2017.root"%(prefix_updated) 
    signal_path_FH = "%sFH_SM2017.root"%(prefix_updated) 
    signal_path_FL = "%sFL_SM2017.root"%(prefix_updated) 
    ttH_path = "%sttHJetToGG_2017.root"%(prefix_updated)
    signal_file_SL = TFile.Open(signal_path_SL)
    signal_file_FH = TFile.Open(signal_path_FH)
    signal_file_FL = TFile.Open(signal_path_FL)
    ttH_file = TFile.Open(ttH_path)


    upd_SL_tree = signal_file_SL.Get("tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0")
    upd_FH_tree = signal_file_FH.Get("tagsDumper/trees/GluGluToHHTo2G4Q_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8_13TeV_HHWWggTag_1")
    upd_FL_tree = signal_file_FL.Get("tagsDumper/trees/GluGluToHHTo2G2l2nu_node_cHHH1_13TeV_HHWWggTag_2")

    upd_ttH_SL_tree = ttH_file.Get('tagsDumper/trees/tth_125_13TeV_HHWWggTag_0')
    upd_ttH_FH_tree = ttH_file.Get('tagsDumper/trees/tth_125_13TeV_HHWWggTag_1')
    upd_ttH_FL_tree = ttH_file.Get('tagsDumper/trees/tth_125_13TeV_HHWWggTag_2')

    ##-- Plot N_goodElectrons, N_goodMuons for fully leptonic final state 
    upd_goodElectrons_h = TH1F("upd_goodElectrons_h","upd_goodElectrons_h",10,0,10)
    LUMI = "41.5"
    SIGNAL_SCALE = "(31.049*0.00097)*(0.107)"
    upd_FL_tree.Draw("N_goodElectrons >> upd_goodElectrons_h","1")
    upd_goodElectrons_h.SetDirectory(0)

    upd_goodMuons_h = TH1F("upd_goodMuons_h","upd_goodMuons_h",10,0,10)
    LUMI = "41.5"
    SIGNAL_SCALE = "(31.049*0.00097)*(0.107)"
    # prev_FL_tree.Draw("N_goodElectrons >> prev_goodElectrons_h","1*weight*%s*%s"%(LUMI,SIGNAL_SCALE))
    upd_FL_tree.Draw("N_goodMuons >> upd_goodMuons_h","1")
    upd_goodMuons_h.SetDirectory(0)
    print"**********Updated IDs******************"

    # signal_SL_g_upd_elec = MakeEffPlot(upd_SL_tree,"SL",ol,"Updated","Electron")
    # signal_SL_g_upd_muon = MakeEffPlot(upd_SL_tree,"SL",ol,"Updated","Muon")
    # signal_FH_g_upd = MakeEffPlot(upd_FH_tree,"FH",ol,"Updated","")
    # signal_FL_g_upd = MakeEffPlot(upd_FL_tree,"FL",ol,"Updated","")    
    print"**********Updated IDs******************"

    # upd_SLTottHRatio_g_elec = ComputeIntegralRatio(upd_SL_tree,upd_ttH_SL_tree,"SL",ol,"Electron",1)
    # upd_SLTottHRatio_g_muon = ComputeIntegralRatio(upd_SL_tree,upd_ttH_SL_tree,"SL",ol,"Muon",1)
    # upd_FHTottHRatio_g = ComputeIntegralRatio(upd_FH_tree,upd_ttH_FH_tree,"FH",ol,"",1)
    upd_FLTottHRatio_g = ComputeIntegralRatio(upd_FL_tree,upd_ttH_FL_tree,"FL",ol,"",1,"ee")
    upd_FLTottHRatio_g = ComputeIntegralRatio(upd_FL_tree,upd_ttH_FL_tree,"FL",ol,"",1,"mumu")
    upd_FLTottHRatio_g = ComputeIntegralRatio(upd_FL_tree,upd_ttH_FL_tree,"FL",ol,"",1,"emu")
    upd_FLTottHRatio_g = ComputeIntegralRatio(upd_FL_tree,upd_ttH_FL_tree,"FL",ol,"",1,"mue")

    ##-- Plot Together 
    # PlotTwoVars(signal_SL_g_prev_elec, signal_SL_g_upd_elec, "SL", ol, "Eff-Electron")
    # PlotTwoVars(signal_SL_g_prev_muon, signal_SL_g_upd_muon, "SL", ol, "Eff-Muon")
    # PlotTwoVars(signal_FH_g_prev, signal_FH_g_upd, "FH", ol, "Eff")
    # PlotTwoVars(signal_FL_g_prev, signal_FL_g_upd, "FL", ol, "Eff")
    print"**********Comparing IDs******************"

    # PlotTwoVars(prev_SLTottHRatio_g_elec, upd_SLTottHRatio_g_elec, "SL", ol, "IntRatio-Electron")
    # PlotTwoVars(prev_SLTottHRatio_g_muon, upd_SLTottHRatio_g_muon, "SL", ol, "IntRatio-Muon")
    # exit(1)
    # PlotTwoVars(prev_FHTottHRatio_g, upd_FHTottHRatio_g, "FH", ol, "IntRatio")
    PlotTwoVars(prev_FLTottHRatio_g, upd_FLTottHRatio_g, "FL", ol, "IntRatio")    
    exit(1) 
    ##-- Plot N_goodElectrons, N_goodMuons for fully leptonic final state 
    # prev_goodElectrons_h = TH1F("prev_goodElectrons_h","prev_goodElectrons_h",10,0,10)
    # upd_goodElectrons_h = TH1F("upd_goodElectrons_h","upd_goodElectrons_h",10,0,10)
    # prev_goodMuons_h = TH1F("prev_goodMuons_h","prev_goodMuons_h",10,0,10)
    # LUMI = "41.5"
    # SIGNAL_SCALE = "(31.049*0.00097)*(0.107)"
    # prev_FL_tree.Draw("N_goodElectrons >> prev_goodElectrons_h","1*weight*%s*%s"%(LUMI,SIGNAL_SCALE))
    # upd_FL_tree.Draw("N_goodElectrons >> upd_goodElectrons_h","1*weight*%s*%s"%(LUMI,SIGNAL_SCALE))

    ##-- Good Electrons
    prev_goodElectrons_h.SetFillColor(kBlue)
    prev_goodElectrons_h.SetTitle("N good Electrons")
    upd_goodElectrons_h.SetFillColor(kRed+2)

    c_comb = TCanvas("c_comb","c_comb",800,600)
    prev_goodElectrons_h.Draw("hist")
    upd_goodElectrons_h.Draw("hist SAME")

    l = TLegend(0.35,0.35,0.6,0.6)
    l.AddEntry(prev_goodElectrons_h,"Previous IDs","f")
    l.AddEntry(upd_goodElectrons_h,"Updated IDs","f")
    l.SetBorderSize(0)
    l.Draw("same")

    c_comb.SaveAs("%s/N_goodElectrons_FL.png"%(ol))

    ##-- Good Muons 
    prev_goodMuons_h.SetFillColor(kBlue)
    prev_goodMuons_h.SetTitle("N good Muons")
    upd_goodMuons_h.SetFillColor(kRed+2)

    c_comb = TCanvas("c_comb","c_comb",800,600)
    prev_goodMuons_h.Draw("hist")
    upd_goodMuons_h.Draw("hist SAME")

    l = TLegend(0.35,0.35,0.6,0.6)
    l.AddEntry(prev_goodMuons_h,"Previous IDs","f")
    l.AddEntry(upd_goodMuons_h,"Updated IDs","f")
    l.SetBorderSize(0)
    l.Draw("same")

    c_comb.SaveAs("%s/N_goodMuons_FL.png"%(ol))    

    ##-- Compute integral with all events once for denominator 
    # h_tmp_all = TH1F("h_tmp_all","h_tmp_all",20,115,135)
    # tree_.Draw("CMS_hgg_mass >> h_tmp_all","1*weight*(%s)*(%s)"%(LUMI,SIGNAL_SCALE))
    # total_weighed_entries = h_tmp_all.Integral()
    # print"total_weighed_entries in signal region:",total_weighed_entries

    ##-- Plot Together 
    # c_comb = TCanvas("c_comb","c_comb",800,600)
    # signal_SL_g_upd.SetMarkerStyle(kSquare)
    # signal_SL_g_prev.Draw()
    # signal_SL_g_upd.Draw("same")
    # TLegend
    # c_comb.SaveAs("%s/"%(ol))

    # ttHeff_SL_g = MakeEffPlot(ttH_SL_tree,"ttH_SL",ol)
    # ttHeff_FH_g = MakeEffPlot(ttH_FH_tree,"ttH_FH",ol)
    # ttHeff_FL_g = MakeEffPlot(ttH_FL_tree,"ttH_FL",ol)

    PlotAllEffs(signal_SL_g, signal_FH_g, signal_FL_g, ol, "Signal","effvsthresh", "WW#gamma#gamma Signal")
    PlotAllEffs(ttHeff_SL_g, ttHeff_FH_g, ttHeff_FL_g, ol, "ttHJet","effvsthresh", "ttHJet")

    # SLTottHRatio_g = ComputeIntegralRatio(SL_tree,ttH_SL_tree,"SL",ol)
    # FHTottHRatio_g = ComputeIntegralRatio(FH_tree,ttH_FH_tree,"FH",ol)
    # FLTottHRatio_g = ComputeIntegralRatio(FL_tree,ttH_FL_tree,"FL",ol)

    CombineRatioGraphs(SLTottHRatio_g, FHTottHRatio_g, FLTottHRatio_g, ol)

    # SL_effvseff_g = PlotEffVsEff(signal_SL_g,ttHeff_SL_g,ol,"SL")
    # FH_effvseff_g = PlotEffVsEff(signal_FH_g,ttHeff_FH_g,ol,"FH")
    # FL_effvseff_g = PlotEffVsEff(signal_FL_g,ttHeff_FL_g,ol,"FL")
   
    # PlotAllEffs(SL_effvseff_g, FH_effvseff_g, FL_effvseff_g, ol, "both", "effvseff")
   
    # PlotEffVsEff(signal_FL_g,ttHeff_FL_g,ol,"FL")
    # PlotEffVsEffsTogether(SL_effvseff_g, FH_effvseff_g, FL_effvseff_g, ol)
    # PlotEffVsEff(SigEff_g,ttHEff_g,ol)
   
