#!/bin/bash
# Abe Tishelman-Charny
# 16 January 2019
# 
# The purpose of this script is to run the CRAB steps to create gen miniAOD's of WWgg for different decay channels. This is so variables can be plotted to see the differences in the processes. 

# Want to change to CMSSW directory which python config file was created in. 

# Location of my pythia fragments 
#/afs/cern.ch/work/a/atishelm/private/HH_WWgg/CMSSW_7_1_25/src/Configuration/GenProduction/python/ggF_X1000_WWgg_enuenugg.py
#/afs/cern.ch/work/a/atishelm/private/HH_WWgg/CMSSW_7_1_25/src/Configuration/GenProduction/python/ggF_X1000_WWgg_jjenugg.py

## Location of my CRAB configuration files (maybe not)
##/afs/cern.ch/work/a/atishelm/private/CRAB/CrabConfig.py

submit_crab_GEN(){

    cmssw_v=$3
    cd /afs/cern.ch/work/a/atishelm/private/HH_WWgg/$3/src/ # Directory where config file was conceived. Need to be in same CMSSW for crab config 
    cmsenv

    # Check if there is a VOMS proxy for using CRAB 
    check_proxy 

    # Source CRAB 
    source /cvmfs/cms.cern.ch/crab3/crab.sh

    # Create CRAB Config file 
    IDName=$1 # Decay identifying name. Anything unique about the process should be contained in the pythia fragment file name 
    IDName=${IDName%???} # Remove .py 

    ccname=$IDName
    ccname+="_CrabConfig.py" # Crab Configuration file name 

    echo "Total events = $2"
    totevts=$2 
    #njobs=10 # Predetermined number of files to spread MC events over 
    njobs=1 # Predetermined number of files to spread MC events over 

    echo "totevts = $totevts"
    echo "njobs = $njobs"

    EvtsPerJob=$((totevts/njobs))
    echo "EvtsPerJob = $EvtsPerJob"

    echo "from CRABClient.UserUtilities import config, getUsernameFromSiteDB" >> TmpCrabConfig.py
    echo "config = config()" >> TmpCrabConfig.py
    echo " " >> TmpCrabConfig.py

    echo "config.General.requestName = '$IDName'" >> TmpCrabConfig.py
    echo "config.General.workArea = 'crab_projects_2'" >> TmpCrabConfig.py # Give this a unique name? 
    echo "config.General.transferOutputs = True" >> TmpCrabConfig.py
    echo "config.General.transferLogs = False" >> TmpCrabConfig.py
    echo " " >> TmpCrabConfig.py
    echo "config.JobType.pluginName = 'PrivateMC'" >> TmpCrabConfig.py
    echo "config.JobType.psetName = '/afs/cern.ch/work/a/atishelm/private/HH_WWgg/$1'" >> TmpCrabConfig.py # Depends on where config file was created  
    echo " " >> TmpCrabConfig.py
    echo "config.Data.outputPrimaryDataset = 'MinBias'" >> TmpCrabConfig.py
    echo "config.Data.splitting = 'EventBased'" >> TmpCrabConfig.py
    echo "config.Data.unitsPerJob = $((EvtsPerJob))" >> TmpCrabConfig.py # number of events per job for MC 
    #echo "NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line." >> TmpCrabConfig.py
    echo "NJOBS = 1  # This is not a configuration parameter, but an auxiliary variable that we use in the next line." >> TmpCrabConfig.py
    echo "config.Data.totalUnits = config.Data.unitsPerJob * NJOBS" >> TmpCrabConfig.py # Total number of events over all jobs (files) 
    #echo "#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB()) " >> TmpCrabConfig.py
    echo "config.Data.outLFNDirBase = '/store/user/atishelm/'" >> TmpCrabConfig.py
    echo "config.Data.publication = True" >> TmpCrabConfig.py
    echo "config.Data.outputDatasetTag = '$IDName'" >> TmpCrabConfig.py
    #echo "config.Data.userInputFiles = ['/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_woPU/190116_184220/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1.root'] # If DR1 step, this should be GEN file " >> TmpCrabConfig.py
    echo " " >> TmpCrabConfig.py
    #echo "config.Site.whitelist = ['T2_CH_CERN']" >> TmpCrabConfig.py  
    echo "config.Site.storageSite = 'T2_CH_CERN'" >> TmpCrabConfig.py

    cp TmpCrabConfig.py $ccname
    rm TmpCrabConfig.py 

    crab submit -c $ccname 
    crab status 

    }
