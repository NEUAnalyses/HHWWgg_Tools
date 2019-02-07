#!/bin/bash

# Create configurations
configs=( enuenu_wPU enuenu_woPU jjenu_wPU jjenu_woPU 
jjenu_wPU_DR1 enuenu_woPU_DR1 enuenu_wPU_DR1 
enuenu_wPU_DR2 enuenu_woPU_DR2 
enuenu_woPU_MINIAOD jjenu_noPU_DR1 jjenu_ePU_DR2 jjenu_wPU_MINIAOD 
jjenu_wPU_DR2 jjenu_woPU_DR2
jjenu_woPU_MINIAOD enuenu_woPU_MICROAOD jjenu_woPU_MICROAOD enuenu_wPU_MINIAOD
munumunu 
jjenu_allj jjenu_allj_noeq 
munumunu_DR1 munumunu_DR2 munumunu_MINIAOD munumunu_MICROAOD
jjenu_939 jjenu_939_DR1_woPU jjenu_939_DR1_wPU jjenu_939_DR2_woPU 
direc_test 
jjenu_939_MINIAOD_woPU )

for config in "${configs[@]}"
do
    :
    unset $config # Make sure array name is free in memory 
    declare -A $config 
done

# Number of events should be a multiple of 10 

# Gen configs 
# filename is pythia fragment in path: 
#   /afs/cern.ch/work/a/atishelm/private/HH_WWgg/CMSSW_X_X_X/src/Configuration/GenProduction/python/<filename>.py 
enuenuwPU=( ["filename"]=ggF_X1000_WWgg_enuenugg ["step"]=GEN ["events"]=1000)
jjenu=( ["filename"]=ggF_X1000_WWgg_jjenugg ["step"]=GEN ["events"]=1000)
munumunu=( ["filename"]=ggF_X1000_WWgg_munumunugg ["step"]=GEN ["events"]=1000)
jjenu_allj=( ["filename"]=ggF_X1000_WWgg_jjenugg_allj ["step"]=GEN ["events"]=1000)
jjenu_allj_noeq=( ["filename"]=ggF_X1000_WWgg_jjenugg_allj_noequal ["step"]=GEN ["events"]=1000)
jjenu_939=( ["filename"]=ggF_X250_WWgg_jjenugg ["step"]=GEN ["events"]=1000)

# Crab output spaces: 
# /eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/
# /eos/cms/store/user/atishelm/

# DR1 configs
# DRInput is the full path to a GEN output file produced with a configuration from the step above
# DRInput (eventually) can either be a single file or a directory. 
# Either ends in .root, or / 
enuenunopuDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_woPU/190116_184220/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1.root ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)
enuenunopuDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_woPU/190116_184220/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1.root ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)
enuenuDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_wPU_1000events_GEN/190119_145144/0000/ ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)
enuenu_wPU_DR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_wPU_1000events_GEN/190120_092641/0000/ggF_X1000_WWgg_enuenugg_wPU_1000events_GEN_1.root ["pileup"]=wPU ["step"]=DR1 ["events"]=1000)
jjenuDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN/190120_092910/0000/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1.root ["pileup"]=wPU ["step"]=DR1 ["events"]=1000)
jjenunoPUDR1=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN/190120_092940/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1.root ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)
munumunu_DR1=( ["DRInput"]=/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1000_WWgg_munumunugg1000events_GEN/190127_224243/0000/ggF_X1000_WWgg_munumunugg1000events_GEN_1.root ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)
jjenu_939_DR1_woPU=( ["DRInput"]=/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X250_WWgg_jjenugg_1000events_GEN_1/190202_165351/0000/ggF_X250_WWgg_jjenugg_1000events_GEN_1.root ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)
jjenu_939_DR1_wPU=( ["DRInput"]=/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X250_WWgg_jjenugg_1000events_GEN/190129_124659/0000/ggF_X250_WWgg_jjenugg_1000events_GEN_1.root ["pileup"]=wPU ["step"]=DR1 ["events"]=1000)
direc_test=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_10000events_woPU/190116_231820/0000/nonLHE/ ["pileup"]=woPU ["step"]=DR1 ["events"]=1000)

# DR2
# DRInput is the full path to a DR1 output file produced with a configuration from the step above
# DRInput (eventually) can either be a single file or a directory. 
# Either ends in .root, or / 
enuenunopuDR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1/190119_113807/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1.root ["pileup"]=woPU ["step"]=DR2 ["events"]=1000)
enuenu_wPU_DR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_wPU_1000events_GEN_1_DR1/190121_084806/0000/ggF_X1000_WWgg_enuenugg_wPU_1000events_GEN_1_DR1_1.root ["pileup"]=wPU ["step"]=DR2 ["events"]=1000)
jjenuDR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1/190120_231313/0000/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1_1.root ["pileup"]=wPU ["step"]=DR2 ["events"]=1000)
jjenu_wPU_DR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1/190120_231313/0000/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1_1.root ["pileup"]=wPU ["step"]=DR2 ["events"]=1000)
jjenu_woPU_DR2=( ["DRInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1/190121_000054/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1.root ["pileup"]=woPU ["step"]=DR2 ["events"]=1000)
munumunu_DR2=( ["DRInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1000_WWgg_munumunugg1000events_GEN_1_DR1/190129_063416/0000/ggF_X1000_WWgg_munumunugg1000events_GEN_1_DR1_1.root ["pileup"]=woPU ["step"]=DR2 ["events"]=1000)
jjenu_939_DR2_woPU=( ["DRInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X250_WWgg_jjenugg_1000events_DR1/190202_193134/0000/ggF_X250_WWgg_jjenugg_1000events_DR1_1.root ["pileup"]=woPU ["step"]=DR2 ["events"]=1000)

# MINIAOD 
# DRInput is the full path to a DR2 output file produced with a configuration from the step above
# DRInput (eventually) can either be a single file or a directory. 
# Either ends in .root, or / 
#enuenunopuMINIAOD=( ["MINIAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2/190119_123028/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1.root ["pileup"]=woPU ["step"]=MINIAOD ["events"]=1000)
jjenu_wPU_MINIAOD=( ["MINIAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1_1_DR2/190121_000523/0000/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1_1_DR2_1.root ["pileup"]=wPU ["step"]=MINIAOD ["events"]=1000)
munumunu_MINIAOD=( ["MINIAODInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1000_WWgg_munumunugg1000events_GEN_1_DR1_1_DR2/190129_073314/0000/ggF_X1000_WWgg_munumunugg1000events_GEN_1_DR1_1_DR2_1.root ["pileup"]=woPU ["step"]=MINIAOD ["events"]=1000)
jjenu_939_MINIAOD_woPU=( ["MINIAODInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X250_WWgg_jjenugg_1000events_DR2/190202_203200/0000/ggF_X250_WWgg_jjenugg_1000events_DR2_1.root ["pileup"]=woPU ["step"]=MINIAOD ["events"]=1000)
#jjenu_woPU_MINIAOD=( ["MINIAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2/190121_093215/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1.root ["pileup"]=woPU ["step"]=MINIAOD ["events"]=1000)
#enuenu_wPU_MINIAOD=( ["MINIAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2/190121_093215/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1.root ["pileup"]=wPU ["step"]=MINIAOD ["events"]=1000)

# MICROAOD
# DRInput is the full path to a MINIAOD output file produced with a configuration from the step above
# DRInput (eventually) can either be a single file or a directory. 
# Either ends in .root, or / 
#enuenu_woPU_MICROAOD=( ["MICROAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root ["pileup"]=woPU ["step"]=MICROAOD ["events"]=1000)
#enuenu_woPU_MICROAOD=( ["MICROAODInput"]=/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root ["pileup"]=woPU ["step"]=MICROAOD ["events"]=1000)
jjenu_woPU_MICROAOD=( ["MICROAODInput"]="/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190121_130646/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root" ["pileup"]=woPU ["step"]=MICROAOD ["events"]=1000 )
munumunu_MICROAOD=( ["MICROAODInput"]="/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1000_WWgg_munumunugg1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190129_081915/0000/ggF_X1000_WWgg_munumunugg1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root" ["pileup"]=woPU ["step"]=MICROAOD ["events"]=1000 )

if [ ${#1} == 0 ]
then
    echo 'Please enter an argument for the MC_Producer configuration'
    echo 
    echo 'Exiting'
    return;
fi