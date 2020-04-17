########################################################################################################################
# Abe Tishelman-Charny
# 17 April 2020
#
# Definitions to be used by Make_Fragments.py
########################################################################################################################

# Check arguments for inconsistencies 
def ArgChecks(args):
    if(not args.NMSSM and not args.EFT):
        print"[Make_Fragments - ERROR]: Need to create either NMSSM or EFT fragments"
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1)     

    if(args.NMSSM and args.EFT):
        print"[Make_Fragments - ERROR]: Need to create either NMSSM or EFT fragments, not both"
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1)   

    if(args.NMSSM and args.gridpacks == ""):
        print"[Make_Fragments - ERROR]: If you want to produce NMSSM fragments, you need to provide a comma separated list of gridpacks"
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1)         

    if(args.NMSSM and args.massPairs==""):
        print"[Make_Fragments - ERROR]: If you want to produce NMSSM fragments, you need to provide a comma separated list of mass points"
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1) 

    if(args.NMSSM) and len(args.massPairs.split(','))%2 != 0:
        print"[Make_Fragments - ERROR]: If you want to produce NMSSM fragments, your mass points must be a multiple of 2 as they are used as pairs"
        print"[Make_Fragments - ERROR]: length of mass pairs:",len(args.massPairs.split(','))
        print"[Make_Fragments - ERROR]: length of mass pairs mod 2:",len(args.massPairs.split(','))%2
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1)         

# Get NMSSM mass pairs from single string of masses 
def GetMassPairs(massPairs,massPairsString):
    onFirst, onSecond = 0, 0
    massPair = []
    for im,mass in enumerate(massPairsString.split(',')):
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

# Resonant gridpacks for different mass points 
# def ResGridpacks():
# Radion gridpacks for different mass points 
# gridpacks = ['/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M260/v1/Radion_hh_narrow_M260_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M270/v1/Radion_hh_narrow_M270_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.6.0/GluGluToRadionToHH_M280/v1/GluGluToRadionToHH_M280_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M300/v1/Radion_hh_narrow_M300_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/GluGluToRadionToHH_M320/v1/GluGluToRadionToHH_M320_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M350/v1/Radion_hh_narrow_M350_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M400/v1/Radion_hh_narrow_M400_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M450/v1/Radion_hh_narrow_M450_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M500/v1/Radion_hh_narrow_M500_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M550/v1/Radion_hh_narrow_M550_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M600/v1/Radion_hh_narrow_M600_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M650/v1/Radion_hh_narrow_M650_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M700/v1/Radion_hh_narrow_M700_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.6.0/GluGluToRadionToHH_M750/v1/GluGluToRadionToHH_M750_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.6.0/GluGluToRadionToHH_M800/v1/GluGluToRadionToHH_M800_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.6.0/GluGluToRadionToHH_M850/v1/GluGluToRadionToHH_M850_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M900/v1/Radion_hh_narrow_M900_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz',
# '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/Radion_hh_narrow_M1000/v1/Radion_hh_narrow_M1000_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'
# ]