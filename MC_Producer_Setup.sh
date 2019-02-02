#!/bin/bash

source /afs/cern.ch/work/a/atishelm/private/HH_WWgg/MC_Producer_Cfgs.sh

# Idea: Read crab status message to see if job is finished, and if it is, obtain the path to the files and run the next step? 
# Make folder for pythia configuration files that end up in HH_WWgg/. Bin? Py_cfgs? 

chosen_config=$1

echo "Chosen configuration: $chosen_config"

chosen_step_=${chosen_config}[step]
chosen_step=${!chosen_step_}

echo "chosen_step = $chosen_step"

if [ $chosen_step == GEN ]
then

    # Params: filename, step, events 

    chosen_filename_=${chosen_config}[filename]
    chosen_events_=${chosen_config}[events]

    chosen_filename=${!chosen_filename_}
    chosen_events=${!chosen_events_}

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  filename: $chosen_filename"
    echo "  events: $chosen_events"

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
    ConfigFileName="cmssw_configs/"
    ConfigFileName+=${GenSimOutput%????} # Remove 'root' # Gensimoutput is a bad name 
    ConfigFileName+=py 

    echo 'Input File Name:' $PythiaFragPath
    echo 'Output File Name:' $GenSimOutput

elif [ $chosen_step == DR1 ] || [ $chosen_step == DR2 ]
then
    # Params: DRInput, pileup, step, events 

    chosen_genoutput_=${chosen_config}[DRInput]
    chosen_genoutput=${!chosen_genoutput_}
    GenSimOutput=$chosen_genoutput

    chosen_pileup_=${chosen_config}[pileup]
    chosen_pileup=${!chosen_pileup_}

    chosen_events_=${chosen_config}[events]
    chosen_events=${!chosen_events_}

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  input filename: $chosen_genoutput"
    echo "  pileup: $chosen_pileup"
    echo "  events: $chosen_events"

elif [ $chosen_step == MINIAOD ]
then

    chosen_genoutput_=${chosen_config}[MINIAODInput]
    chosen_genoutput=${!chosen_genoutput_}
    PrevStepOutput=$chosen_genoutput

    chosen_pileup_=${chosen_config}[pileup]
    chosen_pileup=${!chosen_pileup_}

    chosen_events_=${chosen_config}[events]
    chosen_events=${!chosen_events_}

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  input filename: $chosen_genoutput"
    echo "  pileup: $chosen_pileup"
    echo "  events: $chosen_events"

elif [ $chosen_step == MICROAOD ]
then

    chosen_miniaodoutput_=${chosen_config}[MICROAODInput]
    chosen_miniaodoutput=${!chosen_miniaodoutput_}
    GenSimOutput=$chosen_miniaodoutput

    chosen_pileup_=${chosen_config}[pileup]
    chosen_pileup=${!chosen_pileup_}

    chosen_events_=${chosen_config}[events]
    chosen_events=${!chosen_events_}

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  input filename: $chosen_miniaodoutput"
    echo "  pileup: $chosen_pileup"
    echo "  events: $chosen_events"

else 
    
    echo 'Did not find desired step'
    echo 'Please enter an argument whose array has one of the following for "step":'
    echo '  GEN'
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

    echo "Finished desired step: $chosen_step "
    echo "Exiting"
    cd /afs/cern.ch/work/a/atishelm/private/HH_WWgg
    return;
    #exit 1;
}