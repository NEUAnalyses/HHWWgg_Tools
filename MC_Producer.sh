#!/bin/bash
#
# Abe Tishelman-Charny
# 11 January 2019
# 
# The purpose of this bash script is to create microAOD's from X->HH->WWgg pythia fragments.
# Steps: LHE,GEN,SIM,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016,RAW2DIGI,RECO,EI,PAT,flashggmicroAOD
# Run this from /afs/cern.ch/work/a/atishelm/private

# Read user input for pythia fragment name, number of events 
# To add crab steps, just need to replace cmsRun steps with a crab step. 

# command to run: . Create_WWgg_MicroAOD.sh enuenuggwoPU

source /afs/cern.ch/work/a/atishelm/private/MC_Producer_Setup.sh
source /afs/cern.ch/work/a/atishelm/private/Gen_Crab_Steps.sh

#LHE,GEN,SIM

if [ $chosen_startingstep == GEN ]
then

    started=true 

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

    scram b
    cd ../../
    seed=$(date +%s)
    cmsDriver.py $PythiaFragPath --fileout file:$GenSimOutput --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --python_filename $ConfigFileName --no_exec --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed}%100)" -n $chosen_events

    #cmsRun $ConfigFileName # Replace this with crab command 
    gen_crab $ConfigFileName $chosen_events $chosen_pileup

    if [ $chosen_endingstep == GEN ]
    then
        echo 'Finished final desired step'
        echo 'Exiting'
        cd /afs/cern.ch/work/a/atishelm/private
        return
    fi

fi 

# DR

#---With CMSSW_8_0_21

if [ $chosen_startingstep == DR ] || [ "$started" = true ]
then

    started=true

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

    DR1Output=${GenSimOutput%?????}
    DR1Config=$DR1Output
    DR2Config=$DR1Output
    DR2Output=$DR1Output

    DR1Output+=_DRstep1.root
    DR2Output+=_DRstep2.root
    DR1Config+=_DRstep1.py
    DR2Config+=_DRstep2.py

    voms-proxy-init -voms cms -rfc

    # With Pileup

    if [ $chosen_pileup == wPU ]
    then
        echo 'Performing DR with Pileup'
        cmsDriver.py step1 --filein file:$GenSimOutput --fileout file:$DR1Output --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --nThreads 4 --datamix PreMix --era Run2_2016 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

        cmsRun $DR1Config

        # From MCM
        cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --nThreads 4 --era Run2_2016 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

        cmsRun $DR2Config 
    fi

    if [ $chosen_pileup == woPU ]
    then
        echo 'Performing DR without Pileup'
        # Without Pileup (need to test)

        cmsDriver.py step1 --filein file:$GenSimOutput --fileout file:$DR1Output --mc --eventcontent RAWSIM --pileup NoPileUp --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step DIGI,L1,DIGI2RAW,HLT:@frozen2016 --nThreads 4 --era Run2_2016 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

        cmsRun $DR1Config

        cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent RAWAODSIM --runUnscheduled --datatier RAWAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,L1Reco,RECO,EI --nThreads 4 --era Run2_2016 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

        cmsRun $DR2Config 

    fi

    if [ $chosen_endingstep == DR ]
    then
        echo 'Finished final desired step. Exiting.'
        return
    fi

fi

# MiniAOD

if [ $chosen_startingstep == MINIAOD ] || [ "$started" = true ]
then

    started=true
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

    AODOutput=${GenSimOutput%?????}
    AODConfig=$AODOutput
    AODOutput+=_MiniAOD.root
    AODConfig+=_MiniAOD.py

    #test=

    scram b
    cd ../../
    cmsDriver.py step1 --filein file:$DR2Output --fileout file:$AODOutput --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step PAT --nThreads 4 --era Run2_2016 --python_filename $AODConfig --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

    cmsRun $AODConfig

    if [ $chosen_endingstep == MINIAOD ]
    then
        echo 'Finished final desired step. Exiting.'
        return
    fi

fi 

# # MicroAOD

# if [ $chosen_startingstep == MicroAOD ] || [ "$started" = true ]
# then

#     cd CMSSW_8_0_26_patch1/src/flashgg/
#     cmsenv
#     cmsRun MicroAOD/test/microAODstd.py
#     cmsRun MicroAOD/test/microAODstd.py processType = sig data....=

#     # # # Output file will be MicroAODOutput.root (specified by microAODstd.py. microAODstd.py also needs input file name)

#     Then should run tagger step 
    
# fi 