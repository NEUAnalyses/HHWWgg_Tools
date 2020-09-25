###########################################################################################################################
# Abraham Tishelman-Charny
# 13 May 2020
#
# The purpose of this module is to provide cut related variables and definitions for NtupleAnalysis.py 
#
###########################################################################################################################

from ROOT import TH2F, TCanvas 

def GetCuts(CutsType):
    cuts, cutNames = [], []

    ##-- Only apply preselections. This means applying no cut because preselection already applied to events in microAODs 
    if(CutsType == "PreSelections"):
        cuts = ["1"]
        cutNames = ["PreSelections"]

    elif(CutsType == "OneGoodElec"):
        cuts = ["(N_goodElectrons==1)"]
        cutNames = ["OneGoodElec"]

    elif(CutsType == "OneGoodMuon"):
        cuts = ["(N_goodMuons==1)"]
        cutNames = ["OneGoodMuon"]        

    ##-- Apply Loose selections 
    elif(CutsType == "Loose"):
        ##-- Electrons, Muons, Jets: Keep all analysis selections except dR, pT
        electronCuts = ""
        muonCuts = ""
        jetCuts = ""
        maxObjects = 5

        lepton_pt_cut = 10 
        jet_pt_cut = 25 

        photonCuts = "((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)"
        
        for i in range(0,maxObjects): # info for 5 first electrons, muons, jets saved 
            elec, muon, jet = "allElectrons_%s"%(i), "allMuons_%s"%(i), "allJets_%s"%(i)
            electronCuts += "( (%s_pt >= %s) && (%s_passLooseId==1 && (fabs(%s_eta)<1.4442 || ((fabs(%s_eta)>1.566 && fabs(%s_eta)<2.5) ) ) ) )"%(elec,lepton_pt_cut,elec,elec,elec,elec)
            muonCuts += "((%s_pt >= %s && %s_isTightMuon==1 && fabs(%s_eta)<=2.4))"%(muon,lepton_pt_cut,muon,muon)
            jetCuts += "( (%s_pt>%s) && (%s_passTight2017==1) && fabs(%s_eta) <= 2.4)"%(jet,jet_pt_cut,jet,jet)     

            if(i != maxObjects-1): # if not the last object, multiply by next selection
                electronCuts += "+"
                muonCuts += "+"
                jetCuts += "+"

        cuts = ["( (((%s) + (%s)) == 1) && ((%s) >= 2) && (%s))"%(electronCuts,muonCuts,jetCuts,photonCuts)] # exactly one lepton passing looser selections, at least two jets passing looser selections  
        #print"LOOSE cuts:",cuts
        cutNames = ["Loose"]    
        
    ##-- Apply each analysis selection separately 
    elif(CutsType == "all"):
        cuts = ["1", "passPhotonSels == 1", "passbVeto == 1", "ExOneLep == 1", "goodJets == 1"] # preselections, photon sels, bVeto, exactly 1 lepton, at least 2 good jets
        cutNames = ["PreSelections","PhotonSelections","bVeto","OneLep","TwoGoodJets"]

    ##-- Apply final analysis selections (may be missing one or two like Tight2017 Jet ID)
    elif(CutsType == "final"):
        cuts = ["(passPhotonSels==1)*(passbVeto==1)*(ExOneLep==1)*(goodJets==1)*((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)"]
        cutNames = ["final"]
    
    ##-- Apply b Veto, exactly one good lepton, at least two good jets selections (Tight2017 Jet ID may be missing)
    elif(CutsType == "final-noPhoSels"):
        cuts = ["(passbVeto==1)*(ExOneLep==1)*(goodJets==1)"]
        cutNames = ["final-noPhoSels"]  

    ##-- Apply b Veto, exactly one good lepton, at least two good jets selections (Tight2017 Jet ID may be missing), and photon pT/mgg selections
    elif(CutsType == "final-noPhoMVA"):
        cuts = ["(passbVeto==1)*(ExOneLep==1)*(goodJets==1)*((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)"]
        cutNames = ["final-noPhoMVA"]    

    ##-- Apply b Veto, exactly one good lepton selections 
    elif(CutsType == "bVeto-OneLep"):
        cuts = ["(passbVeto==1)*(ExOneLep==1)"]
        cutNames = ["bVeto-OneLep"]      

    return [cuts,cutNames]

##-- Create table with number of events all backgrounds plus (Blinded) Data for each set cutSet,tag pair 
# def CreateEventsTable(cutName,HHWWggTag,dataNevents,MC_Nevents,MC_names,ol_):

## need a new table for s/sqrt(b) since it's only the signal region and the current table shows MC yields for entire 100->180 region 
# def CreateYieldsTables(cutBatchTag_pairs, dataNevents_list, MC_names, MC_Nevents_lists, MC_Nevents_noweight_lists,
                    #    ol_, Signal_Nevents_list_, removeBackgroundYields_, B_lists_, SidebandSF_):

# def CreateEventsTable(cutCatPairs,dataNevents,MC_Nevents,MC_names):

def CreateYieldsTable(region,cut,Bkg_Names,removeBackgroundYields,S_vals,B_vals,dataNevents,SidebandSF,Bkg_Nevents,ol):
    print'Creating yields table'

    # for s_val in S_vals:
        # print"sval:",s_val
    # for b_val in B_vals:
        # print"bval:",b_val

    yaxisLabels = []
    if(region == "SB"):
        yaxisLabels.append("Data / MC")
        yaxisLabels.append("Data (Blinded)")     
        yaxisLabels.append("S / sqrt(B)")
        yaxisLabels.append("sqrt(B)")
        yaxisLabels.append("B")
        yaxisLabels.append("S")

    elif(region == "SR"):
        yaxisLabels.append("S / sqrt(B)")
        yaxisLabels.append("sqrt(B)")
        yaxisLabels.append("B")
        yaxisLabels.append("S")
        dataNevents = 0 
    else: 
        print "[ERROR] - In CutsTools.py:CreateYieldsTable"
        print "Don't know what to do for region:",region
        print "Exiting"
        exit(1)

    numSpecialCats = len(yaxisLabels)

    if(not removeBackgroundYields): 
        for Bkg_Name in Bkg_Names: 
            yaxisLabels.append(Bkg_Name)

    xaxisLabels = []
    xaxisLabels.append(cut)

    # for cutTagPair in cutBatchTag_pairs: xaxisLabels.append(cutTagPair)
    # firstCutBatch = xaxisLabels[0].split('_')[0]

    nyLabels = len(yaxisLabels)
    nxLabels = len(xaxisLabels)

    # Bkg_sums = []


    # N_allMC_list = []
    # B_vals = []

    # for MC_events_list in MC_Nevents_lists: 
        # N_allMC = sum(MC_events_list)
        # N_allMC_list.append(N_allMC)
    # for B_list in B_lists_:
        # B = sum(B_list)
        # B_vals.append(B)

    # N_allMC_noweight_list = []
    # for MC_events_noweight_list in MC_Nevents_noweight_lists: 
    #     N_allMC_noweight = sum(MC_events_noweight_list)
    #     N_allMC_noweight_list.append(N_allMC_noweight)  

    histTitle = "Weighted Events"

    h_grid = TH2F('h_grid',histTitle,nxLabels,0,nxLabels,nyLabels,0,nyLabels)
    h_grid.SetStats(0)
    h_grid.GetXaxis().SetLabelSize(.03)   

    for yli, yl in enumerate(yaxisLabels):
        h_grid.GetYaxis().SetBinLabel(yli+1,yl)

    for ixL,xLabel in enumerate(xaxisLabels):
        # S = Signal_Nevents_list_[ixL] ##-- assumes only one signal model! 
        S = sum(S_vals) # per bin vals 
        # B = sum(B_vals) # per bin vals in ratio plot 
        B = sum(Bkg_Nevents)

        h_grid.GetXaxis().SetBinLabel(ixL+1,xLabel)
        # MC_Nevents = eval("%s[ixL]"%(MC_Nevents_vals))
        # N_allMC = eval("%s[ixL]"%(MC_sumEvents_l))

        # B = eval("%s[ixL]"%(B_values))

        B *= SidebandSF # SidebandSF_ should be 1 by default 
    
        # if(N_allMC == 0.0)
        if(B <= 0.0): 
            data_over_MC = -1 
            SqrtB = -1 
            sOverSqrtB = -1 
        else: 
            data_over_MC = dataNevents / B
            SqrtB = B**0.5
            sOverSqrtB = S / SqrtB

        # print"S = ",S
        # print"B = ",B
        # print"sqrtB = ",SqrtB
        # print"sOverSqrtB = ",sOverSqrtB

        if(region == "SB"):
            h_grid.Fill(ixL,0,data_over_MC)
            h_grid.Fill(ixL,1,dataNevents)
            h_grid.Fill(ixL,2,sOverSqrtB)
            h_grid.Fill(ixL,3,SqrtB)
            h_grid.Fill(ixL,4,B)
            h_grid.Fill(ixL,5,S)

        elif(region == "SR"):
            h_grid.Fill(ixL,0,sOverSqrtB)
            h_grid.Fill(ixL,1,SqrtB)
            h_grid.Fill(ixL,2,B)
            h_grid.Fill(ixL,3,S)

        # for ie,numEvents in enumerate(MC_Nevents):
        for ie,numEvents in enumerate(Bkg_Nevents):
            h_grid.Fill(ixL,ie+numSpecialCats,numEvents) ## num specialCats is non MC background yield cats 

    outLabel = "Weighted"

    sideScaleOpt = ""
    if(SidebandSF != 1): sideScaleOpt = "WithSidebandScale"
    else: sideScaleOpt = "WithoutSidebandScale"
    outNamepng = "%s/%s_%s_YieldsTable_%s_%s.png"%(ol, region, cut, outLabel, sideScaleOpt)
    outNamepdf = "%s/%s_%s_YieldsTable_%s_%s.pdf"%(ol, region, cut, outLabel, sideScaleOpt)       
    c_tmp = TCanvas('c_tmp','c_tmp',800,600)
    c_tmp.SetRightMargin(0.15)
    c_tmp.SetLeftMargin(0.23)
    c_tmp.SetBottomMargin(0.15)
    c_tmp.SetTopMargin(0.1)
    h_grid.SetMarkerSize(1.2)
    h_grid.Draw("text COL1")
    # label.DrawLatex(0.3,0.95,"HHWWgg 95% CL Limits: " + ml)
    c_tmp.SaveAs(outNamepng)
    c_tmp.SaveAs(outNamepdf) 

    # ##-- Create Two Tables
    # ##-- One without MC weight applied, one with 

    # # for useMCWeight in [0,1]:
    # for useMCWeight in [1]:
    #     histTitles = ["Unweighted Events","Weighted Events"]
    #     outLabels = ["Unweighted","Weighted"]
    #     MC_sumEvents_list = ["N_allMC_noweight_list","N_allMC_list"]
    #     MC_Nevents_vals_Opts = ["MC_Nevents_noweight_lists","MC_Nevents_lists"]
    #     B_vals_list = ["B_vals","B_vals"]        
 
    #     histTitle, outLabel, MC_sumEvents_l, MC_Nevents_vals = histTitles[useMCWeight], outLabels[useMCWeight], MC_sumEvents_list[useMCWeight], MC_Nevents_vals_Opts[useMCWeight]
    #     B_values = B_vals_list[useMCWeight] ### not yet configured for with and without weights...only with weights 
    #     h_grid = TH2F('h_grid',histTitle,nxLabels,0,nxLabels,nyLabels,0,nyLabels)
    #     h_grid.SetStats(0)
    #     h_grid.GetXaxis().SetLabelSize(.03)      

    #     for yli, yl in enumerate(yaxisLabels):
    #         h_grid.GetYaxis().SetBinLabel(yli+1,yl) 

    #     for ixL,xLabel in enumerate(xaxisLabels):
    #         # S = Signal_Nevents_list_[ixL] ##-- assumes only one signal model! 
    #         S_sum = sum(S_vals) # per bin vals 
    #         B_sum = sum(B_vals)

    #         h_grid.GetXaxis().SetBinLabel(ixL+1,xLabel)
    #         dataNevents = dataNevents_list[ixL]
    #         MC_Nevents = eval("%s[ixL]"%(MC_Nevents_vals))
    #         N_allMC = eval("%s[ixL]"%(MC_sumEvents_l))
    #         # B = eval("%s[ixL]"%(B_values))

    #         B *= SidebandSF # SidebandSF_ should be 1 by default 
	    
    #         if(N_allMC == 0.0):
    #           data_over_MC = -1 
    #           N_allMC = -1
    #         else: 
    #           data_over_MC = dataNevents / N_allMC

    #         if(B == 0.0):
    #           sOverSqrtB = -1 
    #         else: 
    #           sOverSqrtB = S / B**0.5 

    #         SqrtB = B**0.5

    #         if(region == "SB"):
    #             h_grid.Fill(ixL,0,data_over_MC)
    #             h_grid.Fill(ixL,1,dataNevents)
    #             h_grid.Fill(ixL,2,sOverSqrtB)
    #             h_grid.Fill(ixL,3,SqrtB)
    #             h_grid.Fill(ixL,4,B)
    #             h_grid.Fill(ixL,5,S)

    #         elif(region == "SR"):
    #             h_grid.Fill(ixL,0,sOverSqrtB)
    #             h_grid.Fill(ixL,1,SqrtB)
    #             h_grid.Fill(ixL,2,B)
    #             h_grid.Fill(ixL,3,S)

    #         for ie,numEvents in enumerate(MC_Nevents):
    #             h_grid.Fill(ixL,ie+numSpecialCats,numEvents) ## num specialCats is non MC background yield cats 

    #     sideScaleOpt = ""
    #     if(SidebandSF != 1): sideScaleOpt = "WithSidebandScale"
    #     else: sideScaleOpt = "WithoutSidebandScale"
    #     outNamepng = "%s/%s_EventsTable_%s_%s.png"%(ol_, firstCutBatch, outLabel, sideScaleOpt)
    #     outNamepdf = "%s/%s_EventsTable_%s_%s.pdf"%(ol_, firstCutBatch, outLabel, sideScaleOpt)       
    #     c_tmp = TCanvas('c_tmp','c_tmp',800,600)
    #     c_tmp.SetRightMargin(0.15)
    #     c_tmp.SetLeftMargin(0.23)
    #     c_tmp.SetBottomMargin(0.15)
    #     c_tmp.SetTopMargin(0.1)
    #     h_grid.SetMarkerSize(1.2)
    #     h_grid.Draw("text COL1")
    #     # label.DrawLatex(0.3,0.95,"HHWWgg 95% CL Limits: " + ml)
    #     c_tmp.SaveAs(outNamepng)
    #     c_tmp.SaveAs(outNamepdf)    
