###########################################################################################################################
# Abraham Tishelman-Charny
# 15 June 2020
#
# The purpose of this module is to provide variables and definitions for NtupleAnalysisTools.py 
#
###########################################################################################################################

def GetMCTreeName(fileName_):
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
        
        "GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",
        "GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        
        "QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8",
        "QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8",

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

        ##-- HHWWgg Signal
        "ggF_SM_WWgg_qqlnugg_Hadded.root":"ggF_SM_WWgg_qqlnugg"
    }

    return MCTreesDict[fileName_]

def GetMCName(fileName_):
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
        "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root" : "THQ_HToGG",

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
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "WW",

        "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "ttHJetToGG",
        "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root" : "TTGG_0Jets",
        "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "TTJets",
        "TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root" : "TTGJets",

        "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "DY",

        ##-- HHWWgg_bkg_v5 
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "WGGJets",
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "WGGJets",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "ttW",

        ##-- HHWWgg Signal
        "ggF_SM_WWgg_qqlnugg_Hadded.root":"HHWWgg_SM"

    }

    return MCNameDict[fileName_]

def GetMCCategory(fileName_):
    MCCategoryDict = {
        ##-- QCD
        "QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD",
        "QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD",
        "QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root" : "QCD",

        ##-- SM Hgg
        "GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "SMhgg",
        "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "SMhgg", 
        "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "SMhgg",
        "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "SMhgg",
        "THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root" : "SMhgg",

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
        "TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "tt",
        "TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "tt",
        "TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root" : "tt",
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

        ##-- Other 
        "WW_TuneCP5_13TeV-pythia8_Hadded.root" : "WW", # non exclusive with WWTo... ?
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "WW",

        "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "tt",
        "TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root" : "tt",
        "TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "tt",
        "TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root" : "tt",

        "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root" : "DY",

        ##-- HHWWgg_bkg_v5 
        "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "WGGJets",
        # "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "WGGJets",
        "ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root": "ttW",

        ##-- HHWWgg Signal
        "ggF_SM_WWgg_qqlnugg_Hadded.root":"HHWWgg_SM"

    }

    return MCCategoryDict[fileName_]

def OrderHistos(histos_,categories_):
    # print"histos_:",histos_
    # MC_Cats = ["QCD", "SMhgg", "GJet", "DiPhoJets", "DiPhoJetsBox","W1JetsToLNu", "W2JetsToLNu", "W3JetsToLNu", "W4JetsToLNu", "WW", "tt", "DY", "WGGJets", "ttW",
    #             "HHWWgg_SM"
    #             ] 
    MC_Cats = ["QCD", "SMhgg", "GJet", "DiPhoJets", "DiPhoJetsBox", "WJets", "WW", "tt", "DY", "WGGJets", "ttW",
                "HHWWgg_SM"
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
        "QCD" : "8",
        "SMhgg" : "9",
        "GJet" : "46",
        # "GJets" : "7",
        "DiPhoJets" : "6",
        "DiPhoJetsBox" : "42",
        # "W1JetsToLNu" : "70",
        # "W2JetsToLNu" : "38",
        # "W3JetsToLNu" : "208",
        # "W4JetsToLNu" : "222",
        "WJets" : "70",
        "WW":"47",
        "tt":"51",
        "DY":"28",
        "WGGJets":"2",
        "ttW":"30",
        "HHWWgg_SM": "56"
        # "other" : "47"
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
        BR_WWgg_finalState = 0.002864 # qqlnu, no taus  
    XS_Scale = float(HH_ProdXS)*float(BR_HH_WWgg)*float(BR_WWgg_finalState)
    return XS_Scale 