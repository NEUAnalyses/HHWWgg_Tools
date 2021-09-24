# CRAB3 config template for flashgg
# More options available on the twiki :
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial
# To actually prepare the jobs, please execute prepareCrabJobs.py

from WMCore.Configuration import Configuration
config = Configuration()
import os

config.section_("General")
config.General.requestName = "W3Jets_14TeV_Private_microaod"
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = "Analysis"
config.JobType.psetName = "microAODstd.py"

## to include local file in the sendbox, this will put the file in the directory where cmsRun runs
config.JobType.inputFiles = ['QGL_AK4chs_94X.db']

## incrase jobs time wall, maximum 2750 minutes (~46 hours)
#config.JobType.maxJobRuntimeMin = 2750

#config.JobType.maxMemoryMB = 2500 # For memory leaks. NB. will block jobs on many sites
## config.JobType.scriptExe = "cmsWrapper.sh"
config.JobType.pyCfgParams = ['datasetName=/W3Jets_14TeV/atishelm-RunIISummer20UL17_MiniAOD-e67f9b5d033cede4d000433a2a96d4fb/USER', 'processType=bkg', 'conditionsJSON=/afs/cern.ch/work/a/atishelm/private/flashgg-microAODs/CMSSW_10_6_8/src/flashgg/MetaData/data/MetaConditions/Era2017_legacy_v1.json']
config.JobType.sendPythonFolder = True
config.JobType.sendExternalFolder = True

config.section_("Data")
config.Data.inputDataset = "/W3Jets_14TeV/atishelm-RunIISummer20UL17_MiniAOD-e67f9b5d033cede4d000433a2a96d4fb/USER"
config.Data.inputDBS = 'phys03'
config.Data.splitting = "EventAwareLumiBased"
config.Data.unitsPerJob = 25000
config.Data.publication = True
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'W3Jets_14TeV_Summer20UL17'
config.Data.outLFNDirBase = "/store/group/phys_higgs/cmshgg/atishelm/flashgg/WJets_14TeV"

config.section_("Site")
config.Site.storageSite = "T2_CH_CERN"
config.Site.blacklist = ["T2_US_Nebraska"]
#config.Site.blacklist = ["T2_UK_London_Brunel","T1_US_FNAL","T2_US_MIT"]

