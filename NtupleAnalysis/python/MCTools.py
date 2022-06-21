###########################################################################################################################
# Abraham Tishelman-Charny
# 15 June 2020
#
# The purpose of this module is to provide MC related variables and definitions to NtupleAnalysisTools.py 
#
###########################################################################################################################

##-- Note: This module can be shrunk by mapping file name to treename, MCName, and MCCategory. Don't need dictionary for each one 

from ROOT import TColor 

def GetMCTreeNameOld(fileName_):
    MCTreesDict = {
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
        "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root" : "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8",
        "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "DYJetsToLL_M_50_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "VBFHToGG_M_125_13TeV_powheg_pythia8",
        "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root" : "TTGJets_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8",

        "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root" : "THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5",

        # HHWWgg_bkg_v2 
        "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT_2500toInf_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT_600to800_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT_800to1200_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT_1200to2500_TuneCP5_13TeV_madgraphMLM_pythia8",
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
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root": "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root":"ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root" : "WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8",

        ##-- HHWWgg Signal
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
        "DiPhotonJetsBox_M40_80_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "DiPhotonJetsBox_M40_80_Sherpa",
        "DiPhotonJets_MGG-80toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "DiPhotonJets_MGG_80toInf_13TeV_amcatnloFXFX_pythia8",
        "WW_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "WW_TuneCP5_13TeV_pythia8",
        "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GluGluHToGG_M_125_13TeV_powheg_pythia8",
        # "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8", 
        "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "ggh_125", 
        "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ggh_125", 
        # "ttHJetToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tth_125",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "tth_125",
        "ttHJetToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "tth_125",
        "DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa",
        
        "GJet_Pt-20to40_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "GJet_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "GJet_Pt-20toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        
        "QCD_Pt-30to40_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "QCD_Pt-30toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        "QCD_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "wzh_125",
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "wzh_125",
        # "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "TTGG_0Jets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8",
        "DYJetsToLL_M-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "DYJetsToLL_M_50_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "VBFHToGG_M_125_13TeV_powheg_pythia8",
        # "TTJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "TTJets_TuneCP5_extra_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8",
        "TTGJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTGJets_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8",

        # "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5",
        "THQ_ctcvcp_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5",

        # HHWWgg_bkg_v2 
        "TTJets_HT-2500toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets_HT_2500toInf_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-600to800_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets_HT_600to800_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-800to1200_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets_HT_800to1200_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTJets_HT-1200to2500_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets_HT_1200to2500_TuneCP5_13TeV_madgraphMLM_pythia8",
        "TTToHadronic_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTToHadronic_TuneCP5_13TeV_powheg_pythia8",

        # HHWWgg_bkg_v3 
        "W1JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W1JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8", 
        "W1JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1JetsToLNu_LHEWpT_100_150_TuneCP5_13TeV_amcnloFXFX_pythia8",

        # HHWWgg_bkg_v4 
        "W2JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W3JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W3JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8",
        "W4JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W4JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8",
        "W2JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu_LHEWpT_100_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
        "W2JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8",

        # HHWWgg_bkg_v5
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WGGJets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WWTo1L1Nu2Q_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8",
        "ttWJets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WGJJToLNuGJJ_EWK_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8",
        "WGJJToLNu_EWK_QCD_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "WGJJToLNu_EWK_QCD_TuneCP5_13TeV_madgraph_pythia8",
        # "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8",

        ##-- HHWWgg Signal
        # "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1",


        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_even_MoreVars_kinWeight_noHgg_v3.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1",
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_even_MoreVars_kinWeight_noHgg_v3.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1",
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1",
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1",


        # "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1",
        # "ggF_SM_WWgg_qqlnugg_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"ggF_SM_WWgg_qqlnugg",
        # "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"GluGluToHHTo_WWgg_qqlnu_nodeSM",
        # "HHWWgg-SL-SM-NLO-2016_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV_powheg_pythia8alesauva_2016_1_10_6_4_v0_RunIISummer16MiniAODv3_PUMoriond17_94X_mcRun2_asymptotic_v3_v1_c3d8a5638586a0e8df7c55ce908b2878USER",
        # "HHWWgg-SL-SM-NLO-2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
        # "HHWWgg-SL-SM-NLO-2017-HggVtx-Trees_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
        # "HHWWgg-SL-SM-NLO-2018_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2018_1_10_6_4_v0_RunIIAutumn18MiniAOD_102X_upgrade2018_realistic_v15_v1_460d9a73477aa42da0177ac2dc7ecf49USER",
        # "output_numEvent500_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8",
    
        ##-- Single Higgs
        "VBFHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "vbf_125",
        "VBFHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "vbf_125",
        "VBFHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "vbf_125",
        "VBFHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "vbf_125",
        "GluGluHToGG_M125_13TeV_2016_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ggh_125",
        "GluGluHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ggh_125",
        "GluGluHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "ggh_125",
        # "VHToGG_M125_13TeV_2016_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "wzh_125",
        "VHToGG_2017_HHWWggTag_0.root" : "wzh_125",
        "VHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "wzh_125",
        "VBFHToGG_M125_13TeV_2018_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "vbf_125",
        "GluGluHToGG_M125_13TeV_2018_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ggh_125",
        "VHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "wzh_125"
    }

    return MCTreesDict[fileName_]

# def GetMCTreeName(fileName_):
#     MCTreesDict = {
#         "DiPhotonJetsBox_M40_80.root" : "DiPhotonJetsBox_M40_80_Sherpa",
#         # "DiPhotonJets_MGG-80toInf.root" : "DiPhotonJets_MGG_80toInf_13TeV_amcatnloFXFX_pythia8",
#         "WW_TuneCP5.root" : "WW_TuneCP5_13TeV_pythia8",
#         # "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "GluGluHToGG_M_125_13TeV_powheg_pythia8",
#         # "GluGluHToGG.root" : "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8", 
#         "GluGluHToGG.root" : "ggh_125", 
#         # "ttHJetToGG.root" : "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
#         "ttHJetToGG.root" : "tth_125",
#         "DiPhotonJetsBox_MGG-80toInf.root" : "DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa",
        
#         "GJet_Pt-20to40.root" : "GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
#         "GJet_Pt-40toInf.root" : "GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
#         "GJet_Pt-20toInf.root" : "GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        
#         "QCD_Pt-30to40.root" : "QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
#         "QCD_Pt-30toInf.root" : "QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
#         "QCD_Pt-40toInf.root" : "QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        
#         "VHToGG.root" : "wzh_125",
#         # "VHToGG.root" : "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
#         "TTGG_0Jets.root" : "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8",
#         "DYJetsToLL_M-50.root" : "DYJetsToLL_M_50_TuneCP5_13TeV_amcatnloFXFX_pythia8",
#         "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "VBFHToGG_M_125_13TeV_powheg_pythia8",
#         "TTJets_TuneCP5.root" : "TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8",
#         "TTGJets_TuneCP5.root" : "TTGJets_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8",

#         # "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root" : "THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5",
#         "THQ_ctcvcp.root" : "THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5",

#         # HHWWgg_bkg_v2 
#         "TTJets_HT-2500toInf.root" : "TTJets_HT_2500toInf_TuneCP5_13TeV_madgraphMLM_pythia8",
#         "TTJets_HT-600to800.root" : "TTJets_HT_600to800_TuneCP5_13TeV_madgraphMLM_pythia8",
#         "TTJets_HT-800to1200.root" : "TTJets_HT_800to1200_TuneCP5_13TeV_madgraphMLM_pythia8",
#         "TTJets_HT-1200to2500.root" : "TTJets_HT_1200to2500_TuneCP5_13TeV_madgraphMLM_pythia8",
#         "TTToHadronic.root" : "TTToHadronic_TuneCP5_13TeV_powheg_pythia8",

#         # HHWWgg_bkg_v3 
#         "W1JetsToLNu_LHEWpT_0-50.root": "W1JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8",
#         "W1JetsToLNu_LHEWpT_50-150.root": "W1JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
#         "W1JetsToLNu_LHEWpT_400-inf.root": "W1JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8",
#         "W1JetsToLNu_LHEWpT_250-400.root": "W1JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8",
#         "W1JetsToLNu_LHEWpT_150-250.root": "W1JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8", 
#         "W1JetsToLNu_LHEWpT_100-150.root": "W1JetsToLNu_LHEWpT_100_150_TuneCP5_13TeV_amcnloFXFX_pythia8",

#         # HHWWgg_bkg_v4 
#         "W2JetsToLNu_LHEWpT_50-150.root": "W2JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
#         "W3JetsToLNu.root": "W3JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8",
#         "W4JetsToLNu.root": "W4JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8",
#         "W2JetsToLNu_LHEWpT_0-50.root": "W2JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8",
#         "W2JetsToLNu_LHEWpT_250-400.root": "W2JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8",
#         "W2JetsToLNu_LHEWpT_400-inf.root": "W2JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8",
#         "W2JetsToLNu_LHEWpT_100-150.root": "W2JetsToLNu_LHEWpT_100_150_TuneCP5_13TeV_amcnloFXFX_pythia8",
#         "W2JetsToLNu_LHEWpT_150-250.root": "W2JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8",

#         # HHWWgg_bkg_v5
#         # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
#         "WGGJets.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
#         "WWTo1L1Nu2Q.root": "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8",
#         "ttWJets.root":"ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8",
#         "WGJJToLNuGJJ_EWK.root" : "WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8",
#         "WGJJToLNu_EWK_QCD.root" : "WGJJToLNu_EWK_QCD_TuneCP5_13TeV_madgraph_pythia8",
#         # "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root" : "WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8",

#         ##-- HHWWgg Signal
#         "GluGluToHHTo2G2Qlnu_node_cHHH1_2017.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1",
#         # "GluGluToHHTo2G2Qlnu_node_cHHH1_2017.root" : "tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1",
#         # "ggF_SM_WWgg_qqlnugg_Hadded.root":"ggF_SM_WWgg_qqlnugg",
#         # "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root":"GluGluToHHTo_WWgg_qqlnu_nodeSM",
#         # "HHWWgg-SL-SM-NLO-2016.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV_powheg_pythia8alesauva_2016_1_10_6_4_v0_RunIISummer16MiniAODv3_PUMoriond17_94X_mcRun2_asymptotic_v3_v1_c3d8a5638586a0e8df7c55ce908b2878USER",
#         # "HHWWgg-SL-SM-NLO-2017.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
#         # "HHWWgg-SL-SM-NLO-2017-HggVtx-Trees_Hadded.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
#         # "HHWWgg-SL-SM-NLO-2018.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2018_1_10_6_4_v0_RunIIAutumn18MiniAOD_102X_upgrade2018_realistic_v15_v1_460d9a73477aa42da0177ac2dc7ecf49USER",
#         # "output_numEvent500.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8",
    
#         ##-- Single Higgs
#         "VBFHToGG.root" : "vbf_125",
#         "GluGluHToGG_M125_13TeV_2016.root" : "ggh_125",
#         "VHToGG_M125_13TeV_2016.root" : "wzh_125",
#         "VBFHToGG_M125_13TeV_2018.root" : "vbf_125",
#         "GluGluHToGG_M125_13TeV_2018.root" : "ggh_125",
#         "VHToGG_M125_13TeV_2018.root" : "wzh_125"
#     }

#     return MCTreesDict[fileName_]

def GetMCName(fileName_):
    MCNameDict = {
        "DiPhotonJetsBox_M40_80_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "DiPhoJetsBox_M40_80",
        "DiPhotonJets_MGG-80toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "DiPhoJets_MGG-80toInf",
        "WW_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "WW",
        "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "GluGluHToGG",
        "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GluGluHToGG",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ttHJetToGG",    
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "ttHJetToGG",     
        "ttHJetToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "ttHJetToGG",
        "DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "DiPhoJetsBox_MGG-80toInf",
        
        "GJet_Pt-20to40_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GJet_20to40",
        "GJet_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GJet_40toInf",
        "GJet_Pt-20toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GJet_20toInf",
        
        "QCD_Pt-30to40_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "QCD_30to40",
        "QCD_Pt-30toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "QCD_30toInf",
        "QCD_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "QCD_40toInf",
        
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "wzh_125",
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "wzh_125",
        # "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "TTGG_0Jets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTGG_0Jets",
        "DYJetsToLL_M-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "DYJetsToLL_M_50",
        # "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "VBFHToGG",
        "TTJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets",
        "TTJets_TuneCP5_extra_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets",
        "TTGJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTGJets",

        # "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5",
        "THQ_ctcvcp_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "THQ",

        # HHWWgg_bkg_v2 
        "TTJets_HT-2500toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets_HT-2500toInf",
        "TTJets_HT-600to800_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets_HT-600to800",
        "TTJets_HT-800to1200_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets_HT-800to1200",
        "TTJets_HT-1200to2500_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTJets_HT-1200to2500",
        "TTToHadronic_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "TTToHadronic", ##-- bbWW --> bbqqqq

        # HHWWgg_bkg_v3 
        "W1JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1Jets_pT_0-50",
        "W1JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1Jets_pT_50-150",
        "W1JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1Jets_pT_400-inf",
        "W1JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1Jets_pT_250-400",
        "W1JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1Jets_pT_150-250", 
        "W1JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1Jets_pT_100-150",

        # HHWWgg_bkg_v4 
        "W2JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2Jets_pT_50-150",
        "W3JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W3Jets",
        "W4JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W4Jets",
        "W2JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2Jets_pT_0-50",
        "W2JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2Jets_pT_250-400",
        "W2JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2Jets_pT_400-inf",
        "W2JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2Jets_pT_100-150",
        "W2JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2Jets_pT_150-250",

        # HHWWgg_bkg_v5
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WGGJets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "WWTo1L1Nu2Q_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "WWTo1L1Nu2Q",
        "ttWJets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"ttWJets",
        "WGJJToLNuGJJ_EWK_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "WGJJToLNuGJJ_EWK_aQGC",
        "WGJJToLNu_EWK_QCD_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "WGJJToLNu_EWK_QCD",
        # "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8",

        ##-- HHWWgg Signal
        "ggF_SM_WWgg_qqlnugg_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"ggF_SM_WWgg_qqlnugg",
        "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"GluGluToHHTo_WWgg_qqlnu_nodeSM",
        "HHWWgg-SL-SM-NLO-2016_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV_powheg_pythia8alesauva_2016_1_10_6_4_v0_RunIISummer16MiniAODv3_PUMoriond17_94X_mcRun2_asymptotic_v3_v1_c3d8a5638586a0e8df7c55ce908b2878USER",
        "HHWWgg-SL-SM-NLO-2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
        "HHWWgg-SL-SM-NLO-2017-HggVtx-Trees_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER",
        "HHWWgg-SL-SM-NLO-2018_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2018_1_10_6_4_v0_RunIIAutumn18MiniAOD_102X_upgrade2018_realistic_v15_v1_460d9a73477aa42da0177ac2dc7ecf49USER",
        "output_numEvent500_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8",
    
        ##-- Single Higgs
        "VBFHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "vbf_125",
        "VBFHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "vbf_125",
        "VBFHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "vbf_125",
        "GluGluHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ggh_125",
        "GluGluHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "ggh_125",
        "VHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "wzh_125",
        "VHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "wzh_125",
        "VBFHToGG_M125_13TeV_2018_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "vbf_125",
        "GluGluHToGG_M125_13TeV_2018_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ggh_125",
        "VHToGG_M125_13TeV_2018_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "wzh_125",



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
        # # "DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "\gamma\gamma+jets",
        # # "DiPhotonJetsBox2BJets_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "\gamma\gamma+jets",
        # "DiPhotonJetsBox_M40_80-Sherpa_Hadded.root" : "DiPhoJetsBox_MGG-40_80",
        # "DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox_MGG-80toInf",

        # # HHWWgg_bkg_v2 
        # "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT-2500toInf",
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

        # ##-- HHWWgg_bkg_v5 
        # "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root" : "W\gamma(s)+jets",
        # "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "W\gamma(s)+jets",
        # # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "W\gamma(s)+jets",
        # "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "tt\gamma(s)+jets",

        # ##-- HHWWgg Signal
        # "ggF_SM_WWgg_qqlnugg_Hadded.root":"Signal",
        # "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root":"Signal",
        # "HHWWgg-SL-SM-NLO-2016.root" : "Signal",
        # "HHWWgg-SL-SM-NLO-2017.root" : "Signal",
        # "HHWWgg-SL-SM-NLO-2018.root" : "Signal"
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_even_MoreVars_kinWeight_noHgg_v3.root" : "Signal",
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017.root" : "Signal"
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
        # "DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "\gamma\gamma+jets",
        # "DiPhotonJetsBox2BJets_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "\gamma\gamma+jets",
        "DiPhotonJetsBox_M40_80-Sherpa_Hadded.root" : "DiPhoJetsBox_MGG-40_80",
        "DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "DiPhoJetsBox_MGG-80toInf",

        # HHWWgg_bkg_v2 
        "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT-2500toInf",
        "TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT-600to800",
        "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "TTJets_HT_1200to2500",
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
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "WWTo1L1Nu2Q",

        "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "ttHJetToGG",
        "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root" : "TTGG_0Jets",
        "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "TTJets",
        "TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root" : "TTGJets",

        "DYJetsToLL_M-50.root" : "DY",
        # "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "DY",

        ##-- HHWWgg_bkg_v5 
        "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root" : "W\gamma(s)+jets",
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "W\gamma(s)+jets",
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "W\gamma(s)+jets",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "tt\gamma(s)+jets",

        ##-- HHWWgg Signal
        "ggF_SM_WWgg_qqlnugg_Hadded.root":"Signal",
        "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root":"Signal",
        "HHWWgg-SL-SM-NLO-2016.root" : "Signal",
        "HHWWgg-SL-SM-NLO-2017.root" : "Signal",
        "HHWWgg-SL-SM-NLO-2018.root" : "Signal"

    }

    return MCNameDict[fileName_]

def GetMCCategory(fileName_):
    MCCategoryDict = {
        ##-- QCD
        "QCD_Pt-30to40_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "QCD",
        "QCD_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "QCD",
        "QCD_Pt-30toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "QCD",

        # ##-- SM Hgg
        # "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "SMhgg",
        # "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "SMhgg", 
        # "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "SMhgg",
        # "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "SMhgg",
        "THQ_ctcvcp_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "THQ",

        # Label per H process:
        ##-- SM Hgg
        # "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "ggH",
        # "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ggH",
        # "GluGluHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ggH",
        # "GluGluHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "ggH",
        # # "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "ggH", 
        # "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "VH",
        # "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "VH",
        # "VHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "VH",
        # "VHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "VH",
        # "VBFHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "VBFH",
        # "VBFHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "VBFH",
        # "VBFHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "VBFH",
        # "VBFHToGG_2017_HHWWggTag.root" : "VBFH",
        # "ttHJetToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ttHJetToGG",        
        # "ttHJetToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "ttHJetToGG",
        # "ttHJetToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "ttHJetToGG",
        # "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "ttHJetToGG",
        # "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "SMhgg",

        # Same label for all:
        "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "H\\rightarrow\gamma\gamma",
        "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "H\\rightarrow\gamma\gamma",
        "GluGluHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "H\\rightarrow\gamma\gamma",
        "GluGluHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "H\\rightarrow\gamma\gamma",
        # "GluGluHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "H\\rightarrow\gamma\gamma", 
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "H\\rightarrow\gamma\gamma",
        "VHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "H\\rightarrow\gamma\gamma",
        "VHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "H\\rightarrow\gamma\gamma",
        "VHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "H\\rightarrow\gamma\gamma",
        "VBFHToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "H\\rightarrow\gamma\gamma",
        "VBFHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "H\\rightarrow\gamma\gamma",
        "VBFHToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "H\\rightarrow\gamma\gamma",
        "VBFHToGG_2017_HHWWggTag.root" : "H\\rightarrow\gamma\gamma",
        "ttHJetToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "H\\rightarrow\gamma\gamma",        
        "ttHJetToGG_HHWWggTag_0_MoreVars_kinWeight_noHgg_noSyst.root" : "H\\rightarrow\gamma\gamma",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "H\\rightarrow\gamma\gamma",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2.root" : "H\\rightarrow\gamma\gamma",
        "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "H\\rightarrow\gamma\gamma",

        ##-- GJet
        "GJet_Pt-20to40_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "\gamma+jet",
        "GJet_Pt-20toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "\gamma+jet",
        "GJet_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "\gamma+jet",

        ##-- GJets 
        # "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GJets",
        # "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "GJets", 

        ##-- DiPhotonJets 
        "DiPhotonJets_MGG-80toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "DiPhoJets",
         

        ##-- DiPhotonJetsBox
        # "DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-Sherpa_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "\gamma\gamma+jets",
        # "DiPhotonJetsBox2BJets_MGG-80toInf_13TeV-Sherpa_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "\gamma\gamma+jets",
        "DiPhotonJetsBox_M40_80_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "\gamma\gamma+jets",
        "DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "\gamma\gamma+jets",

        # HHWWgg_bkg_v2 
        "TTJets_HT-2500toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tt\gamma(s)+jets",
        "TTJets_HT-800to1200_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tt\gamma(s)+jets",
        "TTJets_HT-1200to2500_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tt\gamma(s)+jets",
        "TTJets_HT-600to800_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tt\gamma(s)+jets",
        "TTToHadronic_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tt\gamma(s)+jets",


        # ##-- HHWWgg_bkg_v3 
        # "W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":  "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1JetsToLNu",
        # "W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1JetsToLNu", 
        # "W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W1JetsToLNu",        

        # ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)
        # "W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu",
        # "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W3JetsToLNu",
        # "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W4JetsToLNu",
        # "W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu",
        # "W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W2JetsToLNu",

        ##-- HHWWgg_bkg_v3 
        "W1JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":  "W\gamma(s)+jets",
        "W1JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":  "W\gamma(s)+jets",
        "W1JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "W1JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "W1JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets", 
        "W1JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",        

        ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)
        "W2JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "W3JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "W4JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "W2JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "W2JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "W2JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "W2JetsToLNu_LHEWpT_100-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "W2JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",

        ##-- HHWWgg_bkg_v5 
        "WGJJToLNuGJJ_EWK_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "W\gamma(s)+jets",
        "WGJJToLNu_EWK_QCD_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "W\gamma(s)+jets",

        ##-- Other 
        "WW_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "WW", # non exclusive with WWTo... ?
        "WWTo1L1Nu2Q_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "WW",

        # "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tt\gamma(s)+jets",
        "TTGG_0Jets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tt\gamma(s)+jets",
        "TTJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tt\gamma(s)+jets",
        "TTJets_TuneCP5_extra_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tt\gamma(s)+jets",
        "TTGJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "tt\gamma(s)+jets",

        "DYJetsToLL_M-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "DY",

        ##-- HHWWgg_bkg_v5 
        "WGGJets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "W\gamma(s)+jets",
        "ttWJets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root": "tt\gamma(s)+jets",

        ##-- HHWWgg Signal
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_even_MoreVars_kinWeight_noHgg_v3.root" : "Signal",
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017.root" : "Signal",
        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root" : "Signal",

        "ggF_SM_WWgg_qqlnugg_Hadded_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"Signal",
        "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root":"Signal",
        "HHWWgg-SL-SM-NLO-2016_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "Signal",
        "HHWWgg-SL-SM-NLO-2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "Signal",
        "HHWWgg-SL-SM-NLO-2018_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root" : "Signal",

        "GluGluToHHTo2G2Qlnu_node_cHHH1_2017.root" : "Signal",


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
        "GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "\gamma+jet",
        "GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "\gamma+jet",
        "GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "\gamma+jet",

        ##-- GJets 
        # "GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "GJets",
        # "GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "GJets", 

        ##-- DiPhotonJets 
        "DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "DiPhoJets",
         

        ##-- DiPhotonJetsBox
        # "DiPhotonJetsBox1BJet_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "\gamma\gamma+jets",
        # "DiPhotonJetsBox2BJets_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "\gamma\gamma+jets",
        "DiPhotonJetsBox_M40_80-Sherpa_Hadded.root" : "\gamma\gamma+jets",
        "DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_Hadded.root" : "\gamma\gamma+jets",

        # HHWWgg_bkg_v2 
        "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "tt\gamma(s)+jets",
        "TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "tt\gamma(s)+jets",
        "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "tt\gamma(s)+jets",
        "TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "tt\gamma(s)+jets",
        "TTToHadronic_TuneCP5_13TeV-powheg-pythia8_Hadded.root" : "tt\gamma(s)+jets",


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
        "W1JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  "W\gamma(s)+jets",
        "W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root":  "W\gamma(s)+jets",
        "W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W\gamma(s)+jets",
        "W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W\gamma(s)+jets",
        "W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W\gamma(s)+jets", 
        "W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W\gamma(s)+jets",        

        ##-- HHWWgg_bkg_v4 (W2Jets, W3Jets, W4Jets)
        "W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W\gamma(s)+jets",
        "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W\gamma(s)+jets",
        "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root": "W\gamma(s)+jets",
        "W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W\gamma(s)+jets",
        "W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W\gamma(s)+jets",
        "W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W\gamma(s)+jets",
        "W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W\gamma(s)+jets",
        "W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root": "W\gamma(s)+jets",

        ##-- HHWWgg_bkg_v5 
        "WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root" : "W\gamma(s)+jets",

        ##-- Other 
        "WW_TuneCP5_13TeV-pythia8_Hadded.root" : "WW", # non exclusive with WWTo... ?
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "WW",

        # "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "tt\gamma(s)+jets",
        "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root" : "tt\gamma(s)+jets",
        "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "tt\gamma(s)+jets",
        "TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root" : "tt\gamma(s)+jets",

        "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "DY",

        ##-- HHWWgg_bkg_v5 
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "W\gamma(s)+jets",
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "W\gamma(s)+jets",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "tt\gamma(s)+jets",

        ##-- HHWWgg Signal
        "ggF_SM_WWgg_qqlnugg_Hadded.root":"Signal",
        "ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root":"Signal",
        "HHWWgg-SL-SM-NLO-2016.root" : "Signal",
        "HHWWgg-SL-SM-NLO-2017.root" : "Signal",
        "HHWWgg-SL-SM-NLO-2018.root" : "Signal"


    }

    return MCCategoryDict[fileName_]

def OrderHistos(histos_,categories_):

    MC_Cats = [
           "H\\rightarrow\gamma\gamma",
           "\gamma+jet", 
           "W\gamma(s)+jets", 
           "tt\gamma(s)+jets", 
           "\gamma\gamma+jets", 
           "Signal"
    ]

    orderedHistos = []
    for cat in MC_Cats:
        for ih_,h_ in enumerate(histos_):
            histCat = categories_[ih_] 
            if histCat == cat:
                orderedHistos.append(h_)
    # print"orderedHistos:",orderedHistos 
    return orderedHistos 

def GetMCColor(MC_Category_):

    MCColorsDict = {
        "H\\rightarrow\gamma\gamma": "ROOT.turqoise",
        "\gamma+jet" : "ROOT.peterriver",
        "W\gamma(s)+jets" : "ROOT.wisteria",
        "\gamma\gamma+jets" : "ROOT.sunflower", 
        "tt\gamma(s)+jets":"ROOT.carrot",
        "Signal": "ROOT.alizarin",
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
    elif(sigCampaign_ == "Signal"):
        HH_ProdXS = 33.49
        BR_HH_WWgg = 0.00097
        BR_WWgg_finalState = 0.441 # qqlnu, e mu tau included 
    XS_Scale = float(HH_ProdXS)*float(BR_HH_WWgg)*float(BR_WWgg_finalState)
    return XS_Scale 
