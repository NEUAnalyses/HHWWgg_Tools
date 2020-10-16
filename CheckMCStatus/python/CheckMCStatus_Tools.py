import os 
import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np 

class CheckMC:

    def __init__(self, primaryDatasetName, secondaryDatasetName, step, instance, outDsets):
        self.primaryDatasetName = primaryDatasetName
        self.secondaryDatasetName = secondaryDatasetName
        self.step = step 
        self.instance = instance
        self.outDsets = outDsets

    def GetDatasetNames(self):
        print"Querying DAS..."
        os.system("rm %s.txt"%(self.outDsets))
        dasCommand = "dasgoclient --query='/%s/%s/%s instance=%s' >> %s.txt"%(self.primaryDatasetName, self.secondaryDatasetName, self.step, self.instance, self.outDsets)
        print"DAS Command:",dasCommand
        os.system(dasCommand)
        print"DAS Command:",dasCommand

    def GetDsetMetaData(self, dsets):
        grepString = "nevents"
        outFile = "%s_MetaData.txt"%(self.outDsets)
        outLabel = "MetaData"
        os.system("rm %s"%(outFile))
        for dset in dsets[0]:
            print"dset:",dset
            dasCommand = "dasgoclient --query 'summary dataset=%s instance=%s' -json | grep %s >> %s"%(dset,self.instance, grepString, outFile)
            os.system(dasCommand)

    def Plot(self, dsets, ol):
        MetaData = pd.read_csv('%s_MetaData.txt'%(self.outDsets), header=None)

        datasets = dsets[0].tolist()
        nodes = [str(fullSt.split('/')[1].split('_')[2]) for fullSt in datasets]
        nEvents = [int(nEvent_str.split(':')[-1]) for nEvent_str in MetaData[12]]

        fontsize = 8 
        if(len(nodes) > 15): fontsize = 6

        x_pos = [i for i, _ in enumerate(nodes)]
        y_pos = np.arange(len(nodes))
        plt.figure(figsize=(8, 4))
        plt.bar(y_pos, nEvents, align='center', color=(0.052478,0.2303,0.717,0.5), edgecolor='black')
        plt.xticks(y_pos, nodes)
        plt.ylim(ymin=0,ymax=420000)
        plt.ylabel('Nevents')
        plt.xlabel('Non-Resonant Node')
        plt.xticks(fontsize=fontsize)
        plt.title('%s MiniAOD Nevents'%(self.outDsets))
        plt.hlines(400000,-0.5,len(nodes), linestyles='dashed', colors='black')

        plt.savefig("%s/%s_nEvents.png"%(ol,self.outDsets))
        plt.close()

        # add time stamp to plot 
        # Could also be useful to have three bar plot. One for each year or final state. 

def GetFSLabel(fullFS):
    outName_FS_Dict = {
        "GluGluToHHTo2G2Qlnu*": "Semi-Leptonic", 
        "GluGluToHHTo2G4Q*": "Fully-Hadronic", 
        "GluGluToHHTo2G2l2nu*" : "Fully-Leptonic"
    }
    return outName_FS_Dict[fullFS]

def GetYearLabel(fullYear):
    outName_year_Dict = {
        "*RunIISummer16MiniAODv3*": "2016", 
        "*RunIIFall17MiniAODv2*": "2017", 
        "*RunIIAutumn18MiniAOD*" : "2018"
    }   
    return outName_year_Dict[fullYear]    
      