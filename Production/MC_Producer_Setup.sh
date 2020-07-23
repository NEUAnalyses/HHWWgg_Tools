#!/bin/bash

chosen_step=$1
chosen_events=$2
chosen_jobs=$3
chosen_filename=$4
#chosen_pileup=$5 
LocalGridpack=$6
Campaign=$7
Year=$8
dryRun=$9

echo "chosen_step = $chosen_step"
echo "LocalGridpack: $LocalGridpack "
echo "Campaign: $Campaign"

if [ $chosen_step == GEN-SIM ]
then

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  filename: $chosen_filename"
    echo "  events: $chosen_events"
    echo "  jobs: $chosen_jobs"
    echo "  LocalGridpack: $LocalGridpack"

    # Define Pythia fragment path relative to CMSSW release src 
    PythiaFragPath=Configuration/GenProduction/python/
    PythiaFragPath+=$chosen_filename
    PythiaFragPath+=.py

    # Define output file name 
    GenSimOutput=$chosen_filename

    GenSimOutput+='_'
    GenSimOutput+=$chosen_events
    GenSimOutput+=events
    GenSimOutput+='_'
    GenSimOutput+=$chosen_step 
    GenSimOutput+=.root

    # Config File Name
    mkdir -p cmssw_configs # create directory if it does not already exist
    ConfigFileName="cmssw_configs/${Campaign}_"
    # ConfigFileName="cmssw_configs/"
    ConfigFileName+=${GenSimOutput%????} # Remove 'root' # Gensimoutput is a bad name 
    ConfigFileName+=py 

    echo 'Input File Name:' $PythiaFragPath
    echo 'Output File Name:' $GenSimOutput

    # if using localgridpack, need to change pythia fragment path to gridpack, and add to sandbox in crab. Do pythia part here since cmsDriver step using pythia fragment is before crab 
    LocalGridpackPath="none"
    if [ $LocalGridpack == "1" ]
    then 
        echo "Using a local gridpack. Need to change pythia fragment path and save full path to later add to crab sandbox"
        # go to file PythiaFragPath, grab 
        # args = cms.vstring('/afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/NMSSM/genproductions/bin/MadGraph5_aMCatNLO/NMSSM_XYH_WWgg_MX_300_MY_170_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz'),
        line=`grep -F "args" CMSSW_9_3_9_patch1/src/$PythiaFragPath`
        LocalGridpackPath=$(sed 's/.*(\(.*\)).*/\1/' <<< "$line") # save text between two parentheses 
        endofGridpackPath="${LocalGridpackPath##*/}" # trim everything up to last "/"
        newGridpackPath="'/srv/${endofGridpackPath}"
        echo "Replacing ${LocalGridpackPath} with ${newGridpackPath}"

        filePath="CMSSW_9_3_9_patch1/src/${PythiaFragPath}"
        sed -i "s~$LocalGridpackPath~$newGridpackPath~g" "$filePath" # lesson: if you want to use sed to replace a variable containing slashes, use ~ instead of slashes in sed command for deliminator
        
    fi 
    # end_script


elif [ $chosen_step == GEN ]
then

    # Params: filename, step, events 

    # chosen_filename_=${chosen_config}[filename]
    # chosen_events_=${chosen_config}[events]
    # chosen_jobs_=${chosen_config}[jobs]

    # chosen_filename=${!chosen_filename_}
    # chosen_events=${!chosen_events_}
    # chosen_jobs=${!chosen_jobs_}

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  filename: $chosen_filename"
    echo "  events: $chosen_events"
    echo "  jobs: $chosen_jobs"
    echo "  LocalGridpack: $LocalGridpack"

    # Define Pythia fragment path relative to CMSSW release src 
    PythiaFragPath=Configuration/GenProduction/python/
    PythiaFragPath+=$chosen_filename
    PythiaFragPath+=.py

    # Define output file name 
    GenOutput=$chosen_filename

    GenOutput+='_'
    GenOutput+=$chosen_events
    GenOutput+=events
    GenOutput+='_'
    GenOutput+=$chosen_step 
    GenOutput+=.root

    # Config File Name
    mkdir -p cmssw_configs # create directory if it does not already exist
    ConfigFileName="cmssw_configs/${Campaign}_"
    ConfigFileName+=${GenOutput%????} # Remove 'root' # Gensimoutput is a bad name 
    ConfigFileName+=py 

    echo 'Input File Name:' $PythiaFragPath
    echo 'Output File Name:' $GenOutput

    # if using localgridpack, need to change pythia fragment path to gridpack, and add to sandbox in crab. Do pythia part here since cmsDriver step using pythia fragment is before crab 
    LocalGridpackPath="none"
    if [ $LocalGridpack == "1" ]
    then 
        echo "Using a local gridpack. Need to change pythia fragment path and save full path to later add to crab sandbox"
        # go to file PythiaFragPath, grab 
        # args = cms.vstring('/afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/NMSSM/genproductions/bin/MadGraph5_aMCatNLO/NMSSM_XYH_WWgg_MX_300_MY_170_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz'),
        line=`grep -F "args" CMSSW_9_3_9_patch1/src/$PythiaFragPath`
        LocalGridpackPath=$(sed 's/.*(\(.*\)).*/\1/' <<< "$line") # save text between two parentheses 
        endofGridpackPath="${LocalGridpackPath##*/}" # trim everything up to last "/"
        newGridpackPath="'/srv/${endofGridpackPath}"
        echo "Replacing ${LocalGridpackPath} with ${newGridpackPath}"

        filePath="CMSSW_9_3_9_patch1/src/${PythiaFragPath}"
        sed -i "s~$LocalGridpackPath~$newGridpackPath~g" "$filePath" # lesson: if you want to use sed to replace a variable containing slashes, use ~ instead of slashes in sed command for deliminator
        
    fi 

elif [ $chosen_step == DR1 ] || [ $chosen_step == DR2 ]
then
    # Params: DRInput, pileup, step, events 

    echo "Setting up $chosen_step"

    #chosen_genoutput_=${chosen_config}[DRInput]
    #chosen_genoutput=${!chosen_genoutput_}
    chosen_genoutput=$4 
    GenSimOutput=$chosen_genoutput # Should be a directory ending in '/'
    GenSimOutput+="*"

    
    # Turn directory into comma separated files for DR steps
    # If DR1 step, want to ignore LHE files created by GEN step

    #$GenSimOutput+='*' # to search for all files 

    # Could make a function to do this job. 

    unset f_paths # Make sure array name is free in memory 
    declare -a f_paths # unassociative array 

    f_paths=() 
    #echo "gensimoutput = $GenSimOutput"
    # First performs the grep command, then adds files. This takes a while for 100 files
    for path in $GenSimOutput; do
        #echo "path = $path"
        if [[ $path != *"inLHE"* ]]; then # double brackets allows you to use * outside quotes 
            #echo "path = $path"
            f_paths+=("file:$path"); 
        fi 
        done 

    # for path in `grep -L "inLHE" $GenSimOutput`; # ignore files containing 'inLHE'
    #     #echo "path = $path"
    #     do 
    #     echo "path = $path"
    #     f_paths+=("file:$path");
    #     #echo "checked path"
    #     done  

    # Then want single string whith comma separated names for cmsDriver command 

    SinglePath=${f_paths[0]}

    paths_string=''

    last_path=${f_paths[${#f_paths[@]}-1]} # f_paths[-1] not working for some reason 

    for path in "${f_paths[@]}"; 
        do paths_string+=$path; 
        if [ $path != $last_path ] # If not the path of the last element, add a comma
        then 
            paths_string+=','
        fi 
        done

    #echo "paths_string = $paths_string"

    chosen_events=$2
    chosen_job_size=$3
    chosen_pileup=$5 

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  input file(s) directory: $chosen_genoutput"
    echo "  pileup: $chosen_pileup"
    echo "  events: $chosen_events"
    echo "  job size: $chosen_job_size"  # Number of input files per job  

elif [ $chosen_step == MINIAOD ]
then

    # chosen_genoutput_=${chosen_config}[MINIAODInput]
    # chosen_genoutput=${!chosen_genoutput_}
    chosen_genoutput=$4 
    PrevStepOutput=$chosen_genoutput # directory ending in '/'
    PrevStepOutput+="*"

    unset f_paths # Make sure array name is free in memory 
    declare -a f_paths # unassociative array 

    f_paths=() 
    #echo "gensimoutput = $GenSimOutput"
    # First performs the grep command, then adds files. This takes a while for 100 files
    for path in $PrevStepOutput; do
        #echo "path = $path"
        if [[ $path != *"inLHE"* ]]; then # double brackets allows you to use * outside quotes 
            #echo "path = $path"
            f_paths+=("file:$path"); 
        fi 
        done 

    # f_paths=() 
    # for path in `grep -L "inLHE" $PrevStepOutput`; # ignore files containing 'inLHE'
    #     do f_paths+=("file:$path");
    #     done  

    # Then want single string whith comma separated names for cmsDriver command 

    SinglePath=${f_paths[0]}

    paths_string=''

    last_path=${f_paths[${#f_paths[@]}-1]} # f_paths[-1] not working for some reason 

    for path in "${f_paths[@]}"; 
        do paths_string+=$path; 
        if [ $path != $last_path ] # If not the path of the last element, add a comma
        then 
            paths_string+=','
        fi 
        done

    #echo "paths_string = $paths_string"

    # chosen_pileup_=${chosen_config}[pileup]
    # chosen_pileup=${!chosen_pileup_}

    # chosen_events_=${chosen_config}[events]
    # chosen_events=${!chosen_events_}

    # chosen_job_size_=${chosen_config}[jobsize]
    # chosen_job_size=${!chosen_job_size_}

    chosen_events=$2
    chosen_job_size=$3
    #chosen_pileup=$5 

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  input file(s) directory: $PrevStepOutput"
    #echo "  pileup: $chosen_pileup"
    echo "  events: $chosen_events"
    echo "  job size: $chosen_job_size"

elif [ $chosen_step == MICROAOD ]
then

    chosen_miniaodoutput_=${chosen_config}[MICROAODInput]
    chosen_miniaodoutput=${!chosen_miniaodoutput_}
    GenSimOutput=$chosen_miniaodoutput

    #chosen_pileup_=${chosen_config}[pileup]
    #chosen_pileup=${!chosen_pileup_}

    chosen_events_=${chosen_config}[events]
    chosen_events=${!chosen_events_}

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  input filename: $chosen_miniaodoutput"
    #echo "  pileup: $chosen_pileup"
    echo "  events: $chosen_events"

else 
    
    echo 'Did not find desired step'
    echo 'Please enter an argument whose array has one of the following for "step":'
    echo '  GEN-SIM'
    echo '  DR1'
    echo '  DR2'
    echo '  MINIAOD'
    echo '  MICROAOD'
    echo ''
    echo 'Exiting'
    return;
    #exit 1;


fi 

## Functions for later 

# Check for active VOMS proxy 
check_proxy(){

    voms-proxy-info &> TmpFile.txt  
    output=`cat TmpFile.txt`
    rm TmpFile.txt 

    if [ "$output" = "Proxy not found: /tmp/x509up_u95168 (No such file or directory)" ] ; then # Change to 'if does not equal the message sent when there is a valid proxy'? 
        echo "No active grid proxy"
        echo "Prompting the user now"
        # Get access to LHC Computing Grid resources 
        voms-proxy-init --voms cms --valid 168:00
        # Optional: Have password entered by script here 
    fi 

}

# Exit script
end_script(){

    #echo "Finished desired step: $chosen_step "
    echo "Exiting"
    cd /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production
    return;
    #exit 1;
}

# Edit a CMSSW configuration file to include a seed for shuffling a list of pileup files
shuffle_PU(){

    echo "adding PU shuffling to cmssw config file"
    # open config file
    # add lines 
    
}

if [ $Year == 2016 ]
then 
    source /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production/MC_Producer_2016.sh
fi 

if [ $Year == 2017 ]
then 
    source /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production/MC_Producer_2017.sh
fi 
 
if [ $Year == 2018 ]
then 
    source /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production/MC_Producer_2018.sh
fi 