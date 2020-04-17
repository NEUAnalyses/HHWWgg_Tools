########################################################################################################################
# Abe Tishelman-Charny
# 17 April 2020
#
# The purpose of this python module is to create madgraph/pythia config files for different NMSSM mass points,
# Radion/Graviton mass points, and BSM benchmark models.  
#
# Example Usage:
#
# EFT benchmarks:
# python Make_Fragments.py --template Templates/TEMPLATE_HHWWgg_qqlnu.txt --Decay WWgg --fs qqlnu --EFT --outFolder EFT
#
# NMSSM Points:
# python Make_Fragments.py --template Templates/TEMPLATE_HHWWgg_qqlnu.txt --Decay WWgg --fs qqlnu --NMSSM --outFolder HHWWgg_NMSSM --gridpacks /afs/cern.ch/work/a/atishelm/private/gitClones/HH_WWgg_2/HH_WWgg/HHWWgg_NMSSM/genproductions/bin/MadGraph5_aMCatNLO/NMSSM_XYH_WWgg_MX_500_MY_300_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz --massPairs 500,300
#
########################################################################################################################

import argparse
import os 
from Make_Fragments_Tools import * 
parser = argparse.ArgumentParser(description='Madgraph/pythia configuration creator')
parser.add_argument('--templates', type=str, default="", help="Comma separated list of templates to use for pythia fragments", required=True)
parser.add_argument('--outFolder', type=str, default="none", help="Name of output folder for fragments", required=True)
parser.add_argument('--Decay', type=str, default="", help="HH decay", required=True)
parser.add_argument('--fs', type=str, default="", help="Final state", required=True)
parser.add_argument('--gridpacks', type=str, default="", help="Comma separated string of gridpacks to use", required=False)
parser.add_argument("--NMSSM", action="store_true", default=False, help="Create Y->XH model(s)", required=False)
parser.add_argument('--massPairs', type=str, default="", help="NMSSM: Comma separated string of mass pairs to use", required=False)
parser.add_argument("--EFT", action="store_true", default=False, help="Create EFT Benchmark models", required=False)
parser.add_argument("--verbose", action="store_true", default=False, help="Extra printout statements", required=False)

args = parser.parse_args()

# Perform argument checks 
ArgChecks(args)

# pythia fragment template 
templates = args.templates.split(',')

# Titles for output file names
diHiggsDecay, finalState, outFolder = args.Decay, args.fs, args.outFolder 

# list of gridpacks 
gridpacks = []
if(args.EFT):
    # get gluon gluon fusion HH Benchmark gridpacks
    for i in range(1,13):
        gridpack = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/GF_HH_%s/v1/GF_HH_%s_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'%(str(i),str(i))
        gridpacks.append(gridpack)
    # SM point 
    gridpack = '/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/GF_HH_%s/v1/GF_HH_%s_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'%("SM","SM")
    gridpacks.append(gridpack)

elif(args.NMSSM): gridpacks = args.gridpacks.split(',')

if(args.verbose):
    print'Gridpacks to use:',gridpacks 
    print 'Number of gridpacks:',len(gridpacks)

massPairs = []
if(args.NMSSM): 
    GetMassPairs(massPairs, args.massPairs)
    assert len(gridpacks) == len(massPairs) # number of gridpacks must equal number of mass pairs
    print'Note for NMSSM: Make sure your mass pairs and gridpacks are in the order you want'

# Create output directory if it doesn't exist 
outDirFull = os.getcwd() + "/Fragments/" + outFolder
if not os.path.exists(outDirFull):
    os.mkdir(outDirFull)

for it, template in enumerate(templates):
    for igp,gp in enumerate(gridpacks):
        outputName, fragmentFile = '','' 
        with open(template) as file: fragmentFile = file.read() # get template 

        # Choose output name based on choice to produce NMSSM or EFT 
        if(args.NMSSM):
            massHS = str(massPairs[igp][0]) # mass of heavy scalar
            massIS = str(massPairs[igp][1]) # mass of intermediate scalar

            if(args.verbose):
                print 
                print'Make sure this is the correct gridpack / mass pair combination:'
                print 
                print'Gridpack:',gp 
                print'Masses:',massHS,',',massIS
                print 
            outputName = "Fragments/{0}/NMSSM_XYH_{1}_{2}_MX_{3}_MY_{4}.py".format(outFolder,diHiggsDecay,finalState,massHS,massIS) # output file name 

        elif(args.EFT):
            BMnum = str(igp)
            if(igp==12): BMnum = "SM"
            outputName = "Fragments/{0}/GluGluToHHTo_{1}_{2}_node_{3}.py".format(outFolder,diHiggsDecay,finalState,BMnum) # output file name 

        fragmentFile = fragmentFile.replace("{gridpack}",str(gp))
        fragmentFile += '\n' 

        print'Saving madgraph/pythia config file:',outputName
        with open(outputName, "w") as output:
            output.write(fragmentFile) # write output 
