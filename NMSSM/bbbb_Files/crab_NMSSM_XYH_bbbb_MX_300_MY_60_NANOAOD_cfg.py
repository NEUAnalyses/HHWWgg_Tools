from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'NMSSM_XYH_bbbb_MX_300_MY_60_NANOAOD_Run2016_v1'
config.General.workArea = 'crab_projects_NMSSM_XYH_bbbb_MCproduction_NANOAOD_Run2016_v1'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'NMSSM_XYH_bbbb_NANOAOD_cfg.py'

config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/NMSSM_XYH_bbbb_MX_300_MY_60_madgraph242/fravera-crab_NMSSM_XYH_bbbb_MX_300_MY_60_MINIAOD_Run2016_v2-bd3e7bcff6c9bcad356ea4ed7e4f08b4/USER'
config.Data.splitting = 'FileBased'
config.Data.publication = True
config.Data.unitsPerJob = 20
config.Data.outLFNDirBase = '/store/user/%s/NMSSM_XYH_bbbb_NANOAOD/' % (getUsernameFromSiteDB())
config.Data.outputDatasetTag = 'crab_NMSSM_XYH_bbbb_MX_300_MY_60_NANOAOD_Run2016_v1'

config.Site.storageSite = 'T3_US_FNALLPC'


