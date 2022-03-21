#!/bin/bash

export SCRAM_ARCH=slc7_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_6_17_patch1/src ] ; then
  echo release CMSSW_10_6_17_patch1 already exists
else
  scram p CMSSW CMSSW_10_6_17_patch1
fi
cd CMSSW_10_6_17_patch1/src
eval `scram runtime -sh`

scram b
cd ../..

# cmsDriver command
# cmsDriver.py  --python_filename B2G-RunIISummer20UL17MiniAOD-00765_1_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:B2G-RunIISummer20UL17MiniAOD-00765.root --conditions 106X_mc2017_realistic_v6 --step PAT --geometry DB:Extended --filein file:fff.root --era Run2_2017 --runUnscheduled --no_exec --mc -n 10