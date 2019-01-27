#!/bin/bash
#
# Abe Tishelman-Charny
# 11 January 2019
# 
# The purpose of this bash script is to create microAOD's from X->HH->WWgg pythia fragments.
# Steps: LHE,GEN,SIM,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016,RAW2DIGI,RECO,EI,PAT,flashggmicroAOD
# Run this from /afs/cern.ch/work/a/atishelm/private/HH_WWgg

# command to run: . Create_WWgg_MicroAOD.sh enuenuggwoPU

source /afs/cern.ch/work/a/atishelm/private/HH_WWgg/MC_Producer_Setup.sh
source /afs/cern.ch/work/a/atishelm/private/HH_WWgg/Submit_Crab_GEN.sh
source /afs/cern.ch/work/a/atishelm/private/HH_WWgg/Submit_Crab_postGEN.sh
source /afs/cern.ch/work/a/atishelm/private/HH_WWgg/make_microAOD.sh

#LHE,GEN,SIM

if [ $chosen_step == GEN ]
then

    #started=true 
    cmssw_v=CMSSW_7_1_25

    #!/bin/bash
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    export SCRAM_ARCH=slc6_amd64_gcc481
    if [ -r CMSSW_7_1_25/src ] ; then 
    echo release CMSSW_7_1_25 already exists
    else
    scram p CMSSW CMSSW_7_1_25
    fi
    cd CMSSW_7_1_25/src
    eval `scram runtime -sh`

    echo "Looking for pythia fragment at $PythiaFragPath"

    scram b
    cd ../../
    seed=$(date +%s)
    cmsDriver.py $PythiaFragPath --fileout file:$GenSimOutput --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --python_filename $ConfigFileName --no_exec --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed}%100)" -n $chosen_events

    #cmsRun $ConfigFileName # Replace this with crab command 
    submit_crab_GEN $ConfigFileName $chosen_events $cmssw_v 

    end_script 

fi 

# DR

#---With CMSSW_8_0_21

#if [ $chosen_startingstep == DR ] || [ "$started" = true ]
if [ $chosen_step == DR1 ] || [ $chosen_step == DR2 ]
then

    #started=true
    cmssw_v=CMSSW_8_0_21

    #!/bin/bash
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    export SCRAM_ARCH=slc6_amd64_gcc530
    if [ -r CMSSW_8_0_21/src ] ; then 
    echo release CMSSW_8_0_21 already exists
    else
    scram p CMSSW CMSSW_8_0_21
    fi
    cd CMSSW_8_0_21/src
    eval `scram runtime -sh`

    scram b
    cd ../../

    crab_input=${GenSimOutput#"/eos/cms"} # Remove beginning of gen output (DR1 input) file path so it can be read by the crab config 
    echo "Crab Input = $crab_input"

    PathNoRoot=${GenSimOutput%?????} # remove .root
    EndofPath=${PathNoRoot##*/} # remove everything before and including final '/' in long path /eos/cms/store/...
    # Should be ID of specific decay channel/PUconfig/events 

    DR1Output=$EndofPath 

    DR1Config="cmssw_configs/"
    DR2Config="cmssw_configs/"
    DR1Config+=$EndofPath 
    DR2Config+=$EndofPath 
    DR2Output=$EndofPath 

    DR1Output+=_DR1.root 
    DR2Output+=_DR2.root
    DR1Config+=_DR1.py
    DR2Config+=_DR2.py

    #voms-proxy-init -voms cms -rfc

    # With Pileup

    if [ $chosen_pileup == wPU ]
    then

        if [ $chosen_step == DR1 ]
        then 

            echo 'Performing DR1 with Pileup'

            # Make sure proxy available for pileup files 
            check_proxy

            cmsDriver.py step1 --filein file:$GenSimOutput --fileout file:$DR1Output --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --nThreads 4 --datamix PreMix --era Run2_2016 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

            #cmsRun $DR1Config

            submit_crab_postGEN $DR1Config $cmssw_v $crab_input

            end_script 
 

        elif [ $chosen_step == DR2 ]
        then 
            echo 'Performing DR2 with Pileup'
            # From MCM
            cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --nThreads 4 --era Run2_2016 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

            #cmsRun $DR2Config 

            submit_crab_postGEN $DR2Config $cmssw_v $crab_input

            end_script 

        fi # if wPU and (if DR1 elif DR2) 

    elif [ $chosen_pileup == woPU ]
    then
        
        # Without Pileup (need to test)

        if [ $chosen_step == DR1 ]
        then
            echo 'Performing DR1 without Pileup'

            cmsDriver.py step1 --filein file:$GenSimOutput --fileout file:$DR1Output --mc --eventcontent RAWSIM --pileup NoPileUp --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGI,L1,DIGI2RAW,HLT:@frozen2016 --nThreads 4 --era Run2_2016 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

            #cmsRun $DR1Config

            submit_crab_postGEN $DR1Config $cmssw_v $crab_input

            end_script 

        elif [ $chosen_step == DR2 ]
        then
            echo 'Performing DR2 without Pileup'

            cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent RAWAODSIM --runUnscheduled --datatier RAWAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,L1Reco,RECO,EI --nThreads 4 --era Run2_2016 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

            #cmsRun $DR2Config 

            submit_crab_postGEN $DR2Config $cmssw_v $crab_input

            end_script 
        
        fi # if woPU and (if DR1 elif DR2) 

    fi # if wPU elif woPU 

fi # if DR1 or DR2 

# MiniAOD

if [ $chosen_step == MINIAOD ]
then

    crab_input=${GenSimOutput#"/eos/cms"} # Remove beginning of gen output (DR1 input) file path so it can be read by the crab config 
    echo "Crab Input = $crab_input"

    PathNoRoot=${GenSimOutput%?????} # remove .root
    EndofPath=${PathNoRoot##*/} # remove everything before and including final '/' in long path /eos/cms/store/...
    # Should be ID of specific decay channel/PUconfig/events 

    MINIAODInput=$GenSimOutput

    MINIAODOutput=$EndofPath 
    MINIAODOutput+=_MINIAOD.root

    MINIAODConfig=$EndofPath
    MINIAODConfig+=_MINIAOD.py

    DR1Config=$EndofPath 
    DR2Config=$EndofPath 

    #started=true
    cmssw_v=CMSSW_8_0_21

    #!/bin/bash
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    export SCRAM_ARCH=slc6_amd64_gcc530
    if [ -r CMSSW_8_0_21/src ] ; then 
     echo release CMSSW_8_0_21 already exists
    else
    scram p CMSSW CMSSW_8_0_21
    fi
    cd CMSSW_8_0_21/src
    eval `scram runtime -sh`

    # AODOutput=${GenSimOutput%?????}
    # AODConfig=$AODOutput
    # AODOutput+=_MiniAOD.root
    # AODConfig+=_MiniAOD.py

    scram b
    cd ../../
    cmsDriver.py step1 --filein file:$MINIAODInput --fileout file:$MINIAODOutput --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step PAT --nThreads 4 --era Run2_2016 --python_filename $MINIAODConfig --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

    #cmsRun $AODConfig

    submit_crab_postGEN $MINIAODConfig $cmssw_v $crab_input

    end_script 

fi 

# # MicroAOD

# https://github.com/atishelmanch/H4G/tree/master/Gen/microAOD
# ^^ Follow this for how to do flashgg crab submissions 
# For now will just make one file at a time w/o crab 

if [ $chosen_step == MICROAOD ]
then

#     move to flashgg 
#     cd /afs/cern.ch/work/a/atishelm/15JanFlashgg/CMSSW_8_0_26_patch1/src/flashgg
#     cmsenv

#     make microAODstd.py file which takes desired MINIAOD as input 

      mini_aod_path=${chosen_miniaodoutput#"/eos/cms"} # Remove beginning of gen output (DR1 input) file path so it can be read by the crab config 
      make_microAOD $mini_aod_path $chosen_events
      end_script

#     Then should run tagger step 
    



fi 