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

    ##-- Apply 4 4-jet
    elif(CutsType == "4Jet-Sel"):
        cuts = ["1"]
        # cuts = ["((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)"]
        cutNames = ["4Jet-Sel"]

    ##-- Apply 4 4-jet
    elif(CutsType == "4Jet-SelPhoPt"):
        cuts = ["(HGGCandidate_pt>100)"]
        # cuts = ["((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)"]
        cutNames = ["4Jet-SelPhoPt"]

    ##-- Apply 4 4-jet
    elif(CutsType == "4Jet-Sel0"):
        # cuts = ["(passPhotonSels==1)"]
        cuts = ["((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)"]
        cutNames = ["4Jet-Sel0"]

    ##-- Apply 4 4-jet
    elif(CutsType == "4Jet-Sel1"):
        # cuts = ["(passPhotonSels==1)"]
        cuts = ["((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)*(passPhotonSels==1)"]
        cutNames = ["4Jet-Sel1"]

    elif(CutsType == "4Jet-Sel2"):
        # cuts = ["(passPhotonSels==1)"]
        cuts = ["((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)*(passPhotonSels==1)*(AtLeast4GoodJets0Lep==1)"]
        cutNames = ["4Jet-Sel2"]

    elif(CutsType == "4Jet-Sel3"):
        # cuts = ["(passPhotonSels==1)"]
        cuts = ["((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)*(passPhotonSels==1)*(AtLeast4GoodJets0Lep==1)*(mW1_65To105==1)"]
        cutNames = ["4Jet-Sel3"]

    elif(CutsType == "4Jet-Sel4"):
        # cuts = ["(passPhotonSels==1)"]
        cuts = ["((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)*(passPhotonSels==1)*(AtLeast4GoodJets0Lep==1)*(mW1_65To105==1)*(mH_105To160==1)"]
        cutNames = ["4Jet-Sel4"]

    elif(CutsType == "4Jet-Sel5"):
        # cuts = ["(passPhotonSels==1)"]
        # cuts = ["((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)*(passPhotonSels==1)"]
        ##-- Electrons, Muons, Jets: Keep all analysis selections except dR, pT
        jetCuts = ""
        maxObjects = 5

        lepton_pt_cut = 10
        jet_pt_cut = 25

        photonCuts = "((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)"
        jetCuts = "(Leading_Jet_pt>25) && (Subleading_Jet_pt>25) && (fabs(Subleading_Jet_eta)<=2.4) && (fabs(Leading_Jet_eta)<=2.4)"

        # cuts = ["( (((%s) + (%s)) == 1) && ((%s) >= 2) && (%s))"%(electronCuts,muonCuts,jetCuts,photonCuts)] # exactly one lepton passing looser selections, at least two jets passing looser selections
        cuts = ["((%s))"%(photonCuts)] # exactly one lepton passing looser selections, at least two jets passing looser selections
        cuts = ["(%s) && (%s)"%(photonCuts,jetCuts)]
        print"4Jet-Sel5 cuts:",cuts
        #
        cutNames = ["4Jet-Sel5"]

    elif(CutsType == "4Jet-Sel6"):
        # cuts = ["(passPhotonSels==1)"]
        cuts = ["((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)*(passPhotonSels==1)"]
        cutNames = ["4Jet-Sel6"]

    elif(CutsType == "4Jet-Sel7"):
        # cuts = ["(passPhotonSels==1)"]
        cuts = ["((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25)*(passPhotonSels==1)"]
        cutNames = ["4Jet-Sel7"]

    ##-- Apply 4 4-jet
    elif(CutsType == "4Jet-Sel99"):
        cuts = ["(passbVeto==1)*(passPhotonSels==1)*(AtLeast4GoodJets0Lep==1)*(mW1_65To105==1)*(mH_105To160)"]
        cutNames = ["4Jet-Sel99"]

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
def CreateYieldsTables(cutBatchTag_pairs,dataNevents_list,MC_names,MC_Nevents_lists,MC_Nevents_noweight_lists,ol_):
# def CreateEventsTable(cutCatPairs,dataNevents,MC_Nevents,MC_names):
    print'Creating table of nEvents'
    # yaxisLabels = ['2.5%','16%','50%','84%','97.5%'] # Backgrounds, Background Total, Data
    yaxisLabels = []
    yaxisLabels.append("Data / MC")
    yaxisLabels.append("Data (Blinded)")
    yaxisLabels.append("all_MC")
    for MC_name in MC_names:
        print "=> ",MC_name
        yaxisLabels.append(MC_name)
    xaxisLabels = []
    for cutTagPair in cutBatchTag_pairs:
        print "==> ",cutTagPair
        xaxisLabels.append(cutTagPair)
    firstCutBatch = xaxisLabels[0].split('_')[0]
    nyLabels = len(yaxisLabels)
    nxLabels = len(xaxisLabels)
    N_allMC_list = []
    for MC_events_list in MC_Nevents_lists:
        N_allMC = sum(MC_events_list)
        print "===> ",MC_events_list,"\t",N_allMC
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