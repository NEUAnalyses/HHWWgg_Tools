#!/bin/sh -e

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
