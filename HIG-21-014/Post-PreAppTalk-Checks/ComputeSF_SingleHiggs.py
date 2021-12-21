"""
15 December 2021 
Abraham Tishelman-Charny 

Doing this quickly

Usage: python3 ComputeSF.py 

"""

import argparse 
import uproot 
import numpy as np 
import os 
import pickle 
from SystematicTreeNames import GetSystLabels


# VH 2016 odd nominal 
# ************************
# *    Row   *    weight *
# ************************
# *        0 * 9.503e-05 *
# *        1 * 9.712e-05 *
# *        2 * 0.0001046 *
# *        3 * 0.0001038 *
# *        4 * 9.471e-05 *
# *        5 * 8.862e-05 *
# *        6 * 9.698e-05 *
# *        7 * 0.0001038 *
# *        8 * -9.72e-05 *
# *        9 * -0.000105 *
# *       10 * 8.377e-05 *
# *       11 * 9.709e-05 *
# *       12 * 9.000e-05 *
# *       13 * 6.589e-05 *
# *       14 * 2.383e-07 *
# *       15 * 9.422e-05 *
# *       16 * 9.421e-05 *
# *       17 * 9.705e-05 *
# *       18 * 9.189e-05 *
# *       19 * 9.277e-05 *
# *       20 * 8.984e-05 *
# *       21 * 9.709e-05 *
# *       22 * 0.0001138 *
# *       23 * -4.65e-07 *
# *       24 * 7.960e-05 *

##-- VH 2016 even 
# ************************
# *    Row   *    weight *
# ************************
# *        0 * 8.900e-05 *
# *        1 * 9.570e-05 *
# *        2 * 2.432e-06 *
# *        3 * 9.456e-05 *
# *        4 * -9.23e-05 *
# *        5 * 0.0001066 *
# *        6 * 9.344e-05 *
# *        7 * -9.25e-05 *
# *        8 * 0.0001013 *
# *        9 * 0.0001008 *
# *       10 * 9.360e-05 *
# *       11 * 8.292e-05 *
# *       12 * 9.988e-05 *
# *       13 * 0.0001077 *
# *       14 * 9.795e-05 *
# *       15 * 9.150e-05 *
# *       16 * -9.21e-05 *
# *       17 * 9.085e-05 *
# *       18 * 1.900e-05 *
# *       19 * 8.966e-05 *
# *       20 * 9.127e-05 *
# *       21 * 7.831e-05 *
# *       22 * 9.238e-05 *
# *       23 * -9.16e-05 *
# *       24 * 9.126e-05 *


# parser = argparse.ArgumentParser()
# parser.add_argument("--nodes", type=str, default="1", help = "Comma separated string of nodes to run over")
# args = parser.parse_args()

# check 
# 2016 VH 
# full: 0.24460690
# even: 0.12403186
# odd: 0.12057506

# even SF: 1.9721304537829765
# odd SF: 2.0286685249994703

# looks good 

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

    fileNames =[

        "VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2",
        "ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2",

        "VHToGG_2017_HHWWggTag_0_MoreVars_v2",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2",

        "VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2",
        "ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2"
    ]

    H_Y_Direc_dict = {
        "VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "VH_2016",
        "ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "ttH_2016",

        "VHToGG_2017_HHWWggTag_0_MoreVars_v2" : "VH_2017",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2" : "ttH_2017",

        "VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2" : "VH_2018",
        "ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2" : "ttH_2018"
    }

    SingleHiggsTreeDict = {
        "VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "wzh_125_13TeV_HHWWggTag_0",
        "ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "tth_125_13TeV_HHWWggTag_0",

        "VHToGG_2017_HHWWggTag_0_MoreVars_v2" : "wzh_125_13TeV_HHWWggTag_0",
        "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2" : "tth_125_13TeV_HHWWggTag_0",

        "VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2" : "wzh_125_13TeV_HHWWggTag_0",
        "ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2" : "tth_125_13TeV_HHWWggTag_0"            
    }    

     

    ScaleFactors = {} # dictionary to save all SF values 

    for fileName in fileNames:
        print("fileName:",fileName)
        H_Y_Direc = H_Y_Direc_dict[fileName]   

        if("2016" in fileName): year = "2016"
        if("2017" in fileName): year = "2017"
        if("2018" in fileName): year = "2018"
        
        systLabels = GetSystLabels(year)        

        verbose = 1 
        systLabels = GetSystLabels(year)
        nSyst = len(systLabels)

        #d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/".format(year=year)
        d = "/eos/user/c/chuw/ForAbe/Single_H_hadded/"

        # for each node, open combined file 
        f_all = "{d}/{fileName}.root".format(d=d, fileName=fileName)
        f_all_ur = uproot.open(f_all)
        for syst_i, syst in enumerate(systLabels):
            # if(verbose): print("syst:",syst)
            if(syst_i%10 == 0): print("On systematic %s / %s"%(syst_i, nSyst))
            if(syst == "Nominal"):
                systLabel = ""
            else:
                systLabel = "_{syst}".format(syst=syst)

            # if(syst_i >= 3): 
                # continue

            f_even = "{d}/{H_Y_Direc}_even/{fileName}_{syst}_even.root".format(d=d, H_Y_Direc=H_Y_Direc, fileName=fileName, syst=syst)
            f_odd = "{d}/{H_Y_Direc}_odd/{fileName}_{syst}_odd.root".format(d=d, H_Y_Direc=H_Y_Direc, fileName=fileName, syst=syst)

            f_even_ur = uproot.open(f_even)
            f_odd_ur = uproot.open(f_odd)

            nonSystTreePath = SingleHiggsTreeDict[fileName]

            if(syst == "Nominal"):
                systExt = "v1"
            else:
                systExt = "%s_v1"%(syst)

            t = "%s_%s"%(nonSystTreePath, systExt)

            weight_sum_all = np.sum(f_all_ur[t]["weight"].array())

            # if key not found, reproduce systematic tree 

            weight_sum_even = np.sum(f_even_ur[t]["weight"].array())
            weight_sum_odd = np.sum(f_odd_ur[t]["weight"].array())

            even_SF = float(weight_sum_all) / float(weight_sum_even) 
            odd_SF = float(weight_sum_all) / float(weight_sum_odd)

            exec("ScaleFactors['{fileName}_{syst}_even'] = even_SF".format(fileName=fileName, syst=syst))
            exec("ScaleFactors['{fileName}_{syst}_odd'] = odd_SF".format(fileName=fileName, syst=syst))

            del f_even 
            del f_odd 
            del f_even_ur 
            del f_odd_ur 

    print("ScaleFactors:",ScaleFactors)

    pickle.dump( ScaleFactors, open( "SingleHiggsEvenOddScaleFactors.p", "wb" ))

    print("DONE")

