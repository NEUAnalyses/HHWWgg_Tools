"""
9 November 2021 
Abraham Tishelman-Charny 

The purpose of this module is to combine NLO samples while maintaining normalization, in order to use for reweighting to additional EFT benchmarks for HIG-21-014. 

Example Commands:

# Combine NLO samples 
python Reweight_NLO.py --node cHHH1 --year 2017 --runLowEvents --syst Nominal 
python Reweight_NLO.py --node cHHH1 --year 2017 --runLowEvents --syst MvaShiftUp01sigma

# Reweight to a node 
python Reweight_NLO.py --reweightNode cttHH3 --syst Nominal --runLowEvents --TDirec ""

# Categorize by DNN score 
python Reweight_NLO.py --reweightNode cttHH0p35 --syst Nominal  --TDirec "" --runLowEvents --categorize

"""

import argparse 

# export PYTHONPATH=$CERNBOX_HOME/.local/lib/python3.8/site-packages:$PYTHONPATH

import ROOT 
import os 
from array import array 
from Reweight_Tools import addVariables, Reweight, Categorize

# Normalization factor per sample (Semileptonic)
def GetNorm(year, node):

    # sum of gen weights from flashgg catalogues
    Sum_2016 = (24041.67591 + 10263.27003 + 4392.211129 + 31501.80227)
    Sum_2017 = (21264.42409 + 10588.6642 + 4413.499586 + 17686.79584)
    Sum_2018 = (21358.25083 + 9564.085541 + 3331.597595 + 18889.14688)

    # For semileptonic case 
    NormVals = {
        "2016" : {
                    "cHHH0" : 24041.67591 / Sum_2016,
                    "cHHH1" : 10263.27003 / Sum_2016, 
                    "cHHH2p45" : 4392.211129 / Sum_2016, 
                    "cHHH5" : 31501.80227 / Sum_2016
        },

        "2017" : {
                    "cHHH0" : 21264.42409 / Sum_2017,
                    "cHHH1" : 10588.6642 / Sum_2017,
                    "cHHH2p45" : 4413.499586 / Sum_2017,
                    "cHHH5" : 17686.79584 / Sum_2017
        },

        "2018" : {
                    "cHHH0" : 21358.25083 / Sum_2018,
                    "cHHH1" : 9564.085541 / Sum_2018,
                    "cHHH2p45" : 3331.597595 / Sum_2018,
                    "cHHH5" : 18889.14688 / Sum_2018
        }
    }

    return float(NormVals[year][node]) 

if __name__ == '__main__':
    print("Starting Reweight_NLO.py module")
    # input arguments 
    parser =  argparse.ArgumentParser()
    parser.add_argument('--node', default = "cHHH1", required=False, type=str, help = "Input Node to run")
    parser.add_argument('--year', default = "2017", required=False, type=str, help = "Year to run")
    parser.add_argument('--runLowEvents', action="store_true", required=False, help = "Run on a low number of events (for testing)")
    parser.add_argument('--categorize', action="store_true", required=False, help = "Split trees into categories based on DNN score")
    parser.add_argument('--syst', default = "Nominal", required=False, type=str, help = "Systematic tree to process")
    parser.add_argument('--reweightNode', default = "", required=False, type=str, help = "Node to reweight to, e.g. (updates weight branch)")
    parser.add_argument('--TDirec', default = "tagsDumper/trees", required=False, type=str, help = "TDirectory strucuture of input root file")
    parser.add_argument('--DNN_direc', default = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/", type=str, help = "Directory containing output files with DNN scores.")
    parser.add_argument('--GENnorm', action="store_true", required=False, help = "Normalize weight branch based on relative GEN sums")
    args = parser.parse_args()
    arguments = ["node", "year", "runLowEvents", "syst", "reweightNode", "TDirec", "GENnorm", "categorize", "DNN_direc"]
    print("=====")
    for a in arguments: 
        exec("{a} = args.{a}".format(a=a))
        print("{a}:".format(a=a),eval(a))
    print("=====")
    
    if(categorize):
        node = reweightNode
        # Start with reweighted file 
        d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{reweightNode}/".format(year=year, reweightNode=reweightNode)
        f = "{d}/GluGluToHHTo2G2Qlnu_node_{reweightNode}_{year}.root".format(d=d, year=year, reweightNode=reweightNode, syst=syst)  
        out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{reweightNode}_trees_categorized/".format(year=year, reweightNode=reweightNode)
        if(not os.path.isdir(out_d)):
            print("Creating output directory:",out_d)
            os.system("mkdir -p {out_d}".format(out_d=out_d))
        outName = "{out_d}GluGluToHHTo2G2Qlnu_node_{reweightNode}_{year}_{syst}_Categorized.root".format(out_d=out_d, reweightNode=reweightNode, year=year, syst=syst) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards          
    else:
        if(reweightNode != ""):
            node = reweightNode
            # Start with file which is already a combination of the 4 NLO nodes 
            # DNN_direc 
            f = "{DNN_direc}/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(DNN_direc=DNN_direc, year=year)
            out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{reweightNode}_trees/".format(year=year, reweightNode=reweightNode)
            if(not os.path.isdir(out_d)):
                print("Creating output directory:",out_d)
                os.system("mkdir -p {out_d}".format(out_d=out_d))
            outName = "{out_d}/GluGluToHHTo2G2Qlnu_node_{reweightNode}_{year}_{syst}.root".format(out_d=out_d, reweightNode=reweightNode, year=year, syst=syst) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards    

        else:
            # Start with files with reweight branches for combining 
            d = "/eos/user/p/pmandrik/HHWWgg_central/January_2021_Production_v2/{year}/Signal/SL_NLO_{year}_hadded/".format(year=year)
            f = "{d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}.root".format(d=d, node=node, year=year)
            out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{node}/".format(year=year, node=node)
            outName = "{out_d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}_{syst}.root".format(out_d=out_d, node=node, year=year, syst=syst) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards

    outFile = ROOT.TFile(outName, "RECREATE")
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

    # find tree that this job is meant to process
    # expecting tree name format:
    # nominal tree:    GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0
    # Systematic tree: GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0_<systematic>    

    # Combined file:
    # GluGluToHHTo2G2Qlnu_node_All_NLO_2017_Normalized_13TeV_HHWWggTag_0

    if(categorize):
        treeNode = node 
    else:
        if(reweightNode != ""):
            treeNode = "All_NLO_{year}_Normalized".format(year=year) 
        else:
            treeNode = node
    
    if(categorize):
        if(syst == "Nominal"):
            treeToProcess = "GluGluToHHTo2G2Qlnu_node_{treeNode}_{year}_13TeV_HHWWggTag_0".format(treeNode=treeNode, year=year)
        else: 
            treeToProcess = "GluGluToHHTo2G2Qlnu_node_{treeNode}_{year}_13TeV_HHWWggTag_0_{syst}".format(treeNode=treeNode, year=year, syst=syst)
    else:
        if(syst == "Nominal"):
            treeToProcess = "GluGluToHHTo2G2Qlnu_node_{treeNode}_13TeV_HHWWggTag_0".format(treeNode=treeNode)
        else:
            treeToProcess = "GluGluToHHTo2G2Qlnu_node_{treeNode}_13TeV_HHWWggTag_0_{syst}".format(treeNode=treeNode, syst=syst)   


    print("treeToProcess:",treeToProcess)

    for t_i, treeName in enumerate(treeNames): 
        kname = treeName.GetName()
        # check current tree 
        if(kname == treeToProcess):
            print("Found tree to process: {kname}".format(kname=kname))

            treeInfo = kname.split('_')
            NumTreeKeys = len(treeInfo)

            # already combined files have a different number of underscores in the tree name 
            if(categorize):
                if(reweightNode != ""):
                    if(NumTreeKeys == 7):
                        syst = "Nominal"
                    elif(NumTreeKeys == 8):
                        syst = treeInfo[-1]
                    else:
                        raise Exception("Number of keys in tree name is {NumTreeKeys} -- do not know how to handle that.".format(NumTreeKeys=NumTreeKeys))                
            else:
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
            if(categorize):
                Categorize(inTree, kname, year, runLowEvents, Norm, reweightNode)
            else:
                if(reweightNode != ""):
                    Reweight(inTree, kname, year, runLowEvents, Norm, reweightNode)    
                else: 
                    addVariables(inTree, kname, year, runLowEvents, Norm, reweightNode)                 
                
        else: continue # do not process this tree 
    outFile.Close()        
