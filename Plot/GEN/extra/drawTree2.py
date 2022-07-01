#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms

process = cms.Process("GenDraw")

process.load('Configuration/StandardSequences/Services_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'

##########
# Source #
##########


#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X260_HHWWgg_qqlnu/100000events_GEN-SIM/200523_125055/Hadded/ggF_X260_HHWWgg_qqlnu_100000events_GEN-SIM_Hadded.root'
        )
    )



process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")


process.printTree = cms.EDAnalyzer( "ParticleTreeDrawer",
  src = cms.InputTag("genParticles"),
#    printP4 = cms.untracked.bool( True ),
#    printPtEtaPhi = cms.untracked.bool( True ),
  printStatus = cms.untracked.bool( True ),
#   status = cms.untracked.vint32( 3 ),
  printIndex = cms.untracked.bool(True )
)



process.printDecay = cms.EDAnalyzer( "ParticleDecayDrawer",
   src = cms.InputTag("genParticles"),
   printP4 = cms.untracked.bool( False ),
   printPtEtaPhi = cms.untracked.bool( False ),
   printVertex = cms.untracked.bool( False )
#   printStatus = cms.untracked.bool( True ),
#   status = cms.untracked.vint32( 3 )
#   printIndex = cms.untracked.bool(True )
)




process.ParticleViewer = cms.Sequence(
 #process.printTree 
 process.printDecay
)


process.pathParticleViewer = cms.Path(process.ParticleViewer)

