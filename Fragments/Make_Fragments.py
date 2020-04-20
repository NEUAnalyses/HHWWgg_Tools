########################################################################################################################
# Abe Tishelman-Charny
# 17 April 2020
#
# The purpose of this python module is to create madgraph/pythia config files for Radion/Graviton mass points, 
# NMSSM mass points, and EFT benchmark models.  
#
# Example Usage:
#
# Resonant Points:
# python Make_Fragments.py --template Templates/Resonant_EFT/TEMPLATE_HHWWgg_qqlnu.txt --diHiggsDecay WWgg --fs qqlnu --Resonant --outFolder TestResonant --masses 260,750
#
# EFT benchmarks:
# python Make_Fragments.py --template Templates/Resonant_EFT/TEMPLATE_HHWWgg_qqlnu.txt --diHiggsDecay WWgg --fs qqlnu --EFT --outFolder Test_EFT
#
# NMSSM Points:
# python Make_Fragments.py --template Templates/NMSSM/TEMPLATE_HHWWgg_qqlnu.txt --diHiggsDecay WWgg --fs qqlnu --NMSSM --outFolder HHWWgg_NMSSM --gridpacks /afs/cern.ch/work/a/atishelm/private/gitClones/HH_WWgg_2/HH_WWgg/HHWWgg_NMSSM/genproductions/bin/MadGraph5_aMCatNLO/NMSSM_XYH_WWgg_MX_500_MY_300_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz --masses 500,300
#
########################################################################################################################

import argparse
import os 
from Make_Fragments_Tools import * 
parser = argparse.ArgumentParser(description='Madgraph/pythia configuration creator')
parser.add_argument('--templates', type=str, default="", help="Comma separated list of templates to use for pythia fragments", required=True)
parser.add_argument('--outFolder', type=str, default="none", help="Name of output folder for fragments", required=True)
parser.add_argument('--diHiggsDecay', type=str, default="", help="HH decay", required=True)
parser.add_argument('--fs', type=str, default="", help="Final state", required=True)
parser.add_argument('--gridpacks', type=str, default="", help="Comma separated string of gridpacks to use", required=False)
parser.add_argument("--Resonant", action="store_true", default=False, help="Create Radion/Graviton model", required=False)
parser.add_argument("--NMSSM", action="store_true", default=False, help="Create Y->XH model(s)", required=False)
parser.add_argument("--EFT", action="store_true", default=False, help="Create EFT Benchmark models", required=False)
parser.add_argument('--masses', type=str, default="", help="Resonant or NMSSM: Comma separated string of mass pairs to use.", required=False)
parser.add_argument("--verbose", action="store_true", default=False, help="Extra printout statements", required=False)

args = parser.parse_args()

# Perform argument checks 
ArgChecks(args)

# pythia fragment template 
templates = args.templates.split(',')
masses = args.masses.split(',')

# Titles for output file names
diHiggsDecay, finalState, outFolder = args.diHiggsDecay, args.fs, args.outFolder 

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

elif(args.NMSSM): 
    gridpacks = args.gridpacks.split(',')
    # for igp,gridpack in enumerate(gridpacks): 
        # shortGridpack = gridpack.split('/')[-1]
        # gridpacks[igp] = shortGridpack

elif(args.Resonant):
    # get gluon gluon fusion Radion gridpack for mass point 
    for resMass in masses:
        gridpack = GetResGridpack(resMass) 
        gridpacks.append(gridpack)

if(args.verbose):
    print'[Make_Fragments.py: VERBOSE] - Gridpacks to use:',gridpacks 
    print'[Make_Fragments.py: VERBOSE] - Number of gridpacks:',len(gridpacks)

massPairs = []
if(args.NMSSM): 
    massPairs = GetMassPairs(massPairs, masses)
    assert len(gridpacks) == len(massPairs) # number of gridpacks must equal number of mass pairs
    print'Note for NMSSM: Make sure your mass pairs and gridpacks are in the order you want'

resMasses = []
if(args.Resonant): 
    for m in masses: resMasses.append(m) 

# Create output directory if it doesn't exist 
outDirFull = os.getcwd() + "/Outputs/" + outFolder
if not os.path.exists(outDirFull):
    os.mkdir(outDirFull)

for it, template in enumerate(templates):
    for igp,gp in enumerate(gridpacks):
        outputName, fragmentFile = '','' 
        with open(template) as file: fragmentFile = file.read() # get template 

        # Define output name based on choice to produce NMSSM or EFT 
        if(args.NMSSM):
            massHS = str(massPairs[igp][0]) # mass of heavy scalar
            massIS = str(massPairs[igp][1]) # mass of intermediate scalar

            if(args.verbose):
                print'[Make_Fragments.py: VERBOSE]'
                print 
                print'Make sure this is the correct gridpack / mass pair combination:'
                print 
                print'Gridpack:',gp 
                print'Masses:',massHS,',',massIS
                print 
                print'[Make_Fragments.py: VERBOSE]'
            outputName = "Outputs/{0}/NMSSM_XYH{1}{2}_MX{3}_MY{4}.py".format(outFolder,diHiggsDecay,finalState,massHS,massIS) # output file name 

        elif(args.EFT):
            BMnum = str(igp)
            if(igp==12): BMnum = "SM"
            outputName = "Outputs/{0}/GluGluToHHTo_{1}_{2}_node{3}.py".format(outFolder,diHiggsDecay,finalState,BMnum) # output file name 

        elif(args.Resonant):
            bsmMass = resMasses[igp]
            print'res mass:',bsmMass
            print'res gridpack:',gp 
            outputName = "Outputs/{0}/ggF_X{1}_HH{2}_{3}.py".format(outFolder,bsmMass,diHiggsDecay,finalState)

        fragmentFile = fragmentFile.replace("{gridpack}",str(gp))
        fragmentFile += '\n' 

        print'Saving madgraph/pythia config file:',outputName
        with open(outputName, "w") as output:
            output.write(fragmentFile) # write output 
