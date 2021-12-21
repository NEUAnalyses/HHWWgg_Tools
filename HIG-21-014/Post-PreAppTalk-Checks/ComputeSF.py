"""
22 November 2021 
Abraham Tishelman-Charny 

The purpose of this module is to compute the ratio of sum(weights even/odd) / sum(even + odd weights) in order to derive 
scale factors to apply to even and odd samples, in order to properly normalize samples to be used for training 
and signal modeling for HIG-21-014. 

Usage: python3 ComputeSF.py 

"""

import argparse 
import uproot 
import numpy as np 
import os 
import pickle 
from SystematicTreeNames import GetSystLabels

# Cannot Find: /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted//12_trees_even/GluGluToHHTo2G2Qlnu_node_12_2017_SigmaEOverEShiftUp01sigma_Even.root
# Cannot Find: /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted//12_trees_odd/GluGluToHHTo2G2Qlnu_node_12_2017_SigmaEOverEShiftUp01sigma_Odd.root
# Cannot Find: /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted//20_trees_odd/GluGluToHHTo2G2Qlnu_node_20_2017_Nominal_Odd.root

parser = argparse.ArgumentParser()
parser.add_argument("--nodes", type=str, default="1", help = "Comma separated string of nodes to run over")
args = parser.parse_args()

nodes = args.nodes.split(',')

# a function used to find missing files in a directory (useful for finding failed jobs without having to go through error/output/log files)
def FindMissingSyst(nodes, d, systLabels):
    
    for node in nodes:
        for syst in systLabels:
            f_even = "{d}/{node}_trees_even/GluGluToHHTo2G2Qlnu_node_{node}_{year}_{syst}_Even.root".format(d=d, node=node, year=year, syst=syst)
            f_odd = "{d}/{node}_trees_odd/GluGluToHHTo2G2Qlnu_node_{node}_{year}_{syst}_Odd.root".format(d=d, node=node, year=year, syst=syst)
            isFile_e = os.path.isfile(f_even)
            isFile_o = os.path.isfile(f_odd)

            if(not isFile_e): print("Cannot Find:",f_even)
            if(not isFile_o): print("Cannot Find:",f_odd)

# main function 
if (__name__ == '__main__'):

    # brokenNodes = ["12", "20"]
    brokenNodes = []

    verbose = 1 
    year = "2017"
    systLabels = GetSystLabels(year)
    nSyst = len(systLabels)
    # nodes = [1]
    #nodes = [i for i in range(1,21)]

    for brokenNode in brokenNodes:
        if(brokenNode in nodes): nodes.remove(brokenNode)

    d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/".format(year=year)

    #FindMissingSyst(nodes, d, systLabels)

    ScaleFactors = {} # dictionary to save all SF values 

    for node in nodes:
        if(verbose): print("node:",node)
        # for each node, open combined file 
        f_all = "{d}/{node}/GluGluToHHTo2G2Qlnu_node_{node}_{year}.root".format(d=d, node=node, year=year)
        f_all_ur = uproot.open(f_all)
        for syst_i, syst in enumerate(systLabels):
            # if(verbose): print("syst:",syst)
            if(syst_i%10 == 0): print("On systematic %s / %s"%(syst_i, nSyst))
            if(syst == "Nominal"):
                systLabel = ""
            else:
                systLabel = "_{syst}".format(syst=syst)
            f_even = "{d}/{node}_trees_even/GluGluToHHTo2G2Qlnu_node_{node}_{year}_{syst}_Even.root".format(d=d, node=node, year=year, syst=syst)
            f_odd = "{d}/{node}_trees_odd/GluGluToHHTo2G2Qlnu_node_{node}_{year}_{syst}_Odd.root".format(d=d, node=node, year=year, syst=syst)

            f_even_ur = uproot.open(f_even)
            f_odd_ur = uproot.open(f_odd)

            t = "GluGluToHHTo2G2Qlnu_node_{node}_{year}_13TeV_HHWWggTag_0{systLabel}".format(node=node, year=year, systLabel=systLabel)
            weight_sum_all = np.sum(f_all_ur[t]["weight"].array())

            # if key not found, reproduce systematic tree 

            weight_sum_even = np.sum(f_even_ur[t]["weight"].array())
            weight_sum_odd = np.sum(f_odd_ur[t]["weight"].array())

            even_SF = float(weight_sum_all) / float(weight_sum_even) 
            odd_SF = float(weight_sum_all) / float(weight_sum_odd)

            exec("ScaleFactors['{node}_{syst}_even'] = even_SF".format(node=node, syst=syst))
            exec("ScaleFactors['{node}_{syst}_odd'] = odd_SF".format(node=node, syst=syst))

            del f_even 
            del f_odd 
            del f_even_ur 
            del f_odd_ur 

    print("ScaleFactors:",ScaleFactors)

    pickle.dump( ScaleFactors, open( "EvenOddScaleFactors.p", "wb" ))

    print("DONE")

