"""
9 November 2021 
Abraham Tishelman-Charny 

The purpose of this module is to combine NLO samples while maintaining normalization, in order to use for reweighting to additional EFT benchmarks for HIG-21-014. 

Checks: 
Sum of weights / puweight combining samples for 2017 is: 0.17646497
Summing avg gen weight for the 4 samples: 0.17719645419
Difference would come from scale factors 
"""

import ROOT 
from array import array 
from addVariables import addVariables 

# Normalization factor per sample (Semileptonic)
def GetNorm(year, node):

    Sum_2016 = (24041.67591 + 10263.27003 + 4392.211129 + 31501.80227)
    Sum_2017 = (21264.42409 + 10588.6642 + 4413.499586 + 17686.79584)
    Sum_2018 = (21358.25083 + 9564.085541 + 3331.597595 + 18889.14688)

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
    print("Starting module")

    lowEvents = 1

    years = ["2016", "2017", "2018"]

    years = ["2017"]
    nodes = ["cHHH0", "cHHH1", "cHHH2p45", "cHHH5"]

    for year in years:
        print("year:",year)
        d = "/eos/user/p/pmandrik/HHWWgg_central/January_2021_Production_v2/{year}/Signal/SL_NLO_{year}_hadded/".format(year=year)
        for node in nodes:
            print("node:",node)
            # Define file paths 
            f = "{d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}.root".format(d=d, node=node, year=year)
            out_d = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/".format(year=year)

            outName = "{out_d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}.root".format(out_d=out_d, node=node, year=year)
            outFile = ROOT.TFile(outName, "RECREATE")
            inFile = ROOT.TFile(f,"READ")
            inDir = inFile.Get("tagsDumper/trees")    

            treeNames = inDir.GetListOfKeys()

            Norm = GetNorm(year, node)
            print("Norm:",Norm)

            for t_i, treeName in enumerate(treeNames): 
                if(t_i > 0): 
                    print("STOPPING after one tree on purpose")
                    break 

                kname = treeName.GetName() 
                fullTreePath = "tagsDumper/trees/%s"%(kname)
                inTree = inFile.Get(fullTreePath)        
                outFile.cd()
                addVariables(inTree, kname, year, lowEvents, Norm)

                # # Loop events 
                # for i in range(0, nentries):
                #     if(i%5000==0): print("On event:",i,"out of",int(nentries))
                #     inTree.GetEntry(i) 

                #     # Update weight branch based on normalization factor for file 
                #     Normed_weight = float(inTree.weight) * float(Norm)
                #     weight[0] = Normed_weight

                #     # Add DNN input variables here 
                #     outFile.cd()

                    # outTree.Fill() # Fill branches for each entry        

                # outTree.Write()

            outFile.Close()        
