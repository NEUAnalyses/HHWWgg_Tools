#!/bin/bash

#############################################################
#   This script is used by McM when it performs automatic   #
#  validation in HTCondor or submits requests to computing  #
#                                                           #
#      !!! THIS FILE IS NOT MEANT TO BE RUN BY YOU !!!      #
# If you want to run validation script yourself you need to #
#     get a "Get test" script which can be retrieved by     #
#  clicking a button next to one you just clicked. It will  #
# say "Get test command" when you hover your mouse over it  #
#      If you try to run this, you will have a bad time     #
#############################################################

#cd /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/TSG-SnowmassWinter21wmLHEGEN-00116/

# Make voms proxy
#voms-proxy-init --voms cms --out $(pwd)/voms_proxy.txt --hours 4
#export X509_USER_PROXY=$(pwd)/voms_proxy.txt

export SCRAM_ARCH=slc7_amd64_gcc820

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_11_0_2/src ] ; then
  echo release CMSSW_11_0_2 already exists
else
  scram p CMSSW CMSSW_11_0_2
fi
cd CMSSW_11_0_2/src
eval `scram runtime -sh`

# Download fragment from McM
#curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-SnowmassWinter21wmLHEGEN-00116 --retry 3 --create-dirs -o Configuration/GenProduction/python/TSG-SnowmassWinter21wmLHEGEN-00116-fragment.py
#[ -s Configuration/GenProduction/python/TSG-SnowmassWinter21wmLHEGEN-00116-fragment.py ] || exit $?;
scram b
cd ../..

# Maximum validation duration: 28800s
# Margin for validation duration: 30%
# Validation duration with margin: 28800 * (1 - 0.30) = 20160s
# Time per event for each sequence: 0.3147s
# Threads for each sequence: 1
# Time per event for single thread for each sequence: 1 * 0.3147s = 0.3147s
# Which adds up to 0.3147s per event
# Single core events that fit in validation duration: 20160s / 0.3147s = 64068
# Produced events limit in McM is 10000
# According to 1.0000 efficiency, validation should run 10000 / 1.0000 = 10000 events to reach the limit of 10000
# Take the minimum of 64068 and 10000, but more than 0 -> 10000
# It is estimated that this validation will produce: 10000 * 1.0000 = 10000 events
#EVENTS=10000


# cmsDriver command
#cmsDriver.py Configuration/GenProduction/python/TSG-SnowmassWinter21wmLHEGEN-00116-fragment.py --python_filename TSG-SnowmassWinter21wmLHEGEN-00116_1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN,LHE --fileout file:TSG-SnowmassWinter21wmLHEGEN-00116.root --conditions 110X_mcRun4_realistic_v3 --beamspot HLLHC14TeV --step LHE,GEN --geometry Extended2026D49 --era Phase2C9 --no_exec --mc -n $EVENTS || exit $? ;
