# from ROOT import *

##-- Single Higgs
# python CategorizeTrees.py --iD TestNewFilesRun2/2017SingleHiggs1/ --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFilesRun2/2017SingleHiggs_Trees/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools_again/2017Borders_evalDNN_3cats_testnewfiles_withSidebandScale_xmin-0.000000_binWidth-0.100000.txt --year 2017 --opt SingleHiggs
# python CategorizeTrees.py --iD TestNewFilesRun2/2016SingleHiggs1/ --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFilesRun2/2016SingleHiggs_Trees/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools_again/2017Borders_evalDNN_3cats_testnewfiles_withSidebandScale_xmin-0.000000_binWidth-0.100000.txt --year 2016 --opt SingleHiggs
# python CategorizeTrees.py --iD TestNewFilesRun2/2016SingleHiggs1/ --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFilesRun2/2016SingleHiggs_Trees/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools_again/2017Borders_evalDNN_3cats_testnewfiles_withSidebandScale_xmin-0.000000_binWidth-0.100000.txt --year 2016 --opt SingleHiggs
#
# python CategorizeTrees.py --iD /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/DNN_Tools/2016SingleHiggs1/ --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/WeightsExp/2016SingleHiggs/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools/CustomBorders.txt --year 2016 --opt SingleHiggs 
# python CategorizeTrees.py --iD /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/DNN_Tools/Backgrounds4/ --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/WeightsExp/2017SingleHiggs/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools/CustomBorders.txt --year 2017 --opt SingleHiggs 
# python CategorizeTrees.py --iD /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/DNN_Tools/Backgrounds/ --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/WeightsExp/2017SingleHiggs/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools/CustomBorders.txt --year 2017 --opt SingleHiggs

##-- testnewfiles
# python CategorizeTrees.py --iD TestNewFilesRun2/2017Data/ --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFilesRun2/2017Data/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools_again/2017Borders_evalDNN_3cats_testnewfiles_withSidebandScale_xmin-0.000000_binWidth-0.100000.txt --year 2017 --opt Data
# python CategorizeTrees.py --iD TestNewFilesRun2/2016Signal/ --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFilesRun2/2016Signal/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools_again/2017Borders_evalDNN_3cats_testnewfiles_withSidebandScale_xmin-0.000000_binWidth-0.100000.txt --opt signal --year 2016
# python CategorizeTrees.py --iD TestNewFilesRun2/2018Signal/ --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFilesRun2/2018Signal/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools_again/2017Borders_evalDNN_3cats_testnewfiles_withSidebandScale_xmin-0.000000_binWidth-0.100000.txt --opt signal --year 2018

##-- Signal 
# python CategorizeTrees.py --iD /eos/user/b/bmarzocc/HHWWgg/HHWWgg_DataSignalMCnTuples/PromptPromptApplied-TagsMerged/HHWWyyDNN_binary_testnewfiles_allBkgs/Signal/  --opt signal --year 2017  --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFiles/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools/Borders_withSidebandScale_TestNewFiles.txt

##-- Data 
# python CategorizeTrees.py --iD /eos/user/b/bmarzocc/HHWWgg/HHWWgg_DataSignalMCnTuples/PromptPromptApplied-TagsMerged/HHWWyyDNN_binary_testnewfiles_allBkgs/Data/  --opt Data --year 2017  --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFiles/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools/Borders_withSidebandScale_TestNewFiles.txt

import os 
import ROOT
from optparse import OptionParser

def get_options():

    parser = OptionParser()
    parser.add_option("--iD",type='string',dest="inp_dir",default='')
    # parser.add_option("--i",type='string',dest='inp_files',default='h4g')
    parser.add_option("--m",type='string',dest='m',default='h4g')
    parser.add_option("--opt",type='string',dest="option",default='')
    # parser.add_option("--SingleHiggs",type='string',dest="option",default='')
    parser.add_option("--nCat",type='string',dest="nCat",default='')
    parser.add_option("--year",type='string',dest="year",default='')
    parser.add_option("--oD",type='string',dest="out_dir",default='')
    parser.add_option("--v",type='string',dest='var',default='evalDNN')
    return parser.parse_args()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def GetFiles(nTupleDirec_):
    files = [] 
    Direc = "%s/"%(nTupleDirec_)
    for file in os.listdir(Direc): files.append(file)
    return files 

def GetMCTreeName(MCfileName_):
    TreeDict = {
        "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "VBFHToGG_M_125_13TeV_powheg_pythia8",
        "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8",
        "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8",
        "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "VBFHToGG_M_125_13TeV_powheg_pythia8",
        "merged_GluGluHToGG_M125_13TeV_2016.root" : "ggh_125",
        "merged_VBFHToGG_M125_13TeV_2016.root" : "vbf_125",
        "merged_VHToGG_M125_13TeV_2016.root" : "wzh_125",
        "merged_GluGluHToGG_M125_13TeV_2018.root" : "ggh_125",
        "merged_VBFHToGG_M125_13TeV_2018.root" : "vbf_125",
        "merged_VHToGG_M125_13TeV_2018.root" : "wzh_125",        
        "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8"        
    }

    return TreeDict[MCfileName_]

def GetMCLabel(MCfileName_):
    NameDict = {
        "ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "ttHJetToGG",
        "VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root" : "VBFHToGG",
        "GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded.root" : "GluGluHToGG",
        "VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root" : "VHToGG",
        "merged_GluGluHToGG_M125_13TeV_2016.root" : "GluGluHToGG",
        "merged_VBFHToGG_M125_13TeV_2016.root" : "VBFHToGG",
        "merged_VHToGG_M125_13TeV_2016.root" : "VHToGG",
        "merged_GluGluHToGG_M125_13TeV_2018.root" : "GluGluHToGG",
        "merged_VBFHToGG_M125_13TeV_2018.root" : "VBFHToGG",
        "merged_VHToGG_M125_13TeV_2018.root" : "VHToGG"        
    }

    return NameDict[MCfileName_]    

(opt,args) = get_options()

nTupleDirec = opt.inp_dir

input_files = GetFiles(nTupleDirec)
print("input_files:",input_files)
# exit(1) 
# input_files = opt.inp_files.split(',')
input_names = []

cut_list = []

print opt.nCat
# nCat_file = open(opt.nCat+'_bdt.txt',"r")
nCat_file = open(opt.nCat+'',"r")
nCat_list = []
for word in nCat_file.read().split():
    nCat_list.append(word)

print (nCat_list)
nCat = len(nCat_list)

if (nCat == 3):
    print "2 categories"

    cut_list.append(opt.var+'>='+str(nCat_list[nCat-2]))
    cut_list.append(opt.var+'<'+str(nCat_list[nCat-2]))

if (nCat==4):
    print "3 categories"
    cut_list.append(opt.var+'>='+str(nCat_list[nCat-2]))
    cut_list.append(opt.var+'<'+str(nCat_list[nCat-2])+'&&'+opt.var+'>='+str(nCat_list[nCat-3]))
    cut_list.append(opt.var+'<'+str(nCat_list[nCat-3]))

if (nCat==5):
    print "4 categories"
    cut_list.append(opt.var+'>='+str(nCat_list[nCat-2]))
    cut_list.append(opt.var+'<'+str(nCat_list[nCat-2])+'&&'+opt.var+'>='+str(nCat_list[nCat-3]))
    cut_list.append(opt.var+'<'+str(nCat_list[nCat-3])+'&&'+opt.var+'>='+str(nCat_list[nCat-4]))
    cut_list.append(opt.var+'<'+str(nCat_list[nCat-4]))

if (nCat==6):
    print "5 categories"
    cut_list.append(opt.var+'>='+str(nCat_list[nCat-2]))
    cut_list.append(opt.var+'<'+str(nCat_list[nCat-2])+'&&'+opt.var+'>='+str(nCat_list[nCat-3]))
    cut_list.append(opt.var+'<'+str(nCat_list[nCat-3])+'&&'+opt.var+'>='+str(nCat_list[nCat-4]))
    cut_list.append(opt.var+'<'+str(nCat_list[nCat-4])+'&&'+opt.var+'>='+str(nCat_list[nCat-5]))
    cut_list.append(opt.var+'<'+str(nCat_list[nCat-5]))

systLabels = [""]

# for direction in ["Up","Down"]:
#            systLabels.append("MvaShift%s01sigma"%direction)
#            systLabels.append("SigmaEOverEShift%s01sigma"%direction)
#            systLabels.append("MaterialCentralBarrel%s01sigma"%direction)
#            systLabels.append("MaterialOuterBarrel%s01sigma"%direction)
#            systLabels.append("MaterialForward%s01sigma"%direction)
#            systLabels.append("FNUFEB%s01sigma"%direction)
#            systLabels.append("FNUFEE%s01sigma"%direction)
#            systLabels.append("MCScaleGain6EB%s01sigma"%direction)
#            systLabels.append("MCScaleGain1EB%s01sigma"%direction)
#            systLabels.append("MCScaleGain1EB%s01sigma"%direction)
#            systLabels.append("MCScaleHighR9EB%s01sigma" % direction)
#            systLabels.append("MCScaleHighR9EE%s01sigma" % direction)
#            systLabels.append("MCScaleLowR9EB%s01sigma" % direction)
#            systLabels.append("MCScaleLowR9EE%s01sigma" % direction)
#            systLabels.append("MCSmearHighR9EBPhi%s01sigma" % direction)
#            systLabels.append("MCSmearHighR9EBRho%s01sigma" % direction)
#            systLabels.append("MCSmearHighR9EEPhi%s01sigma" % direction)
#            systLabels.append("MCSmearHighR9EERho%s01sigma" % direction)
#            systLabels.append("MCSmearLowR9EBPhi%s01sigma" % direction)
#            systLabels.append("MCSmearLowR9EBRho%s01sigma" % direction)
#            systLabels.append("MCSmearLowR9EEPhi%s01sigma" % direction)
#            systLabels.append("MCSmearLowR9EERho%s01sigma" % direction)
#            systLabels.append("ShowerShapeHighR9EB%s01sigma" % direction)
#            systLabels.append("ShowerShapeHighR9EE%s01sigma" % direction)
#            systLabels.append("ShowerShapeLowR9EB%s01sigma" % direction)
#            systLabels.append("ShowerShapeLowR9EE%s01sigma" % direction)
#            systLabels.append("SigmaEOverEShift%s01sigma" % direction)

for num,f in enumerate(input_files):
 print 'input file: ',f
#  tfile = ROOT.TFile(opt.inp_dir+f+'.root')
 tfile = ROOT.TFile(opt.inp_dir+f)
 treename = ""
 treelist = []
 if (opt.option == 'signal'):
    for sys_i,syst in enumerate(systLabels):
        systLabel = ""
        # print (syst)
        if syst != "":
           systLabel += '_' + syst
        if (opt.year == '2016'):
            treename = "GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV_powheg_pythia8alesauva_2016_1_10_6_4_v0_RunIISummer16MiniAODv3_PUMoriond17_94X_mcRun2_asymptotic_v3_v1_c3d8a5638586a0e8df7c55ce908b2878USER"
            # treename = "tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_"+opt.m+"_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0"+systLabel
            # treename = "tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_"+opt.m+"_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0"+systLabel
        elif (opt.year == '2017'):
           treename = "GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2017_1_10_6_4_v0_RunIIFall17MiniAODv2_PU2017_12Apr2018_94X_mc2017_realistic_v14_v1_1c4bfc6d0b8215cc31448570160b99fdUSER"
        elif (opt.year == '2018'):
            treename = "GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8alesauva_2018_1_10_6_4_v0_RunIIAutumn18MiniAOD_102X_upgrade2018_realistic_v15_v1_460d9a73477aa42da0177ac2dc7ecf49USER"
        #    treename = "tagsDumper/trees/HAHMHToAA_AToGG_MA_"+opt.m+"GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0"+systLabel
        #    treename = "tagsDumper/trees/HAHMHToAA_AToGG_MA_"+opt.m+"GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0"+systLabel
        treelist.append(treename)
 elif (opt.option == 'SingleHiggs'):
     treename = GetMCTreeName(f)
     print "treename",treename 
     treelist.append(treename)
    #  if(opt.year == '2016'):
    #      treename = ""
    #  elif(opt.year == '2017'):
    #      treename = ""
    #  elif(opt.year == '2018'):
    #      treename = ""
 else:
     treename = "Data"
     treelist.append(treename)

 # treelist.append(treename)
#  f_out = ROOT.TFile.Open(opt.out_dir+opt.inp_files+'_skim.root','RECREATE')
#  f_out = ROOT.TFile.Open(opt.out_dir+'output'+'_skim.root','RECREATE')
 if(opt.option == "SingleHiggs"): 
    MCLabel = GetMCLabel(f)
    print"MCLabel:",MCLabel
    outName = "%s/%s_%s_%s_CategorizedTrees.root"%(opt.out_dir,opt.option,MCLabel,opt.year)
 else: outName = "%s/%s_%s_CategorizedTrees.root"%(opt.out_dir,opt.option,opt.year)
 f_out = ROOT.TFile.Open(outName,'RECREATE')
#  if(opt.option=='signal'): common_cut = '(((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25) && passbVeto==1 && ExOneLep==1 && N_good_Jets >= 1 )'
#  else: common_cut = '(((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25) && passbVeto==1 && ExOneLep==1 && goodJets==1 )'
 common_cut = '(((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25) && passbVeto==1 && ExOneLep==1 && N_goodJets >= 1 )'
 for tree_i, tree in enumerate(treelist):
     ntuple = tfile.Get(treelist[tree_i])
     for icat, cat in enumerate(cut_list):
         # f_out.cd()
         print"ntuple:",ntuple
         ##-- remove non 1d branches because otherwise you run into problems with workspace step treetoarray
         ntuple.SetBranchStatus("pdfWeights",0)
         ntuple.SetBranchStatus("alphaSWeights",0)
         ntuple.SetBranchStatus("scaleWeights",0)

         small = ntuple.CopyTree(common_cut+'&&'+cut_list[icat])
         # treename_tmp = treelist[tree_i].replace('tagsDumper/trees/','')
         # print "on tree: ",treename_tmp, " Cat#: ", icat
         # treename_tmp = treename_tmp.replace('H4GTag_0','H4GTag_0_Cat'+str(icat))
         # treename_tmp = treename_tmp.replace('H4GTag_0','H4GTag_Cat'+str(icat))
         # treename_tmp = 'H4GTag_0_Cat'+str(icat)
         # treename_tmp = 'H4GTag_'+str(icat)+'_13TeV'
         if (tree_i == 0):
             if(opt.option=='signal'): treename_tmp = "GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_%s"%(str(icat))
             elif(opt.option=='SingleHiggs'):
                 Label = GetMCLabel(f)
                 treename_tmp = "%s_13TeV_HHWWggTag_%s"%(Label,str(icat))
             else: treename_tmp = "Data_13TeV_HHWWggTag_%s"%(str(icat))
             
            #  treename_tmp = "GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_%s"%(str(icat))
            #  treename_tmp = 'H4GTag_Cat'+str(icat)+'_13TeV'
         else: treename_tmp = 'H4GTag_Cat'+str(icat)+'_'+systLabels[tree_i]+'_13TeV'
         # print "on tree: ",treename_tmp, " Cat#: ", icat
        #  print small.GetEntries()
         # treename_tmp = treelist[tree_i].replace('tagsDumper/trees/','')
         small.SetName(treename_tmp)
         small.SetTitle(treename_tmp)
         # print treename_tmp+'_Cat'+str(icat)
 # f_out.mkdir('tagsDumper/trees')
 # f_out.cd('tagsDumper/trees')
f_out.Write()
