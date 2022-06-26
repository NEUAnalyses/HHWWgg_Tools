"""
15 December 2021 
Abraham Tishelman-Charny 

Shorter python module for custom reweighting for updated HIG-21-014 SL DNN.
Reweight (cHHH0 + cHHH2p45 + cHHH5) to cHHH1. Remove cHHH1 from sums. 

"""

import ROOT 
import os 
from array import array 
from Reweight_Tools import addVariables, Reweight, Categorize, EvenOddSplit
from SystematicTreeNames import GetSystLabels

# reweigh to cHHH1
year = "2016" 
node = "cHHH1"
#syst = "Nominal"
TDirec = ""
GENnorm = 0
isMC = 1
reweightNode = "cHHH1"
runLowEvents = 0
addNodeBranch = 0 
additionalSF = 0

#H_Y_Direc = "VH_2016"
#fileName = "VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2"  


fileNames =[

    # "VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2",
    # "ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2",

    # "VHToGG_2017_HHWWggTag_0_MoreVars_v2",
    "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2",

    # "VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2",
    # "ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2"
]



for fileName in fileNames:
    print("On file:",fileName)

    H_Y_Direc_dict = {
        "VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "VH_2016",
        "ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "ttH_2016",

        "VHToGG_2017_HHWWggTag_0_MoreVars_v2" : "VH_2017",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2" : "ttH_2017",

        "VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2" : "VH_2018",
        "ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2" : "ttH_2018"
    }

    H_Y_Direc = H_Y_Direc_dict[fileName]

    if("2016" in fileName): year = "2016"
    if("2017" in fileName): year = "2017"
    if("2018" in fileName): year = "2018"
    
    systLabels = GetSystLabels(year)

    for syst_i, syst in enumerate(systLabels):
        print("syst:",syst)
        
        # if(syst_i >= 3): 
        #     continue

        d = "/eos/user/c/chuw/ForAbe/Single_H_hadded/"
        f = "{d}/{fileName}.root".format(d=d, fileName=fileName)

        # direcs 
        thisDirec = "{d}/{H_Y_Direc}_even".format(d=d, H_Y_Direc=H_Y_Direc)
        if(not os.path.isdir(thisDirec)):
            print("Creating output directory:",thisDirec)
            os.system("mkdir {thisDirec}".format(thisDirec=thisDirec))  

        thisDirec = "{d}/{H_Y_Direc}_odd".format(d=d, H_Y_Direc=H_Y_Direc)
        if(not os.path.isdir(thisDirec)):
            print("Creating output directory:",thisDirec)
            os.system("mkdir {thisDirec}".format(thisDirec=thisDirec))    

        outName_even = "{d}/{H_Y_Direc}_even/{fileName}_{syst}_even.root".format(d=d, fileName=fileName, syst=syst, H_Y_Direc=H_Y_Direc)
        outName_odd = "{d}/{H_Y_Direc}_odd/{fileName}_{syst}_odd.root".format(d=d, fileName=fileName, syst=syst, H_Y_Direc=H_Y_Direc)

        outFile_even = ROOT.TFile(outName_even, "RECREATE")
        outFile_odd = ROOT.TFile(outName_odd, "RECREATE")

        inFile = ROOT.TFile(f,"READ")

        if(TDirec != ""):
            inDir = inFile.Get(TDirec)  
            treeNames = inDir.GetListOfKeys()
        else:
            treeNames = inFile.GetListOfKeys()

        if(GENnorm):
            Norm = GetNorm(year, node)    
        else: 
            Norm = 1. 

        print("Norm:",Norm)
        print("Norm:",Norm)
        print("Norm:",Norm)

        SingleHiggsTreeDict = {
            "VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "wzh_125_13TeV_HHWWggTag_0",
            "ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "tth_125_13TeV_HHWWggTag_0",

            "VHToGG_2017_HHWWggTag_0_MoreVars_v2" : "wzh_125_13TeV_HHWWggTag_0",
            "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2" : "tth_125_13TeV_HHWWggTag_0",

            "VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2" : "wzh_125_13TeV_HHWWggTag_0",
            "ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2" : "tth_125_13TeV_HHWWggTag_0"            
        }

        nonSystTreePath = SingleHiggsTreeDict[fileName]

        if(syst == "Nominal"):
            systExt = "v1"
        else:
            systExt = "%s_v1"%(syst)

        fullTreePath = "%s_%s"%(nonSystTreePath, systExt)
        
        EvenOddSplit(inFile, runLowEvents, outFile_even, outFile_odd, fullTreePath, additionalSF, reweightNode, syst) # split events into even and odd

print("DONE")