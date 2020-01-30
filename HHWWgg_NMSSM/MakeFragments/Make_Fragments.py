# Abe Tishelman-Charny
# 30 January 2020
#
# The purpose of this module is to create madgraph/pythia config files for different NMSSM mass points  

import argparse
parser = argparse.ArgumentParser(description='HHWWgg_NMSSM madgraph/pythia configuration creator')
parser.add_argument('--template', type=str, help="Template to use for pythia fragment", required=True)
parser.add_argument('--Decay', type=str, help="HH decay", required=True)
parser.add_argument('--fs', type=str, help="Final state", required=True)

args = parser.parse_args()

# pythia fragment template 
template = args.template

# Titles for output file name 
diHiggsDecay = args.Decay
finalState = args.fs 

# Gridpacks to use 
gridpacks = ['/afs/cern.ch/work/a/atishelm/private/gitClones/HH_WWgg_2/HH_WWgg/HHWWgg_NMSSM/genproductions/bin/MadGraph5_aMCatNLO/NMSSM_XYH_WWgg_MX_500_MY_300_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz',
'/afs/cern.ch/work/a/atishelm/private/gitClones/HH_WWgg_2/HH_WWgg/HHWWgg_NMSSM/genproductions/bin/MadGraph5_aMCatNLO/NMSSM_XYH_WWgg_MX_700_MY_400_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz'
]

# Different mass pairs corrsesponding to gridpack list entries in order 
massPairs = [[500,300],[700,400]]

print'Number of gridpacks:',len(gridpacks)
print'Number of mass pairs:',len(massPairs)

assert len(gridpacks) == len(massPairs) # number of gridpacks must equal number of mass pairs

for ipg,gp in enumerate(gridpacks):

    massHS = str(massPairs[ipg][0]) # mass of heavy scalar
    massIS = str(massPairs[ipg][1]) # mass of intermediate scalar

    outputName = "Fragments/NMSSM_XYH_{0}_{1}_MX_{2}_MY_{3}.py".format(diHiggsDecay,finalState,massHS,massIS) # output file name 

    fragmentFile = ''
    with open(template) as file: fragmentFile = file.read() # get template 
      
    fragmentFile = fragmentFile.replace("{gridpack}",str(gp))
    fragmentFile += '\n' 

    print'Saving madgraph/pythia config file:',outputName
    with open(outputName, "w") as output:
        output.write(fragmentFile) # write output 

