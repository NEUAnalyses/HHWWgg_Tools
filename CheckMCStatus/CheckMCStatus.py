########################################################################################################################
# Abraham Tishelman-Charny                                                                                             #
# 20 October 2020                                                                                                      #
#                                                                                                                      #
# The purpose of this module is to plot MetaData for CMS DAS samples of interest. Can for example                      #
# be used to check the MC status of centrally produced samples by plotting number of events.                           #
#                                                                                                                      #
# Example Usage:                                                                                                       #
#                                                                                                                      #
# voms # (voms-proxy-init --voms cms --valid 168:00)                                                                   #
# python CheckMCStatus.py --outLoc /eos/user/a/atishelm/www/HHWWgg/MCstatus --oneDataset --PhysicsType NonResonant     #
########################################################################################################################

from python.CheckMCStatus_Tools import * 
from python.Options import * 
import pandas as pd 
import subprocess

##-- Get User input Args
args = GetOptions() 

if __name__ == '__main__':
    oneDataset = args.oneDataset
    
    ##-- Set output location and create directory if it doesn't exist, copying index file as well 
    ##-- Note: <outLoc>/../ must exist 
    outLoc = args.outLoc  
    CheckMakeOutLocation(outLoc)

    ##-- Define Dataset Names based on physics process, type, year, step 
    pDsetNames, Processes, sDsetNames, steps, instances, outDsetNames = [], [], [], [], [], []
    finalStates = ["GluGluToHHTo2G2Qlnu*", "GluGluToHHTo2G4Q*", "GluGluToHHTo2G2l2nu*"]
    years = ["*RunIISummer16MiniAODv3*", "*RunIIFall17MiniAODv2*", "*RunIIAutumn18MiniAOD*"]
    step = "MINIAODSIM"
    instance = "prod/global"
    Processes_ = GetProcesses("NonResonant")

    for Process in Processes_:
        for finalState in finalStates:
            for year in years:
                fState_fsetStr = "%s%s"%(finalState,Process)
                pDsetNames.append(fState_fsetStr)
                sDsetNames.append(year)
                steps.append(step)
                instances.append(instance)
                outName_Process = GetProcessLabel(Process)
                Processes.append(outName_Process)
                outName_FS = GetFSLabel(finalState)
                outName_year = GetYearLabel(year)
                outDsetName = "%s-%s-%s"%(outName_Process,outName_FS,outName_year)
                outDsetNames.append(outDsetName)
                if(oneDataset): break
            if(oneDataset): break 

    ##-- Query DAS and plot MetaData for each dataset name 
    for i in range(len(pDsetNames)):
        paramNames = ["pDsetName", "Process", "sDsetName", "step", "instance", "outDsetName"]
        for paramName in paramNames:
            if(paramName.endswith('s')):
                exec("%s = %ses[i]"%(paramName,paramName))
            else: 
                exec("%s = %ss[i]"%(paramName,paramName))
        check = CheckMC(pDsetName, sDsetName, step, instance, outDsetName)
        check.GetDatasetNames() ##-- Get dataset names 
        command = "wc -l Datasets/%s.txt"%(outDsetName)
        nDatasets = int(str(subprocess.check_output(command, shell=True)).split(' ')[0])
        print "nDatasets:",nDatasets
        if(nDatasets > 0): ##-- If the query returns no datasets, cannot plot anything 
            dsets = pd.read_csv('Datasets/%s.txt'%(outDsetName), header=None)
            check.GetDsetMetaData(dsets) ##-- Produce txt file with number of events per dataset 

            ##-- Plot 
            if(Process=="GF"):
                check.Plot(dsets,outLoc,"GF_LO")
                check.Plot(dsets,outLoc,"GF_NLO")
            if(Process=="VBF"):
                check.Plot(dsets,outLoc,"VBF_LO")
