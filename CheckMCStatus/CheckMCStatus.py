from python.CheckMCStatus_Tools import * 
import pandas as pd 

ol = "/eos/user/a/atishelm/www/HHWWgg/MCstatus"

if(not os.path.exists(ol)):
    print"Creating output directory: %s"%(ol)
    beforeOl = "%s/../"%(ol)
    os.system('mkdir %s'%(ol))
    os.system('cp %s/index.php %s'%(beforeOl,ol))   

# os.system("echo'Initializing voms proxy...'")
# os.system("voms-proxy-init --voms cms --valid 168:00")

pDsetNames, sDsetNames, steps, instances, outDsetNames = [], [], [], [], []
finalStates = ["GluGluToHHTo2G2Qlnu*", "GluGluToHHTo2G4Q*", "GluGluToHHTo2G2l2nu*"]
years = ["*RunIISummer16MiniAODv3*", "*RunIIFall17MiniAODv2*", "*RunIIAutumn18MiniAOD*"]
step = "MINIAODSIM"
instance = "prod/global"

for finalState in finalStates:
    for year in years:
        pDsetNames.append(finalState)
        sDsetNames.append(year)
        steps.append(step)
        instances.append(instance)
        outName_FS = GetFSLabel(finalState)
        outName_year = GetYearLabel(year)
        outDsetName = "%s-%s"%(outName_FS,outName_year)
        outDsetNames.append(outDsetName)

for i in range(len(pDsetNames)):
    paramNames = ["pDsetName", "sDsetName", "step", "instance", "outDsetName"]
    for paramName in paramNames:
        exec("%s = %ss[i]"%(paramName,paramName))

    check = CheckMC(pDsetName, sDsetName, step, instance, outDsetName)
    check.GetDatasetNames() ##-- Get dataset names 
    dsets = pd.read_csv('%s.txt'%(outDsetName), header=None)
    check.GetDsetMetaData(dsets) ##-- Produce txt file with number of events per dataset 
    check.Plot(dsets,ol)
