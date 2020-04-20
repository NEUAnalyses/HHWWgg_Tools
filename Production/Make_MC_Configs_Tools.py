########################################################################################################################
# Abe Tishelman-Charny
# 17 April 2020
#
# Definitions to be used by Make_MC_Configs.py 
########################################################################################################################

import os 
from os import path 

# Check arguments for inconsistencies 
def ArgChecks(args):
    steps = ["GEN", "GEN-SIM", "DR1", "DR2", "MINIAOD"]
    if(args.step not in steps):
        print"[Make_MC_Configs - ERROR]:",args.step,"is not a possible step"
        print"[Make_MC_Configs - ERROR]: Must choose one of the following steps:"
        for step in steps: print step 
        print"[Make_MC_Configs - ERROR]: Exiting"
        exit(1) 

    if(not args.Resonant and not args.EFT and not args.NMSSM):
        print"[Make_MC_Configs - ERROR]: Need to choose a type of Signal: Resonant, EFT or NMSSM"
        print"[Make_MC_Configs - ERROR]: Exiting"
        exit(1)

    if(args.Resonant + args.EFT + args.NMSSM) > 1:
        print"[Make_MC_Configs - ERROR]: Need to choose ONE type of Signal: Resonant, EFT or NMSSM"
        print"[Make_MC_Configs - ERROR]: Exiting"
        exit(1)

    if(args.Resonant or args.NMSSM) and args.masses == "":
        print"[Make_MC_Configs - ERROR]: If you are running resonant or NMSSM, you need to provide a comma separated list of mass points"
        print"[Make_MC_Configs - ERROR]: Exiting"
        exit(1) 

    if(args.EFT and args.EFT_BMs == ""):
        print"[Make_MC_Configs - ERROR]: If you are running EFT, you need to provide a comma separated list of Benchmark points to run"
        print"[Make_MC_Configs - ERROR]: Exiting"
        exit(1)         

    if(args.NMSSM and args.masses==""):
        print"[Make_Fragments - ERROR]: If you want to produce NMSSM fragments, you need to provide a comma separated list of mass points"
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1) 

    if(args.NMSSM) and len(args.masses.split(','))%2 != 0:
        print"[Make_Fragments - ERROR]: If you want to produce NMSSM fragments, your mass points must be a multiple of 2 as they are used as pairs"
        print"[Make_Fragments - ERROR]: length of mass pairs:",len(args.masses.split(','))
        print"[Make_Fragments - ERROR]: length of mass pairs mod 2:",len(args.masses.split(','))%2
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1)         

# Get NMSSM mass pairs from single string of masses 
def GetMassPairs(massPairs,massPairsString):
    onFirst, onSecond = 0, 0
    massPair = []
    for im,mass in enumerate(massPairsString):
        if(im == 0 or im%2==0): 
            onFirst, onSecond = 1, 0
        else: 
            onFirst, onSecond = 0, 1
        if(onFirst): 
            massPair = []
            massPair.append(mass)
        if(onSecond): 
            massPair.append(mass)
            massPairs.append(massPair) 
    print'NMSSM massPairs:',massPairs            
    return massPairs 

# Make sure pythia fragment exists and is in proper place before making MC_Configs entry 
# first check CMSSW 
# then check Fragments/Outputs 
def ManageFragment(expectedFragmentEnd_,fragOutDir_,ultimateFragDirec_):
    ultimateFragLoc_ = "%s/%s"%(ultimateFragDirec_,expectedFragmentEnd_)
    firstFragLoc_ = "../Fragments/Outputs/%s/%s"%(fragOutDir_,expectedFragmentEnd_)    
    if(not path.exists(ultimateFragLoc_)): 
        if(not path.exists(firstFragLoc_)):
            print'Neither fragment path exists:'
            print ultimateFragLoc_
            print firstFragLoc_
            print 'Skipping this configuration...'
            return 1 # skip 
        else: 
            os.system('cp %s %s'%(firstFragLoc_,ultimateFragLoc_)) 
            print'Copied fragment from %s to %s'%(firstFragLoc_,ultimateFragLoc_)
            return 0 # don't skip 
    else: return 0 # don't skip 