"""
10 November 2021
Abraham Tishelman-Charny 

The purpose of this module is to parallelize the combination of 4 NLO nodes for HIG-21-014 reweighting, running over 4 NLO nodes (cHHH0, cHHH1, cHHH2p45, cHHH5) and 3 years (2016, 2017, 2018) at once. 

# reweight 
python Reweight_NLO_Condor.py --reweightNodes 12,14,15,16 --years 2016 --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2016/Signal/SL_allNLO_Reweighted/combined_allNodes/ --addNodeBranch

# Split 2017 into even / odd with additional SF 
python Reweight_NLO_Condor.py --reweightNodes 1 --years 2017 --NominalOnly --evenOddSplit --additionalSF
python Reweight_NLO_Condor.py --reweightNodes 1 --years 2017 --NominalOnly --evenOddSplit --additionalSF --fromTree

Debugging:
- python Reweight_NLO_Condor.py --reweightNodes 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 --years 2016 --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2016/Signal/SL_allNLO_Reweighted/combined_allNodes/ --addNodeBranch
- python3 Reweight_NLO.py --reweightNode 1 --syst Nominal --runLowEvents --TDirec "" --addNodeBranch --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted/combined_allNodes/
- python3 /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/HIG-21-014/Post-PreAppTalk-Checks/Reweight_NLO.py --reweightNode 1 --year 2016 --syst MCSmearHighR9EBRhoUp01sigma --TDirec ""  --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2016/Signal/SL_allNLO_Reweighted/combined_allNodes/   --addNodeBranch

Example usage:

# reweight samples for AN_20_165_v7 

python Reweight_NLO_Condor.py --reweightNodes cttHH3,cttHH0p35,3D3 --years 2016 --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2016/Signal/SL_allNLO_Reweighted/combined_allNodes/ --NominalOnly
python Reweight_NLO_Condor.py --reweightNodes cttHH3,cttHH0p35,3D3 --years 2017 --inDir /eos/user/c/chuw/ForAbe/HIG-21-014_Reweighting_Semileptonic/2017/combined_allNodes/ --NominalOnly
python Reweight_NLO_Condor.py --reweightNodes cttHH3,cttHH0p35,3D3 --years 2018 --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2018/Signal/SL_allNLO_Reweighted/combined_allNodes/ --NominalOnly

# Combine NLO samples 

# Nominal only (originally added ad hoc to add up/down systematic branches to nominal tree only)

python Reweight_NLO_Condor.py --nodes cHHH0,cHHH1,cHHH2p45,cHHH5 --years 2016,2017,2018 --NominalOnly

# first get cHHH0, cHHH2p45, cHHH5 without changing tree name, then set flag back to allowing tree name changes and reweight to cttHH3,cttHH0p35,3D3

# Other

python Reweight_NLO_Condor.py --nodes cHHH1 --years 2016 --NominalOnly
python Reweight_NLO_Condor.py --nodes cHHH1 --years 2016
python Reweight_NLO_Condor.py --nodes cHHH0,cHHH1,cHHH2p45,cHHH5 --years 2016,2017,2018
python Reweight_NLO_Condor.py --nodes cHHH0,cHHH2p45,cHHH5 --years 2017

# Reweight combined NLO sample to another node 

python Reweight_NLO_Condor.py --reweightNodes 1 --years 2016 --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2016/Signal/SL_allNLO_Reweighted/combined_allNodes/ --addNodeBranch --NominalOnly 
python Reweight_NLO_Condor.py --reweightNodes 1 --years 2017 --inDir /eos/user/c/chuw/ForAbe/HIG-21-014_Reweighting_Semileptonic/2017/combined_allNodes/ --addNodeBranch --NominalOnly 
python Reweight_NLO_Condor.py --reweightNodes 1 --years 2018 --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2018/Signal/SL_allNLO_Reweighted/combined_allNodes/ --addNodeBranch --NominalOnly 

python Reweight_NLO_Condor.py --reweightNodes 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 --years 2016 --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2016/Signal/SL_allNLO_Reweighted/combined_allNodes/ --addNodeBranch
python Reweight_NLO_Condor.py --reweightNodes 1 --years 2016 --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2016/Signal/SL_allNLO_Reweighted/combined_allNodes/ --addNodeBranch --NominalOnly
python Reweight_NLO_Condor.py --reweightNodes 1,2,3,4,5,6,7,8,9,10,11,12,8a,1b,2b,3b,4b,5b,6b,7b --years 2017 --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted/combined_allNodes/ --addNodeBranch
python Reweight_NLO_Condor.py --reweightNodes 2 --years 2017 --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted/combined_allNodes/ --NominalOnly --addNodeBranch

python Reweight_NLO_Condor.py --reweightNodes 8a --years 2017 --inDir /eos/user/a/atishelm/ntuples/HHWWgg_DNN/BinaryDNN/HHWWyyDNN_binary_EFT_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_withKinWeight_weightSel/ --NominalOnly
python Reweight_NLO_Condor.py --reweightNodes cttHH3,cttHH0p35,3D3  --years 2016,2018 
python Reweight_NLO_Condor.py --reweightNodes cttHH3,cttHH0p35,3D3,8a,1b,2b,3b,4b,5b,6b,7b

# Categorize 
python Reweight_NLO_Condor.py --reweightNodes cttHH3,cttHH0p35,3D3 --categorize

# Split into even / odd weights 
python Reweight_NLO_Condor.py --reweightNodes 2 --years 2017 --NominalOnly --evenOddSplit 

# Split into even / odd weights, additional additional SF to scale back to full sample yield 

# Single higgs even/odd split 

python3 Reweight_NLO_Condor.py --years 2016  --evenOddSplit --Single_Higgs --Single_Higgs_File VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2 --additionalSF
python3 Reweight_NLO_Condor.py --years 2016  --evenOddSplit --Single_Higgs --Single_Higgs_File ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2 --additionalSF

python3 Reweight_NLO_Condor.py --years 2017  --evenOddSplit --Single_Higgs --Single_Higgs_File VHToGG_2017_HHWWggTag_0_MoreVars_v2 --additionalSF
python3 Reweight_NLO_Condor.py --years 2017  --evenOddSplit --Single_Higgs --Single_Higgs_File ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2 --additionalSF

python3 Reweight_NLO_Condor.py --years 2018  --evenOddSplit --Single_Higgs --Single_Higgs_File VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2 --additionalSF
python3 Reweight_NLO_Condor.py --years 2018  --evenOddSplit --Single_Higgs --Single_Higgs_File ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2 --additionalSF


python3 Reweight_NLO_Condor.py --years 2018  --evenOddSplit --Single_Higgs --Single_Higgs_File ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2
python3 Reweight_NLO_Condor.py --years 2018  --evenOddSplit --Single_Higgs --Single_Higgs_File VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2
python3 Reweight_NLO_Condor.py --years 2017 --NominalOnly --evenOddSplit --Single_Higgs --Single_Higgs_File ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2

python3 Reweight_NLO_Condor.py --reweightNodes 1 --years 2017 --NominalOnly --evenOddSplit --additionalSF #python3 for pickle version
python3 Reweight_NLO_Condor.py --reweightNodes 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 --years 2017 --evenOddSplit --additionalSF
python Reweight_NLO_Condor.py --reweightNodes 1 --years 2017 --NominalOnly --evenOddSplit --additionalSF

## Categorize by DNN score 

# SM DNN:

# HH
python Reweight_NLO_Condor.py --reweightNodes cHHH1 --years 2016,2017,2018 --categorize --isHH

# H

python Reweight_NLO_Condor.py --reweightNodes cHHH1 --years 2016,2017,2018 --categorize --Single_Higgs --Single_Higgs_File GluGluHToGG
python Reweight_NLO_Condor.py --reweightNodes cHHH1 --years 2016,2017,2018 --categorize --Single_Higgs --Single_Higgs_File VBFHToGG
python Reweight_NLO_Condor.py --reweightNodes cHHH1 --years 2016,2017,2018 --categorize --Single_Higgs --Single_Higgs_File VHToGG
python Reweight_NLO_Condor.py --reweightNodes cHHH1 --years 2016,2017,2018 --categorize --Single_Higgs --Single_Higgs_File ttHJetToGG

# 20 nodes:

# HH 
python Reweight_NLO_Condor.py --reweightNodes 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 --years 2016,2017,2018 --categorize --isHH

# H 
python Reweight_NLO_Condor.py --reweightNodes 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 --years 2016,2017,2018 --categorize --Single_Higgs --Single_Higgs_File GluGluHToGG
python Reweight_NLO_Condor.py --reweightNodes 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 --years 2016,2017,2018 --categorize --Single_Higgs --Single_Higgs_File VBFHToGG
python Reweight_NLO_Condor.py --reweightNodes 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 --years 2016,2017,2018 --categorize --Single_Higgs --Single_Higgs_File VHToGG
python Reweight_NLO_Condor.py --reweightNodes 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 --years 2016,2017,2018 --categorize --Single_Higgs --Single_Higgs_File ttHJetToGG

# Data 


"""

#!/usr/bin/python
from SystematicTreeNames import GetSystLabels
import sys, getopt
import itertools
import argparse
import operator
import os

if __name__ == '__main__':

  parser =  argparse.ArgumentParser()
  parser.add_argument('--nodes',default = "", required=False, type=str, help = "Comma separated list of nodes to run")
  parser.add_argument('--reweightNodes',default = "cttHH3", required=False, type=str, help = "Comma separated list of nodes to reweight to")
  parser.add_argument('--years',default = "2017", required=False, type=str, help = "Comma separated list of years to run")
  parser.add_argument('--NominalOnly',action="store_true",help = "Only run on nominal tree")
  parser.add_argument('--categorize', action="store_true", required=False, help = "Split trees into categories based on DNN score")
  parser.add_argument('--addNodeBranch', action="store_true", required=False, help = "Add branch with node number for parametric DNN training")
  parser.add_argument('--evenOddSplit', action="store_true", required=False, help = "Split events into even and odd for DNN training")
  parser.add_argument('--additionalSF', action="store_true", required=False, help = "Apply SF to scale yield back to nominal")
  parser.add_argument('--inDir', default = "NOINDIR", type=str, help = "Directory containing file to begin with, at least for reweighting")
  parser.add_argument('--Single_Higgs', action="store_true", required=False, help = "Run over single higgs")
  parser.add_argument('--Single_Higgs_File', default = "NoSingleHiggsFile", required=False, type=str, help = "Single higgs file")  

  parser.add_argument('--isHH', action="store_true", required=False, help = "Run over HH")
  parser.add_argument('--isData', action="store_true", required=False, help = "Run over Data")
  parser.add_argument('--fromTree', action="store_true", required=False, help = "Input file with single tree rather than hadded file")

  args = parser.parse_args()

  nodes = args.nodes.split(',')
  reweightNodes = args.reweightNodes.split(',')
  years = args.years.split(',')
  categorize = args.categorize
  inDir = args.inDir
  addNodeBranch = args.addNodeBranch
  evenOddSplit = args.evenOddSplit
  additionalSF = args.additionalSF
  Single_Higgs = args.Single_Higgs
  Single_Higgs_File = args.Single_Higgs_File
  isHH = args.isHH
  fromTree = args.fromTree

  print("categorize:",categorize)

  scriptName = "condor_job.txt"

  print("nodes:",nodes)
  print("reweightNodes:",reweightNodes)
  print("years:",years)
  print("addNodeBranch:",addNodeBranch)
  print("evenOddSplit:",evenOddSplit)
  print("additionalSF:",additionalSF)

  local = os.getcwd()
  if not os.path.isdir('error'): os.mkdir('error') 
  if not os.path.isdir('output'): os.mkdir('output') 
  if not os.path.isdir('log'): os.mkdir('log') 
   
  # Prepare condor jobs
  condor = '''executable              = run_script.sh
output                  = output/$(ClusterId).$(ProcId).out
error                   = error/$(ClusterId).$(ProcId).err
log                     = log/$(ClusterId).log
transfer_input_files    = run_script.sh
    
+JobFlavour             = "microcentury"
queue arguments from arguments.txt
'''

  with open(scriptName, "w") as cnd_out:
     cnd_out.write(condor)

  #script = '''
  script = '''#!/bin/sh -e

LOCAL=$1
reweightNode=$2
YEAR=$3
SYST=$4
CATEGORIZE=$5
inDir=$6
addNodeBranch=$7
evenOddSplit=$8
additionalSF=$9
Single_Higgs=${10}
Single_Higgs_File=${11}
isHH=${12}
fromTree=${13}

echo "CATEGORIZE: $CATEGORIZE"
echo "addNodeBranch: $addNodeBranch"

addNodeBranchstr=""
if [ "$addNodeBranch" = True ]; then 
  addNodeBranchstr="--addNodeBranch"
fi

evenOddSplitStr=""
if [ "$evenOddSplit" = True ]; then 
  evenOddSplitstr="--evenOddSplit"
fi

pythonString="python" # need python 2 to properly use exec function 
additionalSFStr=""
if [ "$additionalSF" = True ]; then
  additionalSFStr="--additionalSF"
  pythonString="python3" # need python 3 to access pickle file for rescaling 
fi

Single_HiggsStr=""
if [ "$Single_Higgs" = True ]; then
  Single_HiggsStr="--Single_Higgs"
fi 

isHHStr=""
if [ "$isHH" = True ]; then 
  isHHStr="--isHH"
fi 

fromTreeStr=""
if [ "$fromTree" = True ]; then 
  fromTreeStr="--fromTree"
fi 

echo "Defining command now"

if [ "$CATEGORIZE" = True ]; then 
  echo "Categorizing"
  python ${LOCAL}/Reweight_NLO.py --reweightNode ${reweightNode} --year ${YEAR} --syst ${SYST} --TDirec "" --categorize  ${isHHStr}  ${Single_HiggsStr} --Single_Higgs_File ${Single_Higgs_File} --inDir ${inDir}
else 
  # Reweight to a node 
  ${pythonString} ${LOCAL}/Reweight_NLO.py --reweightNode ${reweightNode} --year ${YEAR} --syst ${SYST} --TDirec "" --inDir ${inDir}  ${addNodeBranchstr}  ${evenOddSplitstr}  ${additionalSFStr}  ${Single_HiggsStr} --Single_Higgs_File ${Single_Higgs_File}  ${fromTreeStr}
  
  # combine or gennorm samples 
  
  # without GEN norm 
  #python ${LOCAL}/Reweight_NLO.py --node ${reweightNode} --year ${YEAR} --syst ${SYST} --TDirec "tagsDumper/trees" 
  
  # with GEN norm 
  #python ${LOCAL}/Reweight_NLO.py --node ${reweightNode} --year ${YEAR} --syst ${SYST} --TDirec "tagsDumper/trees" --GENnorm
fi  

echo -e "DONE";
'''

  arguments = []
  
  # Choose what you want to do 

  # # For combining input NLO files or adding variables
  # for year in years:
  #   print("year:",year)
  #   systLabels = GetSystLabels(year)
  #   if(args.NominalOnly): systLabels = ["Nominal"]
  #   print("systematic labels:",systLabels)
  #   for node in nodes:
  #     print("node:",node)
  #     for systLabel in systLabels:
  #       arguments.append("{} {} {} {} {} {} {} {} {} {} {} {} {}".format(local, node, year, systLabel, categorize, "NoInDir", "false", "false", "false", "false", "false", isHH, fromTree))

  # For reweighting already combined file with DNN score, or categorizing 
  for year in years:
    print("year:",year)
    systLabels = GetSystLabels(year)
    if(args.NominalOnly): systLabels = ["Nominal"]
    print("systematic labels:",systLabels)
    for reweightNode in reweightNodes:
      print("reweightNode:",reweightNode)
      for systLabel in systLabels:
        arguments.append("{} {} {} {} {} {} {} {} {} {} {} {} {}".format(local, reweightNode, year, systLabel, categorize, inDir, addNodeBranch, evenOddSplit, additionalSF, Single_Higgs, Single_Higgs_File, isHH, fromTree))

  # Save arguments to text file to be input for condor jobs 
  with open("arguments.txt", "w") as args:
    args.write("\n".join(arguments))

  with open("run_script.sh", "w") as rs:
    rs.write(script) 

  submitCommand = "condor_submit {scriptName}".format(scriptName=scriptName)
  print("$ {submitCommand}".format(submitCommand=submitCommand))
  os.system(submitCommand)
  print("DONE")