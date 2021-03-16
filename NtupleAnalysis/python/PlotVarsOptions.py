

# The purpose of this module is to define options based on user input for running NtupleAnalysis modules 

import argparse 

def GetOptions():
    parser = argparse.ArgumentParser()

    ##-- Setup
    parser.add_argument("--inputFile", type=str, help="Input file", required=True)
    parser.add_argument("--treeName", type=str, help="Name of input file tree with variables to plot", required=True)

    ##-- What to plot 
    parser.add_argument("--variable", type=str, help="If plotting a single variable")
    parser.add_argument("--VarsBatch", default="", type=str, help="Name of variable batch to plot")
    parser.add_argument("--xmin", type=float, help="xmin for single variable")
    parser.add_argument("--xmax", type=float, help="xmax for single variable")
    
    ##-- Misc 
    parser.add_argument("--OutputLoc", type=str, help="Output location for plots", required=True)
    parser.add_argument("--individualPlots", action="store_true", help="Plot each weight")
    parser.add_argument("--plotTogether", action="store_true", help="Plot weights together")
    parser.add_argument("--onePlot", action="store_true", help="Only plot first variable in batch")

    args = parser.parse_args()

    return args 


