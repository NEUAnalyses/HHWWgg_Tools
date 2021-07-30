from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
 
config.General.requestName = 'NMSSM_XYHWWggqqlnu_MX300_MY170_10000events_GEN_1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False
 
config.JobType.pluginName = 'PrivateMC'
config.JobType.inputFiles = ['/afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/NMSSM/genproductions/bin/MadGraph5_aMCatNLO/NMSSM_XYH_WWgg_MX_300_MY_170_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz']
config.JobType.psetName = '/afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Production/cmssw_configs/NMSSM_XYHWWggqqlnu_MX300_MY170_10000events_GEN.py'
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 8000
 
config.Data.outputPrimaryDataset = 'NMSSM_XYHWWggqqlnu_MX300_MY170'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 10  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/'
config.Data.publication = False
config.Data.outputDatasetTag = '10000events_GEN'
 
config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'
