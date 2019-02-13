#!/usr/bin/env python

# 7 February 2019
# Abe Tishelman-Charny 

# This takes some inspiration from TreePlotter.py and PlotterTools.py
# Run from cmssw with cmsenv to access FWLite 
# Might need certain CMSSW version depending on data 
# For now 7_X_X file opens with 9_3_9_patch1

# The purpose of this plotter is to plot variables from GEN level files
# This is to study what the signal looks like with no detector bias
# The outputs of this can tell if the analysis strategy implemented in the flashgg HHWWggCandidateDumper logic is well-formed.
#https://indico.cern.ch/event/795443/contributions/3304650/attachments/1792639/2921042/2019-02-07-physicsPlenary.pdf

from ROOT import * 
import array as arr 
import numpy as np
from GEN_Plotter_Config import * 
import subprocess
#import ROOT
gROOT.SetBatch(True)
#PyConfig.IgnoreCommandLineOptions = True
from DataFormats.FWLite import Handle, Runs, Lumis, Events  #, ChainEvent 
import sys
from os import listdir

gSystem.Load("libFWCoreFWLite.so")
AutoLibraryLoader.enable()
gSystem.Load("libDataFormatsFWLite.so")


print
print 'It\'s time to plot some fun GEN variables'
print

# At the end will contain all histos for combining 
v_histos = [] # [variableindex][particleindex][histogramindex], len(histogramindices) = number of files 

# Plot each variable for each file, then together 
for iv,v in enumerate(vs):
    print 'Plotting variable ', iv, ': ',v[0]

    # will contain all file histos for the current variable
    # for a given unique variable (ex: px, H1) I want them plotted together for comparison 
    # Maybe not super important since what I want for now is reco level plotted with gen level for same variable 
    # How can you know at reco level which is which? Can we only compare di-variables? (ex: invariant mass, dphi, deta)

    v_histos.append([]) # for all variable iv plots 
    for i in range(0,nps): # for each particle, needs to be present in each file 
        #print 'i = ',i
        v_histos[iv].append([]) # list for all plots for given particle 

    #v_histos[0].append([]) # for plots of zeroeth particle 
        
    # fi[1] may actually be a directory path 
    #     
    for fn,f in enumerate(fi):

        #f[1][0] = full path #
        #f[1][1] = path with root://cmsxrootd.fnal.gov/ prefix for 'Events' module 
        #print 'f = ',f
        # assuming directory 
        direc = f[1][0]
        path_ends = [fp for fp in listdir(direc) if 'inLHE' not in fp] # ends of paths. Everything after final '/'
        #print 'path ends = ',path_ends
        paths = []
        for pa in path_ends:
            tmp_path = f[1][1] + pa
            paths.append(tmp_path)

        
        #vector<string> fileNames #paths
        #fileNames.push_back("....root")

        #fwlite::ChainEvent ev(fileNames)

        #ev = ChainEvent ()

        #for( ev.toBegin(); ! ev.atEnd(); ++ev) {
        #     fwlite::Handle<std::vector<...> > objs;
        #     objs.getByLabel(ev,"....")
        #     //now can access data
        #     std::cout <<" size "<<objs.ptr()->size()<<std::endl;
        #     ...
        # }
        
        #print 'paths = ',paths 

        # paths is root labelled files in chosen directory 

        print '   Filling histos for file(s) of type: ',f[0] 

                # Make histograms just before looping file events for given file 
        histos = []
        for spar in sp:
            ID = 'GEN_' + spar + '_' + v[0] + '_' + f[0]
            h = TH1F(ID,ID,v[1],v[2],v[3])
            histos.append([h,ID,spar])


        # Would like a nice way to loop over files so this takes less time 

        #for ip,path in enumerate(0,len(paths)):
        #for ip,path in enumerate(paths):


        #print'Before events opener'
        #events = Events(path) # needs to be file with root prefix 
        #a = array(paths)

        gInterpreter.ProcessLine('vector<string> fileNames;')
        gInterpreter.ProcessLine('fileNames.push_back("root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_8/190212_095439/0000/ggF_X1250_WWgg_qqqqgg_1000events_GEN_1.root");')
        gInterpreter.ProcessLine('fwlite::ChainEvent events(fileNames);')

        #vector<string> fileNames

        #fileNames.push_back("....root");

        #fwlite::ChainEvent ev(fileNames);


        #a = vector('string')(paths)
        #events = fwlite.ChainEvent(paths)
        #events = fwlite.ChainEvent(a)
        #print'After events opener'

        # # Make histograms just before looping file events for given file 
        # histos = []
        # for spar in sp:
        #     ID = 'GEN_' + spar + '_' + v[0] + '_' + f[0]
        #     h = TH1F(ID,ID,v[1],v[2],v[3])
        #     histos.append([h,ID,spar])
            #histos = [particle1,particle2,...] 

        # Loop events 
        # fills histos appropriately each event 
        print'Just before event loop'
        #for iev, event in enumerate(events):
        #for( ev.toBegin();
        #  ! ev.atEnd();
        #  ++ev) {

        gInterpreter.ProcessLine('for( ev.toBegin();')
        gInterpreter.ProcessLine('  ! ev.atEnd();')
        gInterpreter.ProcessLine('  ++ev) {')

        #if iev == me: break # Max events 
        #event.getByLabel('prunedGenParticles', genHandle)
        events.getByLabel('genParticles', genHandle)
        #genParticles = genHandle.product()

        #objs = Handle()

        # Plot for each desired particle 
        for pi,pa in enumerate(sp):
            # H first 
            # pi == 0
            if pa == 'H':

                higgs = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [25]]
                if len(higgs) == 2:
                    for hi,h in enumerate(higgs):
                        #print'filling'
                        val = eval('h.' + v[0] + '()')
                        #print'val = ',val
                        #print 'num entries = ',histos[pi][0].GetEntries()
                        histos[pi][0].Fill(val) 
                                            
                elif len(higgs) != 2:
                    print "Length of higgs vector is not 2. Skipping event"

                else:
                    print "Is it even possible for this condition to occur?"

            # pi == 1
            elif pa == 'W':

                Ws = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [24]]
                if len(Ws) == 2:
                    for Wi,W in enumerate(Ws):
                        val = eval('W.' + v[0] + '()')
                        # Knowing histos[1] is W boson
                        histos[pi][0].Fill(val) #[histo_index][0=histo_object]
                        
                elif len(Ws) != 2:
                    print "Length of W vector is not 2. Skipping event"

                else:
                    print "Is it even possible for this condition to occur?"

            # pi == 2
            elif pa == 'qq':

                qs = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [1,2,3,4,5,6]]

                # Number of quarks
                if len(qs) == 2:
                # Add all quark values 

                    if v[0] == 'invm':
                        val = ROOT.Math.VectorUtil.InvariantMass(qs[0].p4(),qs[1].p4())
                        #val = Math.VectorUtil.InvariantMass(qs[0],qs[1])
                        #val = InvariantMass(qs[0].p4(),qs[1].p4())
                        #val = invmass(qs[0],qs[1])
                        histos[pi][0].Fill(val) 

                    else: 
                        for hi,q in enumerate(qs):
                            val = eval('q.' + v[0] + '()')
                            histos[pi][0].Fill(val) 

                elif len(qs) == 4:
                # get the four quarks 
                # order by pT 
                # Take invariant mass of 

                    if v[0] == 'invm':
                        val = ROOT.Math.VectorUtil.InvariantMass(qs[0].p4(),qs[1].p4())
                        #val = Math.VectorUtil.InvariantMass(qs[0],qs[1])
                        #val = InvariantMass(qs[0].p4(),qs[1].p4())
                        #val = invmass(qs[0],qs[1])
                        histos[pi][0].Fill(val) 

                    else: 
                        for hi,q in enumerate(qs):
                            val = eval('q.' + v[0] + '()')
                            histos[pi][0].Fill(val) 
                else:
                    print 'Not exactly 4 quarks in this event'

            # pi == 3
            elif pa == 'e':

                es = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [11]]

                # Number of electrons. Depends on decay channel.
                # Fully leptonic: 2
                # Semi leptonic: 1 
                if len(es) == 2:
                    for hi,e in enumerate(es):
                        print 'Fully leptonic decay detected'
                        val = eval('e.' + v[0] + '()')
                        histos[pi][0].Fill(val) 

            # pi == 4
            elif pa == 'nu':

                es = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [12]]

                # Number of electrons. Depends on decay channel.
                # Fully leptonic: 2
                # Semi leptonic: 1 
                if len(es) == 2:
                    for hi,e in enumerate(es):
                        print 'Fully leptonic decay detected'
                        val = eval('e.' + v[0] + '()')
                        histos[pi][0].Fill(val) 
                                            
            else:
                print 'I am not prepared for any of the particles in your desired single particles list'
                print 'Please either choose a different desired particle, or write something to deal with your desired particle'
        print 'Just after event loop'
        #print 'Finished going through events in file: ', path
        #if ip == max_files:
            #break 

        # Finished going through all events in directory
        # Save single file histos 
        print 'Finished going through all files in directory: ',direc
        print '   Saving ', f[0], ' histos'
        pn = 0 # particle number 
        # number of histograms in histos is number of particles
        print 'histos = ',histos  
        for hi,h in enumerate(histos):
            print '      Saving histo ',hi 
            #print 'h = ',h
            #print 'v_histos = ',v_histos
            #h[0].SetDirectory(0)
            c1 = TCanvas('c1', 'c1', 800, 600)
            h[0].SetDirectory(0)
            #print 'h[0] = ',h[0]
            h[0].SetLineColor(f[2])
            h[0].SetFillColor(f[3])
            h[0].Draw()
            #c1.Update()
            subprocess.Popen("rm " + outputLoc + h[1] + '.png') # if file already exists, remove it before saving 
            c1.SaveAs(outputLoc + h[1] + '.png')
            #h[0].SetDirectory(0) # This avoids problem later on when introducing legend 
            #c1.Destructor()
            #h.SaveAs("histopath.root")
            #v_histos[iv].append([]) # For each particle
            #v_histos[iv][hi].append(h)
            # Check which particle, add to its list of plots for this variable 

            # This method puts (variable, particle) ('iv','i') plots in v_histos[iv][i]
            if h[2] == 'H': # Currently [iv][0] associated with H, [iv][1] with W. 
                v_histos[iv][0].append(h)
            elif h[2] == 'W':
                v_histos[iv][1].append(h)
            elif h[2] == 'qq':
                v_histos[iv][2].append(h)
            elif h[2] == 'e':
                v_histos[iv][3].append(h)
            else:
                'Can\'t find this plot\'s particle:', h[2] ,' in list of expected particles'

            # total number of histos per file = num_particles = nps
            #if (hi%(nps/nfi) == 0) and (hi != 0): # on the next particle, increment v_histos to keep particle plots separate 
            #    v_histos[iv].append([]) 
            #    pn += 1
            #    v_histos[iv][pn].append(h)
            #else:
            #    v_histos[iv][pn].append(h)

    print '   Plotted variable: ', v[0], 'for all files'
    print '   Now combining results for each particle'

    # For a given variable there are len(single_particles) plots 

    # Is it interesting to plot the same variable for different particles? 
    # Should it be separated by particle? 
    #for particle in v_histos[iv] 

    for phists in v_histos[iv]:

        #print 'phists[2][0] = ',phists[2][0]
        c0 = TCanvas('c0', 'c0', 800, 600)
        #leg = TLegend(0.6, 0.7, 0.89, 0.89) # might want destructors later to be more memory efficient 

        for hi,hinfo in enumerate(phists):
            histo = hinfo[0]
            #these_hists_[hi].SetFillColor(kWhite)
            histo.SetTitle( hinfo[2] + v[0] + ' Combined ') # <particle> <variable> combined 
            histo.SetFillColor(kWhite)
            if hi == 0:
                #hh1[0].SetTitle(v[1] + ' Combined ')
                #gStyle.SetOptStat(0) # No Stats Box
                histo.SetStats(0)
                histo.Draw('h')
            if hi > 0:
                histo.SetStats(0)
                #gStyle.SetOptStat(0) # No Stats Box
                histo.Draw('h same')

        leg = TLegend(0.6, 0.7, 0.89, 0.89)
        for i in range(0,len(phists)):
            leg.AddEntry(phists[i][0],phists[i][1], 'lf') # histo object, legend entry (ID)
            #leg.SetTextSize(0.02)
        #gStyle.SetOptStat(0) # No Stats Box
        leg.Draw('same')
        c0.SaveAs( outputLoc + 'GEN_' + hinfo[2] + '_' + v[0] + '_combined' + '.png')
        #leg.~TLegend()

print 'All variables plotted. My work here is done' 