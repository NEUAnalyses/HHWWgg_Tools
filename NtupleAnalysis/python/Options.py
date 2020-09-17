# The purpose of this module is to define options based on user input for running NtupleAnalysis modules 

import argparse 

def GetOptions():
    parser = argparse.ArgumentParser()

    ##-- Analysis Options
    parser.add_argument("--Efficiency", action="store_true", default=False, help="Compute cutflow efficiency", required=False)
    parser.add_argument("--DataMC", action="store_true", default=False, help="Produce Data / MC Comparisons", required=False)
    parser.add_argument("--GenReco", action="store_true", default=False, help="Perform Gen Reco analysis", required=False)

    ##-- Efficiency Plots 
    parser.add_argument("--ratio", action="store_true", default=False, help="Efficiency Ratio", required=False)
    parser.add_argument('--folders', type=str, default="", help="Comma separated list of ntuple folders", required=False)
    parser.add_argument('--campaigns', type=str, default="", help="Comma separated list of campaigns", required=False)
    parser.add_argument('--massPoints', type=str, default="", help="Comma separated list of mass points to run", required=False)
    parser.add_argument("-p","--plot", action="store_true", default=False, help="Plot", required=False)
    parser.add_argument("-n","--norm", action="store_true", default=False, help="normalize plots", required=False)
    parser.add_argument("-df","--df", action="store_true", default=False, help="deep flavour b score", required=False)
    parser.add_argument("-csv","--dcsv", action="store_true", default=False, help="deep csv b score", required=False)
    parser.add_argument("-l","--log", action="store_true", default=False, help="Log y scale plot", required=False)
    parser.add_argument("--Res", action="store_true", default=False, help="Resonant analysis", required=False)
    parser.add_argument("--EFT", action="store_true", default=False, help="EFT analysis", required=False)
    parser.add_argument("--NMSSM", action="store_true", default=False, help="NMSSM Analysis", required=False)
    parser.add_argument("--SumTags", action="store_true", default=False, help="Sum entries from tags", required=False)
    parser.add_argument('--note', type=str, default="", help="Note for titles and file path", required=False)
    parser.add_argument('--folder', type=str, default="", help="Input folder with hadded files", required=False)

    ##-- Data / MC comparison 
    parser.add_argument('--dataFolder', type=str, default="", help="Input folder with hadded Data ntuples", required=False)
    parser.add_argument('--mcFolder', type=str, default="", help="Input folder with hadded MC ntuples", required=False)
    parser.add_argument('--signalFolder', type=str, default="", help="Input folder with hadded Signal ntuples", required=False)
    parser.add_argument('--VarBatch', type=str, default="basic", help="Batch of variables to plot. Options: basic, MVA, loose, all ", required=False)
    parser.add_argument('--CutsType', type=str, default="Loose", help="Cuts type. Ex: PS, Loose, Medium, all", required=False)
    parser.add_argument("--drawPads", action="store_true", default=False, help="Draw each MC contribution to stack", required=False)
    parser.add_argument('--Lumi', type=float, default=0, help="Luminosity for scaling MC (in fb-1)", required=False)
    parser.add_argument('--SigScale', type=float, default=-999, help="Artificial scale for signal", required=False)
    parser.add_argument('--Tags', type=str, default="", help="Comma separated list of tags to run. Ex: HHWWggTag_0,HHWWggTag_1,HHWWggTag_2 or HHWWggTag_2 or HHWWggTag_2,combined", required=False)
    parser.add_argument("--noQCD", action="store_true", default=False, help="Turn on to skip QCD", required=False)

    ##-- Gen Reco Analysis

    ##-- Misc
    parser.add_argument('--verbose', action="store_true", default=False, help="Verbosity. Set true for extra output information", required=False)
    parser.add_argument('--testFeatures', action="store_true", default=False, help="Change output to testing area", required=False)
    parser.add_argument('--signalCut', action="store_true", default=False, help="Apply selections to signal", required=False)
    parser.add_argument('--prefix', type=str, default="", help="Tree prefix. Example: tagsDumper/trees/", required=False)

    args = parser.parse_args()

    return args 