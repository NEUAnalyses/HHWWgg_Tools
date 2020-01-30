#!/bin/bash

# Create configurations
# Your desired configuration has to be on this list to work 

# Get configurations from crab_jobs.json 

jq '.' MC_Configs.json 

# Get names from json then create config arrays here 

# array
# configs=( 
# jjenu_939_MINIAOD_woPU
# qqqqgg_GEN
# qqqqgg_DR1_nopu
# qqqqgg_DR2_nopu
# qqenugg_GEN
# qqenugg_DR1_nopu
# qqenugg_DR2_nopu
# qqenugg_MINIAOD_nopu
# qqmunugg_GEN
# enuenugg_GEN 
# munumunugg_GEN
# qqqqgg_MINIAOD_nopu 
# qqmunugg_DR1_nopu
# munumunugg_DR1_nopu
# enuenugg_DR1_nopu
# qqqqgg_DR1_nopu
# qqmunugg_DR2_nopu
# munumunugg_DR2_nopu
# enuenugg_DR2_nopu
# qqqqgg_DR2_nopu
# qqmunugg_MINIAOD_nopu
# enuenugg_MINIAOD_nopu
# munumunugg_MINIAOD_nopu
# qqqqgg_MINIAOD_nopu )

for config in "${configs[@]}"
do
    :
    unset $config # Make sure array name is free in memory 
    declare -A $config # associative array 
done

# Number of events should be a multiple of number of jobs 

# Should make a json file or something for input of desired jobs 

# Config by fragment:
# qqqqgg_nopu
# GEN 
qqqqgg_GEN=( ["filename"]=ggF_X1250_WWgg_qqqqgg ["step"]=GEN ["events"]=10000 ["jobs"]=10 )
qqenugg_GEN=( ["filename"]=ggF_X1250_WWgg_qqenugg ["step"]=GEN ["events"]=10000 ["jobs"]=10 )
qqmunugg_GEN=( ["filename"]=ggF_X1250_WWgg_qqmunugg ["step"]=GEN ["events"]=10000 ["jobs"]=10 )
enuenugg_GEN=( ["filename"]=ggF_X1250_WWgg_enuenugg ["step"]=GEN ["events"]=10000 ["jobs"]=10 )
munumunugg_GEN=( ["filename"]=ggF_X1250_WWgg_munumunugg ["step"]=GEN ["events"]=10000 ["jobs"]=10 )

# DR1
# DRInput should be directory path ending in '*'
# jobsize = number of input files to use per job 
# ex: if you have 10 input GEN files in the DRInput directory, and you set jobsize = 2, you will get 5 output DR1 files 
qqqqgg_DR1_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_8/190212_095439/0000/* ["pileup"]=woPU ["step"]=DR1 ["events"]=1000 ["jobsize"]=1 )
qqenugg_DR1_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqenugg_10000events_GEN_1/190214_151938/0000/* ["pileup"]=woPU ["step"]=DR1 ["events"]=10000 ["jobsize"]=1 )

qqmunugg_DR1_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqmunugg_10000events_GEN/190214_152058/0000/* ["pileup"]=woPU ["step"]=DR1 ["events"]=10000 ["jobsize"]=1 )
munumunugg_DR1_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_munumunugg_10000events_GEN/190214_152500/0000/* ["pileup"]=woPU ["step"]=DR1 ["events"]=10000 ["jobsize"]=1 )
enuenugg_DR1_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_enuenugg_10000events_GEN/190214_152338/0000/* ["pileup"]=woPU ["step"]=DR1 ["events"]=10000 ["jobsize"]=1 )
qqqqgg_DR1_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_10000events_GEN/190214_151733/0000/* ["pileup"]=woPU ["step"]=DR1 ["events"]=10000 ["jobsize"]=1 )

# DR2 
qqqqgg_DR2_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_woPU_DR1_2/190214_172114/0000/* ["pileup"]=woPU ["step"]=DR2 ["events"]=1000 ["jobsize"]=1 )
qqenugg_DR2_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_qqenugg_10000events_woPU_DR1/190215_145524/0000/* ["pileup"]=woPU ["step"]=DR2 ["events"]=10000 ["jobsize"]=1 )

qqmunugg_DR2_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_qqmunugg_10000events_woPU_DR1/190305_115433/0000/* ["pileup"]=woPU ["step"]=DR2 ["events"]=10000 ["jobsize"]=1 )
munumunugg_DR2_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_munumunugg_10000events_woPU_DR1/190305_115657/0000/* ["pileup"]=woPU ["step"]=DR2 ["events"]=10000 ["jobsize"]=1 )
enuenugg_DR2_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_enuenugg_10000events_woPU_DR1/190305_120115/0000/* ["pileup"]=woPU ["step"]=DR2 ["events"]=9000 ["jobsize"]=1 )
qqqqgg_DR2_nopu=( ["DRInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_qqqqgg_10000events_woPU_DR1/190305_120444/0000/* ["pileup"]=woPU ["step"]=DR2 ["events"]=10000 ["jobsize"]=1 )

# MINIAOD
# Don't need to specify pileup 
qqqqgg_MINIAOD_nopu=( ["MINIAODInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_woPU_DR2_4/190214_213232/0000/* ["step"]=MINIAOD ["events"]=1000 ["jobsize"]=1 )
qqenugg_MINIAOD_nopu=( ["MINIAODInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_qqenugg_10000events_woPU_DR2/190225_123824/0000/* ["step"]=MINIAOD ["events"]=10000 ["jobsize"]=1 )

qqmunugg_MINIAOD_nopu=( ["MINIAODInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_qqmunugg_10000events_woPU_DR2/190305_134809/0000/* ["step"]=MINIAOD ["events"]=10000 ["jobsize"]=1 )
munumunugg_MINIAOD_nopu=( ["MINIAODInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_munumunugg_10000events_woPU_DR2/190305_135355/0000/* ["step"]=MINIAOD ["events"]=10000 ["jobsize"]=1 )
enuenugg_MINIAOD_nopu=( ["MINIAODInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_enuenugg_10000events_woPU_DR2/190305_135715/0000/* ["step"]=MINIAOD ["events"]=9000 ["jobsize"]=1 )
qqqqgg_MINIAOD_nopu=( ["MINIAODInput"]=/eos/cms/store/user/atishelm/postGEN_Outputs/ggF_X1250_WWgg_qqqqgg_10000events_woPU_DR2/190305_140444/0000/* ["step"]=MINIAOD ["events"]=10000 ["jobsize"]=1 )
# ---

# Gen configs 
# filename is pythia fragment in path: 
#   /afs/cern.ch/work/a/atishelm/private/HH_WWgg/CMSSW_X_X_X/src/Configuration/GenProduction/python/<filename>.py 
#qqqqgg_GEN=( ["filename"]=ggF_X1250_WWgg_qqqqgg ["step"]=GEN ["events"]=1000 ["jobs"]=10 )

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
