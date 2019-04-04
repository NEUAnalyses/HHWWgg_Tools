#!/usr/bin/env python

# 7 February 2019
# Abe Tishelman-Charny 

# The purpose of this plotter is to compare GEN and RECO variables 
# This is to study the effects of the detector on GEN level info 
# The outputs of this can tell if the analysis strategy implemented in the flashgg HHWWggCandidateDumper logic is well-formed.
#https://indico.cern.ch/event/795443/contributions/3304650/attachments/1792639/2921042/2019-02-07-physicsPlenary.pdf

# Big update 3 March 

from ROOT import * 
import array as arr 
import numpy as np
from gen_reco_plot_config import * 
import subprocess
gROOT.SetBatch(True)
import sys
from os import listdir

# Particles to Plot
# Need to set here for now 

ptp = []

#ptp.append('H')
#ptp.append('l')
#ptp.append('le') # leading electron 
#ptp.append('sle') # subleading electron 
#ptp.append('lm') # leading muon 
#ptp.append('slm') # subleading muon 
#ptp.append('nu')
#ptp.append('q')
#ptp.append('j')
#ptp.append('mjj') # Matching jj pair (qq for gen)
ptp.append('nmjj') # Non-Matching jj pair (qq for gen)

nps = len(ptp)

print
print 'It\'s time to plot some fun MC variables'
print

# For each EventDumper directory/file 
for dn,dinfo in enumerate(ds):
    print'dinfo = ',dinfo

    ch = dinfo[0] # channel (SL,FL or FH)
    DID = dinfo[1] # Directory ID (ex: X1250_qqenugg)
    direc = dinfo[2] # full path of directory (ex: )
    #rd = dinfo[2][1] # direc path with root://cmsxrootd.fnal.gov/ prefix for 'Events' module  
    lc = dinfo[3] # histo line color
    fc = dinfo[4] # histo fill color 

    # Save file paths 
    #path_ends = [fp for fp in listdir(direc) if 'inLHE' not in fp] 
    path_ends = [fp for fp in listdir(direc)] 
    paths = []
    for pa in path_ends:
        tmp_path = direc + pa
        paths.append(tmp_path)

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
            print 'Plotting particle', p, ': ',variable
            print
            gen_reco_ID = p + '_' + variable + '_' + DID 
            # Make GEN Plot
            g_variable = var_map(variable,p,1)
            gen_ID = 'GEN_' + p + '_' + variable + '_' + DID
            gen_hist = import_ED(paths[0],g_variable,gen_ID,xbins,xmin,xmax) 
            #gen_colors = [416,416-10]
            dec_gen_hist = save_histo(gen_hist,gen_ID,p,variable,gen_colors[0],gen_colors[1]) # 416 is kGreen 

            # Make RECO Plot 
            r_variable = var_map(variable,p,0)
            reco_ID = 'RECO_' + p + '_' + variable + '_' + DID
            reco_hist = import_ED(paths[0],r_variable,reco_ID,xbins,xmin,xmax) 
            #reco_colors = [600,600-10]
            dec_reco_hist = save_histo(reco_hist,reco_ID,p,variable,reco_colors[0],reco_colors[1]) # 600 is kBlue 

            #print 'dec_gen_hist = ', dec_gen_hist 
            #print 'dec_reco_hist = ', dec_reco_hist 

            # Make RECO/GEN plot 
            input_histos_info = []
            input_histos_info.append([dec_gen_hist,gen_ID,p,[gen_colors[0],gen_colors[1]]])
            input_histos_info.append([dec_reco_hist,reco_ID,p,[reco_colors[0],reco_colors[1]]]) # Be aware, the RECO variable label used is the GEN variable. This assumes you're plotting the same variable. 

            #var_copy = v[0][:]
            var_copy = variable[:]
            #combine_histos(input_histos_info,eval(lc),eval(fc),var_copy) # Saves combined /RECO canvas 
            max_val = combine_histos(input_histos_info,var_copy) # Saves combined GEN/RECO canvas 
            #print 'max_val = ',max_val 
            plot_ratio(input_histos_info,max_val,xbins,gen_reco_ID)