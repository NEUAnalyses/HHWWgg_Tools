import FWCore.ParameterSet.Config as cms                                                                                                                                                  
# link to card:                                                                                                                                                                                             
# https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/VBF_HH                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                            
externalLHEProducer = cms.EDProducer("ExternalLHEProducer",                                                                                                                                                 
    nEvents = cms.untracked.uint32(5000),                                                                                                                                                                   
    outputFile = cms.string('cmsgrid_final.lhe'),                                                                                                                                                           
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),                                                                                                       
    numberOfParameters = cms.uint32(1),                                                                                                                                                                     
	args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc630/14TeV/madgraph/V5_2.6.5/VBF_HH_CV_1_C2V_1_C3_0_14TeV/VBF_HH_CV_1_C2V_1_C3_0_14TeV-madgraph_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),
)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

import FWCore.ParameterSet.Config as cms                                                                                                                                      
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
            '24:mMin = 0.05', # the lower limit of the allowed mass range generated by the Breit-Wigner (in GeV)
            '24:onMode = off', # Turn off all W decays 
            '24:onIfAny = 1 2 3 4 5', # Add W->qq decays 
            '25:onMode = off', # Turn off all H decays 
            '25:onIfMatch = 22 22', # Add H->gg decay
            '25:onIfMatch = 24 -24', # Add H->WW decay 
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:udscbAsEquivalent  = on',  #on: treat udscb quarks as equivalent
            'ResonanceDecayFilter:mothers = 25,24', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:daughters = 1,1,1,1,22,22', # qq,qq,gg 
                                                                                                                                                                      
          ),                                                                                                                                                                                                
        parameterSets = cms.vstring('pythia8CommonSettings',                                                                                                                                                
                                    'pythia8CP5Settings',                                                                                                                                                   
                                    'processParameters'                                                                                                                                                     
                                    )                                                                                                                                                                       
        )                                                                                                                                                                                                   
                         )                                                                                                                                                                                  
                                                                                                                                                                                                            
ProductionFilterSequence = cms.Sequence(generator)                                                                                                                                                          
