######################################################################################################################################################################################################
# Abraham Tishelman-Charny                                                                                                                                                                           #
# 3 November 2020                                                                                                                                                                                    #
#                                                                                                                                                                                                    #        
# The purpose of this python module is to plot root tree variables using root_numpy and pyplot.                                                                                                      #
#                                                                                                                                                                                                    #
# ##-- Run on every lxplus instance: source /cvmfs/sft.cern.ch/lcg/views/LCG_98/x86_64-centos7-gcc10-opt/setup.sh                       						                                     #               
#                                                                                                                                                                                                    #
# ##-- Example usage:   
# python PlotVars.py --inputFile output_numEvent500.root --VarsBatch ScaleFactors --xmin 0 --xmax 1.3  --individualPlots --treeName tagsDumper/trees/GluGluToHHTo2G2l2nu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8_13TeV_HHWWggTag_0 --OutputLoc /eos/user/a/atishelm/www/HHWWgg/SF-Checks-SLTag/
# python PlotVars.py --inputFile output_numEvent500.root --VarsBatch ScaleFactors --xmin 0 --xmax 1.3  --individualPlots --treeName tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8_13TeV_HHWWggTag_0 --OutputLoc /eos/user/a/atishelm/www/HHWWgg/SF-Checks-SL/
# python PlotVars.py --inputFile output_numEvent500.root --VarBatch ScaleFactors --xmin 0 --xmax 1.3  --individualPlots --treeName tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8_13TeV_HHWWggTag_0 --OutputLoc /eos/user/a/atishelm/www/HHWWgg/SF-Checks/ 
# python PlotVars.py --inputFile output_numEvent500.root --variable weight --xmin 0 --xmax 1.3  --individualPlots --treeName tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8_13TeV_HHWWggTag_0 --OutputLoc /eos/user/a/atishelm/www/HHWWgg/SF-Checks/   
# python PlotVars.py --inputFile output_numEvent500.root --variable centralObjectWeight --xmin 0 --xmax 1.3  --individualPlots --treeName tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8_13TeV_HHWWggTag_0 --OutputLoc /eos/user/a/atishelm/www/HHWWgg/SF-Checks/
# python PlotVars.py --inputFile output_numEvent500.root --VarsBatch ScaleFactors --individualPlots --treeName tagsDumper/trees/GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8_13TeV_HHWWggTag_0 --OutputLoc /eos/user/a/atishelm/www/HHWWgg/SF-Checks/            
# python PlotVars.py --inputFile MergeOutputs/merged_output_numEvent500.root --VarsBatch ScaleFactors --individualPlots --onePlot --treeName GluGluToHHTo2G2Qlnu_node_cHHH1_TuneCP5_PSWeights_13TeV_powheg_pythia8 --OutputLoc /eos/user/a/atishelm/www/HHWWgg/SF-Checks2/                                                                                                                                                                #            
# python PlotVars.py --inputFile /eos/user/a/atishelm/ntuples/HHWWgg_flashgg/DoubleH-Weights-allEvents/hadded/skimmed_ggF_SM_WWgg_qqlnugg_Hadded.root --VarsBatch ScaleFactors --individualPlots     #
######################################################################################################################################################################################################

##-- Imports
import ROOT as R 
import argparse 
import sys 
import os 

##-- Import SubModules
from python.PlotVarsOptions import * 
from python.PlotVarsTools import * 

##-- Define flags and variables based on user input 
args = GetOptions()
CreateDirec(args.OutputLoc)
inArgNames = ['inputFile','treeName','VarsBatch','OutputLoc','individualPlots','plotTogether','onePlot','variable', 'xmin', 'xmax']
for argName in inArgNames:
    exec("%s = args.%s"%(argName,argName))

##-- Make output folder if it doesn't exist  
# outputFolder = "%s/%s"%(ol_,cutName)
# if(not os.path.exists(OutputLoc)):
    # os.system('mkdir %s'%(OutputLoc))
    # os.system('cp %s/../index.php %s'%(OutputLoc,OutputLoc)) 

file = R.TFile(inputFile)
print"treeName:",treeName
tree = file.Get(treeName)

if(VarsBatch != ""): 
    # Vars, xmin, xmax = GetVarsList(VarsBatch)
    Vars, xmin, xmax = GetVarsList(VarsBatch)
    print"Vars:",Vars

# if(variable != ""):
    # PlotVar(variable,tree,OutputLoc,xmin,xmax)

if(individualPlots):
    for Var in Vars:
        # print "Plotting variable ",Var
        PlotVar(Var,tree,OutputLoc,xmin,xmax)
        if(onePlot): 
            print"Only plotting first variable in batch"
            print"Stopping now"
            break 

# ##-- Up/Downs 
# if(VarsBatch == "ScaleFactors"):
#     skipVars = ["weight","centralObjectWeight","puweight"]
#     for SFname in Vars:
#         if(SFname in skipVars): continue 
#         SFnames = []
#         SFnames.append(SFname)
#         # print"SFname:",SFname
#         for shift in ["Up01sigma","Down01sigma"]:
#             SFnameCopy = SFname[:]
#             SFnameCopy = SFnameCopy.replace("Central","")
#             shiftedVarName = "%s%s"%(SFnameCopy,shift)
#             # print"shiftedVarName",shiftedVarName
#             SFnames.append(shiftedVarName)
#         ##-- should plot central, and +/- 1 sigma scale factors together for each scale factor 

#         # PlotSFVariations(SFnames,tree,OutputLoc,xmin,xmax)
#         PlotSFDifferences(SFnames,tree,OutputLoc,-0.2,0.2)
#         if(onePlot): 
#             print"Only plotting first variable in batch"
#             print"Stopping now"
#             break 
# else: 
#     ##-- Plot each variable on an individual canvas 
#     if(individualPlots):
#         for Var in Vars:
#             PlotVar(Var,tree,OutputLoc,xmin,xmax)
#             if(onePlot): 
#                 print"Only plotting first variable in batch"
#                 print"Stopping now"
#                 break 

#     ##-- Plot all variables in batch on same canvas
#     if(plotTogether):
#         PlotVarsTogether(Vars,tree,OutputLoc,VarsBatch,xmin,xmax)
