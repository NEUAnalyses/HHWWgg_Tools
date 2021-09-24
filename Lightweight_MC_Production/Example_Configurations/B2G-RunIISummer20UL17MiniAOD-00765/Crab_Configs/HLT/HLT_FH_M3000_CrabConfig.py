import os 

##-- Get input files from previous step 
inputFiles = [] 
inDir = "/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/Private_UL_For_Efficiency_Checks/X3000_GluGluToRadionToHHTo2G2WTo2G4Q/RunIISummer20UL17_DIGI/210804_203137/0000/"
inDir_noPrefix = inDir.replace("/eos/cms", "")
for root, dirs, files in os.walk(inDir):
    path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        if((".root" in file) and ("inLHE" not in file)):
            # print(len(path) * '---', file)
            inputFiles.append("%s/%s"%(inDir_noPrefix, file))
for inF in inputFiles:
    print(inF)
from CRABClient.UserUtilities import config
config = config()
 
config.General.requestName = 'X3000_GluGluToRadionToHHTo2G2WTo2G4Q_HLT'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False
 
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Lightweight_MC_Production/Test/B2G-RunIISummer20UL17HLT-00765_1_cfg.py'
#config.JobType.numCores = 8
#config.JobType.maxMemoryMB = 8000
 
config.Data.outputPrimaryDataset = 'X3000_GluGluToRadionToHHTo2G2WTo2G4Q'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/Private_UL_For_Efficiency_Checks/'
config.Data.publication = False 
config.Data.outputDatasetTag = 'RunIISummer20UL17_HLT'

config.Data.userInputFiles = inputFiles
 
config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'
