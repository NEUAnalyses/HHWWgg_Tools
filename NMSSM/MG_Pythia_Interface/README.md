# NMSSM validation

The goal of this validation is to confirm that we can use NMSSM cards to produce X->YH and then decay YH with pythia so that we can use a common set of gridpacks for all YH decays. 

## Step 1

Reproduce NMSSM gridpack using NMSSM_XYoYH_MX_500_MY_300 cards (need a genproductions repository).

## Step 2 

Decay YH with https://github.com/NEUAnalyses/HHWWgg_Tools/blob/80634da3c95af92ef44db5f18f2f496fa095b566/NMSSM/MG_Pythia_Interface/XToYHTo2B2Z_pythia_config.py
Note -- make sure local gridpack name is correct.

With this you can produce 10 GEN events locally. 

## Step 3 

Look at kinematics with HHWWgg_Tools/Plot/GEN/ 

## Step 4 

If there is something non-zero, produce 10k events on CRAB. Then repeat Step 3. 
