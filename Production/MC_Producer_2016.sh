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
    # https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/HIG-RunIISummer15wmLHEGS-01390
    # https://cms-pdmv.cern.ch/mcm/requests?prepid=HIG-RunIISummer15wmLHEGS-01390%20--%3E%20HIG-RunIISummer16DR80Premix-03426%20%20--%3E%20HIG-RunIISummer16MiniAODv3-01245&page=0&shown=127
    
    # DR: https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/HIG-RunIISummer16DR80Premix-03426
    # MiniAOD: https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/HIG-RunIISummer16MiniAODv3-01245

    echo "about to export scram and source cvmfs"
    chosen_threads=8
    cmssw_v=CMSSW_7_1_26
    # export SCRAM_ARCH=slc6_amd64_gcc481
    # source /cvmfs/cms.cern.ch/cmsset_default.sh
    # if [ -r CMSSW_7_1_26/src ] ; then 
    # echo release CMSSW_7_1_26 already exists
    # else
    # scram p CMSSW CMSSW_7_1_26
    # fi
    scram p CMSSW CMSSW_7_1_26
    cd CMSSW_7_1_26/src
    eval `scram runtime -sh`
    cmsenv 
    echo "in MC_Producer_2016.sh"
    source /cvmfs/cms.cern.ch/slc6_amd64_gcc700/external/curl/7.59.0/etc/profile.d/init.sh # https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#crab_commands_fails_with_Error_U
    echo "Looking for pythia fragment at $PythiaFragPath"
    # curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-RunIISummer15wmLHEGS-01390 --retry 2 --create-dirs -o Configuration/GenProduction/python/HIG-RunIISummer15wmLHEGS-01390-fragment.py 
    # [ -s Configuration/GenProduction/python/HIG-RunIISummer15wmLHEGS-01390-fragment.py ] || exit $?;
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
    
    ##-- I couldn't find an nThreads flag for cmsDriver.py in this CMSSW. Just going to try more jobs with less events 
    echo "COMMAND:"
    # echo "cmsDriver.py $PythiaFragPath --fileout file:$GenSimOutput --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --nThreads $chosen_threads --geometry DB:Extended --era Run2_2017 --python_filename $ConfigFileName --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int(${seed}%100) -n $chosen_events"
    echo "cmsDriver.py $PythiaFragPath --fileout file:$GenSimOutput --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step ${step_arg} --magField 38T_PostLS1 --python_filename $ConfigFileName --no_exec --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int(${seed}) -n $chosen_events "
    # cmsDriver.py Configuration/GenProduction/python/HIG-RunIISummer15wmLHEGS-01390-fragment.py --fileout file:HIG-RunIISummer15wmLHEGS-01390.root --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --python_filename HIG-RunIISummer15wmLHEGS-01390_1_cfg.py --no_exec --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n 125 || exit $? ; 
    cmsDriver.py $PythiaFragPath --fileout file:$GenSimOutput --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step ${step_arg} --magField 38T_PostLS1 --python_filename $ConfigFileName --no_exec --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n $chosen_events
    submit_crab_GEN $ConfigFileName $chosen_events $cmssw_v $chosen_threads $chosen_jobs $LocalGridpackPath $Campaign $dryRun $Year

fi 

# # DR

# #---With CMSSW_8_0_21

# #if [ $chosen_startingstep == DR ] || [ "$started" = true ]
# if [ $chosen_step == DR1 ] || [ $chosen_step == DR2 ]
# then

#     # Maybe make nthreads variable 
#     #started=true
#     cmssw_v=CMSSW_9_4_7

#     #!/bin/bash

#     source /cvmfs/cms.cern.ch/cmsset_default.sh
#     export SCRAM_ARCH=slc6_amd64_gcc630
#     if [ -r CMSSW_9_4_7/src ] ; then 
#     echo release CMSSW_9_4_7 already exists
#     else
#     scram p CMSSW CMSSW_9_4_7
#     fi
#     cd CMSSW_9_4_7/src
#     eval `scram runtime -sh`


#     scram b
#     cd ../../

#     #crab_input=''
#     #crab_input=${GenSimOutput#"/eos/cms"} # Remove beginning of gen output (DR1 input) file path so it can be read by the crab config 
#     #echo "Crab Input = $crab_input"

#     # If path ends in '.root', it's a single file  
#     # If path ends in '/', it's a directory

#     PathNoRoot=${GenSimOutput%?????} # remove .root
#     EndofPath=${PathNoRoot##*/} # remove everything before and including final '/' in long path /eos/cms/store/...
#     # Should be ID of specific decay channel/PUconfig/events 

#     SinglePathNoRoot=${SinglePath%?????} # remove .root
#     EndofSinglePath=${SinglePathNoRoot##*/} # remove everything before and including final '/' in long path /eos/cms/store/...
#     # Should be ID of specific decay channel/PUconfig/events 

#     echo "EndofSinglePath = $EndofSinglePath"

#     #DR1Output=$EndofPath 
#     DR1Output=$EndofSinglePath 
#     DR2Output=$EndofSinglePath 

#     mkdir -p $cmssw_v/src/cmssw_configs/ # create directory if it doesn't exist 

#     DR1Config=$cmssw_v/src/cmssw_configs/${Campaign}_
#     DR2Config=$cmssw_v/src/cmssw_configs/${Campaign}_
#     #DR1Config+=$EndofPath 
#     DR1Config+=$EndofSinglePath 
#     #DR2Config+=$EndofPath 
#     DR2Config+=$EndofSinglePath 

#     #DR2Output=$EndofPath 

#     # Remove previous step from name 

#     DR1Output=${DR1Output%_GEN-SIM*}
#     #DR1Output=${DR1Output%_GEN*}
#     DR2Output=${DR2Output%_DR1*}
#     DR1Config=${DR1Config%_GEN-SIM*}
#     #DR1Config=${DR1Config%_GEN*}
#     DR2Config=${DR2Config%_DR1*}

#     # Add PU info to file names 
#     # Should carry through to MINIAOD and MICROAOD names 
#     if [ $chosen_pileup == "wPU" ]
#         then
#         DR1Output+="_wPU"
#         DR1Config+="_wPU"

#     fi 

#     if [ $chosen_pileup == "woPU" ]
#         then
#         DR1Output+="_woPU"
#         DR1Config+="_woPU"

#     fi 

#     DR1Output+=_DR1.root
#     DR2Output+=_DR2.root
#     DR1Config+=_DR1.py 
#     DR2Config+=_DR2.py

#     #voms-proxy-init -voms cms -rfc

#     # With Pileup

#     if [ $chosen_pileup == "wPU" ]
#     then

#         if [ $chosen_step == DR1 ]
#         then 

#             echo 'Performing DR1 with Pileup'

#             # Make sure proxy available for pileup files 
#             check_proxy

#             chosen_threads=8

#             #cmsDriver.py step1 --filein file:$GenSimOutput --fileout file:$DR1Output  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads $chosen_threads --datamix PreMix --era Run2_2017 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

#             echo "COMMAND:"
#             echo "cmsDriver.py step1 --filein $paths_string --fileout file:$DR1Output  --pileup_input dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads $chosen_threads --datamix PreMix --era Run2_2017 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events"

            
#             cmsDriver.py step1 --filein $paths_string --fileout file:$DR1Output --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads $chosen_threads --datamix PreMix --era Run2_2017 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events > /dev/null # do not output the many many pileup files

#             # Need to edit cmssw config to shuffle pileup each time 
#             #shuffle_PU $DR1Config

#             submit_crab_postGEN $DR1Config $cmssw_v $chosen_threads $chosen_job_size $chosen_step $Campaign $dryRun "${f_paths[@]}"

#         elif [ $chosen_step == DR2 ]
#         then 
#             echo 'Performing DR2 with Pileup'
#             # From MCM

#             chosen_threads=8
#             echo "COMMAND:"
#             echo "cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads $chosen_threads --era Run2_2017 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events"

#             cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads $chosen_threads --era Run2_2017 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

#             #cmsRun $DR2Config 

#             #submit_crab_postGEN $DR2Config $cmssw_v $crab_input $chosen_threads
#             submit_crab_postGEN $DR2Config $cmssw_v $chosen_threads $chosen_job_size $chosen_step $Campaign $dryRun "${f_paths[@]}" 

#             #end_script 

#         fi # if wPU and (if DR1 elif DR2) 

#     elif [ $chosen_pileup == "woPU" ]
#     then
        
#         # Without Pileup (need to test)

#         if [ $chosen_step == DR1 ]
#         then
#             echo 'Performing DR1 without Pileup'

#             # 7125 DR1 With Pileup 
#             #  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/GEN-SIM-DIGI-RAW" --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 --nThreads 4 --datamix PreMix --era Run2_2016 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

#             # 939 DR1 With Pileup
#             #  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW"  --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

#             chosen_threads=8

#             #cmsDriver.py step1 --filein file:$GenSimOutput --fileout file:$DR1Output --mc --eventcontent RAWSIM --pileup NoPileUp --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGI,L1,DIGI2RAW,HLT:2e34v40 --nThreads $chosen_threads --era Run2_2017 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events
#             echo "COMMAND:"
#             echo "cmsDriver.py step1 --filein $paths_string --fileout file:$DR1Output --mc --eventcontent RAWSIM --pileup NoPileUp --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGI,L1,DIGI2RAW,HLT:2e34v40 --nThreads $chosen_threads --era Run2_2017 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events"
#             cmsDriver.py step1 --filein $paths_string --fileout file:$DR1Output --mc --eventcontent RAWSIM --pileup NoPileUp --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGI,L1,DIGI2RAW,HLT:2e34v40 --nThreads $chosen_threads --era Run2_2017 --python_filename $DR1Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

#             # The one below worked once for some reason, while I remember the top one failing, even though they look the same 
#             #cmsDriver.py step1 --filein file:testoutput.root --fileout file:test_Dr1output.root --mc --eventcontent RAWSIM --pileup NoPileUp --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGI,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --era Run2_2017 --python_filename DR1config.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

#             # Put 939 nopileup DR1 here

#             #cmsRun $DR1Config

#             #echo "DR1Config = $DR1Config"

#             #submit_crab_postGEN $DR1Config $cmssw_v $crab_input $chosen_threads $chosen_jobs "${f_paths[@]}"
#             #submit_crab_postGEN $DR1Config $cmssw_v $chosen_threads $chosen_job_size $chosen_events "${f_paths[@]}"
#             submit_crab_postGEN $DR1Config $cmssw_v $chosen_threads $chosen_job_size $chosen_step $Campaign $dryRun "${f_paths[@]}" 

#             #end_script 

#         elif [ $chosen_step == DR2 ]
#         then
#             echo 'Performing DR2 without Pileup'

#             # 7125 DR2 With Pileup 
#             # cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,RECO,EI --nThreads 4 --era Run2_2016 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

#             # 939 DR2 With Pileup
#             # cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads 8 --era Run2_2017 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

#             # 7125 DR2 Without Pileup
#             #cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent RAWAODSIM --runUnscheduled --datatier RAWAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --step RAW2DIGI,L1Reco,RECO,EI --nThreads 4 --era Run2_2016 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

#             # 7125: RAW2DIGI,RECO,EI -> RAW2DIGI,L1Reco,RECO,EI
#             # 939: RAW2DIGI,RECO,RECOSIM,EI -> RAW2DIGI,L1Reco,RECO,RECOSIM,EI
            

#             # Put 939 nopileup DR2 here

#             chosen_threads=8

#             #cmsDriver.py step2 --filein file:$DR1Output --fileout file:$DR2Output --mc --eventcontent RAWAODSIM --runUnscheduled --datatier RAWAODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --nThreads $chosen_threads --era Run2_2017 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events
#             echo "COMMAND:"
#             echo "cmsDriver.py step2 --filein $paths_string --fileout file:$DR2Output --mc --eventcontent RAWAODSIM --runUnscheduled --datatier RAWAODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --nThreads $chosen_threads --era Run2_2017 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events"
#             cmsDriver.py step2 --filein $paths_string --fileout file:$DR2Output --mc --eventcontent RAWAODSIM --runUnscheduled --datatier RAWAODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --nThreads $chosen_threads --era Run2_2017 --python_filename $DR2Config --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

            

#             #cmsRun $DR2Config 

#             #submit_crab_postGEN $DR2Config $cmssw_v $crab_input $chosen_threads
#             submit_crab_postGEN $DR2Config $cmssw_v $chosen_threads $chosen_job_size $chosen_step $Campaign $dryRun "${f_paths[@]}" 

#             #end_script 
        
#         fi # if woPU and (if DR1 elif DR2) 

#     fi # if wPU elif woPU 

# fi # if DR1 or DR2 

# # MiniAOD

# if [ $chosen_step == MINIAOD ]
# then

#     cmssw_v=CMSSW_9_4_7

#     #crab_input=${PrevStepOutput#"/eos/cms"} # Remove beginning of gen output (DR1 input) file path so it can be read by the crab config 
#     #echo "Crab Input = $crab_input"

#     PathNoRoot=${PrevStepOutput%?????} # remove .root
#     EndofPath=${PathNoRoot##*/} # remove everything before and including final '/' in long path /eos/cms/store/...
#     # Should be ID of specific decay channel/PUconfig/events 

#     SinglePathNoRoot=${SinglePath%?????} # remove .root
#     EndofSinglePath=${SinglePathNoRoot##*/} # remove everything before and including final '/' in long path /eos/cms/store/...

#     echo "EndofSinglePath = $EndofSinglePath"

#     MINIAODInput=$PrevStepOutput

#     # Remove previous step from name 
#     #MINIAODOutput=$EndofPath 
#     MINIAODOutput=$EndofSinglePath 
#     MINIAODOutput=${MINIAODOutput%_DR2*}
#     MINIAODOutput+=_MINIAOD.root

#     mkdir -p $cmssw_v/src/cmssw_configs/ # create directory if it doesn't exist 

#     MINIAODConfig=$cmssw_v/src/cmssw_configs/${Campaign}_
#     #MINIAODConfig+=$EndofPath
#     MINIAODConfig+=$EndofSinglePath
#     MINIAODConfig=${MINIAODConfig%_DR2*}
#     MINIAODConfig+=_MINIAOD.py

#     #!/bin/bash
#     source /cvmfs/cms.cern.ch/cmsset_default.sh
#     export SCRAM_ARCH=slc6_amd64_gcc630
#     if [ -r CMSSW_9_4_7/src ] ; then 
#     echo release CMSSW_9_4_7 already exists
#     else
#     scram p CMSSW CMSSW_9_4_7
#     fi
#     cd CMSSW_9_4_7/src
#     eval `scram runtime -sh`

#     # AODOutput=${PrevStepOutput%?????}
#     # AODConfig=$AODOutput
#     # AODOutput+=_MiniAOD.root
#     # AODConfig+=_MiniAOD.py

#     chosen_threads=4

#     scram b
#     cd ../../
#     echo "COMMAND:"
#     echo "cmsDriver.py step1 --filein $paths_string --fileout file:$MINIAODOutput --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mc2017_realistic_v14 --step PAT --nThreads $chosen_threads --scenario pp --era Run2_2017,run2_miniAOD_94XFall17 --python_filename $MINIAODConfig --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events"
#     cmsDriver.py step1 --filein $paths_string --fileout file:$MINIAODOutput --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mc2017_realistic_v14 --step PAT --nThreads $chosen_threads --scenario pp --era Run2_2017,run2_miniAOD_94XFall17 --python_filename $MINIAODConfig --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n $chosen_events

#     #cmsRun $AODConfig

#     submit_crab_postGEN $MINIAODConfig $cmssw_v $chosen_threads $chosen_job_size $chosen_step $Campaign $dryRun "${f_paths[@]}" 

#     #end_script 

# fi 
