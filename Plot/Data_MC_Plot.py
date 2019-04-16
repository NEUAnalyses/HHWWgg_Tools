#!/usr/bin/env python

# Abe Tishelman-Charny 
# 16 April 2019

# The purpose of this plotter is to compare Data/MC

from ROOT import * 
import array as arr 
import numpy as np
from Data_MC_Plot_Config import ds, vs, var_map, import_ED, ptp, Data_colors, MC_colors, save_histo, save_histo_stack, combine_histos, plot_ratio
import subprocess
gROOT.SetBatch(True)
import sys
from os import listdir

nps = len(ptp)
print 
print '---------------------------------------------'
print 
print 'It\'s time to plot some fun Data/MC variables'

# For each EventDumper directory
for dn,dinfo in enumerate(ds):

    # Get necessary info 
    Data_direc = dinfo[0][0] # full path of directory (ex: )
    MC_direc = dinfo[0][1] # full path of directory (ex: )
    Data_tree_prefix = dinfo[1][0]
    MC_tree_prefix = dinfo[1][1]
    lc = dinfo[2] # histo line color
    fc = dinfo[3] # histo fill color 

    # Save file paths 
    #path_ends = [fp for fp in listdir(direc) if 'inLHE' not in fp] 
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

    # For each variable
    for iv,v in enumerate(vs):
        variable = v[0] 
        xbins = v[1]
        xmin = v[2]
        xmax = v[3]
        #print 'Plotting variable ', iv, ': ',variable

        # For each particle
        for p in ptp:
            # For each set of cuts
            #for 
            print
            print 'Plotting particle \'',p, '\':',variable
            print
            ED_variable = var_map(variable,p,0) # Variable as called by the event dumper. Call it a non-gen variable to keep map consistent 
            Data_MC_ID = p + '_' + variable # + '_' #+ DID 

            # Make Data Plot
            Data_ID = 'Data_' + p + '_' + variable # + '_' #+ DID
            Data_hist = import_ED(Data_paths,ED_variable,Data_ID,xbins,xmin,xmax,Data_tree_prefix) 
            dec_Data_hist = save_histo(Data_hist,Data_ID,p,variable,Data_colors[0],Data_colors[1]) 

            # Make MC THStack Plot 
            MC_ID = 'MC_' + p + '_' + variable # + '_' #+ DID
            MC_hist = import_ED(MC_paths,ED_variable,MC_ID,xbins,xmin,xmax,MC_tree_prefix) 
            dec_MC_hist = save_histo_stack(MC_hist,MC_ID,p,variable,MC_colors[0],MC_colors[1]) 

            # Make Data/MC plot 
            input_histos_info = []
            input_histos_info.append([dec_Data_hist,Data_ID,p,[Data_colors[0],Data_colors[1]]])
            input_histos_info.append([dec_MC_hist,MC_ID,p,[MC_colors[0],MC_colors[1]]]) # Beware, the MC variable label used is the Data variable. This assumes you're plotting the same variable. 

            #var_copy = v[0][:]
            var_copy = variable[:]
            #combine_histos(input_histos_info,eval(lc),eval(fc),var_copy) # Saves combined /MC canvas 
            max_val = combine_histos(input_histos_info,var_copy) # Saves combined Data/MC canvas 
            #print 'max_val = ',max_val 
            plot_ratio(input_histos_info,max_val,xbins,Data_MC_ID)