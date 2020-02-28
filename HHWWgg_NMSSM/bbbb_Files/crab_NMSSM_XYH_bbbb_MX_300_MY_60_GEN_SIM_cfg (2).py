from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'NMSSM_XYH_bbbb_MX_300_MY_60_GEN_SIM_Run2016_v15'
config.General.workArea = 'crab_projects_NMSSM_XYH_bbbb_MCproduction_Run2016_v15'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'NMSSM_XYH_bbbb_MX_300_MY_60_GEN_SIM_cfg.py'
config.JobType.inputFiles = ['/uscms_data/d3/fravera/NMSSM_XYH_bbbb_MCproduction_Run2016/CMSSW_7_1_19/src/GridPacks/NMSSM_XYH_bbbb_MX_300_MY_60_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz']
config.JobType.maxMemoryMB = 4000

config.Data.outputPrimaryDataset = 'NMSSM_XYH_bbbb_MX_300_MY_60_madgraph242'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 500  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/NMSSM_XYH_bbbb_v15' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'crab_NMSSM_XYH_bbbb_MX_300_MY_60_GEN_SIM_v15'

config.Site.storageSite = 'T3_US_FNALLPC'
