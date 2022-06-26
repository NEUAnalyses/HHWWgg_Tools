#!/bin/bash

export SCRAM_ARCH=slc7_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_6_4/src ] ; then
  echo release CMSSW_10_6_4 already exists
else
  scram p CMSSW CMSSW_10_6_4
fi
cd CMSSW_10_6_4/src
eval `scram runtime -sh`

scram b
eval `scramv1 runtime -sh`
scram b 
#cmsenv
cd ../..

# cmsDriver command
# cmsDriver.py  --python_filename HIG-RunIISummer19UL17DIGIPremix-00434_1_cfg.py --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --fileout file:HIG-RunIISummer19UL17DIGIPremix-00434.root --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer19ULPrePremix-UL17_106X_mc2017_realistic_v6-v1/PREMIX" --conditions 106X_mc2017_realistic_v6 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --filein file:HIG-RunIISummer19UL17SIM-00545.root --datamix PreMix --era Run2_2017 --runUnscheduled --no_exec --mc -n 10
