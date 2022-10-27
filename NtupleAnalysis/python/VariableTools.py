###########################################################################################################################
# Abraham Tishelman-Charny
# 15 June 2020
#
# The purpose of this module is to define variable related objects
###########################################################################################################################

import numpy as np

##-- Get variables to plot based on user input variable batch name
def GetVars(VarBatch):

    ##-- Definitions of some special variables, created from existing branch values
    mjj = "sqrt(2*goodJets_0_pt*goodJets_1_pt*(cosh(goodJets_0_eta-goodJets_1_eta)-cos(goodJets_0_phi-goodJets_1_phi)))"
    e_mT = "sqrt(2*goodElectrons_0_pt*MET_pt*(1-cos(goodElectrons_0_phi-MET_phi)))"
    mu_mT = "sqrt(2*goodMuons_0_pt*MET_pt*(1-cos(goodMuons_0_phi-MET_phi)))"
    dr_gg = "sqrt( fabs(Leading_Photon_eta - Subleading_Photon_eta)**2 + fabs( Leading_Photon_phi - Subleading_Photon_phi )**2  )"
    dr_jj = "sqrt( fabs(allJets_0_eta - allJets_1_eta)**2 + fabs( allJets_0_phi - allJets_1_phi )**2  )"
    pT_gg = "Leading_Photon_pt + Subleading_Photon_pt"
    Scaled_Leading_Photon_pt = "(Leading_Photon_pt / CMS_hgg_mass)"
    Scaled_Subleading_Photon_pt = "(Subleading_Photon_pt / CMS_hgg_mass)"
    Scaled_Leading_Photon_E = "(Leading_Photon_E / CMS_hgg_mass)"
    Scaled_Subleading_Photon_E = "(Subleading_Photon_E / CMS_hgg_mass)"
    Leading_Jet_bscore = "(goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probb + goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probbb + goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_problepb)"
    Subleading_Jet_bscore = "(goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probb + goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probbb + goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_problepb)"
    Subleading2_Jet_bscore = "(goodJets_2_bDiscriminator_mini_pfDeepFlavourJetTags_probb + goodJets_2_bDiscriminator_mini_pfDeepFlavourJetTags_probbb + goodJets_2_bDiscriminator_mini_pfDeepFlavourJetTags_problepb)"
    Subleading3_Jet_bscore = "(goodJets_3_bDiscriminator_mini_pfDeepFlavourJetTags_probb + goodJets_3_bDiscriminator_mini_pfDeepFlavourJetTags_probbb + goodJets_3_bDiscriminator_mini_pfDeepFlavourJetTags_problepb)"
    Subleading4_Jet_bscore = "(goodJets_4_bDiscriminator_mini_pfDeepFlavourJetTags_probb + goodJets_4_bDiscriminator_mini_pfDeepFlavourJetTags_probbb + goodJets_4_bDiscriminator_mini_pfDeepFlavourJetTags_problepb)"

    ##-- Variable batch definitions

    # Just diphoton mass
    # make dictionary
    if(VarBatch == "mass"):
        return ["CMS_hgg_mass"]
    elif(VarBatch == "DNN"):
        return ["evalDNN"]
    elif(VarBatch == "FHDNN"):
        TrainingVars = [
        "evalDNN_WWvsAll",
        "evalDNN_BBvsAll",
        "CMS_hgg_mass",
        "PhotonID_min",
        "PhotonID_max"
        ]
        return TrainingVars

    elif(VarBatch == "Jet"):
        return ["Leading_Jet_pt","Leading_Jet_E","Leading_Jet_eta","N_goodJets"]

    elif(VarBatch == "Ngood"):
        return ["N_goodElectrons","N_goodMuons","N_goodLeptons","N_goodJets"]

    elif(VarBatch == "LeadPhopt"):
        return ["Leading_Photon_pt"]

    elif(VarBatch == "diphopt"):
        return [pT_gg]

    elif(VarBatch == "TrainingVariables"):
        TrainingVars = [
            "evalDNN_HH",
            "METCor_phi", # just to check
            # "evalDNN",
            Scaled_Leading_Photon_pt,
            "goodJets_0_pt",
            "goodLepton_pt",
            "Wmass_goodJets12",
            Scaled_Subleading_Photon_pt,
            "goodJets_1_E",
            "goodJets_1_pt",
            "goodLepton_E",
            "METCor_pt",
            "goodJets_0_E",
            "goodLepton_phi",
            "Leading_Photon_MVA",
            "goodLepton_eta",
            "goodJets_1_eta",
            "goodJets_1_phi",
            "Subleading_Photon_eta",
            Leading_Jet_bscore,
            Subleading_Jet_bscore,
            "Subleading_Photon_phi",
            "N_goodJets",
            "goodJets_0_phi",
            Scaled_Leading_Photon_E,
            Scaled_Subleading_Photon_E,
            "Leading_Photon_phi",
            "Subleading_Photon_MVA",
            "goodJets_0_eta",
            "Leading_Photon_eta",
            "Wmt_L"
        ]
        return TrainingVars

    # elif(VarBatch == "RestOfTrainingVars"):
    #     RestOfTrainingVars = [
    #         "goodLepton_phi",
    #         "Leading_Photon_MVA",
    #         "goodLepton_eta",
    #         "goodJets_1_eta",
    #         "goodJets_1_phi",
    #         "Subleading_Photon_eta",
    #         Leading_Jet_bscore,
    #         Subleading_Jet_bscore,
    #         "Subleading_Photon_phi",
    #         "N_goodJets",
    #         "goodJets_0_phi",
    #         Scaled_Leading_Photon_E,
    #         Scaled_Subleading_Photon_E,
    #         "Leading_Photon_phi",
    #         "Subleading_Photon_MVA",
    #         "goodJets_0_eta",
    #         "Leading_Photon_eta",
    #         "Wmt_L"

    #     ]
    #     return RestOfTrainingVars

    # Some potentially useful MVA variables
    elif(VarBatch == "ThreeTopVar_FH"):
        TrainingVars = [
        # "New_DR_gg",
        # Scaled_Leading_Photon_pt,
        # "New_pTBasedSel_WW_pT",
        "New_DPhi_gg",
        "New_SumTwoMaxBScore",
        "New_pTBasedSel_a_costheta2",
        "CMS_hgg_mass",
        # "evalDNN_WWvsAll"
        ]
        return TrainingVars
    elif(VarBatch == "FH_DNN_TrainingVars"):
        TrainingVars = [
        "evalDNN_WWvsAll",
        "CMS_hgg_mass",
        Scaled_Leading_Photon_pt,
        Scaled_Subleading_Photon_pt,
        Scaled_Leading_Photon_E,
        Scaled_Subleading_Photon_E,
        "Leading_Photon_eta",
        "Leading_Photon_phi",
        "Subleading_Photon_eta",
        "Subleading_Photon_phi",

        "New_DPhi_gg",
        "New_DR_gg",
        "PhotonID_min",
        "PhotonID_max",

        "N_goodJets",
        "New_SumTwoMaxBScore",

        "goodJets_0_pt",
        "goodJets_0_eta",
        "goodJets_0_phi",
        "goodJets_0_E",
        "goodJets_1_pt",
        "goodJets_1_eta",
        "goodJets_1_phi",
        "goodJets_1_E",

        "goodJets_2_pt",
        "goodJets_2_eta",
        "goodJets_2_phi",
        "goodJets_2_E",
        "goodJets_3_pt",
        "goodJets_3_eta",
        "goodJets_3_phi",
        "goodJets_3_E",
        "goodJets_4_pt",
        "goodJets_4_eta",
        "goodJets_4_phi",
        "goodJets_4_E",

        Leading_Jet_bscore,
        Subleading_Jet_bscore,
        Subleading2_Jet_bscore,
        Subleading3_Jet_bscore,
        Subleading4_Jet_bscore,

        "New_pTBasedSel_minDeltaR_gg4j",
        "New_pTBasedSel_maxDeltaR_gg4j",
        "New_pTBasedSel_minDeltaR_4j",
        "New_pTBasedSel_maxDeltaR_4j",

        "New_pTBasedSel_DPhi_HH",
        "New_pTBasedSel_DR_HH",

        "New_pTBasedSel_a_costheta1",
        "New_pTBasedSel_a_costheta2",
        "New_pTBasedSel_a_costhetastar",
        "New_pTBasedSel_a_Phi",
        "New_pTBasedSel_a_Phi1",
        "New_pTBasedSel_HelicityCostheta1",
        "New_pTBasedSel_HelicityCostheta2",

        "New_pTBasedSel_W1_pT",
        "New_pTBasedSel_W1_eta",
        "New_pTBasedSel_W1_mass",

        "New_pTBasedSel_W2_pT",
        "New_pTBasedSel_W2_eta",
        "New_pTBasedSel_W2_mass",

        "New_pTBasedSel_WW_pT",
        "New_pTBasedSel_WW_eta",
        "New_pTBasedSel_WW_mass"
        ]
        return TrainingVars
    elif(VarBatch == "FH_DNN"):
        L2vars =  [
            "evalDNN_WWvsAll",
            "CMS_hgg_mass",
            Scaled_Leading_Photon_E,
            Scaled_Subleading_Photon_E,
            "Leading_Photon_MVA",
            "Subleading_Photon_MVA",
            "Leading_Photon_SC_eta",
            "Leading_Photon_r9",
            "Leading_Photon_passElectronVeto",
            "Leading_Photon_hasPixelSeed",
            "Subleading_Photon_r9",
            "Subleading_Photon_passElectronVeto"
            "Subleading_Photon_hasPixelSeed",
            "Leading_Photon_E",
            "Leading_Photon_pt",
            "Leading_Photon_eta",
            "Leading_Photon_phi",
            "Subleading_Photon_E",
            "Subleading_Photon_pt",
            "Subleading_Photon_eta",
            "Subleading_Photon_phi",
            "PhotonID_min",
            "PhotonID_max",
            "N_goodJets",
            "New_Leading_Jet_E",
            "New_Leading_Jet_pt",
            "New_Leading_Jet_px",
            "New_Leading_Jet_py",
            "New_Leading_Jet_pz",
            "New_Leading_Jet_eta",
            "New_Leading_Jet_phi",
            "New_Subleading_Jet_E",
            "New_Subleading_Jet_pt",
            "New_Subleading_Jet_px",
            "New_Subleading_Jet_py",
            "New_Subleading_Jet_pz",
            "New_Subleading_Jet_eta",
            "New_Subleading_Jet_phi",
            "New_Sub2leading_Jet_E",
            "New_Sub2leading_Jet_pt",
            "New_Sub2leading_Jet_px",
            "New_Sub2leading_Jet_py",
            "New_Sub2leading_Jet_pz",
            "New_Sub2leading_Jet_eta",
            "New_Sub2leading_Jet_phi",
            "New_Sub3leading_Jet_E",
            "New_Sub3leading_Jet_pt",
            "New_Sub3leading_Jet_px",
            "New_Sub3leading_Jet_py",
            "New_Sub3leading_Jet_pz",
            "New_Sub3leading_Jet_eta",
            "New_Sub3leading_Jet_phi",
            "New_OnShellW_LeadingJet_bDis",
            "New_OnShellW_SubLeadingJet_bDis",
            "New_OffShellW_LeadingJet_bDis",
            "New_OffShellW_SubLeadingJet_bDis",
            "New_OnShellW_E",
            "New_OnShellW_Mass",
            "New_OnShellW_pt",
            "New_OnShellW_px",
            "New_OnShellW_py",
            "New_OnShellW_pz",
            "New_OnShellW_eta",
            "New_OnShellW_phi",
            "New_OffShellW_E",
            "New_OffShellW_Mass",
            "New_OffShellW_pt",
            "New_OffShellW_px",
            "New_OffShellW_py",
            "New_OffShellW_pz",
            "New_OffShellW_eta",
            "New_OffShellW_phi",
            "New_HWW_E",
            "New_HWW_Mass",
            "New_HWW_pt",
            "New_HWW_px",
            "New_HWW_py",
            "New_HWW_pz",
            "New_HWW_eta",
            "New_HWW_phi",
            "HGGCandidate_pt", "HGGCandidate_eta", "HGGCandidate_phi",
            "New_dR_Hgg_Jet1",
            "New_dR_Hgg_Jet2",
            "New_dR_Hgg_Jet3",
            "New_dR_Hgg_Jet4",
            "New_dPhi_Hgg_Jet1",
            "New_dPhi_Hgg_Jet2",
            "New_dPhi_Hgg_Jet3",
            "New_dPhi_Hgg_Jet4",
            "New_DPhi_gg",
            "New_DR_gg",
            "New_DPhi_HH",
            "New_DR_HH",
            "New_minDeltaR_gg4j",
            "New_maxDeltaR_gg4j",
            "New_minDeltaR_4j",
            "New_maxDeltaR_4j",
            "a_costheta1",
            "a_costheta2",
            "a_costhetastar",
            "a_Phi",
            "a_Phi1",
            "CosThetaStar_CS",
            "CosThetaStar_CS_old",
            "HelicityCostheta1",
            "HelicityCostheta2",
            "MET_pt","MET_phi"
            ]
        return L2vars

    # Some potentially useful MVA variables
    elif(VarBatch == "MVA"):
        L2vars =  [
            "CMS_hgg_mass",
            "Leading_Photon_pt","Leading_Photon_eta","Leading_Photon_E","Leading_Photon_MVA",
            "Subleading_Photon_pt","Subleading_Photon_eta","Subleading_Photon_E","Subleading_Photon_MVA",
            "N_allElectrons","N_allMuons","N_allJets",
            "N_goodElectrons","N_goodMuons","N_goodJets",
            "goodElectrons_0_pt","goodMuons_0_pt",
            "goodJets_0_pt","goodJets_1_pt",
            "MET_pt"
            ]
        return L2vars

    # More possible MVA variables
    elif(VarBatch == "MVA2"):
        L2vars =  [
            "Leading_Photon_eta", "Leading_Photon_phi",
            "Subleading_Photon_eta", "Subleading_Photon_phi",
            "goodElectrons_0_eta", "goodElectrons_0_phi", "goodElectrons_0_E",
            "goodMuons_0_eta", "goodMuons_0_phi", "goodMuons_0_E",
            "goodJets_0_eta", "goodJets_0_phi", "goodJets_0_E",
            "goodJets_1_eta", "goodJets_1_phi", "goodJets_1_E",
            "MET_phi"
            ]
        return L2vars

    # MET variables
    elif(VarBatch == "MET"):
        METvars = [
            "MET_pt","MET_phi"
        ]
        return METvars

    # Photon variables
    elif(VarBatch == "Photon"):
        PhotonVars = [
            "Leading_Photon_pt","Leading_Photon_eta","Leading_Photon_E","Leading_Photon_MVA",
            "Subleading_Photon_pt","Subleading_Photon_eta","Subleading_Photon_E","Subleading_Photon_MVA"
        ]
        return PhotonVars

    # Photon variables
    elif(VarBatch == "LeadingPhoton"):
        PhotonVars = [
            "Leading_Photon_pt","Leading_Photon_eta","Leading_Photon_E","Leading_Photon_MVA"
        ]
        return PhotonVars

    elif(VarBatch =="bScores"):
        bScores = []
        scores = ['bDiscriminator_mini_pfDeepFlavourJetTags_probb','bDiscriminator_mini_pfDeepFlavourJetTags_probbb','bDiscriminator_mini_pfDeepFlavourJetTags_problepb']
        # scoresum = "(goodJets_0_%s + goodJets_0_%s + goodJets_0_%s)"%(scores[0],scores[1],scores[2])
        # bScores.append(scoresum)
        for score in scores:
            bScores.append("goodJets_0_%s"%(score))
        return bScores

    # Variables that should be combined with Loose cuts. Plots kinematics of leading lepton (which changes event by event)
    elif(VarBatch == "Loose"):
        LooseVars = []
        LooseVarsNames = []
        kinVars = ["pt","eta","E"]
        maxObjects = 5
        lepton_pt_cut = 10
        for kinVar in kinVars:
            LooseGoodLepton_var = ""
            for i in range(0,maxObjects):
                elec, muon = "allElectrons_%s"%(i), "allMuons_%s"%(i)
                elecCut = "( (%s_pt >= %s) && (%s_passLooseId==1 && (fabs(%s_eta)<1.4442 || ((fabs(%s_eta)>1.566 && fabs(%s_eta)<2.5) ) ) ) )"%(elec,lepton_pt_cut,elec,elec,elec,elec)
                muonCut = "((%s_pt >= %s && %s_isTightMuon==1 && fabs(%s_eta)<=2.4))"%(muon,lepton_pt_cut,muon,muon)
                varMatrixElement = "((%s_%s*%s) + (%s_%s*%s))"%(elec,kinVar,elecCut,muon,kinVar,muonCut)
                LooseGoodLepton_var += varMatrixElement
                if(i != maxObjects-1): LooseGoodLepton_var += " + "
            LooseVars.append(LooseGoodLepton_var)
            LooseVarsNames.append("Loose-Good_Lepton_%s"%(kinVar))
        return LooseVars,LooseVarsNames

    # All known tree variables. This is a LOT
    elif(VarBatch == "all"):
        finalStateVars_ = []
        ##-- Add lepton, jet variables
        # p4_variables = ["E","pt","px","py","pz","eta","phi"]
        p4_variables = ["E","pt","eta","phi"]
        checkN = 3
        objectVectors = []
        objs = ["Electrons","Muons","Jets"]
        vecTypes = ["all","good"]
        for t in vecTypes:
            for o in objs:
                objVec = "%s%s"%(t,o)
                objectVectors.append(objVec)
        for objV in objectVectors:
            vtitle = "N_%s"%(objV)
            entry = "%s"%(vtitle)
            finalStateVars_.append(entry)
            for v in p4_variables:
                for i in range(checkN):
                    vtitle = "%s_%s_%s"%(objV,i,v)
                    entry = "%s"%(vtitle)
                    finalStateVars_.append(entry)
            if("Electrons" in objV):
                eVars = ["passLooseId","passMediumId","passTightId","passMVALooseId","passMVAMediumId","passMVATightId"]
                for eV in eVars:
                    for i in range(checkN):
                        vtitle = "%s_%s_%s"%(objV,i,eV)
                        entry = "%s"%(vtitle)
                        finalStateVars_.append(entry)
            if("Muons" in objV):
                mVars = ["pfIsolationR04().sumChargedHadronPt","pfIsolationR04().sumNeutralHadronEt","pfIsolationR04().sumPhotonEt",
                            "pfIsolationR04().sumPUPt"]
                mVarTitles = ["sumChargedHadronPt","sumNeutralHadronEt","sumPhotonEt","sumPUPt"]
                for imV,mV in enumerate(mVars):
                    mVarTitle = mVarTitles[imV]
                    for i in range(checkN):
                        vtitle = "%s_%s_%s"%(objV,i,mVarTitle)
                        entry = "%s"%(vtitle)
                        finalStateVars_.append(entry)

            if("Jets" in objV):
                bscores = ["bDiscriminator('mini_pfDeepFlavourJetTags:probb')","bDiscriminator('pfDeepCSVJetTags:probb')",
                            "bDiscriminator('mini_pfDeepFlavourJetTags:probbb')","bDiscriminator('pfDeepCSVJetTags:probbb')"]

                btitles = ["bDiscriminator_mini_pfDeepFlavourJetTags_probb","bDiscriminator_pfDeepCSVJetTags_probb",
                            "bDiscriminator_mini_pfDeepFlavourJetTags_probbb","bDiscriminator_pfDeepCSVJetTags_probbb"
                            ]
                for ib,bscore in enumerate(bscores):
                    btitle = btitles[ib]
                    for i in range(checkN):
                        vtitle = "%s_%s_%s"%(objV,i,btitle)
                        entry = "%s"%(vtitle)
                        finalStateVars_.append(entry)

        # finalStateVars_.append("Leading_Photon_genMatchType")
        # finalStateVars_.append("Subleading_Photon_genMatchType")

        ##-- Add photon variables
        objects = ["Leading_Photon","Subleading_Photon","MET"]
        finalStateVars_.append("Leading_Photon_MVA")
        finalStateVars_.append("Subleading_Photon_MVA")
        for obj in objects:
            for var in p4_variables:
                vtitle = "%s_%s"%(obj,var)
                finalStateVars_.append(vtitle)

        return finalStateVars_

    # Just dR between two leading jets
    elif(VarBatch == "special"):
        return [dr_jj]

##-- Get bins for a variable
def GetBins(variable_,DNNbinWidth_):
# def GetBins(variable_,DNNbinWidth_ = 0.1):

    # evalDNNmin, evalDNNmax = 0, 1.00001
    # evalDNNmin, evalDNNmax = 0.9, 1.00001
    # evalDNNmin, evalDNNmax = 0, 1.00001
    evalDNNmin, evalDNNmax = 0.1, 1
    nDNNbins = int(float((evalDNNmax - evalDNNmin)) / float(DNNbinWidth_))

    if(DNNbinWidth_ != 0.1):
        print"nDNNbins: ",nDNNbins
    # Specify bins for specific variables
    binDict = {
        "Leading_Photon_MVA": [20,-1,1],
        "Subleading_Photon_MVA": [20,-1,1],
        "CMS_hgg_mass": [16,100,180],
        "weight":[1000,-10,10],
        "puweight":[1000,-2,2],
        "mjj" : [100,0,300],
        "e_mT" : [100,0,300],
        "mu_mT" : [100,0,300],
        "dr_gg" : [60,0,3],
        "dr_jj" : [60,0,3],
        "pT_gg" : [40,0,400],

        "N_goodJets": [10, 4, 14],
        "goodJets_0_pt" : [18,0,360],
        "goodLepton_pt" : [18,0,360],
        "Wmass_goodJets12": [25,0,500],
        # "Subleading_Photon_pt/CMS_hgg_mass",
        "goodJets_1_E": [18,0,360],
        "goodJets_1_pt": [18,0,360],
        "goodJets_2_pt": [25,0,200],
        "goodJets_3_pt": [25,0,200],
        "goodJets_4_pt": [25,0,150],
        "goodJets_3_E": [21,0,300],
        "goodJets_4_E": [21,0,300],
        "goodLepton_E": [18,0,360],
        "METCor_pt": [40,0,400],
        "goodJets_0_E": [18,0,360],
        "Scaled_Leading_Photon_pt" : [30,0,3],
        "Scaled_Subleading_Photon_pt" : [15,0,1.5],
        "Scaled_Leading_Photon_E" : [30,0,3],
        "Scaled_Subleading_Photon_E" : [15,0,1.5],
        "Leading_Jet_bscore" : [11,0,1],
        "Subleading_Jet_bscore" : [11,0,1],
        "Subleading2_Jet_bscore" : [11,0,1],
        "Subleading3_Jet_bscore" : [11,0,1],
        "Subleading4_Jet_bscore" : [11,0,1],
        "Wmt_L" : [30,0,300],
        # "evalDNN" : [20,0,1.00001] # To include value == 1
        # "evalDNN" : [10,0,1.00001] # To include value == 1
        # "evalDNN" : [25,0,1.00001] # To include value == 1
        # "evalDNN" : [100,0,1.00001] # To include value == 1
        # "evalDNN_WWvsAll" : [nDNNbins,evalDNNmin,evalDNNmax], # To include value == 1
        "evalDNN_WWvsAll" : [20,0.1,1.0], # To include value == 1
        # "evalDNN_WWvsAll" : [10,0.974285714286,1.0], # To include value == 1 # Cat 0
        # "evalDNN_WWvsAll" : [5,0.961428571429,0.974285714286], # To include value == 1 # Cat 1
        # "evalDNN_WWvsAll" : [10,0.807142857143,0.961428571429], # To include value == 1 # Cat 2
        # "evalDNN_WWvsAll" : [10,0.807142857143,1.0], # To include value == 1 # Cat 012
        "evalDNN_BBvsAll" : [nDNNbins,evalDNNmin,evalDNNmax], # To include value == 1
        "Subleading_Photon_pt" : [24,0,120],
        # "evalDNN" : [10,0,1] # To include value == 1
        "HWWCandidate_M" : [25,50,1000],
        "HGGCandidate_pt": [25,100,500],
        "PhotonID_min": [10,-1,1],
        "PhotonID_max": [10,-1,1],
        "a_costheta1": [10,-1,1],
        "a_costheta2": [10,-1,1],
        "CosThetaStar_CS": [10, -1, 1],
        "CosThetaStar_CS_old": [10, -1, 1],
        "HelicityCostheta1": [10, -1, 1],
        "HelicityCostheta2": [10, -1, 1],
        "a_costhetastar": [10,-1,1],
        "a_Phi": [10,-1,1],
        "a_Phi1": [10,-1,1],
        "W2Candidate_M": [25,0,300],
        "W2Candidate_pt": [25,0,400],
        "New_DPhi_gg": [20,-3.14,3.14],
        "New_DR_gg": [10,0,4],
        "New_DPhi_HH": [20,-3.14,3.14],
        "New_DR_HH": [20,0,6],
        "New_HWW_E": [50, 80, 1000],
        "New_HWW_Mass": [50, 80, 1000],
        "New_OnShellW_E": [50, 0, 700],
        "New_OnShellW_Mass": [50, 0, 200],
    }
    specialVars = ["Subleading_Photon_pt","Leading_Photon_MVA","Subleading_Photon_MVA","CMS_hgg_mass","weight","puweight","mjj","e_mT","mu_mT","dr_gg","dr_jj","pT_gg","evalDNN",
                    "N_goodJets",
                    "goodJets_0_pt", "goodLepton_pt", "Wmass_goodJets12", "goodJets_1_E", "goodJets_1_pt", "goodLepton_E", "METCor_pt", "goodJets_0_E",
                    "goodJets_2_pt","goodJets_3_pt","goodJets_4_pt","goodJets_3_E","goodJets_4_E",
                    "Scaled_Leading_Photon_pt", "Scaled_Subleading_Photon_pt",
                    "Leading_Jet_bscore", "Subleading_Jet_bscore", "Subleading2_Jet_bscore", "Subleading3_Jet_bscore","Subleading4_Jet_bscore",
                     "Scaled_Leading_Photon_E", "Scaled_Subleading_Photon_E", "Wmt_L","HWWCandidate_M", "HGGCandidate_pt",
                    "PhotonID_min", "PhotonID_max",
                    "a_costheta1", "a_costheta2", "a_Phi", "a_Phi1",
                    "a_costhetastar", "W2Candidate_M", "W2Candidate_pt",
                    "New_DPhi_gg", "New_DR_gg",
                    "New_DPhi_HH", "New_DR_HH",
                    "CosThetaStar_CS",
                    "CosThetaStar_CS_old",
                    "HelicityCostheta1",
                    "HelicityCostheta2",
                    "New_HWW_E",
                    "New_HWW_Mass",
                    "New_OnShellW_E",
                    "New_OnShellW_Mass", "evalDNN_WWvsAll", "evalDNN_BBvsAll"
    ]

    scores = ['bDiscriminator_mini_pfDeepFlavourJetTags_probb','bDiscriminator_mini_pfDeepFlavourJetTags_probbb','bDiscriminator_mini_pfDeepFlavourJetTags_problepb']
    scoresum = "(goodJets_0_%s + goodJets_0_%s + goodJets_0_%s)"%(scores[0],scores[1],scores[2])
    if variable_ == scoresum: return [50,0,1]
    if variable_ in specialVars:
        return binDict[variable_]

    # If variable is a number of objects
    elif "N_" in variable_:
        return [10,0,10]

    # Specified binning if variable has phi, eta or pt in name
    else:
        # if("phi" in variable_): return [20,-3.14,3.14]
        if("Costheta" in variable_): return [14,-1.,1.]
        if("costheta" in variable_): return [14,-1.,1.]
        if("phi" in variable_): return [14,-3.14,3.15]
        if("Phi" in variable_): return [14,-3.14,3.15]
        # elif("eta" in variable_): return [16,-4,4]
        elif("eta" in variable_): return [10,-2.5,2.5]
        elif ("pt" in variable_): return [30,0,400]
        elif ("_M" in variable_): return [55,0,200]
        elif ("WW_mass" in variable_): return [55,50,1200]
        elif ("DPhi" in variable_): return [10,-3.14,3.14]
        elif ("_dR_" in variable_): return [10,0,10]
        elif ("_DR_" in variable_): return [10,0,10]
        elif ("DeltaR" in variable_): return [10,0,10]
        elif ("_r9" in variable_): return [10,0,1.0]
        elif("bDiscriminator" in variable_): return [20,0,1]
        elif("BScore" in variable_): return [20,0,1]
        elif("bscore" in variable_): return [20,0,1]
        elif("bDis" in variable_): return [20,0,1]
        elif("dPhi_" in variable_): return [10,0,5]
        elif("hasPixelSeed" in variable_): return [2,0,2]
        elif("passElectron" in variable_): return [2,0,2]
        else: return [30,0,300] # if variable name meets none of the above conditions, default to this binning

##-- Get x axis title for ratio plot depending on the variable
def GetXaxisTitle(variable_):
    xAxisTitle = ""
    variableName = variable_
    variableUnit = ""

    variableUnitDict = {
        "CMS_hgg_mass": "GeV",
        "E" : "GeV",
        "pt" : "GeV",
        "eta" : "rad",
        "phi" : "rad",
        "MVA": "unitless",
        "weight":"unitless",
        "N_" : "unitless",
        "mjj": "GeV",
        "e_mT" : "GeV",
        "mu_mT" : "GeV",
        "dr_gg" : "rad",
        "dr_jj" : "rad",
        "New_DR_gg": "rad",
        "pT_gg" : "GeV",
        "DeepJetScore" : "unitless",
        "evalDNN" : "unitless",
        "evalDNN_HH" : "unitless",
        "Scaled_Leading_Photon_pt" : "unitless",
        "Scaled_Subleading_Photon_pt" : "unitless",
        "Leading_Jet_bscore" : "unitless",
        "Subleading_Jet_bscore" : "unitless",
        "Subleading2_Jet_bscore" : "unitless",
        "Subleading3_Jet_bscore" : "unitless",
        "Subleading4_Jet_bscore" : "unitless",
        "Scaled_Leading_Photon_E" : "unitless",
        "Scaled_Subleading_Photon_E" : "unitless",
        "Wmt_L" : "GeV",
        "New_pTBasedSel_WW_pT": "GeV",
        "New_DPhi_gg":"unitless",
        "New_SumTwoMaxBScore":"unitless",
        "New_pTBasedSel_a_costheta2":"unitless"
    }

    variableName_Rep = {
        "New_DR_gg": "#Delta R(#gamma #gamma)",
        "Scaled_Leading_Photon_pt": "p_{T}(#gamma #gamma)/M_{#gamma #gamma}",
        "New_pTBasedSel_WW_pT": "p_{T}(WW)",
        "evalDNN_WWvsAll": "DNN Score",
        "CMS_hgg_mass": "M_{#gamma #gamma}",
        "New_DPhi_gg":"#Delta #phi(#gamma #gamma)",
        "New_SumTwoMaxBScore":"Sum of two highest b-jet score",
        "New_pTBasedSel_a_costheta2":"cos(#theta_{2})"
    }

    for varRep in variableName_Rep:
        print "===> ",varRep, variableName
        if varRep in variableName:
            XAxisTitle_ = variableName_Rep[varRep]
            break
        else:
            XAxisTitle_ = variableName
    for varFrag in variableUnitDict:
        varUnit = variableUnitDict[varFrag]
        if varFrag in variableName: variableUnit = varUnit

    xAxisTitle = "%s [%s]"%(XAxisTitle_,variableUnit)
    if variableUnit ==  "unitless":
        xAxisTitle = "%s "%(XAxisTitle_)
    return xAxisTitle

##-- Get the name of variable. Useful for variables that have long strings in draw statement. This returns a shortened value to be used for plot title and output file name
def GetVarTitle(varName):
    varTitle = ""
    scores = ['bDiscriminator_mini_pfDeepFlavourJetTags_probb','bDiscriminator_mini_pfDeepFlavourJetTags_probbb','bDiscriminator_mini_pfDeepFlavourJetTags_problepb']
    # scoresum = "(goodJets_0_%s + goodJets_0_%s + goodJets_0_%s)"%(scores[0],scores[1],scores[2])
    mjj = "sqrt(2*goodJets_0_pt*goodJets_1_pt*(cosh(goodJets_0_eta-goodJets_1_eta)-cos(goodJets_0_phi-goodJets_1_phi)))"
    e_mT = "sqrt(2*goodElectrons_0_pt*MET_pt*(1-cos(goodElectrons_0_phi-MET_phi)))"
    mu_mT = "sqrt(2*goodMuons_0_pt*MET_pt*(1-cos(goodMuons_0_phi-MET_phi)))"
    dr_gg = "sqrt( fabs(Leading_Photon_eta - Subleading_Photon_eta)**2 + fabs( Leading_Photon_phi - Subleading_Photon_phi )**2  )"
    dr_jj = "sqrt( fabs(allJets_0_eta - allJets_1_eta)**2 + fabs( allJets_0_phi - allJets_1_phi )**2  )"
    pT_gg = "Leading_Photon_pt + Subleading_Photon_pt"
    Scaled_Leading_Photon_pt = "(Leading_Photon_pt / CMS_hgg_mass)"
    Scaled_Subleading_Photon_pt = "(Subleading_Photon_pt / CMS_hgg_mass)"
    Scaled_Leading_Photon_E = "(Leading_Photon_E / CMS_hgg_mass)"
    Scaled_Subleading_Photon_E = "(Subleading_Photon_E / CMS_hgg_mass)"
    Leading_Jet_bscore = "(goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probb + goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probbb + goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_problepb)"
    Subleading_Jet_bscore = "(goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probb + goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probbb + goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_problepb)"
    Subleading2_Jet_bscore = "(goodJets_2_bDiscriminator_mini_pfDeepFlavourJetTags_probb + goodJets_2_bDiscriminator_mini_pfDeepFlavourJetTags_probbb + goodJets_2_bDiscriminator_mini_pfDeepFlavourJetTags_problepb)"
    Subleading3_Jet_bscore = "(goodJets_3_bDiscriminator_mini_pfDeepFlavourJetTags_probb + goodJets_3_bDiscriminator_mini_pfDeepFlavourJetTags_probbb + goodJets_3_bDiscriminator_mini_pfDeepFlavourJetTags_problepb)"
    Subleading4_Jet_bscore = "(goodJets_4_bDiscriminator_mini_pfDeepFlavourJetTags_probb + goodJets_4_bDiscriminator_mini_pfDeepFlavourJetTags_probbb + goodJets_4_bDiscriminator_mini_pfDeepFlavourJetTags_problepb)"

    if(varName == mjj): varTitle = "mjj"
    elif(varName == e_mT): varTitle = "e_mT"
    elif(varName == mu_mT): varTitle = "mu_mT"
    elif(varName == dr_gg): varTitle = "dr_gg"
    # elif(varName == "New_DR_gg"): varTitle = "#Delta R(#gamma #gamma)"
    elif(varName == "New_DR_gg"): varTitle = "New_DR_gg"
    elif(varName == dr_jj): varTitle = "dr_jj"
    elif(varName == pT_gg): varTitle = "pT_gg"
    # elif(varName == scoresum): varTitle = "DeepJetScore"
    elif(varName == Scaled_Leading_Photon_pt): varTitle = "Scaled_Leading_Photon_pt"
    elif(varName == Scaled_Subleading_Photon_pt): varTitle = "Scaled_Subleading_Photon_pt"
    elif(varName == Scaled_Leading_Photon_E): varTitle = "Scaled_Leading_Photon_E"
    elif(varName == Scaled_Subleading_Photon_E): varTitle = "Scaled_Subleading_Photon_E"
    elif(varName == Leading_Jet_bscore) : varTitle = "Leading_Jet_bscore"
    elif(varName == Subleading_Jet_bscore): varTitle = "Subleading_Jet_bscore"
    elif(varName == Subleading2_Jet_bscore): varTitle = "Subleading2_Jet_bscore"
    elif(varName == Subleading3_Jet_bscore): varTitle = "Subleading3_Jet_bscore"
    elif(varName == Subleading4_Jet_bscore): varTitle = "Subleading4_Jet_bscore"
    elif(varName == "New_pTBasedSel_WW_pT"): varTitle = "New_pTBasedSel_WW_pT"
    else: varTitle = varName
    return varTitle

##-- Compute chi squared for a data / mc plot
def GetChiSquared(DataHist_,stackSum_):
    # the two histos should have the same binning
    Nbins = DataHist_.GetNbinsX()
    assert(Nbins == stackSum_.GetNbinsX())
    chi2_total = 0
    for bin_i in range(1,Nbins): # skip underflow bin
        data_y, MC_sum_y = DataHist_.GetBinContent(bin_i), stackSum_.GetBinContent(bin_i)
        chi2_num = pow(abs(float(data_y)-float(MC_sum_y)),2)
        # avoid a denominator of 0
        if(data_y == 0.0 and MC_sum_y == 0.0): continue
        elif(data_y == 0.0 and MC_sum_y != 0.0): chi2_den = MC_sum_y
        else: chi2_den = data_y
        # print"data_y:",data_y
        # print"MC_sum_y:",MC_sum_y
        chi2 = chi2_num / chi2_den
        chi2_total += chi2
    chi2_total /= Nbins
    return chi2_total
