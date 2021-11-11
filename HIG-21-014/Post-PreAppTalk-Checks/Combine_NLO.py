"""
9 November 2021 
Abraham Tishelman-Charny 

The purpose of this module is to combine NLO samples while maintaining normalization, in order to use for reweighting to additional EFT benchmarks for HIG-21-014. 

Example Commands:
python Combine_NLO.py --node cHHH1 --year 2017 --runLowEvents --syst Nominal 
python Combine_NLO.py --node cHHH1 --year 2017 --runLowEvents --syst MvaShiftUp01sigma

"""

import argparse 

# export PYTHONPATH=$CERNBOX_HOME/.local/lib/python3.8/site-packages:$PYTHONPATH

import ROOT 
from array import array 
from addVariables import addVariables 

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
    print("Starting Combine_NLO.py module")
    # input arguments 
    parser =  argparse.ArgumentParser()
    parser.add_argument('--node', default = "cHHH1", required=False, type=str, help = "Node to run")
    parser.add_argument('--year', default = "2017", required=False, type=str, help = "Year to run")
    parser.add_argument('--runLowEvents', action="store_true", required=False, help = "Run on a low number of events (for testing)")
    # parser.add_argument('--runSystematicsTrees', action="store_true", required=False, help = "Run on all systematics trees (necessary for final results)")
    parser.add_argument('--syst', default = "Nominal", required=False, type=str, help = "Systematic tree to process")
    args = parser.parse_args()
    arguments = ["runLowEvents", "year", "node", "syst"]
    print("=====")
    for a in arguments: 
        exec("{a} = args.{a}".format(a=a))
        print("{a}:".format(a=a),a)
    print("=====")
    d = "/eos/user/p/pmandrik/HHWWgg_central/January_2021_Production_v2/{year}/Signal/SL_NLO_{year}_hadded/".format(year=year)
    f = "{d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}.root".format(d=d, node=node, year=year)
    out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{node}/".format(year=year, node=node)
    outName = "{out_d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}_{syst}.root".format(out_d=out_d, node=node, year=year, syst=syst) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards
    outFile = ROOT.TFile(outName, "RECREATE")
    inFile = ROOT.TFile(f,"READ")
    inDir = inFile.Get("tagsDumper/trees")    
    treeNames = inDir.GetListOfKeys()
    Norm = GetNorm(year, node)
    print("Norm:",Norm)
    # find tree that this job is meant to process
    # expecting tree name format:
    # nominal tree:    GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0
    # Systematic tree: GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0_<systematic>    
    if(syst == "Nominal"):
        treeToProcess = "GluGluToHHTo2G2Qlnu_node_{node}_13TeV_HHWWggTag_0".format(node=node)
    else:
        treeToProcess = "GluGluToHHTo2G2Qlnu_node_{node}_13TeV_HHWWggTag_0_{syst}".format(node=node, syst=syst)    

    for t_i, treeName in enumerate(treeNames): 
        kname = treeName.GetName()

        # check current tree 
        if(kname == treeToProcess):
            print("Found tree to process: {kname}".format(kname=kname))

            # if((t_i > 0) and (not runSystematicsTrees)):
            #     print("input argument runSystematicsTrees set to:",runSystematicsTrees)
            #     print("STOPPING after one input tree")
            #     break 

            treeInfo = kname.split('_')
            NumTreeKeys = len(treeInfo)
            if(NumTreeKeys == 6):
                syst = "Nominal"
            elif(NumTreeKeys == 7):
                syst = treeInfo[-1]
            else:
                raise Exception("Number of keys in tree name is {NumTreeKeys} -- do not know how to handle that.".format(NumTreeKeys=NumTreeKeys))

            fullTreePath = "tagsDumper/trees/%s"%(kname)
            inTree = inFile.Get(fullTreePath)        
            outFile.cd()
            addVariables(inTree, kname, year, runLowEvents, Norm)
        else: continue # do not process this tree 
    outFile.Close()        
