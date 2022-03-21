import FWCore.ParameterSet.Config as cms


externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
   args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/14TeV/madgraph/V5_2.6.5/WJetsToLNu/W2JetsToLNu_14TeV-madgraphMLM-pythia8_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

#Link to datacards:
#https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/WJetsToLNu/W4JetsToLNu_13TeV-madgraphMLM-pythia8


from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(14000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 5.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = 19.', #this is the actual merging scale
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            'JetMatching:nJetMax = 4', #number of partons in born matrix element for highest multiplicity
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
            'TimeShower:mMaxGamma = 4.0',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
    )
)
gj_filter = cms.EDFilter("PythiaFilterGammaGamma",
    PtSeedThr = cms.double(5.0),
    EtaSeedThr = cms.double(2.8),
    PtGammaThr = cms.double(0.0),
    EtaGammaThr = cms.double(2.8),
    PtElThr = cms.double(2.0),
    EtaElThr = cms.double(2.8),
    dRSeedMax = cms.double(0.0),
    dPhiSeedMax = cms.double(0.2),
    dEtaSeedMax = cms.double(0.12),
    dRNarrowCone = cms.double(0.02),
    PtTkThr = cms.double(1.6),
    EtaTkThr = cms.double(2.2),
    dRTkMax = cms.double(0.2),
    PtMinCandidate1 = cms.double(15.),
    PtMinCandidate2 = cms.double(15.),
    EtaMaxCandidate = cms.double(3.0),
    NTkConeMax = cms.int32(2),
    NTkConeSum = cms.int32(4),
    InvMassMin = cms.double(80.0),
    InvMassMax = cms.double(14000.0),
    EnergyCut = cms.double(1.0),
    AcceptPrompts = cms.bool(True),
    PromptPtThreshold = cms.double(15.0)   
    
    )
 
ProductionFilterSequence = cms.Sequence(generator*gj_filter)
