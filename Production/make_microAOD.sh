#!/bin/bash

make_microAOD(){

    # Take input file path 

    miniaod_path=$1 # Does not include '/eos/cms/'
    nevents=$2
    output_name="myMicroAODOutput_"
    output_name+=${miniaod_path##*/} # <filename>.root 

    echo "Making flashgg microaod from miniaod located at: $miniaod_path"

    cd /afs/cern.ch/work/a/atishelm/15JanFlashgg/CMSSW_8_0_26_patch1/src/flashgg
    cmsenv

    # Create microAODstd config file with desired input miniaod file 

    echo 'import FWCore.ParameterSet.Config as cms' >> mymicroAODstd.py
    echo 'import FWCore.Utilities.FileUtils as FileUtils'>> mymicroAODstd.py
    echo ' ' >> mymicroAODstd.py
    echo 'process = cms.Process("FLASHggMicroAOD")' >> mymicroAODstd.py
    echo ' ' >> mymicroAODstd.py
    echo 'process.load("FWCore.MessageService.MessageLogger_cfi")' >> mymicroAODstd.py
    echo ' ' >> mymicroAODstd.py
    echo 'process.load("Configuration.StandardSequences.GeometryDB_cff")' >> mymicroAODstd.py
    echo 'process.load("Configuration.StandardSequences.MagneticField_cff")' >> mymicroAODstd.py
    echo '#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff") # gives deprecated message in 80X but still runs' >> mymicroAODstd.py
    echo 'process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")' >> mymicroAODstd.py
    echo 'from Configuration.AlCa.GlobalTag import GlobalTag' >> mymicroAODstd.py
    echo ' ' >> mymicroAODstd.py

    #echo 'process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( $nevents ) )' >> mymicroAODstd.py # max events here 

    input_events='process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32('
    input_events+=$nevents
    input_events+=') )'

    echo "$input_events" >> mymicroAODstd.py

    echo ' ' >> mymicroAODstd.py 
    echo 'import os' >> mymicroAODstd.py
    echo 'if os.environ["CMSSW_VERSION"].count("CMSSW_8_0"):' >> mymicroAODstd.py
    echo "    process.GlobalTag = GlobalTag(process.GlobalTag,'80X_mcRun2_asymptotic_2016_TrancheIV_v7','')" >> mymicroAODstd.py


    #echo '    process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("$miniaod_path"))' >> mymicroAODstd.py # Input MINIAOD path here 

    input_path='    process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("'
    input_path+=$miniaod_path
    input_path+='"))'

    echo "$input_path" >> mymicroAODstd.py

    echo "#    process.GlobalTag = GlobalTag(process.GlobalTag,'80X_dataRun2_2016LegacyRepro_v4','')" >> mymicroAODstd.py
    echo '#    process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2016B/SingleElectron/MINIAOD/07Aug17_ver1-v1/110000/0248293E-578B-E711-A639-44A842CFC9D9.root")))' >> mymicroAODstd.py
    echo 'elif os.environ["CMSSW_VERSION"].count("CMSSW_9_2") or os.environ["CMSSW_VERSION"].count("CMSSW_9_4"):' >> mymicroAODstd.py
    echo "    process.GlobalTag = GlobalTag(process.GlobalTag,'92X_dataRun2_Prompt_v11','')" >> mymicroAODstd.py
    echo '    process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring("/store/data/Run2017F/DoubleEG/MINIAOD/PromptReco-v1/000/305/040/00000/2E5E7E62-29B2-E711-9E47-02163E019D16.root"))' >> mymicroAODstd.py
    echo "else:" >> mymicroAODstd.py
    echo '    raise Exception,"The default setup for microAODstd.py does not support releases other than 80X, 92X (being deprecated), and 94X"' >> mymicroAODstd.py
    #
    #
    #
    echo " " >> mymicroAODstd.py
    echo 'process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService")' >> mymicroAODstd.py
    echo "process.RandomNumberGeneratorService.flashggRandomizedPhotons = cms.PSet(" >> mymicroAODstd.py
    echo "          initialSeed = cms.untracked.uint32(16253245)" >> mymicroAODstd.py
    echo "        )" >> mymicroAODstd.py
    echo "# Bunch of commented out stuff here for other year configurations " >> mymicroAODstd.py
    echo "process.MessageLogger.cerr.threshold = 'ERROR' # can't get suppressWarning to work: disable all warnings for now" >> mymicroAODstd.py
    echo 'process.load("flashgg/MicroAOD/flashggMicroAODSequence_cff")' >> mymicroAODstd.py
    echo '#process.weightsCount.pileupInfo = "addPileupInfo"' >> mymicroAODstd.py
    echo " " >> mymicroAODstd.py
    echo "from flashgg.MicroAOD.flashggMicroAODOutputCommands_cff import microAODDefaultOutputCommand" >> mymicroAODstd.py

    output_file='process.out = cms.OutputModule("PoolOutputModule",'

    output_file+="fileName = cms.untracked.string('" 
    output_file+=$output_name
    output_file+="'),"

    echo "$output_file" >> mymicroAODstd.py
    echo "                               outputCommands = microAODDefaultOutputCommand" >> mymicroAODstd.py
    echo "                               )" >> mymicroAODstd.py
    echo "# All jets are now handled in MicroAODCustomize.py" >> mymicroAODstd.py
    echo "# Switch from PFCHS to PUPPI with puppi=1 argument (both if puppi=2)" >> mymicroAODstd.py
    echo " " >> mymicroAODstd.py
    echo "process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')" >> mymicroAODstd.py
    echo "process.load('RecoMET.METFilters.globalTightHalo2016Filter_cfi')" >> mymicroAODstd.py
    echo "process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')" >> mymicroAODstd.py
    echo " " >> mymicroAODstd.py
    echo 'process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")' >> mymicroAODstd.py
    echo 'process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")' >> mymicroAODstd.py
    echo 'process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")' >> mymicroAODstd.py
    echo 'process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")' >> mymicroAODstd.py
    echo " " >> mymicroAODstd.py
    echo "process.flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)" >> mymicroAODstd.py
    echo "process.flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)" >> mymicroAODstd.py
    echo "process.flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)" >> mymicroAODstd.py
    echo " " >> mymicroAODstd.py
    echo "process.p = cms.Path(process.flashggMicroAODSequence)" >> mymicroAODstd.py
    echo "process.e = cms.EndPath(process.out)" >> mymicroAODstd.py

    # Uncomment these lines to run the example commissioning module and send its output to root
    #process.commissioning = cms.EDAnalyzer('flashggCommissioning',
    #                                       PhotonTag=cms.untracked.InputTag('flashggPhotons'),
    #                                       DiPhotonTag = cms.untracked.InputTag('flashggDiPhotons'),
    #                                       VertexTag=cms.untracked.InputTag('offlineSlimmedPrimaryVertices')
    #)
    #process.TFileService = cms.Service("TFileService",
    #                                   fileName = cms.string("commissioningTree.root")
    #)
    #process.p *= process.commissioning

    echo "from flashgg.MicroAOD.MicroAODCustomize import customize" >> mymicroAODstd.py
    echo "customize(process)" >> mymicroAODstd.py
    echo " " >> mymicroAODstd.py
    echo 'if "DY" in customize.datasetName or "SingleElectron" in customize.datasetName or "DoubleEG" in customize.datasetName:' >> mymicroAODstd.py
    echo "  customize.customizeHLT(process)" >> mymicroAODstd.py
    echo " " >> mymicroAODstd.py
    echo "#open('dump.py', 'w').write(process.dumpPython())" >> mymicroAODstd.py

    cp mymicroAODstd.py MicroAOD/test/mymicroAODstd.py
    rm mymicroAODstd.py
    cmsRun MicroAOD/test/mymicroAODstd.py processType=sig datasetName=glugluh
    #cmsRun Taggers/test/simple_Tag_test.py # If this is used, make sure input file path is correct 

    cd /afs/cern.ch/work/a/atishelm/private/HH_WWgg

}