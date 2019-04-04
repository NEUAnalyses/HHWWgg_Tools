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

submit_crab_postGEN(){

    #!/bin/bash

    unset file_paths # Make sure array name is free in memory 
    declare -a file_paths # unassociative array 
    
    # echo "0 = $0"
    # echo "1 = $1"
    # echo "2 = $2"
    # echo "3 = $3"
    # echo "4 = $4"

    cmssw_v=$2
    chosen_threads=$3 
    chosen_job_size=$4
    #chosen_events=$5
    file_paths=("$@") # saves all inputs to array. Could be convinient for cleaning up later.

    echo "chosen_job_size = $chosen_job_size" # Number of input files per job 
    # Remove first four arguments 

    file_paths=("${file_paths[@]:4}") 

    # EvtsPerJob=$((totevts/chosen_jobs))
    # echo "EvtsPerJob = $EvtsPerJob"

    # Create userInputFiles list for crab submission:

    path_list=''

    last_path=${file_paths[${#file_paths[@]}-1]} # file_paths[-1] not working for some reason 
    echo "last_path = $last_path"


    #crab_input=${GenSimOutput#"/eos/cms"} # Remove beginning of gen output (DR1 input) file path so it can be read by the crab config 
    #echo "Crab Input = $crab_input"

    for path in "${file_paths[@]}"; 
        do echo "path = $path"
        path_=$path
        path=${path#"file:/eos/cms"}; # remove prefix. Don't need this for crab config userinput files 
        path="${path:0:p}'${path:p}" # add starting quote
        path+="'" # add end quote
        path_list+=$path; 

        if [ $path_ != $last_path ] # If not the path of the last element, add a comma
        then 
            path_list+=','
        fi 
    done

    echo "path list = $path_list"

    echo "chosen threads: $chosen_threads "
    cd /afs/cern.ch/work/a/atishelm/private/HH_WWgg/$cmssw_v/src/ # Directory where config file was conceived. Need to be in same CMSSW for crab config 
    cmsenv

    # Check if there is a VOMS proxy for using CRAB 
    check_proxy 

    # Source CRAB 
    source /cvmfs/cms.cern.ch/crab3/crab.sh

    # Create CRAB Config file 
    IDName=$1 # Decay identifying name. Anything unique about the process should be contained in the pythia fragment file name 
    #IDName=${IDName#"cmssw_configs/"} # Remove cmssw folder part from eventual crab config path
    IDName=${IDName#"$cmssw_v/src/cmssw_configs/"} # Remove 'CMSSW_X_X_X/src/cmssw_configs' from ID 
    
    IDName=${IDName%???} # Remove .py 

    echo "IDName = $IDName"

    # This naming convention assumes IDName of the form:
    # <ProductionProcess>_<ResonantParticle>_<ResonantDecay>_<Channel>_<numEvents>_<pileupOption>_<Step>
    # ex: ggF_X1250_WWgg_enuenugg_10000events_woPU_DR1
    primdset=`echo $IDName | cut -d _ -f -4` # Primary dataset name 
    snddset=`echo $IDName | cut -d _ -f 5-` # Secondary dataset name 

    echo "primary dataset name = $primdset"
    echo "secondary dataset name = $snddset"

    ccname=$IDName
    ccname+="_CrabConfig.py" # Crab Configuration file name 

    totfiles=1 # (I think) this is the number of files to spread the crab output across. It may also be the number of files to use as input 

    echo "from CRABClient.UserUtilities import config, getUsernameFromSiteDB" >> TmpCrabConfig.py
    echo "config = config()" >> TmpCrabConfig.py
    echo " " >> TmpCrabConfig.py

    # if crab working area already exists, increment to unique name 
    #working_area=/afs/cern.ch/work/a/atishelm/private/HH_WWgg/$cmssw_v/src/crab_projects/crab_$IDName
    working_area=/afs/cern.ch/work/a/atishelm/private/HH_WWgg/$cmssw_v/src/crab_projects/crab_$IDName

    # Do until unused working area name is found 
    # Make into some unique name function? Don't need to yet I guess 
    i=$((0))
    while : ; do

        if [ $i == 0 ]; then

            # If default working area doesn't exist, use this name 
            if [ ! -d $working_area ]; then 

                echo "Creating crab working area: '$working_area' for this crab request"
                # No need to increment IDName 
                break 
        
            fi

        else 
        
            tmp_IDName=$IDName
            tmp_IDName+=_$i 
            working_area=/afs/cern.ch/work/a/atishelm/private/HH_WWgg/$cmssw_v/src/crab_projects/crab_$tmp_IDName 
            if [ ! -d $working_area ]; then

                echo "Creating crab working area: '$working_area' for this crab request"
                IDName=$tmp_IDName 
                # Use incremented IDName 
                break 

            fi 
    
        fi

    i=$((i+1))

    #echo "i = $i"
    #if [ $i == 2 ]; then
    #    break 
    #fi

    done

    echo "config.General.requestName = '$IDName'" >> TmpCrabConfig.py # leave this name the same since it's just the crab working area name
    #echo "config.General.requestName = '$snddset'" >> TmpCrabConfig.py

    echo "config.General.workArea = 'crab_projects'" >> TmpCrabConfig.py
    echo "config.General.transferOutputs = True" >> TmpCrabConfig.py
    echo "config.General.transferLogs = False" >> TmpCrabConfig.py
    echo " " >> TmpCrabConfig.py
    echo "config.JobType.pluginName = 'Analysis'" >> TmpCrabConfig.py
    #echo "arg = $1"
    echo "config.JobType.psetName = '/afs/cern.ch/work/a/atishelm/private/HH_WWgg/$1'" >> TmpCrabConfig.py # Depends on cmssw config memory location  
    #s_str='SEED=$CRAB_Id'
    #echo "config.JobType.pyCfgParams = [$s_str]" >> TmpCrabConfig.py



    if [ $chosen_threads != noval ]
    then
        echo "config.JobType.numCores = $chosen_threads" >> TmpCrabConfig.py  
        echo "config.JobType.maxMemoryMB = 8000" >> TmpCrabConfig.py
    else
        echo "no thread customization chosen. Not including numCores or maxMemory options in crab config file."
    fi 

    echo " " >> TmpCrabConfig.py

    #echo "config.Data.outputPrimaryDataset = 'postGEN_Outputs'" >> TmpCrabConfig.py
    echo "config.Data.outputPrimaryDataset = '$primdset'" >> TmpCrabConfig.py    


    echo "config.Data.splitting = 'FileBased'" >> TmpCrabConfig.py
    echo "config.Data.unitsPerJob = $chosen_job_size" >> TmpCrabConfig.py # Number of input files per job  
    #echo "config.Data.unitsPerJob = $chosen_jobs" >> TmpCrabConfig.py # Number of output files (need to verify this for DR1)  

    #echo "#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB()) " >> TmpCrabConfig.py
    echo "config.Data.outLFNDirBase = '/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/'" >> TmpCrabConfig.py
    #echo "config.Data.outLFNDirBase = '/store/user/atishelm/'" >> TmpCrabConfig.py
    echo "config.Data.publication = True" >> TmpCrabConfig.py
    #echo "config.Data.outputDatasetTag = '$IDName'" >> TmpCrabConfig.py
    echo "config.Data.outputDatasetTag = '$snddset'" >> TmpCrabConfig.py

    echo "config.Data.userInputFiles = [$path_list] # If DR1 step, this should be GEN file(s) " >> TmpCrabConfig.py # input files 
    echo " " >> TmpCrabConfig.py
    echo "config.Site.whitelist = ['T2_CH_CERN']" >> TmpCrabConfig.py # might need this..might not. I'm not sure. 
    echo "config.Site.storageSite = 'T2_CH_CERN'" >> TmpCrabConfig.py

    # Now using multiple cmssw version, so will have a crab_configs and cmssw_configs folder for each CMSSW 
    
    #echo "pwd = $PWD" 
    #echo "ccname = $ccname"

    cp TmpCrabConfig.py $ccname
    #mv $ccname ../../crab_configs/$ccname  
    mv $ccname crab_configs/$ccname  
    rm TmpCrabConfig.py 

    #crab submit -c ../../crab_configs/$ccname 

    # Just need last two 
    crab submit -c crab_configs/$ccname 
    crab status 

    }
