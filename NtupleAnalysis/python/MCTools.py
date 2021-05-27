###########################################################################################################################
# Abraham Tishelman-Charny
# 15 June 2020
#
# The purpose of this module is to provide MC related variables and definitions to NtupleAnalysisTools.py
#
###########################################################################################################################

##-- Note: This module can be shrunk by mapping file name to treename, MCName, and MCCategory. Don't need dictionary for each one

def GetMCTreeNameOld(fileName_):
    MCTreesDict = {
        # 
        # "DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhotonJetsBox1BJet_MGG_80toInf_13TeV_Sherpa",
        # "DiPhotonJetsBox2BJets_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhotonJetsBox2BJets_MGG_80toInf_13TeV_Sherpa",

        "DiPhotonJetsBox_M40_80-Sherpa_Hadded.root" : "DiPhotonJetsBox_M40_80_Sherpa",
        "DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "DiPhotonJets_MGG_80toInf_13TeV_amcatnloFXFX_pythia8",
        "WW_TuneCP5_13TeV-pythia8_Hadded.root" : "WW_TuneCP5_13TeV_pythia8",

        # "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "GJets_HT_40To100_TuneCP5_13TeV_madgraphMLM_pythia8",
        # "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "GJets_HT_600ToInf_TuneCP5_13TeV_madgraphMLM_pythia8",
        "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "GluGluHToGG_M_125_13TeV_powheg_pythia8",
        "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8",
        "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa",
        
        "GJet_Pt-20to40.root" : "GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "GJet_Pt-40toInf.root" : "GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "GJet_Pt-20toInf.root" : "GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        
        #"GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        #"GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        #"GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        
        "QCD_Pt-30to40.root" : "QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "QCD_Pt-30toInf.root" : "QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        "QCD_Pt-40toInf.root" : "QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        
        #"QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        #"QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        #"QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",

        "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root" : "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8sethzenz_RunIIFall17_3_1_0_3_1_0_v1_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v2_dfb4aebb0a34a36b04b8bd8eb2ddfe46USER",
        "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "DYJetsToLL_M_50_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "VBFHToGG_M_125_13TeV_powheg_pythia8",
        "VBFHToGG_M125_13TeV_amcatnlo_pythia8_Hadded.root" : "VBFHToGG_M125_13TeV_amcatnlo_pythia8",
        "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root" : "TTGJets_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8",

        "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root" : "THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5",

        # HHWWgg_bkg_v2
        "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT_2500toInf_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT_600to800_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT_800to1200_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT_1200to2500_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTToHadronic_TuneCP5_13TeV-powheg-pythia8_Hadded.root" : "TTToHadronic_TuneCP5_13TeV_powheg_pythia8",

        # HHWWgg_bkg_v3
        "W1JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu_LHEWpT_100_150_TuneCP5_13TeV_amcnloFXFX_pythia8",

        # HHWWgg_bkg_v4
        "W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W3JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8",
        "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W4JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8",
        "W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_LHEWpT_100_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8",

        # HHWWgg_bkg_v5
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8.root": "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root":"ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root" : "WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8",

        ##-- HHWWgg Signal
        "GluGluToHHTo2G4Q_node_cHHH1_2017.root": "HHWWgg_SM",
        "ggF_SM_WWgg_qqlnugg_Hadded.root":"ggF_SM_WWgg_qqlnugg",
        "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root":"GluGluToHHTo_WWgg_qqlnu_nodeSM",
        "HHWWgg-SL-SM-NLO-2016.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV_powheg_pythia8alesauva_2016_1_10_6_4_v0_RunIISummer16MiniAODv3_PUMoriond17_94X_mcRun2_asymptotic_v3_v1_c3d8a5638586a0e8df7c55ce908b2878USER",
        "HHWWgg-SL-SM-NLO-2017.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
        "HHWWgg-SL-SM-NLO-2017-HggVtx-Trees_Hadded.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
        "HHWWgg-SL-SM-NLO-2018.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2018_1_10_6_4_v0_RunIIAutumn18MiniAOD_102X_upgrade2018_realistic_v15_v1_460d9a73477aa42da0177ac2dc7ecf49USER",
        "output_numEvent500.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8",
    
        ##-- Single Higgs
        "VBFHToGG_M125_13TeV_2016.root" : "vbf_125",
        "GluGluHToGG_M125_13TeV_2016.root" : "ggh_125",
        "VHToGG_M125_13TeV_2016.root" : "wzh_125",
        "VBFHToGG_M125_13TeV_2018.root" : "vbf_125",
        "GluGluHToGG_M125_13TeV_2018.root" : "ggh_125",
        "VHToGG_M125_13TeV_2018.root" : "wzh_125"
    }

    return MCTreesDict[fileName_]

def GetMCTreeName(fileName_):
    MCTreesDict = {
        #########################
        #       FH Trees        #
        #########################
        "DiPhotonJetsBox_MGG-80toInf_13TeV.root": "DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa",
        "GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV.root": "GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV.root": "GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        "GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf.root": "GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "GluGluHToGG_M125_TuneCP5_13TeV.root": "ggh_125",
        "QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV.root": "QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV.root": "QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        "QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf.root": "QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "allData_QCD_2017.root": "Data", # QCD from QCD_Data
        "Data_2017.root": "Data", # QCD from QCD_Data
        "datadrivenQCD_v2.root": "Data", # QCD from QCD_Data
        "TTGG_0Jets_TuneCP5_13TeV.root": "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8",
        "TTGJets_TuneCP5_13TeV.root": "TTGJets_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8",
        "TTJets_TuneCP5_13TeV.root": "TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "VBFHToGG_M125_13TeV.root": "vbf_125",
        "VHToGG_M125_13TeV.root": "wzh_125",
        "WW_TuneCP5_13TeV-pythia8.root": "WW_TuneCP5_13TeV_pythia8",
        "ttHJetToGG_M125_13TeV.root": "tth_125",
        "TTToHadronic_TuneCP5_13TeV-powheg-pythia8.root": "TTToHadronic_TuneCP5_13TeV_powheg_pythia8",

        # DY
        "DYJetsToLL_M-50_TuneCP5_13TeV.root": "DYJetsToLL_M_50_TuneCP5_13TeV_amcatnloFXFX_pythia8", # FH

        # DiPhoton + Jets
        "DiPhotonJetsBox_M40_80.root": "DiPhotonJetsBox_M40_80_Sherpa", # FH
        "DiPhotonJetsBox_M40_80_HHWWggTag_0_MoreVars.root" : "DiPhotonJetsBox_M40_80_Sherpa",
        "DiPhotonJets_MGG-80toInf_HHWWggTag_0_MoreVars.root" : "DiPhotonJets_MGG_80toInf_13TeV_amcatnloFXFX_pythia8",
        "WW_TuneCP5_HHWWggTag_0_MoreVars.root" : "WW_TuneCP5_13TeV_pythia8",
        "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded_HHWWggTag_0_MoreVars.root" : "GluGluHToGG_M_125_13TeV_powheg_pythia8",
        # "GluGluHToGG_HHWWggTag_0_MoreVars_noSyst.root" : "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8", 
        "GluGluHToGG_HHWWggTag_0_MoreVars_noSyst.root" : "ggh_125", 
        "GluGluHToGG_HHWWggTag_0_MoreVars.root" : "ggh_125", 
        # "ttHJetToGG_HHWWggTag_0_MoreVars_noSyst.root" : "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars.root" : "tth_125",
        "ttHJetToGG_HHWWggTag_0_MoreVars_noSyst.root" : "tth_125",
        "DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars.root" : "DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa",
        
        "GJet_Pt-20to40_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "GJet_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "GJet_Pt-20toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        
        # QCD
        "QCD_Pt-30to40_HHWWggTag_0_MoreVars.root" : "QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "QCD_Pt-30toInf_HHWWggTag_0_MoreVars.root" : "QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        "QCD_Pt-40toInf_HHWWggTag_0_MoreVars.root" : "QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",


        "QCD_HT50to100_TuneCP5_13TeV_hadd.root": "QCD_HT50to100_TuneCP5_13TeV_madgraphMLM_pythia8",
        "QCD_HT100to200_TuneCP5_13TeV_hadd.root": "QCD_HT100to200_TuneCP5_13TeV_madgraph_pythia8",
        "QCD_HT200to300_TuneCP5_13TeV_hadd.root": "QCD_HT200to300_TuneCP5_13TeV_madgraph_pythia8",
        "QCD_HT300to500_TuneCP5_13TeV_hadd.root": "QCD_HT300to500_TuneCP5_13TeV_madgraph_pythia8",
        "QCD_HT500to700_TuneCP5_13TeV_hadd.root": "QCD_HT500to700_TuneCP5_13TeV_madgraph_pythia8",
        "QCD_HT700to1000_TuneCP5_13TeV_hadd.root": "QCD_HT700to1000_TuneCP5_13TeV_madgraph_pythia8",
        "QCD_HT1000to1500_TuneCP5_13TeV_hadd.root": "QCD_HT1000to1500_TuneCP5_13TeV_madgraph_pythia8",
        "QCD_HT1500to2000_TuneCP5_13TeV_hadd.root": "QCD_HT1500to2000_TuneCP5_13TeV_madgraph_pythia8",
        "QCD_HT2000toInf_TuneCP5_13TeV_hadd.root": "QCD_HT2000toInf_TuneCP5_13TeV_madgraph_pythia8",
        
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "wzh_125",
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "wzh_125",
        # "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "TTGG_0Jets_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8",
        "DYJetsToLL_M-50_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "DYJetsToLL_M_50_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "VBFHToGG_M_125_13TeV_powheg_pythia8",
        # "TTJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "TTJets_TuneCP5_extra_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "TTGJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "TTGJets_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8",

        # "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5",
        "THQ_ctcvcp_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5",

        # HHWWgg_bkg_v2 
        "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT_2500toInf_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT_600to800_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT_800to1200_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT_1200to2500_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTToHadronic_HHWWggTag_0_MoreVars.root" : "TTToHadronic_TuneCP5_13TeV_powheg_pythia8",

        # HHWWgg_bkg_v3 
        "W1JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8", 
        "W1JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1JetsToLNu_LHEWpT_100_150_TuneCP5_13TeV_amcnloFXFX_pythia8",

        # HHWWgg_bkg_v4 
        "W2JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W3JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W3JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8",
        "W4JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W4JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8",
        "W2JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu_LHEWpT_100_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8",

        # HHWWgg_bkg_v5
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0_HHWWggTag_0_MoreVars.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8.root":"WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8", #FH
        "WGGJets_HHWWggTag_0_MoreVars.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WWTo1L1Nu2Q_HHWWggTag_0_MoreVars.root": "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8",
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8.root": "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8.root":"ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WGJJToLNuGJJ_EWK_HHWWggTag_0_MoreVars.root" : "WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8",
        "WGJJToLNu_EWK_QCD_HHWWggTag_0_MoreVars.root" : "WGJJToLNu_EWK_QCD_TuneCP5_13TeV_madgraph_pythia8",
        "WGJJToLNu_EWK_QCD_TuneCP5_13TeV-madgraph-pythia8.root" : "WGJJToLNu_EWK_QCD_TuneCP5_13TeV_madgraph_pythia8",
        # "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8_HHWWggTag_0_MoreVars.root" : "WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8",

        ##-- HHWWgg Signal
        "GluGluToHHTo2G4Q_node_cHHH1_2017.root": "GluGluToHHTo2G4Q_node_cHHH1",
        # "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1",
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_even_MoreVars.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1",
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_even_MoreVars.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1",
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1",
        # "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1",
        # "ggF_SM_WWgg_qqlnugg_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root":"ggF_SM_WWgg_qqlnugg",
        # "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus_HHWWggTag_0_MoreVars_kinWeight_noHgg.root":"GluGluToHHTo_WWgg_qqlnu_nodeSM",
        # "HHWWgg-SL-SM-NLO-2016_HHWWggTag_0_MoreVars_kinWeight_noHgg.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV_powheg_pythia8alesauva_2016_1_10_6_4_v0_RunIISummer16MiniAODv3_PUMoriond17_94X_mcRun2_asymptotic_v3_v1_c3d8a5638586a0e8df7c55ce908b2878USER",
        # "HHWWgg-SL-SM-NLO-2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
        # "HHWWgg-SL-SM-NLO-2017-HggVtx-Trees_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
        # "HHWWgg-SL-SM-NLO-2018_HHWWggTag_0_MoreVars_kinWeight_noHgg.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2018_1_10_6_4_v0_RunIIAutumn18MiniAOD_102X_upgrade2018_realistic_v15_v1_460d9a73477aa42da0177ac2dc7ecf49USER",
        # "output_numEvent500_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8",
    
        ##-- Single Higgs
        "VBFHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "vbf_125",
        "VBFHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "vbf_125",
        "VBFHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "vbf_125",
        "GluGluHToGG_M125_13TeV_2016_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "ggh_125",
        "GluGluHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "ggh_125",
        # "VHToGG_M125_13TeV_2016_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "wzh_125",
        "VHToGG_2017_HHWWggTag_0.root" : "wzh_125",
        "VBFHToGG_M125_13TeV_2018_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "vbf_125",
        "GluGluHToGG_M125_13TeV_2018_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "ggh_125",
        "VHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "wzh_125"
    }

    return MCTreesDict[fileName_]

def GetMCName(fileName_):
    MCNameDict = {
        "DiPhotonJetsBox_MGG-80toInf_13TeV.root": "DiPhoJets_MGG-80toInf",  # FH
        "GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV.root": "GJet_20to40",  # FH
        "GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV.root": "GJet_20toInf",  # FH
        "GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf.root": "GJet_40toInf",  # FH
        "QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV.root": "QCD_30to40",  # FH
        "QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV.root": "QCD_30toInf",  # FH
        "QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf.root": "QCD_40toInf",  # FH
        "allData_QCD_2017.root": "QCD_Data", # QCD from Data
        "Data_2017.root": "QCD_Data", # QCD from Data
        "datadrivenQCD_v2.root": "QCD_Data", # QCD from QCD_Data
        "TTGG_0Jets_TuneCP5_13TeV.root": "TTGG_0Jets",  # FH
        "TTGJets_TuneCP5_13TeV.root": "TTGJets",  # FH
        "TTJets_TuneCP5_13TeV.root": "TTJets",  # FH
        "WW_TuneCP5_13TeV-pythia8.root": "WW",  # FH
        "GluGluHToGG_M125_TuneCP5_13TeV.root": "ggh_125",  # FH
        "VBFHToGG_M125_13TeV.root": "vbf_125",  # FH
        "VHToGG_M125_13TeV.root": "wzh_125",  # FH
        "ttHJetToGG_M125_13TeV.root": "tth_125",  # FH
        "TTToHadronic_TuneCP5_13TeV-powheg-pythia8.root": "TTToHadronic",

        "DiPhotonJetsBox_M40_80.root": "DiPhoJetsBox_M40_80", # FH
        "DiPhotonJetsBox_M40_80_HHWWggTag_0_MoreVars.root" : "DiPhoJetsBox_M40_80",
        "DiPhotonJets_MGG-80toInf_HHWWggTag_0_MoreVars.root" : "DiPhoJets_MGG-80toInf",
        "WW_TuneCP5_HHWWggTag_0_MoreVars.root" : "WW",
        "GluGluHToGG_HHWWggTag_0_MoreVars_noSyst.root" : "GluGluHToGG",
        "GluGluHToGG_HHWWggTag_0_MoreVars.root" : "GluGluHToGG",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars.root" : "ttHJetToGG",         
        "ttHJetToGG_HHWWggTag_0_MoreVars_noSyst.root" : "ttHJetToGG",
        "DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars.root" : "DiPhoJetsBox_MGG-80toInf",
        
        "GJet_Pt-20to40_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJet_20to40",
        "GJet_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJet_40toInf",
        "GJet_Pt-20toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJet_20toInf",
        
        "QCD_Pt-30to40_HHWWggTag_0_MoreVars.root" : "QCD_30to40",
        "QCD_Pt-30toInf_HHWWggTag_0_MoreVars.root" : "QCD_30toInf",
        "QCD_Pt-40toInf_HHWWggTag_0_MoreVars.root" : "QCD_40toInf",

        "QCD_HT50to100_TuneCP5_13TeV_hadd.root": "QCD_HT50to100",
        "QCD_HT100to200_TuneCP5_13TeV_hadd.root": "QCD_HT100to200",
        "QCD_HT200to300_TuneCP5_13TeV_hadd.root": "QCD_HT200to300",
        "QCD_HT300to500_TuneCP5_13TeV_hadd.root": "QCD_HT300to500",
        "QCD_HT500to700_TuneCP5_13TeV_hadd.root": "QCD_HT500to700",
        "QCD_HT700to1000_TuneCP5_13TeV_hadd.root": "QCD_HT700to1000",
        "QCD_HT1000to1500_TuneCP5_13TeV_hadd.root": "QCD_HT1000to1500",
        "QCD_HT1500to2000_TuneCP5_13TeV_hadd.root": "QCD_HT1500to2000",
        "QCD_HT2000toInf_TuneCP5_13TeV_hadd.root": "QCD_HT2000toInf",        
        
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "wzh_125",
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "wzh_125",
        # "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "TTGG_0Jets_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "TTGG_0Jets",
        "DYJetsToLL_M-50_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "DYJetsToLL_M_50",
        # "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "VBFHToGG",
        "TTJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "TTJets",
        "TTJets_TuneCP5_extra_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "TTJets",
        "TTGJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "TTGJets",

        # "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5",
        "THQ_ctcvcp_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "THQ",

        # HHWWgg_bkg_v2 
        "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT-2500toInf",
        "TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT-600to800",
        "TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT-800to1200",
        "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT-1200to2500",
        "TTToHadronic_HHWWggTag_0_MoreVars.root" : "TTToHadronic", ##-- bbWW --> bbqqqq

        # HHWWgg_bkg_v3 
        "W1JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1Jets_pT_0-50",
        "W1JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1Jets_pT_50-150",
        "W1JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1Jets_pT_400-inf",
        "W1JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1Jets_pT_250-400",
        "W1JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1Jets_pT_150-250", 
        "W1JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1Jets_pT_100-150",

        # HHWWgg_bkg_v4 
        "W2JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2Jets_pT_50-150",
        "W3JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W3Jets",
        "W4JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W4Jets",
        "W2JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2Jets_pT_0-50",
        "W2JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2Jets_pT_250-400",
        "W2JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2Jets_pT_400-inf",
        "W2JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2Jets_pT_100-150",
        "W2JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2Jets_pT_150-250",

        # HHWWgg_bkg_v5
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0_HHWWggTag_0_MoreVars.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WGGJets_HHWWggTag_0_MoreVars.root": "WGGJets",
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8.root":"WGGJets", #FH
        "WWTo1L1Nu2Q_HHWWggTag_0_MoreVars.root": "WWTo1L1Nu2Q",
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8.root": "WWTo1L1Nu2Q",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8.root":"ttWJets",
        "WGJJToLNuGJJ_EWK_HHWWggTag_0_MoreVars.root" : "WGJJToLNuGJJ_EWK_aQGC",
        "WGJJToLNu_EWK_QCD_HHWWggTag_0_MoreVars.root" : "WGJJToLNu_EWK_QCD",
        "WGJJToLNu_EWK_QCD_TuneCP5_13TeV-madgraph-pythia8.root" : "WGJJToLNu_EWK_QCD",
        # "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8_HHWWggTag_0_MoreVars.root" : "WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8",

        ##-- HHWWgg Signal
        "GluGluToHHTo2G4Q_node_cHHH1_2017.root": "HHWWgg_SM",
        "ggF_SM_WWgg_qqlnugg_Hadded_HHWWggTag_0_MoreVars.root":"ggF_SM_WWgg_qqlnugg",
        "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus_HHWWggTag_0_MoreVars.root":"GluGluToHHTo_WWgg_qqlnu_nodeSM",
        "HHWWgg-SL-SM-NLO-2016_HHWWggTag_0_MoreVars.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV_powheg_pythia8alesauva_2016_1_10_6_4_v0_RunIISummer16MiniAODv3_PUMoriond17_94X_mcRun2_asymptotic_v3_v1_c3d8a5638586a0e8df7c55ce908b2878USER",
        "HHWWgg-SL-SM-NLO-2017_HHWWggTag_0_MoreVars.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
        "HHWWgg-SL-SM-NLO-2017-HggVtx-Trees_Hadded_HHWWggTag_0_MoreVars.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
        "HHWWgg-SL-SM-NLO-2018_HHWWggTag_0_MoreVars.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2018_1_10_6_4_v0_RunIIAutumn18MiniAOD_102X_upgrade2018_realistic_v15_v1_460d9a73477aa42da0177ac2dc7ecf49USER",
        "output_numEvent500_HHWWggTag_0_MoreVars.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8",
    
        ##-- Single Higgs
        "VBFHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "vbf_125",
        "VBFHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "vbf_125",
        "GluGluHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "ggh_125",
        "VHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "wzh_125",
        "VBFHToGG_M125_13TeV_2018_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "vbf_125",
        "GluGluHToGG_M125_13TeV_2018_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "ggh_125",
        "VHToGG_M125_13TeV_2018_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "wzh_125",



        # ##-- QCD
        # "QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt-30to40",
        # "QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt-40toInf",
        # "QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt-30toInf",

        # ##-- SM Hgg
        # "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "GluGluHToGG",
        # "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "GluGluHToGG", 
        # "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "VHToGG",
        # "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "VBFHToGG",
        # # "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root" : "THQ_HToGG",
        # "THQ_ctcvcp.root" : "THQ_HToGG",

        # ##-- GJet
        # "GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt-20to40_MGG-80toInf",
        # "GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt-20toInf_MGG-40to80",
        # "GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt-40toInf_MGG-80toInf",

        # ##-- GJets 
        # # "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "GJets",
        # # "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "GJets", 

        # ##-- DiPhotonJets 
        # "DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "DiPhoJets_MGG-80-Inf",
         

        # ##-- DiPhotonJetsBox
        # # "DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox",
        # # "DiPhotonJetsBox2BJets_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox",
        # "DiPhotonJetsBox_M40_80-Sherpa_Hadded.root" : "DiPhoJetsBox_MGG-40_80",
        # "DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox_MGG-80toInf",

        # # HHWWgg_bkg_v2 
        # "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT-2500toInf",
        # "TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT-600to800",
        # "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT_1200to2500",
        # "TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT_800to1200",
        # "TTToHadronic_TuneCP5_13TeV-powheg-pythia8_Hadded.root" : "TTToHadronic",

        # ##-- HHWWgg_bkg_v3 
        # "W1JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  "W1Jets_LHEWpT_0-50",
        # "W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  "W1Jets_LHEWpT_50-150",
        # "W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1Jets_LHEWpT_400-inf",
        # "W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1Jets_LHEWpT_250-400",
        # "W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1Jets_LHEWpT_150-250", 
        # "W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1Jets_LHEWpT_100-150",        

        # ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)
        # "W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_50-150",
        # "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W3JetsToLNu",
        # "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W4JetsToLNu",
        # "W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_0-50",
        # "W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_250-400",
        # "W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_400-inf",
        # "W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_100-150",
        # "W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_150-250",

        # ##-- Other 
        # "WW_TuneCP5_13TeV-pythia8_Hadded.root" : "WW", # non exclusive with WWTo... ?
        # "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "WWTo1L1Nu2Q",

        # "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "ttHJetToGG",
        # "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root" : "TTGG_0Jets",
        # "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "TTJets",
        # "TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root" : "TTGJets",

        # "DYJetsToLL_M-50.root" : "DY",
        # # "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "DY",
        "DYJetsToLL_M-50_TuneCP5_13TeV.root": "DY",

        # ##-- HHWWgg_bkg_v5 
        # "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root" : "WGJJ",
        # "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "WGGJets",
        # # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "WGGJets",
        # "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "ttW",

        # ##-- HHWWgg Signal
        # "ggF_SM_WWgg_qqlnugg_Hadded.root":"HHWWgg_SM",
        # "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root":"HHWWgg_SM",
        # "HHWWgg-SL-SM-NLO-2016.root" : "HHWWgg_SM",
        # "HHWWgg-SL-SM-NLO-2017.root" : "HHWWgg_SM",
        # "HHWWgg-SL-SM-NLO-2018.root" : "HHWWgg_SM"
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_even_MoreVars_kinWeight_noHgg.root" : "HHWWgg_SM"
    }

    return MCNameDict[fileName_]

def GetMCNameOld(fileName_):
    MCNameDict = {
        ##-- QCD
        "QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt-30to40",
        "QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt-40toInf",
        "QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt-30toInf",

        ##-- SM Hgg
        "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "GluGluHToGG",
        "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "GluGluHToGG",
        "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "VHToGG",
        "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "VBFHToGG",
        # "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root" : "THQ_HToGG",
        "THQ_ctcvcp.root" : "THQ_HToGG",

        ##-- GJet
        "GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt-20to40_MGG-80toInf",
        "GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt-20toInf_MGG-40to80",
        "GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt-40toInf_MGG-80toInf",

        ##-- GJets
        # "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "GJets",
        # "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "GJets",

        ##-- DiPhotonJets
        "DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "DiPhoJets_MGG-80-Inf",


        ##-- DiPhotonJetsBox
        # "DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox",
        # "DiPhotonJetsBox2BJets_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox",
        "DiPhotonJetsBox_M40_80.root": "DiPhoJetsBox_M40_80", # FH
        "DiPhotonJetsBox_M40_80-Sherpa_Hadded.root" : "DiPhoJetsBox_MGG-40_80",
        "DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox_MGG-80toInf",

        # HHWWgg_bkg_v2
        "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT-2500toInf",
        "TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT-600to800",
        "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "TTJets_HT_1200to2500",
        "TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT_800to1200",
        "TTToHadronic_TuneCP5_13TeV-powheg-pythia8_Hadded.root" : "TTToHadronic",

        # ##-- HHWWgg_bkg_v3
        # "W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu",

        # ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)
        # "W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",
        # "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W3JetsToLNu",
        # "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W4JetsToLNu",
        # "W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",

        ##-- HHWWgg_bkg_v3
        "W1JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  "W1Jets_LHEWpT_0-50",
        "W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  "W1Jets_LHEWpT_50-150",
        "W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1Jets_LHEWpT_400-inf",
        "W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1Jets_LHEWpT_250-400",
        "W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1Jets_LHEWpT_150-250",
        "W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1Jets_LHEWpT_100-150",

        ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)
        "W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_50-150",
        "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W3JetsToLNu",
        "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W4JetsToLNu",
        "W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_0-50",
        "W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_250-400",
        "W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_400-inf",
        "W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_100-150",
        "W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu_150-250",

        ##-- Other
        "WW_TuneCP5_13TeV-pythia8_Hadded.root" : "WW", # non exclusive with WWTo... ?
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8.root" : "WWTo1L1Nu2Q",

        "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "ttHJetToGG",
        "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root" : "TTGG_0Jets",
        "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "TTJets",
        "TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root" : "TTGJets",

        "DYJetsToLL_M-50_TuneCP5_13TeV.root":"DY",
        "DYJetsToLL_M-50.root" : "DY",
        # "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "DY",

        ##-- HHWWgg_bkg_v5
        "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root" : "WGJJ",
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8.root":"WGGJets", #FH
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "WGGJets",
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "WGGJets",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "ttW",

        ##-- HHWWgg Signal
        "ggF_SM_WWgg_qqlnugg_Hadded.root":"HHWWgg_SM",
        "GluGluToHHTo_WWgg_qqqq_nodeSM.root":"HHWWgg_SM",
        "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root":"HHWWgg_SM",
        "HHWWgg-SL-SM-NLO-2016.root" : "HHWWgg_SM",
        "HHWWgg-SL-SM-NLO-2017.root" : "HHWWgg_SM",
        "HHWWgg-SL-SM-NLO-2018.root" : "HHWWgg_SM"

    }

    return MCNameDict[fileName_]

def GetMCCategory(fileName_):
    MCCategoryDict = {

        "DiPhotonJetsBox_MGG-80toInf_13TeV.root": "DiPhoJetsBox",  # FH
        "GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV.root": "GJet",  # FH
        "GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV.root": "GJet",  # FH
        "GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf.root": "GJet",  # FH
        "QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV.root": "QCD",  # FH
        "QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV.root": "QCD",  # FH
        "QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf.root": "QCD",  # FH
        "allData_QCD_2017.root": "QCD_Data", # QCD from Data
        "Data_2017.root": "QCD_Data", # QCD from Data
        "datadrivenQCD_v2.root": "QCD_Data", # QCD from QCD_Data
        "TTGG_0Jets_TuneCP5_13TeV.root": "tt",  # FH
        "TTGJets_TuneCP5_13TeV.root": "tt",  # FH
        "TTJets_TuneCP5_13TeV.root": "tt",  # FH
        "WW_TuneCP5_13TeV-pythia8.root": "WW",  # FH
        "GluGluHToGG_M125_TuneCP5_13TeV.root": "ggH",  # FH
        "VBFHToGG_M125_13TeV.root": "VBFH",  # FH
        "VHToGG_M125_13TeV.root": "VH",  # FH
        "ttHJetToGG_M125_13TeV.root": "ttHJetToGG",  # FH
        "TTToHadronic_TuneCP5_13TeV-powheg-pythia8.root": "TTToHadronic",
                                                  #     
        ##-- QCD
        "QCD_Pt-30to40_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "QCD",
        "QCD_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "QCD",
        "QCD_Pt-30toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "QCD",

        "QCD_HT50to100_TuneCP5_13TeV_hadd.root": "QCD",
        "QCD_HT100to200_TuneCP5_13TeV_hadd.root": "QCD",
        "QCD_HT200to300_TuneCP5_13TeV_hadd.root": "QCD",
        "QCD_HT300to500_TuneCP5_13TeV_hadd.root": "QCD",
        "QCD_HT500to700_TuneCP5_13TeV_hadd.root": "QCD",
        "QCD_HT700to1000_TuneCP5_13TeV_hadd.root": "QCD",
        "QCD_HT1000to1500_TuneCP5_13TeV_hadd.root": "QCD",
        "QCD_HT1500to2000_TuneCP5_13TeV_hadd.root": "QCD",
        "QCD_HT2000toInf_TuneCP5_13TeV_hadd.root": "QCD",  

        ##DY
        "DYJetsToLL_M-50_TuneCP5_13TeV.root": "DY",

        

        # ##-- SM Hgg
        # "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "SMhgg",
        # "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "SMhgg", 
        # "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "SMhgg",
        # "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "SMhgg",
        "THQ_ctcvcp_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "THQ",

        ##-- SM Hgg
        "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "ggH",
        "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "ggH",
        "GluGluHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "ggH",
        # "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "ggH", 
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "VH",
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "VH",
        "VHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "VH",
        "VBFHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "VBFH",
        "VBFHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "VBFH",
        "VBFHToGG_2017_HHWWggTag.root" : "VBFH",
        "ttHJetToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "ttHJetToGG",        
        "ttHJetToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "ttHJetToGG",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "ttHJetToGG",
        # "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "SMhgg",

        ##-- GJet
        "GJet_Pt-20to40_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJet",
        "GJet_Pt-20toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJet",
        "GJet_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJet",

        ##-- GJets 
        # "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJets",
        # "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "GJets", 

        ##-- DiPhotonJets 
        "DiPhotonJets_MGG-80toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "DiPhoJets",
         

        ##-- DiPhotonJetsBox
        # "DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-Sherpa_Hadded_HHWWggTag_0_MoreVars.root" : "DiPhoJetsBox",
        # "DiPhotonJetsBox2BJets_MGG-80toInf_13TeV-Sherpa_Hadded_HHWWggTag_0_MoreVars.root" : "DiPhoJetsBox",
        "DiPhotonJetsBox_M40_80.root": "DiPhoJetsBox", # FH
        "DiPhotonJetsBox_M40_80_HHWWggTag_0_MoreVars.root" : "DiPhoJetsBox",
        "DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars.root" : "DiPhoJetsBox",

        # HHWWgg_bkg_v2 
        "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "tt",
        "TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "tt",
        "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "tt",
        "TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "tt",
        "TTToHadronic_HHWWggTag_0_MoreVars.root" : "tt",
        # # "DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-Sherpa_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "DiPhoJetsBox",
        # # "DiPhotonJetsBox2BJets_MGG-80toInf_13TeV-Sherpa_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "DiPhoJetsBox",
        # "DiPhotonJetsBox_M40_80_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "DiPhoJetsBox",
        # "DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "DiPhoJetsBox",

        # # HHWWgg_bkg_v2
        # "TTJets_HT-2500toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "tt",
        # "TTJets_HT-800to1200_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "tt",
        # "TTJets_HT-1200to2500_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "tt",
        # "TTJets_HT-600to800_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "tt",
        # "TTToHadronic_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "tt",


        # ##-- HHWWgg_bkg_v3 
        # "W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root":  "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1JetsToLNu", 
        # "W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W1JetsToLNu",        

        # ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)
        # "W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu",
        # "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W3JetsToLNu",
        # "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W4JetsToLNu",
        # "W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "W2JetsToLNu",

        ##-- HHWWgg_bkg_v3 
        "W1JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg.root":  "WJets",
        "W1JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root":  "WJets",
        "W1JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",
        "W1JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",
        "W1JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets", 
        "W1JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",        

        ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)
        "W2JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",
        "W3JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",
        "W4JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",
        "W2JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",
        "W2JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",
        "W2JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",
        "W2JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",
        "W2JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg.root": "WJets",

        ##-- HHWWgg_bkg_v5 
        "WGJJToLNuGJJ_EWK_HHWWggTag_0_MoreVars.root" : "WGJJ",
        "WGJJToLNu_EWK_QCD_HHWWggTag_0_MoreVars.root" : "WGJJ",
        "WGJJToLNu_EWK_QCD_TuneCP5_13TeV-madgraph-pythia8.root" : "WGJJ",

        ##-- Other 
        "WW_TuneCP5_HHWWggTag_0_MoreVars.root" : "WW", # non exclusive with WWTo... ?
        "WWTo1L1Nu2Q_HHWWggTag_0_MoreVars.root" : "WW",
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8.root": "WW",
        # "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded_HHWWggTag_0_MoreVars.root" : "tt",
        "TTGG_0Jets_HHWWggTag_0_MoreVars.root" : "tt",
        "TTJets_TuneCP5_HHWWggTag_0_MoreVars.root" : "tt",
        "TTJets_TuneCP5_extra_HHWWggTag_0_MoreVars.root" : "tt",
        "TTGJets_TuneCP5_HHWWggTag_0_MoreVars.root" : "tt",


        "DYJetsToLL_M-50_HHWWggTag_0_MoreVars_kinWeight_noHgg.root" : "DY",

        ##-- HHWWgg_bkg_v5 
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8.root":"WGGJets", #FH
        "WGGJets_HHWWggTag_0_MoreVars.root": "WGGJets",
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0_HHWWggTag_0_MoreVars.root": "WGGJets",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8.root": "ttW",


        ##-- HHWWgg Signal
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_even_MoreVars_kinWeight_noHgg.root" : "HHWWgg_SM",
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root" : "HHWWgg_SM",

        "GluGluToHHTo2G4Q_node_cHHH1_2017.root": "HHWWgg_SM",
        "ggF_SM_WWgg_qqlnugg_Hadded_HHWWggTag_0_MoreVars.root":"HHWWgg_SM",
        "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus_HHWWggTag_0_MoreVars.root":"HHWWgg_SM",
        "HHWWgg-SL-SM-NLO-2016_HHWWggTag_0_MoreVars.root" : "HHWWgg_SM",
        "HHWWgg-SL-SM-NLO-2017_HHWWggTag_0_MoreVars.root" : "HHWWgg_SM",
        "HHWWgg-SL-SM-NLO-2018_HHWWggTag_0_MoreVars.root" : "HHWWgg_SM"



    }

    return MCCategoryDict[fileName_]

def GetMCCategoryOld(fileName_):
    MCCategoryDict = {
        ##-- QCD
        "QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD",
        "QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD",
        "QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD",

        

        # ##-- SM Hgg
        # "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "SMhgg",
        # "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "SMhgg", 
        # "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "SMhgg",
        # "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "SMhgg",
        "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root" : "THQ",

        ##-- SM Hgg
        "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "ggH",
        "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "ggH", 
        "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "VH",
        "VBFHToGG.root" : "VBFH",
        "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "ttHJetToGG",
        # "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root" : "SMhgg",

        ##-- GJet
        "GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet",
        "GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet",
        "GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet",

        ##-- GJets
        # "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "GJets",
        # "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "GJets",

        ##-- DiPhotonJets
        "DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "DiPhoJets",


        ##-- DiPhotonJetsBox
        # "DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox",
        # "DiPhotonJetsBox2BJets_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox",
        "DiPhotonJetsBox_M40_80-Sherpa_Hadded.root" : "DiPhoJetsBox",
        "DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox",

        # HHWWgg_bkg_v2
        "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "tt",
        "TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "tt",
        "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8.root" : "tt",
        "TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "tt",
        "TTToHadronic_TuneCP5_13TeV-powheg-pythia8_Hadded.root" : "tt",


        # ##-- HHWWgg_bkg_v3
        # "W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W1JetsToLNu",

        # ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)
        # "W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",
        # "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W3JetsToLNu",
        # "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W4JetsToLNu",
        # "W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W2JetsToLNu",

        ##-- HHWWgg_bkg_v3
        "W1JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  "WJets",
        "W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  "WJets",
        "W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "WJets",
        "W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "WJets",
        "W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "WJets",
        "W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "WJets",

        ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)
        "W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "WJets",
        "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "WJets",
        "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "WJets",
        "W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "WJets",
        "W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "WJets",
        "W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "WJets",
        "W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "WJets",
        "W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "WJets",

        ##-- HHWWgg_bkg_v5
        "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root" : "WGJJ",

        ##-- Other
        "WW_TuneCP5_13TeV-pythia8_Hadded.root" : "WW", # non exclusive with WWTo... ?
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8.root" : "WW",

        # "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "tt",
        "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root" : "tt",
        "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "tt",
        "TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root" : "tt",

        "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "DY",
        "DYJetsToLL_M-50_TuneCP5_13TeV.root": "DY",

        ##-- HHWWgg_bkg_v5
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8.root":"WGGJets", #FH
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "WGGJets",
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "WGGJets",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "ttW",

        ##-- HHWWgg Signal
        "ggF_SM_WWgg_qqlnugg_Hadded.root":"HHWWgg_SM",
        "GluGluToHHTo_WWgg_qqqq_nodeSM.root":"HHWWgg_SM",
        "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root":"HHWWgg_SM",
        "HHWWgg-SL-SM-NLO-2016.root" : "HHWWgg_SM",
        "HHWWgg-SL-SM-NLO-2017.root" : "HHWWgg_SM",
        "HHWWgg-SL-SM-NLO-2018.root" : "HHWWgg_SM"

    }

    return MCCategoryDict[fileName_]

def OrderHistos(histos_,categories_):
    # print"histos_:",histos_
    # MC_Cats = ["QCD", "SMhgg", "GJet", "DiPhoJets", "DiPhoJetsBox","W1JetsToLNu", "W2JetsToLNu", "W3JetsToLNu", "W4JetsToLNu", "WW", "tt", "DY", "WGGJets", "ttW",
    #             "HHWWgg_SM"
    #             ] 
    # MC_Cats = ["QCD", "SMhgg", "GJet", "DiPhoJets", "DiPhoJetsBox", "WJets", "WW", "tt", "DY", "WGGJets", "ttW", "WGJJ",
                # "HHWWgg_SM"
                # ]                 
    MC_Cats = ["QCD", "SMhgg", "GJet", "DiPhoJets", "DiPhoJetsBox", "WJets", "WW", "tt", "DY", "WGGJets", "ttW", "WGJJ",
               "HHWWgg_SM", "ggH","VH","VBFH","ttHJetToGG","THQ","TTToHadronic", "QCD_Data"
               ]                   

    orderedHistos = []
    for cat in MC_Cats:
        for ih_,h_ in enumerate(histos_):
            histCat = categories_[ih_]
            if histCat == cat:
                orderedHistos.append(h_)
    print"orderedHistos:",orderedHistos
    return orderedHistos

def GetMCColor(MC_Category_):

    # MCColorsDict = {
    #     "QCD" : "8",
    #     "SMhgg" : "9",
    #     "GJet" : "46",
    #     # "GJets" : "7",
    #     "DiPhoJets" : "6",
    #     "DiPhoJetsBox" : "42",
    #     # "W1JetsToLNu" : "70",
    #     # "W2JetsToLNu" : "38",
    #     # "W3JetsToLNu" : "208",
    #     # "W4JetsToLNu" : "222",
    #     "WJets" : "70",
    #     "WW":"47",
    #     "tt":"51",
    #     "DY":"28",
    #     "WGGJets":"2",
    #     "ttW":"30",
    #     "WGJJ":"12",
    #     "HHWWgg_SM": "56"
    #     # "other" : "47"
    # }

    MCColorsDict = {
        "WGGJets":"2",
        "DiPhoJets" : "6",
        "TTToHadronic": "7",
        "QCD" : "8",
        "QCD_Data": "8",
        # "SMhgg" : "9",
        "THQ" : "9",
        "WGJJ":"11",
        "ggH" : "12",
        "DY":"28",
        "VH" : "28",
        "ttW":"30",
        "ttHJetToGG" : "41",
        # "GJets" : "7",
        "DiPhoJetsBox" : "42",
        "GJet" : "46",
        "WW":"47",
        "tt":"51",
        "HHWWgg_SM": "56",
        # "W1JetsToLNu" : "70",
        # "W2JetsToLNu" : "38",
        # "W3JetsToLNu" : "208",
        # "W4JetsToLNu" : "222",
        "WJets" : "70",
        # "other" : "47",
        "VBFH" : "70",
    }    

    return MCColorsDict[MC_Category_]

def ReWeightMC(MCpath_):
    doReWeight, reWeightScale = 0, 1

    # "<sampleName>" : [nEventsInMicroAOD, nEventsInMiniAOD]
    reWeightDict = {
        ##-- HHWWgg_bkg_v3 (W1JetsToLNu)
        "W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  [13599,88882941],
        "W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": [7116,4465538],
        "W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": [32290,42817232],
        "W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": [47897,108925160],
        "W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": [20929,78556157],

        ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)[ToLNu]
        "W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": [1,1],
        "W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": [6905,35696676], #
        "W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": [102984,143562166], #
        "W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": [65864,60722664], #
        "W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": [1,1],
        "W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": [1,1],
        "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": [2766,19700377],
        "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": [2502,11103685],

        ##-- HHWWgg_bkg_v5
        "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": [11241,428364],
        "ttWJets_Hadded.root": [17821,9425384]
    }

    if MCpath_ in reWeightDict:
        doReWeight = 1
        N_microAOD, N_miniAOD = reWeightDict[MCpath_][0], reWeightDict[MCpath_][1]
        reWeightScale = float(N_microAOD) / float(N_miniAOD)

    return [doReWeight, reWeightScale]

def GetEvents(mass_,campaign_):
    evDict = {
        "X250": 98443,
        # "X260": 99932, # no taus or bs
        # "X260": 99942, # with taus and bs HHWWgg_v2-5
        "X260": 99942, # All tau decays added. HHWWgg_v2-6
        "X270": 99952,
        "X280": 99936,
        "X300": 99931,
        "X320": 99941,
        "X350": 99945,
        "X400": 99937,
        "X500": 99947,
        "X550": 99940,
        # "X600": 99961,
        # "X600": 99938, # HHWWgg_v2-5
        "X600": 99933, # HHWWgg_v2-6
        "X650": 99450,
        "X700": 99449,
        "X750": 99953,
        "X800": 99443,
        "X850": 99942,
        "X900": 99945,
        # "X1000": 99450,
        # "X1000": 99931, # HHWWgg_v2-5
        "X1000": 99936, # HHWWgg_v2-6
        "X1250": 97940,
        "SM": 99931,
        # "SM": 99431, # 199/200 files
        "node2": 99944,
        "node9": 99938,
        "MX1000_MY800": 100000,
        "MX1600_MY400": 100000,
        "MX2000_MY1800": 100000,
        "MX300_MY170": 100000
    }

    if(campaign_=="HHWWgg_v2-3"):
        evDict["X260"] = 99932
        evDict["X600"] = 99961
        evDict["X1000"] = 99450

    return evDict[mass_]

# Get signal cross section to scale. In flashgg default is 1fb --> Scale here
def GetXScale(sigCampaign_):
    XS_Scale = 1 
    HH_ProdXS = 1 
    if(sigCampaign_ == "HHWWgg_v2-6"): 
        HH_ProdXS = 33.49 # 33.49 fb 
        BR_HH_WWgg = 0.001 
        BR_WWgg_finalState = 0.002864 # qqlnu, no taus ## - is this right?  
    elif(sigCampaign_ == "HHWWgg_SM"):
        HH_ProdXS = 33.49
        BR_HH_WWgg = 0.00097
        BR_WWgg_finalState = 0.441 # qqlnu, e mu tau included 
    XS_Scale = float(HH_ProdXS)*float(BR_HH_WWgg)*float(BR_WWgg_finalState)
    return XS_Scale 
