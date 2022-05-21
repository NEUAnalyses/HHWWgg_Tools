"""
27 April 2022 
Abraham Tishelman-Charny 

The purpose of this module is to get HH->WWgg VBF MiniAOD dataset names for HIG-21-014, in order to produce MicroAODs from them. 

Need to set voms proxy first in order to access datasets

voms-proxy-init --voms cms --valid 168:00
"""

import os 

finalStates = [
    "2G2Qlnu",
    "2G2l2nu",
    "2G4Q",
    "2G2ZTo2G4Q"
]

yearKeys = {
    "2016" : "RunIISummer16MiniAODv3", # 2016 
    "2017" : "RunIIFall17MiniAODv2-PU2017", # 2017
    "2018" : "RunIIAutumn18MiniAOD-102X_upgrade2018" # 2018 
}

for yearKey in yearKeys:
    outFile = "VBF_HH_MiniAODs_%s.txt"%(yearKey)
    for finalState in finalStates:
        print("yearKey:",yearKey)
        yearVal = yearKeys[yearKey]
        dataset = "/VBFHHTo{finalState}*/*{yearVal}*/MINIAODSIM".format(finalState=finalState, yearVal=yearVal)
        c = 'dasgoclient -query="dataset={dataset} instance=prod/global" >> {outFile}'.format(dataset=dataset, outFile=outFile)
        print("$",c)
        os.system(c)