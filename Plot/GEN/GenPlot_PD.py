########################################################################################################################
# Abe Tishelman-Charny
# 23 July 2020
#
# GEN analysis using pandas dataframes 
#
# Example Usage:
#
# ##-- Create pandas dataframe 
# python GenPlot_PD.py --CreateDataframe --genType NONRES --nEvents 1000  --maxFiles 1 --dfOutName PhaseII_HHWWgg --DatasetBatch PhaseIIHHWWgg-GF-nonres-SM --printerval 100
# python GenPlot_PD.py --CreateDataframe --genType NONRES --nEvents 1000  --maxFiles 1 --dfOutName PhaseII_HHWWgg_Test --DatasetBatch PhaseIIHHWWgg-GF-nonres-SM --printerval 100
# python GenPlot_PD.py --CreateDataframe --genType VBFNONRES --nEvents 2000  --maxFiles 1 --dfOutName HHWWgg-SM-NonRes-VBF_WWgg_qqlnu_{node}_df --DatasetBatch HHWWgg-VBF-nonres-SM --printerval 500 
# python GenPlot_PD.py --CreateDataframe --genType VBFRES --nEvents 10000  --maxFiles 1 --dfOutName VBFToBulkGravitonToHH_WWgg_qqlnu_{node}_df --DatasetBatch VBF-Resonant --printerval 500
# python GenPlot_PD.py --CreateDataframe --genType RES --nEvents 9000 --requireHardProcess --maxFiles 4 --dfOutName GluGluToHHToRadionTo_WWgg_qqlnu_{node}_df --DatasetBatch Resonant
# python GenPlot_PD.py --CreateDataframe --genType NONRES --nEvents 1000 --requireHardProcess --maxFiles 3 --dfOutName GluGluToHHTo_WWgg_qqlnu_{node}_df --DatasetBatch Non-Resonant
# python GenPlot_PD.py --CreateDataframe --genType RES --nEvents 1000 --requireHardProcess --maxFiles 3 --dfOutName GluGluToHHToRadionTo_WWgg_qqlnu_{node}_df --DatasetBatch Non-Resonant
# lowevents: python GenPlot_PD.py --CreateDataframe --genType VBFRES-LowEvents --nEvents 1000  --maxFiles 1 --dfOutName VBFToBulkGravitonToHH_WWgg_qqlnu_{node}_df --DatasetBatch VBF-RES-2-6-5 --printerval 100
#
# ##-- Plot dataframe variables 
# python GenPlot_PD.py --PlotDataFrame --dfTypes NONRES --outDirectory NONRES_PhaseII --extraVariables HH_invmass --particles Lead_H,Sublead_H --variables pt --plotSingles
# python GenPlot_PD.py --PlotDataFrame --dfTypes VBFNONRES --outDirectory VBFNONRES --extraVariables HH_invmass --particles Lead_H,Sublead_H --variables pt --plotSingles
# python GenPlot_PD.py --PlotDataFrame --dfTypes VBFNONRES --outDirectory VBFNONRES --extraVariables HH_invmass --particles Lead_H,Sublead_H --variables pt --plotSingles
# python GenPlot_PD.py --PlotDataFrame --dfTypes VBFRES-Compare-2-4-2-and-2-6-5-X850 --outDirectory Compare-2-4-2-and-2-6-5-X850 --extraVariables HH_DeltaR,qq_invmass,qq_DeltaR,outVBFqoutVBFq_invmass,outVBFqoutVBFq_DeltaR,incVBFqincVBFq_invmass --particles Lead_H,Sublead_H,Lead_q,Sublead_q,nu,Lead_outVBFq,Sublead_outVBFq --variables pt --doRatioHists
# python GenPlot_PD.py --PlotDataFrame --dfTypes VBFRES-LowEvents --outDirectory VBFRES-LowEvents-2-6-5 --extraVariables HH_DeltaR,qq_invmass,qq_DeltaR,outVBFqoutVBFq_invmass,outVBFqoutVBFq_DeltaR,incVBFqincVBFq_invmass --particles Lead_H,Sublead_H,Lead_q,Sublead_q,nu,Lead_outVBFq,Sublead_outVBFq --variables pt
# python GenPlot_PD.py --PlotDataFrame --dfTypes VBFRESlowEvents --outDirectory VBFRES_lowEvents --extraVariables qq_invmass,qq_DeltaR --particles Lead_q --variables pt
########################################################################################################################

from python.CreateDataFrame import * 
from python.PlotDataFrame import * 
from python.PlotDataFrames import * 

import argparse

parser = argparse.ArgumentParser(description='GEN and GEN-SIM ntuple production and comparison')

##-- Create Pandas Dataframe with GEN variables  
parser.add_argument("--CreateDataframe", action="store_true", default=False, help="Create GEN Ntuple", required=False)
parser.add_argument("--DatasetBatch", type=str, default="none", help="Batch of datasets to create dataframes of")
parser.add_argument("--dfOutName", type=str, default="outputDataframe", help="Name of output dataframe")
parser.add_argument("--maxFiles", type=int, default=-1, help="Max number of files in inFolder to combine", required=False)
parser.add_argument('-v', type=str, default="pdgId", help="Comma separated list of variables to plot", required=False)
parser.add_argument('-sp', type=str, default="", help="Single particles to plot variables of", required=False)
parser.add_argument('--genType', type=str, default="GEN", help="Gen type. Used to create output folder", required=False)
parser.add_argument('--nEvents', type=float, default=-1, help="Max number of events to run on", required=False)
parser.add_argument('--firstEvent', type=int, default=-1, help="Max number of events to run on", required=False)

##-- Plot Pandas Dataframe variables  
# parser.add_argument("--PlotDataFrame", action="store_true", default=False, help="Plot dataframe(s)", required=False)
parser.add_argument("--PlotDataFrames", action="store_true", default=False, help="Plot dataframe(s)", required=False)
# parser.add_argument("--lowEvents", action="store_true", default=False, help="Plot low number of events to test framework", required=False)
parser.add_argument('--dfTypes', type=str, default="RES", help="Comma separated string of dataframe types", required=False)
parser.add_argument('--particles', type=str, default="", help="Comma separated string of particle names", required=False)
parser.add_argument('--variables', type=str, default="", help="Comma separated string of variable names", required=False)
parser.add_argument('--extraVariables', type=str, default="", help="Comma separated string of extra vari    able names", required=False)
parser.add_argument('--outDirectory', type=str, default="gen_output", help="Output directory for plots", required=False)
parser.add_argument("--ExtraStyles", action="store_true", default=False, help="Plot dataframe(s)", required=False)
parser.add_argument("--plotSingles", action="store_true", default=False, help="Plot variables for individual dataframes", required=False)
parser.add_argument("--doRatioHists", action="store_true", default=False, help="If plotting ratio, plot hists and bars", required=False)
parser.add_argument('--maxEvents', type=int, default=999999999, help="Max number of events to run on", required=False)
parser.add_argument("--upLeftLegend", action="store_true", default=False, help="Place legend on upper left", required=False)

##-- Misc
parser.add_argument("--debug", action="store_true", default=False, help="Extra print statements for debugging", required=False)
parser.add_argument("--condor", action="store_true", default=False, help="Change handling of outputs when running on condor", required=False)
parser.add_argument('--printerval', type=int, default=1000, help="Print event info every X events", required=False)

args = parser.parse_args()

if(args.CreateDataframe): CreateDataFrame(args)
elif(args.PlotDataFrames): PlotDataFrames(args)
elif(args.PlotDataFrame): PlotDataFrame(args)
