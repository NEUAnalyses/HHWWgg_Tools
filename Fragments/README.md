# Fragments

This directory is used to combine pythia fragments with MadGraph gridpacks. 



## NMSSM 

. The python module used for pythia fragment production is HHWWgg_Tools/Fragments/Make_Fragments.py:

    cd HHWWgg_Tools/Fragments

In order to create a Madgraph / pythia fragment, you need to have a template in MakeFragments/Templates. This should have a spot for the gridpack path: '{gridpack}', and the decays for the Higgs (pdgid 25) and intermediate scalar (pdgid 35). You can find some examples in the Templates folder. 



The gridpacks you would like to match with pythia fragments need to be specified in Make_Fragments.py, the main python module of the folder. You also need to specify the mass pairs, which should correspond to the gridpacks in order. As long as these are set and your template is available in the Templates directory, you can run following this example:

    cd HHWWgg_Tools/NMSSM/MakeFragments
    python Make_Fragments.py --template Templates/TEMPLATE_HHWWgg_qqlnu.txt --Decay WWgg --fs qqlnu

if it works properly, this will produce two madgraph/pythia configuration files, output to MakeFragments/Fragments. 