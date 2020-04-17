#!/usr/bin/env python
# 7 February 2019
# Abe Tishelman-Charny 
# Updated 31 May 2019 for HH MC 
# from ROOT import * 
import ROOT 
import array as arr 
import numpy as np
from GEN_Plotter_Config import * 
import subprocess
import ROOT
ROOT.gROOT.SetBatch(True)
from DataFormats.FWLite import Handle, Runs, Lumis, Events  #, ChainEvent 
import sys
import os 
from os import listdir
print '.'
print 'Plotting HH Variables'
print '.'
ol = '/eos/user/a/atishelm/www/HHWWgg_Analysis/GEN/'
# me, genHandle = -1, Handle('vector<reco::GenParticle>')
# summary = Handle('<LumiSummary>')
# For each variable
for iv,v in enumerate(vs):
    variable = v[0]
    print 'Plotting variable ', iv, ': ',v[0]
    # For each directory 
    histos = [] 
    # mg_title = v[0]
    # mg = ROOT.TMultiGraph('mg',mg_title)
    for dn,dir in enumerate(d):
        direc = dir[0] # full path of directory 
        rd = dir[1] # direc path with root://cmsxrootd.fnal.gov/ prefix for 'Events' module  
        mass = dir[2]
        channel = dir[3]  

        path_ends = [fp for fp in listdir(direc) if 'inLHE' not in fp]  # Save paths of non-LHE files
        #path_ends = [fp for fp in listdir(direc)]  # Save all paths 
        paths = []
        for pa in path_ends:
            tmp_path = rd + pa
            paths.append(tmp_path)
        # print '  Creating histos for file(s) of type: ',DID 
        # Get chosen particles to plot and number of them 
        pparams = []
        pparams = get_pparams(ptp)
        xbins = v[1]
        xmin = v[2]
        xmax = v[3] # Mass_Channel_Variable 
        plot_title = mass + ', ' + channel 
        h1 = ROOT.TH1F('h1',plot_title,xbins,xmin,xmax)
        for ip,path in enumerate(paths):
            if ip == max_files: break 
            print '    Processing file ', ip+1, ': ',path 
            events = Events(path) # needs to be file with root prefix                 
            # db = (float(xmax) - float(xmin)) / float(xbins) 
            # Loop events 
            # Add to sum 
            for iev, event in enumerate(events):
                if iev%100 == 0: print'on event',iev 
                if iev == me: break # Max events 
                
                #event.getByLabel('prunedGenParticles', genHandle)
                events.getByLabel('genParticles', genHandle)
                genParticles = genHandle.product()

                # Fill histograms with current variable 
                for params in pparams:
                    particle = params[0]
                    nparticles = params[1]
                    pdgIDs = params[2]
                    # ps = [p for p in genParticles if p.isHardProcess() and abs(p.daughter(0).pdgId() == 25)]
                    ps = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in pdgIDs]

                    # ps = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in pdgIDs and abs(p.daughter(0).pdgId() == 25)]   
                    # ps = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in pdgIDs and abs(p.daughter(0).pdgId() == 22)]   
                    # ps = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in pdgIDs]   
                    # for p in ps:
                    #     print'p = ',p.p4()
                    if v[0] == 'pt':
                        val = ps[0].p4().pt() 

                    if nparticles == 2:


                        if v[0] == 'invm':
                            val = invmass(ps[0].p4(),ps[1].p4())
                            # val = ps[0].p4().pt()

                            # if particle == 'R':
                                # avoid double count 
                            h1.Fill(val)
                            # get invmass 
                    else: 
                        for p in ps:
                            val = eval("p." + v[0] + "()")
                            h1.Fill(val)
        output_path = ol + mass + '_' + channel + '_' + particle + '_' + variable 
        c1 = ROOT.TCanvas()
        color = dir[4]
        h1.SetLineColor(eval(color))
        h1.Draw() 
        c1.SaveAs(output_path + ".png")
        h1.SaveAs(output_path + ".C")
        h1.SaveAs(output_path + ".root")    
        histos.append(h1)

    print'histos = ',histos 

    # c2 = ROOT.TCanvas()
    # for ih,h in enumerate(histos):
    #     print'h = ',h
    #     h.SetStats(0)
    #     if ih == 0:
    #         h.Draw()
    #     else:
    #         h.Draw('same')
    # xmin, ymin, xmax, ymax = 0.6,0.5,0.8,0.7
    # legend = ROOT.TLegend(xmin,ymin,xmax,ymax)
    # for ih,h in enumerate(histos):
    #     legend.AddEntry(h)
    # legend.Draw('same')
    # c2.Update()
    # c2.SaveAs(ol + variable + '_Combined.png')
                                   