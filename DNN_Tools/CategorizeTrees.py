# from ROOT import *

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
            treename = "tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_"+opt.m+"_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0"+systLabel
            # treename = "tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_"+opt.m+"_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0"+systLabel
        elif (opt.year == '2017'):
           treename = "GluGluToHHTo_WWgg_qqlnu_nodeSM"
        elif (opt.year == '2018'):
           treename = "tagsDumper/trees/HAHMHToAA_AToGG_MA_"+opt.m+"GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0"+systLabel
        #    treename = "tagsDumper/trees/HAHMHToAA_AToGG_MA_"+opt.m+"GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0"+systLabel
        treelist.append(treename)
 else:
     treename = "Data"
     treelist.append(treename)
 # treelist.append(treename)
#  f_out = ROOT.TFile.Open(opt.out_dir+opt.inp_files+'_skim.root','RECREATE')
#  f_out = ROOT.TFile.Open(opt.out_dir+'output'+'_skim.root','RECREATE')
 outName = "%s/%s_CategorizedTrees.root"%(opt.out_dir,opt.option)
 f_out = ROOT.TFile.Open(outName,'RECREATE')
#  if(opt.option=='signal'): common_cut = '(((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25) && passbVeto==1 && ExOneLep==1 && N_good_Jets >= 1 )'
#  else: common_cut = '(((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25) && passbVeto==1 && ExOneLep==1 && goodJets==1 )'
 common_cut = '(((Leading_Photon_pt/CMS_hgg_mass) > 0.35)*((Subleading_Photon_pt/CMS_hgg_mass) > 0.25) && passbVeto==1 && ExOneLep==1 && N_goodJets >= 1 )'
 for tree_i, tree in enumerate(treelist):
     ntuple = tfile.Get(treelist[tree_i])
     for icat, cat in enumerate(cut_list):
         # f_out.cd()
         print"ntuple:",ntuple
         small = ntuple.CopyTree(common_cut+'&&'+cut_list[icat])
         # treename_tmp = treelist[tree_i].replace('tagsDumper/trees/','')
         # print "on tree: ",treename_tmp, " Cat#: ", icat
         # treename_tmp = treename_tmp.replace('H4GTag_0','H4GTag_0_Cat'+str(icat))
         # treename_tmp = treename_tmp.replace('H4GTag_0','H4GTag_Cat'+str(icat))
         # treename_tmp = 'H4GTag_0_Cat'+str(icat)
         # treename_tmp = 'H4GTag_'+str(icat)+'_13TeV'
         if (tree_i == 0):
             if(opt.option=='signal'): treename_tmp = "GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_%s"%(str(icat))
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
