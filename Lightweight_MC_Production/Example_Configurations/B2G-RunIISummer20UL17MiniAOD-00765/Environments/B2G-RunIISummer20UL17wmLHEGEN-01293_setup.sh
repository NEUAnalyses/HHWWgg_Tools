#!/bin/bash

export SCRAM_ARCH=slc7_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_6_25/src ] ; then
  echo release CMSSW_10_6_25 already exists
else
  scram p CMSSW CMSSW_10_6_25
fi
cd CMSSW_10_6_25/src
eval `scram runtime -sh`

# Download fragment from McM
#curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/B2G-RunIISummer20UL17wmLHEGEN-01293 --retry 3 --create-dirs -o Configuration/GenProduction/python/B2G-RunIISummer20UL17wmLHEGEN-01293-fragment.py
#[ -s Configuration/GenProduction/python/B2G-RunIISummer20UL17wmLHEGEN-01293-fragment.py ] || exit $?;

scram b
cd ../..

# cmsDriver command 
# cmsDriver.py Configuration/GenProduction/python/B2G-RunIISummer20UL17wmLHEGEN-01293-fragment.py --python_filename B2G-RunIISummer20UL17wmLHEGEN-01293_1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN,LHE --fileout file:B2G-RunIISummer20UL17wmLHEGEN-01293.root --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --customise_commands process.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --step LHE,GEN --geometry DB:Extended --era Run2_2017 --no_exec --mc -n 10 
