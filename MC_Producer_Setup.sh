#!/bin/bash

# Idea: Read crab status message to see if job is finished, and if it is, obtain the path to the files and run the next step? 
# Make folder for pythia configuration files that end up in HH_WWgg/. Bin? Py_cfgs? 

# Create configurations
declare -A enuenu
declare -A enuenunopu
declare -A jjenu
declare -A jjenunopu
declare -A enuenunopuDR1
declare -A enuenunopuDR2
declare -A enuenunopuMINIAOD

# Number of events should be a multiple of 10 
#enuenu=( ["filename"]=ggF_X1000_WWgg_enuenugg ["pileup"]=wPU ["startingstep"]=GEN ["endingstep"]=GEN ["events"]=10000)

# Gen configs 
# Need to include pythia fragment
enuenu=( ["filename"]=ggF_X1000_WWgg_enuenugg ["pileup"]=wPU ["step"]=GEN ["events"]=1000)
enuenunopu=( ["filename"]=ggF_X1000_WWgg_enuenugg ["pileup"]=woPU ["step"]=GEN ["events"]=1000)
jjenu=( ["filename"]=ggF_X1000_WWgg_jjenugg ["pileup"]=wPU ["step"]=GEN ["events"]=1000)
jjenunopu=( ["filename"]=ggF_X1000_WWgg_jjenugg ["pileup"]=woPU ["step"]=GEN ["events"]=1000)

# DR1 config
# Need to include location of Gen output file 
enuenunopuDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_woPU/190116_184220/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1.root ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)

# DR2
enuenunopuDR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1/190119_113807/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1.root ["pileup"]=woPU ["step"]=DR2 ["events"]=1000)

# MINIAOD 
enuenunopuMINIAOD=( ["MINIAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2/190119_123028/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1.root ["pileup"]=woPU ["step"]=MINIAOD ["events"]=1000)

if [ ${#1} == 0 ]
then
    echo 'Please enter an argument for the configuration'
    echo 'Current options are:'
    echo 
    echo 'GEN:'
    echo '  enuenu'
    echo '  enuenunopu'
    echo '  jjenu'
    echo '  jjenunopu'
    echo 
    echo 'DR:'
    echo '  enuenunopuDR1'
    echo '  enuenunopuDR2'
    echo 
    echo 'MINIAOD:'
    echo '  enuenunopuMINIAOD'
    echo 
    echo 'Exiting'
    return
fi

chosen_config=$1

echo "Chosen configuration: $chosen_config"

chosen_step_=${chosen_config}[step]
chosen_step=${!chosen_step_}

echo "chosen_step = $chosen_step"

if [ $chosen_step == DR1 ] || [ $chosen_step == DR2 ]
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
    # 
    chosen_genoutput_=${chosen_config}[MINIAODInput]
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

else 
    # Params: filename, pileup, step, events 

    chosen_filename_=${chosen_config}[filename]
    chosen_pileup_=${chosen_config}[pileup]
    chosen_events_=${chosen_config}[events]

    chosen_filename=${!chosen_filename_}
    chosen_pileup=${!chosen_pileup_}
    chosen_events=${!chosen_events_}

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  filename: $chosen_filename"
    echo "  pileup: $chosen_pileup"
    echo "  events: $chosen_events"

    #started=false

    # Define Pythia fragment path
    PythiaFragPath=Configuration/GenProduction/python/
    PythiaFragPath+=$chosen_filename
    PythiaFragPath+=.py

    # Define output file name 
    GenSimOutput=$chosen_filename
    GenSimOutput+='_'

    # Add PU info to file name 
    if [ $chosen_pileup == wPU ]
        then
        GenSimOutput+="wPU"

    fi 

    if [ $chosen_pileup == woPU ]
        then
        GenSimOutput+="woPU"

    fi 

    GenSimOutput+='_'

    GenSimOutput+=$chosen_events
    GenSimOutput+=events
    GenSimOutput+='_'
    GenSimOutput+=$chosen_step 
    GenSimOutput+=.root

    # Config File Name
    ConfigFileName=${GenSimOutput%????}
    ConfigFileName+=py 

    echo 'Input File Name:' $PythiaFragPath
    echo 'Output File Name:' $GenSimOutput


fi 

## Functions for later 

# Check for active VOMS proxy 
check_proxy(){

    voms-proxy-info &> TmpFile.txt  
    output=`cat TmpFile.txt`
    rm TmpFile.txt 

    if [ "$output" = "Proxy not found: /tmp/x509up_u95168 (No such file or directory)" ] ; then
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
    return
}