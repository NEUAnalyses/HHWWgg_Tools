"""
5 January 2021 
Abraham Tishelman-Charny 

The purpose of this macro is to replace a nominal tree missing up/down SFs with one which does. 

Example usage:
python Hadd_withUpdatedNominal.py --node 1 --year 2017 --oneTree --verbose

DNN evaluted:
python Hadd_withUpdatedNominal.py --node 1 --year 2016 --oneTree --verbose
python Hadd_withUpdatedNominal.py --node 1 --year 2017 --verbose --syst SigmaEOverEShiftDown01sigma

"""

import ROOT
import os 
import argparse 
import psutil
from SystematicTreeNames import GetSystLabels

parser =  argparse.ArgumentParser()
parser.add_argument('--node',default = "NO_NODE", required=True, type=str, help = "Node to run on")
parser.add_argument('--year',default = "NO_YEAR", required=True, type=str, help = "Year of CMS conditions to run")
parser.add_argument('--oneTree', action="store_true", default = False, help = "Year of CMS conditions to run")
parser.add_argument('--hadd', action="store_true", default = False, help = "Run hadd step")
parser.add_argument('--verbose', action="store_true", default = False, help = "Extra debug statements")
parser.add_argument('--syst', default = "NONE", required=False, type=str, help = "Systematic tree to process")

args = parser.parse_args()

node = args.node
year = args.year
oneTree = args.oneTree
verbose = args.verbose 
hadd = args.hadd 
syst = args.syst

#inDir = "/eos/user/c/chuw/ForAbe/HIG-21-014_Reweighting_Semileptonic/{year}/".format(year=year) # 2016 and 2018 hadded NLO combined files are in atishelm hgg space. 2017 is in Chu space.
inDir = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted/EFT_DNN_Training/HHWWyyDNN_binary_EFT_noHgg_noNegWeights_BalanceYields_allBkgs_NLO_Reweighted_20nodes_noPtOverM_withKinWeight_weightSel_Parametrized_CorMET/"

# /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2016/Signal/SL_allNLO_Reweighted

if(verbose):
  print("node:",node)
  print("year:",year)
  print("oneTree:",oneTree)
  print("verbose:",verbose)


# hadd with updated nominal tree 
if(hadd):
  print("hadding")
  pass 

else: 

  # If doing 2017, split into even and odd events
  if(year == "2017"):
    divs = ["_odd"]
  else:
    divs = [""]

  for div in divs:
    print("divisor:",div)

    # Copy full file, not including nominal tree 

    signalEndStr = ""
    if( (year == "2017") ): signalEndStr = "_odd"

    # Input files are DNN evaluated:
    processStrInFile = "GluGluToHHTo2G2Qlnu"    
    inFile_path = "{inDir}/{processStrInFile}_node_{node}_{year}{signalEndStr}.root".format(inDir=inDir, year=year, node=node, signalEndStr=signalEndStr, processStrInFile=processStrInFile) 
    print("Input file:",inFile_path)
    
    # Other:
    #inFile_path = "{inDir}/{node}{div}/GluGluToHHTo2G2Qlnu_node_{node}_{year}{div}.root".format(inDir=inDir, div=div, node=node, year=year) 
    inFile = ROOT.TFile(inFile_path, "READ")
    treeNames = inFile.GetListOfKeys()

    treeToProcess = "GluGluToHHTo2G2Qlnu_node_{node}_{year}_13TeV_HHWWggTag_0_{syst}".format(node=node, year=year, syst=syst)
    print("treeToProcess:",treeToProcess)
    # 5,14,20

    #for t_i, treeName in enumerate(treeNames):
    #  kname = treeName.GetName() 

    #  if(kname == treeToProcess):
    #    print("Found tree to process:",kname)

    #print("tree %s: %s"%(t_i, kname))
    #print("percentage of RAM in use:",psutil.virtual_memory().percent)
    #print("percentage of CPU in use:",psutil.cpu_percent())      

    # skip nominal tree
    Nominal_Tree_Name = "GluGluToHHTo2G2Qlnu_node_{node}_{year}_13TeV_HHWWggTag_0".format(node=node, year=year)
    if(treeToProcess == Nominal_Tree_Name): 
     print("Skipping nominal tree")
     continue 

    #out_d = "{inDir}/{node}_trees/".format(inDir=inDir, node=node) # to use the input directory space 

    # starting with DNN evaluated files 
    out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/DNN_Score_Evaluated/{node}_trees{div}/".format(year=year, node=node, div=div)
    
    # before DNN evaluation 
    #out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{node}_trees{div}/".format(year=year, node=node, div=div) # to use the HIG space 

    if(not os.path.isdir(out_d)):
        print("Creating output directory:",out_d)
        os.system("mkdir -p {out_d}".format(out_d=out_d))  # no "-p" if you don't have the full directory permissions. Use "-p" if you do have permissions.

    outName = "{out_d}/{treeToProcess}.root".format(out_d=out_d, treeToProcess=treeToProcess)
    outFile = ROOT.TFile(outName, "RECREATE")
    outFile.cd()
    tree = inFile.Get(treeToProcess)
    outFile.cd()
    outTree = tree.CloneTree(0)
    nentries = tree.GetEntries()
    for i in range(0, nentries):
      tree.GetEntry(i)
      if(i%100000==0):
        print("Entry:",i)
      outTree.Fill()

    outTree.Write(treeToProcess)
    outFile.Close()

      #else: continue 

      # if(oneTree):
      #   if(t_i == 0):
      #     raise Exception("Leaving after one tree")
