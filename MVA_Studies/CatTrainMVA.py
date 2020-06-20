#####################################################################################################################v
# Abe Tishelman-Charny 
#
# The purpose of this module is to train a TMVA 
#
# ##-- Example Usage:
#
# python CatTrainMVA.py --mcFolder DataMC_2017_Short --sigFolder DataMC_2017_Signal --Tags combined
#
# ##-- After running:
# root -l 
# TMVA::TMVAGui("CatTrainMVA_output.root")
#####################################################################################################################v

import ROOT
import argparse
import os 

parser =  argparse.ArgumentParser(description='MVA Training')
parser.add_argument('--mcFolder', type=str, default="", help="Input folder with hadded MC ntuples", required=False)
parser.add_argument('--sigFolder', type=str, default="", help="Input folder with hadded signal ntuples", required=False)
parser.add_argument('--outName', type=str, default="", help="Output file name", required=False)
parser.add_argument('--Tags', type=str, default="", help="Comma separated list of tags to run. Ex: HHWWggTag_0,HHWWggTag_1,HHWWggTag_2 or HHWWggTag_2 or HHWWggTag_2,combined", required=False)
args = parser.parse_args()

def GetMCTreeName(fileName_):
    MCTreesDict = {
        "DiPhotonJetsBox_M40_80-Sherpa_Hadded.root" : "DiPhotonJetsBox_M40_80_Sherpa",
        "DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "DiPhotonJets_MGG_80toInf_13TeV_amcatnloFXFX_pythia8",
        "WW_TuneCP5_13TeV-pythia8_Hadded.root" : "WW_TuneCP5_13TeV_pythia8",
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

        # HHWWgg_bkg_v3 
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
        "output_WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_bmarzocc-HHWWgg_bkg_v5-94X_mc2017-RunIIFall18-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1-db49498e7dc78d32430682b35e9cae55_USER_0.root": "WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8",
        "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root": "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8",
        "ttWJets_Hadded.root":"ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8",

        ##-- HHWWgg Signal
        "ggF_SM_WWgg_qqlnugg_Hadded.root":"ggF_SM_WWgg_qqlnugg"
    }

    return MCTreesDict[fileName_]

nTupleDirec = "/eos/user/a/atishelm/ntuples/HHWWgg"

mcFolder = str(args.mcFolder)
mcDirec = "%s/%s"%(nTupleDirec,mcFolder)
mcFiles = []
for file in os.listdir(mcDirec):
    mcFiles.append(file)
print"mcFiles:",mcFiles 

sigFolder = str(args.sigFolder)
sigDirec = "%s/%s"%(nTupleDirec,sigFolder)
sigFiles = []
for file in os.listdir(sigDirec):
    sigFiles.append(file)
print"sigFiles:",sigFiles 

##-- Background Files 
if(args.Tags=="combined"):
    bkgChain = ROOT.TChain()
    sigChain = ROOT.TChain()
    for bkgFile in mcFiles:
        bkgTree = GetMCTreeName(bkgFile)
        # print"%s/%s/tagsDumper/trees/%s_13TeV_HHWWggTag_0"%(mcDirec,bkgFile,bkgTree)
        # bkgChain.AddFile("%s/%s/tagsDumper/trees/%s_13TeV_HHWWggTag_0"%(mcDirec,bkgFile,bkgTree)) 
        # bkgChain.AddFile("%s/%s/tagsDumper/trees/%s_13TeV_HHWWggTag_1"%(mcDirec,bkgFile,bkgTree))
        bkgChain.AddFile("%s/%s/tagsDumper/trees/%s_13TeV_HHWWggTag_2"%(mcDirec,bkgFile,bkgTree)) 
    for sigFile in sigFiles:
        sigTree = GetMCTreeName(sigFile)
        # print"sigTree:",sigTree
        # sigChain.AddFile("%s/%s/tagsDumper/trees/%s_13TeV_HHWWggTag_0"%(sigDirec,sigFile,sigTree))
        # sigChain.AddFile("%s/%s/tagsDumper/trees/%s_13TeV_HHWWggTag_1"%(sigDirec,sigFile,sigTree))
        sigChain.AddFile("%s/%s/tagsDumper/trees/%s_13TeV_HHWWggTag_2"%(sigDirec,sigFile,sigTree)) 

    # # if(HHWWggTag=="combined"):
    #     mc_ch = TChain('tagsDumper/trees/%s_13TeV_HHWWggTag_0'%(treeName))
    #     mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_0"%(mcPath,treeName))
    #     mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_1"%(mcPath,treeName))
    #     mc_ch.Add("%s/tagsDumper/trees/%s_13TeV_HHWWggTag_2"%(mcPath,treeName))
    # else:
    #     mc_ch = TChain('tagsDumper/trees/%s_13TeV_%s'%(treeName,HHWWggTag))
    #     mc_ch.Add(mcPath)        

# sig_file = ROOT.TChain()
# sig_file.AddFile('/afs/cern.ch/work/a/atishelm/21JuneFlashgg/CMSSW_10_5_0/src/flashgg/output_numEvent500.root/tagsDumper/trees/ggF_X250_WWgg_qqlnugg_13TeV_HHWWggTag_0')
# sig_file.AddFile('/eos/user/t/twamorka/1April2020_CatTrainign/Input_Ntuple/signal_m_60_skim.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/signal_m_60_skim_preselapplied.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# # bkg_file = ROOT.TChain()
# # bkg_file.AddFile('/eos/user/t/twamorka/31March2020_MixedData/data_mix_add.root/Data_13TeV_4photons')
# # bkg_file.AddFile('/afs/cern.ch/work/t/twamorka/Scripts/forH4G/test_mix_30March_2.root/Data_13TeV_4photons')
# # bkg_file.AddFile('/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/SameBranchName/data_mix_MVATrain_presel.root/Data_13TeV_4photons')
# #bkg_file.AddFile('/eos/user/t/twamorka/Quaruntuples_11032020/hadd/OldPairing/Mixed/sameBranchName/data_mixed_presel.root/Data_13TeV_4photons')
print 'Background events: ', bkgChain.GetEntries()
# sig_file = ROOT.TChain()
# sig_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/signal_m_'+str(mass)+'_skim.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# # sig_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/signal_m_'+str(mass)+'_skim.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
print 'Signal events: ', sigChain.GetEntries()

# f_out = ROOT.TFile(outputDir+output+'.root','RECREATE')

##-- Output File 
f_out = ROOT.TFile('%s.root'%(args.outName),'RECREATE')

ROOT.TMVA.Tools.Instance()
factory = ROOT.TMVA.Factory("TMVAClassification", f_out,"AnalysisType=Classification")

##-- Training Variables 
mvaVars = [
'MET_pt',
'Leading_Photon_MVA',
'Subleading_Photon_MVA',
'Leading_Photon_pt',
'Subleading_Photon_pt',
'goodJets_0_pt'
]

dataloader = ROOT.TMVA.DataLoader("dataset")

for x in mvaVars:
    #factory.AddVariable(x,"F")
    dataloader.AddVariable(x,"F")

dataloader.AddSignalTree(sigChain)
dataloader.AddBackgroundTree(bkgChain)

# if (WP == 'veryLoose'):
#     Cut_MVA = 'pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9'
# elif (WP == 'Loose'):
#     Cut_MVA = 'pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.75 && pho4_MVA > -0.75'
# elif (WP == 'Medium'):
#     Cut_MVA = 'pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.75 && pho4_MVA > -0.75'
# else:
#     Cut_MVA = 'pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.5 && pho4_MVA > -0.5'

# Cut_Signal = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass <180 &&'
# Cut_Background = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass <180 && !((tp_mass > 115 && tp_mass < 135)) && '

# Cut_Signal = 'weight_VBF'
# Cut_Background = 'weight_VBF'

# sigCut = ROOT.TCut(Cut_Signal+Cut_MVA)
# bkgCut = ROOT.TCut(Cut_Background+Cut_MVA)

# sigCut = ROOT.TCut(Cut_Signal)
# bkgCut = ROOT.TCut(Cut_Background)


##-- Signal + Background Selections 
##-- Maybe Start with pass photon selections 
selection = "passPhotonSels == 1"
    
sigCut = ROOT.TCut(selection)
bkgCut = ROOT.TCut(selection)

print "S Cut: ", sigCut
print "B Cut: ", bkgCut

dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")
method = factory.BookMethod( dataloader, ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=200")#:nCuts=200")

# dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")
# method = factory.BookMethod( dataloader, ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=20:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625:nCuts=200")






# method = factory.BookMethod( dataloader, ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625:nCuts=200")


#factory.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")
#method = factory.BookMethod( ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625")#:nCuts=200")

#factory.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")
#method = factory.BookMethod( dataloader, ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625")#:nCuts=200")
#method = factory.BookMethod(ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20")
# dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")
# dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")
# method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=200")#:nCuts=200")
# method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625:nCuts=200")

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

# 1*weight*((CMS_hgg_mass < 115 || CMS_hgg_mass > 135))*((CMS_hgg_mass != 0) && (CMS_hgg_mass != -999))*(1)
# 1*weight*((CMS_hgg_mass < 115 || CMS_hgg_mass > 135))*((Subleading_Photon_pt != 0) && (Subleading_Photon_pt != -999))*(1)*(passPhotonSels == 1)*(passbVeto == 1)*(ExOneLep == 1)*(goodJets == 1)

f_out.Close()

# c1 = factory.GetROCCurve(dataloader)
# c1.SaveAs('/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/CatMVAWeights/ROC_'+str(mass)+'.pdf')
# c1.SaveAs('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/CatMVAWeights_20Jan2020/ROC_20Jan2020_'+str(mass)+'.pdf')
