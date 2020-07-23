#!/bin/bash
######################################################################################################################################
# Abe Tishelman-Charny
# 14 July 2020
# 
# The purpose of this bash script is to submit crab jobs for MC steps processing pythia fragments interfaced with MadGraph.
# Made to be compatible with 2016 conditions. 
######################################################################################################################################

source /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production/Submit_Crab_GEN.sh
source /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production/Submit_Crab_postGEN.sh

if [ $chosen_step == GEN-SIM ] || [ $chosen_step == GEN ]
then
    # MCM pages 
    # 2018 PPD Recipe: HIG-RunIIFall18wmLHEGS-01909
    # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/HIG-RunIIFall18wmLHEGS-01909

    chosen_threads=8
    cmssw_v=CMSSW_10_2_13_patch1

    #!/bin/bash
    export SCRAM_ARCH=slc6_amd64_gcc700
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    if [ -r CMSSW_10_2_13_patch1/src ] ; then 
    echo release CMSSW_10_2_13_patch1 already exists
    else
    scram p CMSSW CMSSW_10_2_13_patch1
    fi
    cd CMSSW_10_2_13_patch1/src
    eval `scram runtime -sh`

    scram b
    cd ../../
    seed=$(($(date +%s) % 100 + 1))

    if [ $chosen_step == GEN-SIM ]
    then 
        step_arg=LHE,GEN,SIM
    fi 

    if [ $chosen_step == GEN ]
    then 
        step_arg=LHE,GEN
    fi 
    
    echo "COMMAND:"
    echo "cmsDriver.py $PythiaFragPath --fileout file:$GenSimOutput --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step ${step_arg} --nThreads $chosen_threads --geometry DB:Extended --era Run2_2018 --python_filename $ConfigFileName --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int(${seed}%100) -n $chosen_events"
    
    cmsDriver.py $PythiaFragPath --fileout file:$GenSimOutput --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step ${step_arg} --nThreads $chosen_threads --geometry DB:Extended --era Run2_2018 --python_filename $ConfigFileName --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n $chosen_events  
    submit_crab_GEN $ConfigFileName $chosen_events $cmssw_v $chosen_threads $chosen_jobs $LocalGridpackPath $Campaign $dryRun $Year

fi 


# DR

if [ $chosen_step == DR1 ] || [ $chosen_step == DR2 ]
then

    cmssw_v=CMSSW_10_2_5 

    export SCRAM_ARCH=slc6_amd64_gcc700
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    if [ -r CMSSW_10_2_5/src ] ; then 
    echo release CMSSW_10_2_5 already exists
    else
    scram p CMSSW CMSSW_10_2_5
    fi
    cd CMSSW_10_2_5/src
    eval `scram runtime -sh`   

    scram b
    cd ../../

    ##-- HIG-RunIIAutumn18DRPremix-01476
    # cmsDriver.py step1 --fileout file:HIG-RunIIAutumn18DRPremix-01476_step1.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads 8 --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename HIG-RunIIAutumn18DRPremix-01476_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 2626 || exit $? ; 
    # cmsDriver.py step2 --filein file:HIG-RunIIAutumn18DRPremix-01476_step1.root --fileout file:HIG-RunIIAutumn18DRPremix-01476.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 102X_upgrade2018_realistic_v15 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --procModifiers premix_stage2 --nThreads 8 --era Run2_2018 --python_filename HIG-RunIIAutumn18DRPremix-01476_2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 2626 || exit $? ;     

    crab_input=''
    crab_input=${GenSimOutput#"/eos/cms"} # Remove beginning of gen output (DR1 input) file path so it can be read by the crab config 
    echo "Crab Input = $crab_input"

    # If path ends in '.root', it's a single file  
    # If path ends in '/', it's a directory

    PathNoRoot=${GenSimOutput%?????} # remove .root
    EndofPath=${PathNoRoot##*/} # remove everything before and including final '/' in long path /eos/cms/store/...
    # Should be ID of specific decay channel/PUconfig/events 

    SinglePathNoRoot=${SinglePath%?????} # remove .root
    EndofSinglePath=${SinglePathNoRoot##*/} # remove everything before and including final '/' in long path /eos/cms/store/...
    # Should be ID of specific decay channel/PUconfig/events 

    echo "EndofSinglePath = $EndofSinglePath"

    #DR1Output=$EndofPath 
    DR1Output=$EndofSinglePath 
    DR2Output=$EndofSinglePath 

    mkdir -p $cmssw_v/src/cmssw_configs/ # create directory if it doesn't exist 

    DR1Config=$cmssw_v/src/cmssw_configs/${Campaign}_
    DR2Config=$cmssw_v/src/cmssw_configs/${Campaign}_
    #DR1Config+=$EndofPath 
    DR1Config+=$EndofSinglePath 
    #DR2Config+=$EndofPath 
    DR2Config+=$EndofSinglePath 

    #DR2Output=$EndofPath 

    # Remove previous step from name 

    DR1Output=${DR1Output%_GEN-SIM*}
    #DR1Output=${DR1Output%_GEN*}
    DR2Output=${DR2Output%_DR1*}
    DR1Config=${DR1Config%_GEN-SIM*}
    #DR1Config=${DR1Config%_GEN*}
    DR2Config=${DR2Config%_DR1*}

    # Add PU info to file names 
    # Should carry through to MINIAOD and MICROAOD names 
    if [ $chosen_pileup == "wPU" ]
        then
        DR1Output+="_wPU"
        DR1Config+="_wPU"

    fi 

    if [ $chosen_pileup == "woPU" ]
        then
        DR1Output+="_woPU"
        DR1Config+="_woPU"

    fi 

    DR1Output+=_DR1.root
    DR2Output+=_DR2.root
    DR1Config+=_DR1.py 
    DR2Config+=_DR2.py

    # With Pileup

    if [ $chosen_pileup == "wPU" ]
    then

        if [ $chosen_step == DR1 ]
        then 

            echo 'Performing DR1 with Pileup'

            # Make sure proxy available for pileup files 
            check_proxy
            chosen_threads=8

            echo "COMMAND:" ##-- originially missing "--filein" on McM 
            echo "cmsDriver.py step1 --filein $paths_string --fileout file:$DR1Output  --pileup_input dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads $chosen_threads --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events > /dev/null"

            cmsDriver.py step1 --filein $paths_string --fileout file:$DR1Output  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads $chosen_threads --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events > /dev/null # do not output the many many pileup files names
             
            #shuffle_PU $DR1Config # To manually shuffle pileup each time

            submit_crab_postGEN $DR1Config $cmssw_v $chosen_threads $chosen_job_size $chosen_step $Campaign $dryRun "${f_paths[@]}"

        elif [ $chosen_step == DR2 ]
        then 
            chosen_threads=8
            echo 'Performing DR2 with Pileup'
            echo "COMMAND:"
            echo "cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 102X_upgrade2018_realistic_v15 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --procModifiers premix_stage2 --nThreads $chosen_threads --era Run2_2018 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events "
            cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 102X_upgrade2018_realistic_v15 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --procModifiers premix_stage2 --nThreads $chosen_threads --era Run2_2018 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

            submit_crab_postGEN $DR2Config $cmssw_v $chosen_threads $chosen_job_size $chosen_step $Campaign $dryRun "${f_paths[@]}" 

        fi # if wPU and (if DR1 elif DR2) 
    fi # if wPU elif woPU 
fi # if DR1 or DR2 


# MiniAOD

if [ $chosen_step == MINIAOD ]
then

    cmssw_v=CMSSW_10_2_5

    #crab_input=${PrevStepOutput#"/eos/cms"} # Remove beginning of gen output (DR1 input) file path so it can be read by the crab config 
    #echo "Crab Input = $crab_input"

    PathNoRoot=${PrevStepOutput%?????} # remove .root
    EndofPath=${PathNoRoot##*/} # remove everything before and including final '/' in long path /eos/cms/store/...
    # Should be ID of specific decay channel/PUconfig/events 

    SinglePathNoRoot=${SinglePath%?????} # remove .root
    EndofSinglePath=${SinglePathNoRoot##*/} # remove everything before and including final '/' in long path /eos/cms/store/...

    echo "EndofSinglePath = $EndofSinglePath"

    MINIAODInput=$PrevStepOutput

    # Remove previous step from name 
    #MINIAODOutput=$EndofPath 
    MINIAODOutput=$EndofSinglePath 
    MINIAODOutput=${MINIAODOutput%_DR2*}
    MINIAODOutput+=_MINIAOD.root


    MINIAODConfig=$cmssw_v/src/cmssw_configs/${Campaign}_
    #MINIAODConfig+=$EndofPath
    MINIAODConfig+=$EndofSinglePath
    MINIAODConfig=${MINIAODConfig%_DR2*}
    MINIAODConfig+=_MINIAOD.py

    export SCRAM_ARCH=slc6_amd64_gcc700
    source /cvmfs/cms.cern.ch/cmsset_default.sh
    if [ -r CMSSW_10_2_5/src ] ; then 
    echo release CMSSW_10_2_5 already exists
    else
    scram p CMSSW CMSSW_10_2_5
    fi
    cd CMSSW_10_2_5/src
    eval `scram runtime -sh`

    # AODOutput=${PrevStepOutput%?????}
    # AODConfig=$AODOutput
    # AODOutput+=_MiniAOD.root
    # AODConfig+=_MiniAOD.py

    chosen_threads=8

    scram b
    cd ../../
    mkdir -p $cmssw_v/src/cmssw_configs/ # create directory if it doesn't exist 

    echo "COMMAND:"
    echo "cmsDriver.py step1 --filein $paths_string --fileout file:$MINIAODOutput --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 102X_upgrade2018_realistic_v15 --step PAT --nThreads $chosen_threads --geometry DB:Extended --era Run2_2018 --python_filename $MINIAODConfig --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events"
    
    cmsDriver.py step1 --filein $paths_string --fileout file:$MINIAODOutput --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 102X_upgrade2018_realistic_v15 --step PAT --nThreads $chosen_threads --geometry DB:Extended --era Run2_2018 --python_filename $MINIAODConfig --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

    submit_crab_postGEN $MINIAODConfig $cmssw_v $chosen_threads $chosen_job_size $chosen_step $Campaign $dryRun "${f_paths[@]}" 

fi 
