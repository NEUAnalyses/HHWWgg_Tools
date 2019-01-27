#!/bin/bash

# Idea: Read crab status message to see if job is finished, and if it is, obtain the path to the files and run the next step? 
# Make folder for pythia configuration files that end up in HH_WWgg/. Bin? Py_cfgs? 

# Break this setup into two files? One just for dictionaries? 

# Create configurations
configs=( enuenu_wPU enuenu_woPU jjenu_wPU jjenu_woPU 
jjenu_wPU_DR1 enuenu_woPU_DR1 enuenu_wPU_DR1 
enuenu_wPU_DR2 enuenu_woPU_DR2 
enuenu_woPU_MINIAOD jjenu_noPU_DR1 jjenu_ePU_DR2 jjenu_wPU_MINIAOD 
jjenu_wPU_DR2 jjenu_woPU_DR2
jjenu_woPU_MINIAOD enuenu_woPU_MICROAOD jjenu_woPU_MICROAOD enuenu_wPU_MINIAOD
munumunu 
jjenu_allj )

for config in "${configs[@]}"
do
    :
    unset $config # Make sure array name is free in memory 
    declare -A $config 
done

# Number of events should be a multiple of 10 

# Currently using this group space for crab outputs:
# /eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/
# /eos/cms/store/user/atishelm/

# Gen configs 
# Need to include pythia fragment
enuenuwPU=( ["filename"]=ggF_X1000_WWgg_enuenugg ["step"]=GEN ["events"]=1000)
jjenu=( ["filename"]=ggF_X1000_WWgg_jjenugg ["step"]=GEN ["events"]=1000)
munumunu=( ["filename"]=ggF_X1000_WWgg_munumunugg ["step"]=GEN ["events"]=1000)
jjenu_allj=( ["filename"]=ggF_X1000_WWgg_jjenugg_allj ["step"]=GEN ["events"]=1000)

# DR1 config
# Need to include location of Gen output file 
enuenunopuDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_woPU/190116_184220/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1.root ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)
enuenunopuDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_woPU/190116_184220/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1.root ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)
enuenuDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_wPU_1000events_GEN/190119_145144/0000/ ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)
enuenu_wPU_DR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_wPU_1000events_GEN/190120_092641/0000/ggF_X1000_WWgg_enuenugg_wPU_1000events_GEN_1.root ["pileup"]=wPU ["step"]=DR1 ["events"]=1000)

jjenuDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN/190120_092910/0000/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1.root ["pileup"]=wPU ["step"]=DR1 ["events"]=1000)
jjenunoPUDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN/190120_092940/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1.root ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)

# DR2
# Need to include location of DR1 output 
enuenunopuDR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1/190119_113807/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1.root ["pileup"]=woPU ["step"]=DR2 ["events"]=1000)
enuenu_wPU_DR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_wPU_1000events_GEN_1_DR1/190121_084806/0000/ggF_X1000_WWgg_enuenugg_wPU_1000events_GEN_1_DR1_1.root ["pileup"]=wPU ["step"]=DR2 ["events"]=1000)
jjenuDR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1/190120_231313/0000/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1_1.root ["pileup"]=wPU ["step"]=DR2 ["events"]=1000)

jjenu_wPU_DR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1/190120_231313/0000/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1_1.root ["pileup"]=wPU ["step"]=DR2 ["events"]=1000)
jjenu_woPU_DR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1/190121_000054/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1.root ["pileup"]=woPU ["step"]=DR2 ["events"]=1000)

# MINIAOD 
# Need to include location of DR2 output 
#enuenunopuMINIAOD=( ["MINIAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2/190119_123028/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1.root ["pileup"]=woPU ["step"]=MINIAOD ["events"]=1000)
jjenu_wPU_MINIAOD=( ["MINIAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1_1_DR2/190121_000523/0000/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1_1_DR2_1.root ["pileup"]=wPU ["step"]=MINIAOD ["events"]=1000)
#jjenu_woPU_MINIAOD=( ["MINIAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2/190121_093215/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1.root ["pileup"]=woPU ["step"]=MINIAOD ["events"]=1000)
#enuenu_wPU_MINIAOD=( ["MINIAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2/190121_093215/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1.root ["pileup"]=wPU ["step"]=MINIAOD ["events"]=1000)

# MICROAOD
# Include location of MINIAOD 
#enuenu_woPU_MICROAOD=( ["MICROAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root ["pileup"]=woPU ["step"]=MICROAOD ["events"]=1000)
#enuenu_woPU_MICROAOD=( ["MICROAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root ["pileup"]=woPU ["step"]=MICROAOD ["events"]=1000)
jjenu_woPU_MICROAOD=( ["MICROAODInput"]="/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190121_130646/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root" ["pileup"]=woPU ["step"]=MICROAOD ["events"]=1000 )


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
    exit 1;
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

elif [ $chosen_step == MICROAOD ]
then

    chosen_miniaodoutput_=${chosen_config}[MICROAODInput]
    chosen_miniaodoutput=${!chosen_miniaodoutput_}
    #GenSimOutput=$chosen_miniaodoutput

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
    # GEN 
    # Params: filename, pileup, step, events 

    chosen_filename_=${chosen_config}[filename]
    #chosen_pileup_=${chosen_config}[pileup]
    chosen_events_=${chosen_config}[events]

    chosen_filename=${!chosen_filename_}
    #chosen_pileup=${!chosen_pileup_}
    chosen_events=${!chosen_events_}

    echo "Chosen setup parameters:"
    echo "  step: $chosen_step"
    echo "  filename: $chosen_filename"
    #echo "  pileup: $chosen_pileup"
    echo "  events: $chosen_events"

    #started=false

    # Define Pythia fragment path
    PythiaFragPath=Configuration/GenProduction/python/
    PythiaFragPath+=$chosen_filename
    PythiaFragPath+=.py

    # Define output file name 
    GenSimOutput=$chosen_filename
    #GenSimOutput+='_'

    # Add PU info to file name 
    # if [ $chosen_pileup == wPU ]
    #     then
    #     GenSimOutput+="wPU"

    # fi 

    # if [ $chosen_pileup == woPU ]
    #     then
    #     GenSimOutput+="woPU"

    # fi 

    #GenSimOutput+='_'

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
    exit 1;
}