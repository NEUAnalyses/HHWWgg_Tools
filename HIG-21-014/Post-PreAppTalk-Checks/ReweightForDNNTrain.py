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

# Normalization factor per sample (Semileptonic)
def GetNorm(year, node):

    # sum of gen weights from flashgg catalogues (semileptonic, assuming you're including cHHH0,1,2p45,5)
    Sum_2016 = (24041.67591 + 4392.211129 + 31501.80227)
    Sum_2017 = (21264.42409 + 4413.499586 + 17686.79584)
    Sum_2018 = (21358.25083 + 3331.597595 + 18889.14688)

    # For semileptonic case 
    NormVals = {
        "2016" : {
                    "cHHH0" : 24041.67591 / Sum_2016,
                    "cHHH2p45" : 4392.211129 / Sum_2016, 
                    "cHHH5" : 31501.80227 / Sum_2016
        },

        "2017" : {
                    "cHHH0" : 21264.42409 / Sum_2017,
                    "cHHH2p45" : 4413.499586 / Sum_2017,
                    "cHHH5" : 17686.79584 / Sum_2017
        },

        "2018" : {
                    "cHHH0" : 21358.25083 / Sum_2018,
                    "cHHH2p45" : 3331.597595 / Sum_2018,
                    "cHHH5" : 18889.14688 / Sum_2018
        }
    }

    return float(NormVals[year][node]) 


# begin with original
# year = "2017" 
# node = "cHHH0"
# # node = "cHHH2p45"
# # node = "cHHH5"
# syst = "Nominal"
# TDirec = "tagsDumper/trees"
# GENnorm = 1
# isMC = 1
# reweightNode = ""
# runLowEvents = 0
# addNodeBranch = 0 

# reweigh to cHHH1
year = "2017" 
node = "cHHH1"
syst = "Nominal"
TDirec = ""
GENnorm = 0
isMC = 1
reweightNode = "cHHH1"
runLowEvents = 0
addNodeBranch = 0 

if(reweightNode != ""):
    node = reweightNode
    # Start with file which is already a combination of the 3 NLO nodes 
    f = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted_3Nodes/Combined.root"
    # f = "{inDir}/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(inDir=inDir, year=year)
    out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted_3Nodes/".format(year=year, reweightNode=reweightNode)

    if(not os.path.isdir(out_d)):
        print("Creating output directory:",out_d)
        os.system("mkdir {out_d}".format(out_d=out_d))
        # os.system("mkdir -p {out_d}".format(out_d=out_d))
    outName = "{out_d}/GluGluToHHTo2G2Qlnu_node_{reweightNode}_{year}_{syst}.root".format(out_d=out_d, reweightNode=reweightNode, year=year, syst=syst) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards    

else:
    # Start with files with reweight branches for combining 
    d = "/eos/user/p/pmandrik/HHWWgg_central/January_2021_Production_v2/{year}/Signal/SL_NLO_{year}_hadded/".format(year=year)
    f = "{d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}.root".format(d=d, node=node, year=year)
    out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted_3Nodes/{node}/".format(year=year, node=node)
    if(not os.path.isdir(out_d)):
        print("Creating output directory:",out_d)
        os.system("mkdir -p {out_d}".format(out_d=out_d))            
    outName = "{out_d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}_{syst}.root".format(out_d=out_d, node=node, year=year, syst=syst) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards




outFile = ROOT.TFile(outName, "RECREATE")
print("outName:",outName)

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

if(reweightNode != ""):
    treeNode = "All_NLO_{year}_Normalized".format(year=year) 
else:
    treeNode = node



treeToProcess = "GluGluToHHTo2G2Qlnu_node_{treeNode}_13TeV_HHWWggTag_0".format(treeNode=treeNode)


print("treeToProcess:",treeToProcess)
for t_i, treeName in enumerate(treeNames): 
    kname = treeName.GetName()
    # check current tree 
    if(kname == treeToProcess):
        print("Found tree to process: {kname}".format(kname=kname))

        treeInfo = kname.split('_')
        NumTreeKeys = len(treeInfo)


        if(reweightNode != ""):
            if(NumTreeKeys == 9):
                syst = "Nominal"
            elif(NumTreeKeys == 10):
                syst = treeInfo[-1]
            else:
                raise Exception("Number of keys in tree name is {NumTreeKeys} -- do not know how to handle that.".format(NumTreeKeys=NumTreeKeys))

        else:
            if(NumTreeKeys == 6):
                syst = "Nominal"
            elif(NumTreeKeys == 7):
                syst = treeInfo[-1]
            else:
                raise Exception("Number of keys in tree name is {NumTreeKeys} -- do not know how to handle that.".format(NumTreeKeys=NumTreeKeys)) 

        if(TDirec != ""): fullTreePath = "%s/%s"%(TDirec, kname)
        else: fullTreePath = kname

        inTree = inFile.Get(fullTreePath)   
        outFile.cd()
        print("reweightNode:",reweightNode)
        if(reweightNode != ""):
            Reweight(inTree, kname, year, runLowEvents, Norm, reweightNode, addNodeBranch) # reweight already combined sample 
        else: # add variables 
            addVariables(inTree, kname, year, runLowEvents, Norm, reweightNode, isMC)    
        
outFile.Close() 
print("DONE")