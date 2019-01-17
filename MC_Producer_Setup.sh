#!/bin/bash

# Create configurations
declare -A enuenu
declare -A enuenunopu
declare -A jjenu
declare -A jjenunopu

# Number of events should be a multiple of 10 
enuenu=( ["filename"]=ggF_X1000_WWgg_enuenugg ["pileup"]=wPU ["startingstep"]=GEN ["endingstep"]=GEN ["events"]=10000)
enuenunopu=( ["filename"]=ggF_X1000_WWgg_enuenugg ["pileup"]=woPU ["startingstep"]=GEN ["endingstep"]=GEN ["events"]=10000)
jjenu=( ["filename"]=ggF_X1000_WWgg_jjenugg ["pileup"]=wPU ["startingstep"]=GEN ["endingstep"]=GEN ["events"]=10000)
jjenunopu=( ["filename"]=ggF_X1000_WWgg_jjenugg ["pileup"]=woPU ["startingstep"]=GEN ["endingstep"]=GEN ["events"]=10000)

if [ ${#1} == 0 ]
then
    echo 'Please enter an argument for the configuration'
    echo 'Current options are:'
    echo '  enuenu'
    echo '  enuenunopu'
    echo '  jjenu'
    echo '  jjenunopu'
    echo 
    echo 'Exiting'
    return
fi

chosen_config=$1

echo "Chosen configuration: $chosen_config"

chosen_filename_=${chosen_config}[filename]
chosen_pileup_=${chosen_config}[pileup]
chosen_startingstep_=${chosen_config}[startingstep]
chosen_endingstep_=${chosen_config}[endingstep]
chosen_events_=${chosen_config}[events]

chosen_filename=${!chosen_filename_}
chosen_pileup=${!chosen_pileup_}
chosen_startingstep=${!chosen_startingstep_}
chosen_endingstep=${!chosen_endingstep_}
chosen_events=${!chosen_events_}

echo "Chosen setup parameters:"
echo "  filename: $chosen_filename"
echo "  pileup: $chosen_pileup"
echo "  startingstep: $chosen_startingstep"
echo "  endingstep: $chosen_endingstep"
echo "  events: $chosen_events"

started=false

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
GenSimOutput+=.root

# Config File Name
ConfigFileName=${GenSimOutput%????}
ConfigFileName+=py 

echo 'Input File Name:' $PythiaFragPath
echo 'Output File Name:' $GenSimOutput

# Functions for later 

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