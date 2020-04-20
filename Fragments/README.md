# Fragments

This directory is used to combine pythia fragments with MadGraph gridpacks. 


## Example Usage

The main module is Make_Fragments.py. Here are example commands to produce fragments for Radion / Graviton resonance, EFT benchmarks, and NMSSM points:

Resonant Points:

    python Make_Fragments.py --template Templates/Resonant_EFT/TEMPLATE_HHWWgg_qqlnu.txt --Decay WWgg --fs qqlnu --Resonant --outFolder TestResonant --masses 260,750

EFT benchmarks:

    python Make_Fragments.py --template Templates/Resonant_EFT/TEMPLATE_HHWWgg_qqlnu.txt --Decay WWgg --fs qqlnu --EFT --outFolder Test_EFT

NMSSM Points:

    python Make_Fragments.py --template Templates/TEMPLATE_HHWWgg_qqlnu.txt --Decay WWgg --fs qqlnu --NMSSM --outFolder HHWWgg_NMSSM --gridpacks /afs/cern.ch/work/a/atishelm/private/gitClones/HH_WWgg_2/HH_WWgg/HHWWgg_NMSSM/genproductions/bin/MadGraph5_aMCatNLO/NMSSM_XYH_WWgg_MX_500_MY_300_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz --masses 500,300

If everything works properly, you should find your fragments in HHWWgg_Tools/Fragments/Outputs/<outFolder>

## NMSSM 

. The python module used for pythia fragment production is HHWWgg_Tools/Fragments/Make_Fragments.py:

    cd HHWWgg_Tools/Fragments

In order to create a Madgraph / pythia fragment, you need to have a template in MakeFragments/Templates. This should have a spot for the gridpack path: '{gridpack}', and the decays for the Higgs (pdgid 25) and intermediate scalar (pdgid 35). You can find some examples in the Templates folder. 

The gridpacks you would like to match with pythia fragments need to be specified in Make_Fragments.py, the main python module of the folder. You also need to specify the mass pairs, which should correspond to the gridpacks in order. As long as these are set and your template is available in the Templates directory, you can run following this example:

    cd HHWWgg_Tools/Fragments
    python Make_Fragments.py --template Templates/TEMPLATE_HHWWgg_qqlnu.txt --Decay WWgg --fs qqlnu --NMSSM --outFolder HHWWgg_NMSSM --gridpacks /afs/cern.ch/work/a/atishelm/private/gitClones/HH_WWgg_2/HH_WWgg/HHWWgg_NMSSM/genproductions/bin/MadGraph5_aMCatNLO/NMSSM_XYH_WWgg_MX_500_MY_300_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz --masses 500,300

if this works properly, this will produce a madgraph/pythia configuration file, output to Fragments/Outputs/HHWWgg_NMSSM. 