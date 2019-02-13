import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.6.0/GluGluToRadionToHH_M1250/v1/GluGluToRadionToHH_M1250_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

#Link to datacards:
#https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/exo_diboson/Spin-0


from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            #'15:onMode = off',
            #'15:onIfAny = 11 13', # only leptonic tau decays
            '24:mMin = 0.05',
            '24:onMode = off',
            #'24:onIfAny = 1 2 3 4 5 11 13 15', # W->jets decay and a leptonic charged Z decay, including taus
            #'24:onIfAny = 1 2 3 4 11 13 15', # W->jets decay and a leptonic charged Z decay, including taus
            '24:onIfAny = 1 2 3 4 5 13', # W->qq decay and W->enu  
            #'24:mMin = 0.05',
            #'24:onMode = off',
            '25:m0 = 125.09',
            '25:onMode = off',
            '25:onIfMatch = 22 22',
            '25:onIfMatch = 24 -24',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            #'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as equivalent
            #'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
            #'ResonanceDecayFilter:allNuAsEquivalent  = off', #on: treat all three neutrino flavours as equivalent
            #'ResonanceDecayFilter:udscAsEquivalent   = on', #on: treat udsc quarks as equivalent
            'ResonanceDecayFilter:udscbAsEquivalent  = on',  #on: treat udscb quarks as equivalent
            'ResonanceDecayFilter:mothers = 25,24', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            #'ResonanceDecayFilter:daughters = 5,5,23,23,1,1,11,11', # Do you need Z or W in daughters? 
            #'ResonanceDecayFilter:daughters = 24,24,1,1,11,12', # qq,enu 
            'ResonanceDecayFilter:daughters = 1,1,13,14,22,22', # qq,munu,gg 
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters'
                                    )
        )
                         )


ProductionFilterSequence = cms.Sequence(generator)
