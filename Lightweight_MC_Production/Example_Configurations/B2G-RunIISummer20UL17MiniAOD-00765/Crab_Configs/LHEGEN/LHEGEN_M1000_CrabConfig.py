from CRABClient.UserUtilities import config
config = config()
 
config.General.requestName = 'X1000_GluGluToRadionToHHTo2G2WTo2G4Q'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False
 
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '/afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Lightweight_MC_Production/Test/CMSSW_10_6_25/src/B2G-RunIISummer20UL17wmLHEGEN-01293_WWgg_M1000_cfg.py'
#config.JobType.numCores = 8
#config.JobType.maxMemoryMB = 8000
 
config.Data.outputPrimaryDataset = 'X1000_GluGluToRadionToHHTo2G2WTo2G4Q'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 250
NJOBS = 40  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/Private_UL_For_Efficiency_Checks/'
config.Data.publication = False
config.Data.outputDatasetTag = 'RunIISummer20UL17_LHEGEN'
 
config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'
