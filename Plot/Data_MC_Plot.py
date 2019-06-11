#!/usr/bin/env python
# Abe Tishelman-Charny 
# The purpose of this plotter is to compare Data/MC

from ROOT import * 
import array as arr 
import numpy as np
from Data_MC_Plot_Config import ds, vs, import_ED, ptp, Save_Data_Histos, Save_Stack_Histos, combine_histos, plot_ratio, cuts 
from Variable_Map import var_map 
import subprocess
gROOT.SetBatch(True)
import sys
from os import listdir

nps = len(ptp)
print '...'
print 'It\'s time to plot some fun Data/MC variables'
print '...'

def main():
    # Get Data, MC Ntuple paths 
    Data_direc = ds[0][0] # full path of directory (ex: /eos/user/a/atishelm/2016_Data/)
    MC_direc = ds[0][1] # full path of directory (ex: /eos/user/a/atishelm/2016_Bkg/)
    Data_tree_prefix = ds[1][0] # 'Data'
    MC_tree_prefix = ds[1][1] # 'Dummy' 

    # Save file paths 
    #path_ends = [fp for fp in listdir(direc) if 'inLHE' not in fp] # to exclude certain paths 
    # Data 
    Data_path_ends = [fp for fp in listdir(Data_direc)] 
    Data_paths = []
    for pa in Data_path_ends:
        tmp_path = Data_direc + pa
        Data_paths.append(tmp_path)

    # MC 
    MC_path_ends = [fp for fp in listdir(MC_direc)] 
    MC_paths = []
    for pa in MC_path_ends:
        tmp_path = MC_direc + pa
        MC_paths.append(tmp_path)

    # Need list of : variable, particle, cut  
    plotting_info = []
    for v in vs:
        for p in ptp:
            for c in cuts:
                tmp_entry = []
                tmp_entry.append(v)
                tmp_entry.append(p)
                tmp_entry.append(c)
                plotting_info.append(tmp_entry)

    # Make Data Plots
    # Data_hists = import_ED(Data_paths, plotting_info,"Data",vs,ptp,cuts)
    # dec_Data_hists = Save_Data_Histos(Data_hists) 
    # Make MC Plots
    MC_hists = import_ED(MC_paths, plotting_info, "MC",vs,ptp,cuts) # MC label is a dummy  
    dec_MC_hists = Save_Stack_Histos(MC_hists) 
    exit(0)

    # Gather Histograms
    input_histos_info = []
    input_histos_info.append(dec_Data_hists) # Data 
    input_histos_info.append(dec_MC_hists) # Beware, the MC variable label used is the Data variable. This assumes you're plotting the same variable. 
 
    # Make Ratio Plots
    max_vals = combine_histos(input_histos_info, plotting_info) # Saves combined Data/MC canvas and gets max_value for y axis 
    plot_ratio(input_histos_info, max_vals, plotting_info)

if __name__ == "__main__":
    main()