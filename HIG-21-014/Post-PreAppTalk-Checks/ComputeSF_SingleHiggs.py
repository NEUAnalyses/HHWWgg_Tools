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

