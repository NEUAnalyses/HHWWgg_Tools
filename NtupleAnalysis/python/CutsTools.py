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
    if(CutsType == "PS"):
        cuts = ["1"]
        cutNames = ["PreSelections"]
    elif(CutsType == "Loose"):
        ##-- Electrons, Muons, Jets: Keep all analysis selections except dR, pT

        ## Selections that need to be kept:
        # Electrons: eta, passLooseID --> Then look at pT 
        # Muons: eta, isTightMuon --> Then look at pT and isolation 
        # Jets: pT > 10 GeV, eta, Tight2017 --> Then look at pT   


        # Make cuts a boolean that exactly 1 of the allElectrons or exactly of the allMuons passes selections 
        # Then if true want to plot the distributions of the 
        electronCuts = ""
        muonCuts = ""
        jetCuts = ""
        maxObjects = 5

        lepton_pt_cut = 10 
        jet_pt_cut = 25 

        photonCuts = "((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)"
        
        # electronCuts, muonCuts, jetCuts = ""
        # for i in range(0,5): # info for 5 first electrons, muons, jets saved 
        for i in range(0,maxObjects): # info for 5 first electrons, muons, jets saved 
            elec, muon, jet = "allElectrons_%s"%(i), "allMuons_%s"%(i), "allJets_%s"%(i)
            # electronCuts += "((%s_passLooseId==1)*(fabs(%s_eta)<1.4442 || ((fabs(%s_eta)>1.566 && fabs(%s_eta)<2.5))))"%(elec,elec,elec,elec)
            # muonCuts += "((%s_isTightMuon==1)*(fabs(%s_eta)<=2.4))"%(muon,muon)
            # jetCuts += "((%s_passTight2017==1))"%(jet)
            electronCuts += "( (%s_pt >= %s) && (%s_passLooseId==1 && (fabs(%s_eta)<1.4442 || ((fabs(%s_eta)>1.566 && fabs(%s_eta)<2.5) ) ) ) )"%(elec,lepton_pt_cut,elec,elec,elec,elec)
            muonCuts += "((%s_pt >= %s && %s_isTightMuon==1 && fabs(%s_eta)<=2.4))"%(muon,lepton_pt_cut,muon,muon)
            jetCuts += "( (%s_pt>%s) && (%s_passTight2017==1) && fabs(%s_eta) <= 2.4)"%(jet,jet_pt_cut,jet,jet)     

            if(i != maxObjects-1): # if not the last object, multiply by next selection
                electronCuts += "+"
                muonCuts += "+"
                jetCuts += "+"
        # print"electronCuts:",electronCuts
        # print"muonCuts:",muonCuts
        # print"jetCuts:",jetCuts

        # exit(1)
        cuts = ["( (((%s) + (%s)) == 1) && ((%s) >= 2) && (%s))"%(electronCuts,muonCuts,jetCuts,photonCuts)] # exactly one lepton passing looser selections, at least two jets passing looser selections  
        # cuts = ["((%s)*(%s)*(%s))"%(electronCuts,muonCuts,jetCuts)]
        print"LOOSE cuts:",cuts
        cutNames = ["Loose"]    
        # electronCuts = "((allElectrons_0_passLooseId==1)*(   fabs(allElectrons_0_eta)<1.4442 || ((fabs(allElectrons_0_eta)>1.566 && fabs(allElectrons_0_eta)<2.5))   ) )"
        # # electronCuts = "(   fabs(allElectrons_0_eta)<1.4442 || ((fabs(allElectrons_0_eta)>1.566 && fabs(allElectrons_0_eta)<2.5))   )  "
        # # electronCuts = "((allElectrons_0_passLooseId==1))"
        # # electronCuts = "((allElectrons_0_passLooseId==1))"
        # muonCuts = "((fabs(allMuons_0_eta) <= 2.4))"
        # orLepCuts = "(%s || %s)"%(electronCuts,muonCuts)    
        
        # jetCuts = "((fabs(allJets_0_eta) <= 2.4)*(fabs(allJets_1_eta) <= 2.4))"
        # cuts = ["(N_allElectrons == 1 || N_allMuons == 1)*(N_allJets >= 2)*(Leading_Photon_MVA>-0.1)*(Subleading_Photon_MVA>-0.1)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["(N_allElectrons >= 1 || N_allMuons >= 1)*(N_allJets >= 2)*(Leading_Photon_MVA>-0.5)*(Subleading_Photon_MVA>-0.5)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["(N_allElectrons >= 1 || N_allMuons >= 1)*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["( (N_allElectrons >= 1 && N_allElectrons <= 2) || (N_allMuons >= 1 && N_allMuons <= 2) )*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["( N_allElectrons >= 1 || N_allMuons >= 1 )*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["( N_allElectrons == 1 )*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,electronCuts)]
        # cuts = ["( N_allElectrons == 1 )*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,electronCuts)]
        # cuts = ["( N_allElectrons == 1 )*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,electronCuts)]
        # cuts = ["( N_allElectrons == 1 || N_allMuons == 1 )*(N_allJets >= 2)*(passPhotonSels==1)*%s"%(jetCuts)]
        # cuts = ["((N_allElectrons == 1 && N_allMuons == 0 ) || (N_allElectrons == 0 && N_allMuons == 1 ))*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["((N_allElectrons == 1 && N_allMuons == 0 ) || (N_allElectrons == 0 && N_allMuons == 1 ))*(N_allJets >= 2)*(passPhotonSels==1)*%s"%(jetCuts)]
    elif(CutsType == "Medium"):
        cuts = ["(N_allElectrons + N_allMuons == 1)*(N_goodJets >= 2)*(passPhotonSels==1)"]
        cutNames = ["Medium"]
    elif(CutsType == "all"):
        cuts = ["1", "passPhotonSels == 1", "passbVeto == 1", "ExOneLep == 1", "goodJets == 1"] # preselections, photon sels, bVeto, exactly 1 lepton, at least 2 good jets
        cutNames = ["PreSelections","PhotonSelections","bVeto","OneLep","TwoGoodJets"]
    elif(CutsType == "finalwJetID"):
        cuts = ["(passPhotonSels==1)*(passbVeto==1)*(ExOneLep==1)*(goodJets==1)*(allJets_0_passTight2017==1)*(allJets_1_passTight2017==1)"]
        cutNames = ["finalwJetID"]    
    elif(CutsType == "final"):
        cuts = ["(passPhotonSels==1)*(passbVeto==1)*(ExOneLep==1)*(goodJets==1)*((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)"]
        cutNames = ["final"]
    elif(CutsType == "final-noPhoSels"):
        cuts = ["(passbVeto==1)*(ExOneLep==1)*(goodJets==1)"]
        cutNames = ["final-noPhoSels"]  
    elif(CutsType == "final-noPhoMVA"):
        cuts = ["(passbVeto==1)*(ExOneLep==1)*(goodJets==1)*((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)"]
        cutNames = ["final-noPhoMVA"]          
    elif(CutsType == "bVeto-OneLep"):
        cuts = ["(passbVeto==1)*(ExOneLep==1)"]
        cutNames = ["bVeto-OneLep"]          
    # elif(CutsType == "final-noPhoSels-withJetID"):
        # cuts = ["(passbVeto==1)*(ExOneLep==1)*(goodJets==1*())"]
        # cutNames = ["final-noPhoSels-withJetID"]                
    return [cuts,cutNames]

##-- Create table with number of events all backgrounds plus (Blinded) Data for each set cutSet,tag pair 
# def CreateEventsTable(cutName,HHWWggTag,dataNevents,MC_Nevents,MC_names,ol_):
def CreateEventsTable(cutBatchTag_pairs,dataNevents_list,MC_names,MC_Nevents_lists,MC_Nevents_noweight_lists,ol_):
# def CreateEventsTable(cutCatPairs,dataNevents,MC_Nevents,MC_names):
    print'Creating table of nEvents'
    # yaxisLabels = ['2.5%','16%','50%','84%','97.5%'] # Backgrounds, Background Total, Data
    yaxisLabels = []
    yaxisLabels.append("Data / MC")
    yaxisLabels.append("Data (Blinded)")     
    yaxisLabels.append("all_MC")
    for MC_name in MC_names: yaxisLabels.append(MC_name)
    xaxisLabels = []
    for cutTagPair in cutBatchTag_pairs: xaxisLabels.append(cutTagPair)
    firstCutBatch = xaxisLabels[0].split('_')[0]
    nyLabels = len(yaxisLabels)
    nxLabels = len(xaxisLabels)
    N_allMC_list = []
    for MC_events_list in MC_Nevents_lists: 
        N_allMC = sum(MC_events_list)
        N_allMC_list.append(N_allMC)

    N_allMC_noweight_list = []
    for MC_events_noweight_list in MC_Nevents_noweight_lists: 
        N_allMC_noweight = sum(MC_events_noweight_list)
        N_allMC_noweight_list.append(N_allMC_noweight)  

    # for ml in massLabels: # for pair of cutName, HHWWggTag 
    # print'ml:',ml

    # lowestMedianVal, lowestMedianLabel, lowestMedianIndex = 9999999, "", -99
    # highestMedianVal, highestMedianLabel, highestMedianIndex = -9999999, "", -99

    ##-- Create Two Tables
    ##-- One without MC weight applied, one with 

    for useMCWeight in [0,1]:
        histTitles = ["Unscaled Events","Scaled Events"]
        outLabels = ["Unscaled","Scaled"]
        MC_sumEvents_list = ["N_allMC_noweight_list","N_allMC_list"]
        MC_Nevents_vals_Opts = ["MC_Nevents_noweight_lists","MC_Nevents_lists"]
        histTitle, outLabel, MC_sumEvents_l, MC_Nevents_vals = histTitles[useMCWeight], outLabels[useMCWeight], MC_sumEvents_list[useMCWeight], MC_Nevents_vals_Opts[useMCWeight]
        h_grid = TH2F('h_grid',histTitle,nxLabels,0,nxLabels,nyLabels,0,nyLabels)
        h_grid.SetStats(0)
        h_grid.GetXaxis().SetLabelSize(.03)      

        for yli, yl in enumerate(yaxisLabels):
            h_grid.GetYaxis().SetBinLabel(yli+1,yl) 

        for ixL,xLabel in enumerate(xaxisLabels):
            h_grid.GetXaxis().SetBinLabel(ixL+1,xLabel)
            dataNevents = dataNevents_list[ixL]
            # MC_Nevents = MC_Nevents_lists[ixL]
            MC_Nevents = eval("%s[ixL]"%(MC_Nevents_vals))
            N_allMC = eval("%s[ixL]"%(MC_sumEvents_l))

            # N_allMC = N_allMC_list[ixL]
            if(N_allMC == 0): data_over_MC = 999
            else: data_over_MC = dataNevents / N_allMC 
            
            h_grid.Fill(ixL,0,data_over_MC)
            h_grid.Fill(ixL,1,dataNevents)
            h_grid.Fill(ixL,2,N_allMC)
            for ie,numEvents in enumerate(MC_Nevents):
                h_grid.Fill(ixL,ie+3,numEvents)
            
        # for gl_i,gl in enumerate(args.GridLabels):
        #     h_grid.GetXaxis().SetBinLabel(gl_i+1,gl)
        #     # file_name = gl + "_limits/HHWWgg_v2-3_2017_" + ml + "_" + gl + "_HHWWgg_qqlnu.root"
        #     # limit = getLimits(file_name)
        #     # m2sig, m1sig, median, p1sig, p2sig = limit[0], limit[1], limit[2], limit[3], limit[4] 
        #     limits = [m2sig, m1sig, median, p1sig, p2sig]
        #     for il,l in enumerate(limits):
        #         h_grid.Fill(gl_i,il,l)
        #     if(median < lowestMedianVal): 
        #         lowestMedianVal = median 
        #         lowestMedianLabel = gl 
        #         lowestMedianIndex = gl_i
        #     if(median > highestMedianVal): 
        #         highestMedianVal = median 
        #         highestMedianLabel = gl 
        #         highestMedianIndex = gl_i                    

        # lowestLabel = "#color[3]{%s}"%(lowestMedianLabel) # color label with lowest median limit 
        # highestLabel = "#color[2]{%s}"%(highestMedianLabel) # color label with lowest median limit 

        # h_grid.GetXaxis().SetBinLabel(lowestMedianIndex+1,lowestLabel)
        # h_grid.GetXaxis().SetBinLabel(highestMedianIndex+1,highestLabel)

        # h_grid.SetMarkerSize(1.8)
        # label = TLatex()
        # label.SetNDC()
        # label.SetTextAngle(0)
        # label.SetTextColor(kBlack)
        # label.SetTextFont(42)
        # label.SetTextSize(0.045)
        # label.SetLineWidth(2)

        # outNamepng = "%s/%s_grid.png"%(ol_,ml)
        # outNamepdf = "%s/%s_grid.pdf"%(ol_,ml)
        # outNamepng = "%s/EventsTable_%s.png"%(ol_,selections)
        # outNamepdf = "%s/EventsTable_%s.pdf"%(ol_,selections)    
        outNamepng = "%s/%s_EventsTable_%s.png"%(ol_,firstCutBatch,outLabel)
        outNamepdf = "%s/%s_EventsTable_%s.pdf"%(ol_,firstCutBatch,outLabel)       
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