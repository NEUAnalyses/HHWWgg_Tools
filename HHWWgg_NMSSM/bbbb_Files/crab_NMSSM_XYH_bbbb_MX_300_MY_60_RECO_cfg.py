from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'NMSSM_XYH_bbbb_MX_300_MY_60_RECO_Run2016_v1'
config.General.workArea = 'crab_projects_NMSSM_XYH_bbbb_MCproduction_RECO_Run2016_v1'
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.maxMemoryMB = 8000

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'NMSSM_XYH_bbbb_RECO_cfg.py'

config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/NMSSM_XYH_bbbb_MX_300_MY_60_madgraph242/fravera-crab_NMSSM_XYH_bbbb_MX_300_MY_60_DIGI_Run2016_v2-16ca0fac1b892ff3c3d45d801745cbbf/USER'
config.Data.splitting = 'FileBased'
config.Data.publication = True
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/NMSSM_XYH_bbbb_RECO/' % (getUsernameFromSiteDB())
config.Data.outputDatasetTag = 'crab_NMSSM_XYH_bbbb_MX_300_MY_60_RECO_Run2016_v1'

config.Site.storageSite = 'T3_US_FNALLPC'
config.JobType.numCores = 4

