#!/usr/bin/env python

# Python only 

# 7 February 2019
# Abe Tishelman-Charny 

# This takes some inspiration from TreePlotter.py and PlotterTools.py
# Run from cmssw with cmsenv to access FWLite 
# Might need certain CMSSW version depending on data 
# Currently running from CMSSW_10

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
import os 
from os import listdir

print
print 'It\'s time to plot some fun GEN variables'
print

# Will contain all histos so you can combine whichever you'd like, such as like variables for different particles
v_histos = [] # [variableindex][particleindex][histogramindex], len(histogramindices) = number of files 

# Plot each variable for each directory of files, then together 
for iv,v in enumerate(vs):
    print 'Plotting variable ', iv, ': ',v[0]

    v_histos.append([]) # add entry for variable iv 
    for i in range(0,nps): # add entry for each particle 
        v_histos[iv].append([]) # list for all plots for given particle 

    # For each directory of files 
    # Instead of a single file, just give its directory 
    for dn,d in enumerate(d):
        # Could make definition to take d, return all of these variables 
        ch = d[0]
        DID = d[1] # file ID
        direc = d[2][0] # full path of directory 
        rd = d[2][1] # direc path with root://cmsxrootd.fnal.gov/ prefix for 'Events' module  
        lc = d[3] # histo line color
        fc = d[4] # histo fill color 

        # Save paths of non-LHE files
        #direc = f[1][0] # full directory path 
        path_ends = [fp for fp in listdir(direc) if 'inLHE' not in fp] 
        paths = []
        for pa in path_ends:
            tmp_path = rd + pa
            paths.append(tmp_path)

        print '  Creating histos for file(s) of type: ',DID 

        # Get chosen particles to plot and number of them 
        pparams = []
        pparams = get_pparams(ch,ptp) #particle parameters 
        print 'pparams = ',pparams 

        # Create histrograms to be filled in event loop 
        histos = []
        for params in pparams:
            pstring = params[0] # string of particle 
            nump = params[1] # number of this particle per event

            # For now, three cases for number of particles
            # 1,2,4 
            # if there is 1, just one histogram
            # 2, leading and subleading pT histograms 
            # 4, leading, subleading, subsubleading, and subsubsubleading pT histograms 

            # just make ID then run definition 

            if nump == 1:
                ID = 'GEN_' + pstring + '_' + v[0] + '_' + DID # unique histo ID 
                h = TH1F(ID,ID,v[1],v[2],v[3])
                histos.append([[h,ID,pstring]])

            elif nump == 2:
                LID = 'GEN_' + pstring + '_' + 'leading-' + v[0] + '_' + DID # unique histo ID 
                h1 = TH1F(LID,LID,v[1],v[2],v[3])
                #histos.append([h,LID,pstring])

                SLID = 'GEN_' + pstring + '_' + 'subleading-' + v[0] + '_' + DID # unique histo ID 
                h2 = TH1F(SLID,SLID,v[1],v[2],v[3])
                histos.append([[h1,LID,pstring],[h2,SLID,'sl'+pstring]])
            
            elif nump == 4:
                LID = 'GEN_' + pstring + '_' + 'leading-' + v[0] + '_' + DID # unique histo ID 
                h1 = TH1F(LID,LID,v[1],v[2],v[3])

                #histos.append([h,LID,pstring])

                SLID = 'GEN_' + pstring + '_' + 'subleading-' + v[0] + '_' + DID # unique histo ID 
                h2 = TH1F(SLID,SLID,v[1],v[2],v[3])
                #histos.append([h,SLID,pstring])

                SSLID = 'GEN_' + pstring + '_' + 'subsubleading-' + v[0] + '_' + DID # unique histo ID 
                h3 = TH1F(SSLID,SSLID,v[1],v[2],v[3])
                #histos.append([h,SSLID,pstring])

                SSSLID = 'GEN_' + pstring + '_' + 'subsubsubleading-' + v[0] + '_' + DID # unique histo ID 
                h4 = TH1F(SSSLID,SSSLID,v[1],v[2],v[3])
                histos.append([h4,SSSLID,pstring])
                histos.append([[h1,LID,pstring],[h2,SLID,'sl'+pstring],[h3,SSLID,'ssl'+pstring],[h4,SSSLID,'sssl'+pstring]])

            else:
                print 'Don\'t have a way to deal with ', nump, ' ', pstring, ' particles'
                print 'Exiting'
                sys.exit()

        # Might want to look into eventchain  

        # For each file in directory
        print 'paths = ',paths 
        for ip,path in enumerate(paths):
            print '    Processing file ', ip, ': ',path 
            events = Events(path) # needs to be file with root prefix 

            # Loop events
            for iev, event in enumerate(events):
                if iev == me: break # Max events 
                #event.getByLabel('prunedGenParticles', genHandle)
                events.getByLabel('genParticles', genHandle)
                genParticles = genHandle.product()

                # Fill histograms with current variable 
                for params in pparams:
                    particle = params[0]
                    #nparticles = params[1]
                    pdgIDs = params[2]
                    ps = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in pdgIDs]

                    # Get particles in order of pT 

                    # If one particle, just add entry 
                    if len(ps) == 1:
                        val = eval('ps[0].' + v[0] + '()')
                        for h_ in histos:
                            #print 'h_ = ',h_
                        
                            if (len(h_) == 1) and  h_[0][2] == particle:
                                print 'val = ',val
                                h_[0][0].Fill(val)    
                                 
                    elif len(ps) == 2:
                        ops = order_particles(ps)


                    elif len(ps) == 4:
                        print 'not setup yet'


                    else:
                        print 'Not prepared for ', len(ps), ' ', particle, ' particles'
                        print 'Exiting'
                        sys.exit()


                        #ops = order_particles(ps) # particles ordered by pT

                    #ps[0].p4()

                    # pi == 0
                    # if pa == 'H':

                    #     higgs = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [25]]
                    #     if len(higgs) == 2:

                    #         if v[0] == 'invm':
                    #             val = ROOT.Math.VectorUtil.InvariantMass(higgs[0].p4(),higgs[1].p4())
                    #             histos[pi][0].Fill(val) 

                    #         else: 
                    #             for hi,h in enumerate(higgs):
                    #                 #print'filling'
                    #                 val = eval('h.' + v[0] + '()')
                    #                 #print'val = ',val
                    #                 #print 'num entries = ',histos[pi][0].GetEntries()
                    #                 histos[pi][0].Fill(val) 
                                                    
                    #     elif len(higgs) != 2:
                    #         print "Length of higgs vector is not 2. Skipping event"

                    #     else:
                    #         print "Is it even possible for this condition to occur?"

                    # # pi == 1
                    # elif pa == 'W':

                    #     Ws = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [24]]
                    #     if len(Ws) == 2:
                    #         if v[0] == 'invm':
                    #             val = ROOT.Math.VectorUtil.InvariantMass(Ws[0].p4(),Ws[1].p4())
                    #             histos[pi][0].Fill(val) 

                    #         else:
                    #             for Wi,W in enumerate(Ws):
                    #                 val = eval('W.' + v[0] + '()')
                    #                 # Knowing histos[1] is W boson
                    #                 histos[pi][0].Fill(val) #[histo_index][0=histo_object]
                                
                    #     elif len(Ws) != 2:
                    #         print "Length of W vector is not 2. Skipping event"

                    #     else:
                    #         print "Is it even possible for this condition to occur?"

                    # # pi == 2
                    # elif pa == 'q':

                    #     #qs = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [1,2,3,4,5,6]]
                    #     qs = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [1,2,3,4,5]]

                    #     # Number of quarks
                    #     if len(qs) == 2:
                    #     # Add all quark values 

                    #         if v[0] == 'invm':
                    #             val = ROOT.Math.VectorUtil.InvariantMass(qs[0].p4(),qs[1].p4())
                    #             #val = Math.VectorUtil.InvariantMass(qs[0],qs[1])
                    #             #val = InvariantMass(qs[0].p4(),qs[1].p4())
                    #             #val = invmass(qs[0],qs[1])
                    #             histos[pi][0].Fill(val) 

                    #         else: 
                    #             for hi,q in enumerate(qs):
                    #                 val = eval('q.' + v[0] + '()')
                    #                 histos[pi][0].Fill(val) 

                    #     elif len(qs) == 4:
                    #     # get the four quarks 
                    #     # order by pT 
                    #     # Take invariant mass of 

                    #         if v[0] == 'invm':
                    #             val = ROOT.Math.VectorUtil.InvariantMass(qs[0].p4(),qs[1].p4())
                    #             #val = Math.VectorUtil.InvariantMass(qs[0],qs[1])
                    #             #val = InvariantMass(qs[0].p4(),qs[1].p4())
                    #             #val = invmass(qs[0],qs[1])
                    #             histos[pi][0].Fill(val) 

                    #         else: 
                    #             for hi,q in enumerate(qs):
                    #                 val = eval('q.' + v[0] + '()')
                    #                 histos[pi][0].Fill(val) 
                    #     else:
                    #         print 'Not exactly 4 quarks in this event'

                    # # # pi == 3
                    # # elif pa == 'e': # maybe change to leptons then subcat for flavor 

                    # #     es = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [11]] # Make 11,13 for leptons 

                    # #     # Number of electrons. Depends on decay channel.
                    # #     # Fully leptonic: 2
                    # #     # Semi leptonic: 1 
                    # #     if len(es) == 2:

                    # #         # if pt 
                    # #         if (v[0] == 'pt'):
                    # #             # if plot leading and subleading separately for later combination 
                    # #             if (v[4] == 'ls'):
                    # #                 # get values 1 and 2 
                    # #                 val1 = eval('es[0].' + v[0] + '()')
                    # #                 val2 = eval('es[1].' + v[0] + '()')
                    # #                 # value 1 is leading 
                    # #                 if val1 > val2:
                    # #                     histos[pi][0].Fill(val1)
                    # #                     histos[pi][3].Fill(val2)
                    # #                 # value 2 is leading
                    # #                 elif val2 > val1:
                    # #                     histos[pi][0].Fill(val2)
                    # #                     histos[pi][3].Fill(val1)
                    # #                 # value 1 = value 2
                    # #                 else:
                    # #                     print 'Values are equal'
                    # #                     histos[pi][0].Fill(val1)
                    # #                     histos[pi][3].Fill(val2)

                    # #             else:
                    # #                 print 'Don\'t know what to plot for pt'

                    # #         # if both together
                    # #         else: 

                    # #             for hi,e in enumerate(es):
                    # #                 #print 'Fully leptonic decay detected'
                    # #                 val = eval('e.' + v[0] + '()')
                    # #                 histos[pi][0].Fill(val) 


                    # # pi == 3
                    # elif pa == 'l': # leptons

                    #     ls = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [11,13]] # Make 11,13 for leptons 

                    #     # Number of electrons. Depends on decay channel.
                    #     # Fully leptonic: 2
                    #     # Semi leptonic: 1 
                    #     if len(ls) == 2:

                    #         # if pt 
                    #         if (v[0] == 'pt'):
                    #             # if plot leading and subleading separately for later combination 
                    #             if (v[4] == 'ls'):
                    #                 # get values 1 and 2 
                    #                 val1 = eval('ls[0].' + v[0] + '()')
                    #                 val2 = eval('ls[1].' + v[0] + '()')
                    #                 # value 1 is leading 
                    #                 if val1 > val2:
                    #                     histos[pi][0].Fill(val1)
                    #                     histos[pi][3].Fill(val2)
                    #                 # value 2 is leading
                    #                 elif val2 > val1:
                    #                     histos[pi][0].Fill(val2)
                    #                     histos[pi][3].Fill(val1)
                    #                 # value 1 = value 2
                    #                 else:
                    #                     print 'Values are equal'
                    #                     histos[pi][0].Fill(val1)
                    #                     histos[pi][3].Fill(val2)

                    #             else:
                    #                 print 'Don\'t know what to plot for pt'

                    #         # if both together
                    #         else: 

                    #             for hi,e in enumerate(es):
                    #                 #print 'Fully leptonic decay detected'
                    #                 val = eval('e.' + v[0] + '()')
                    #                 histos[pi][0].Fill(val) 

                    # # pi == 4
                    # elif pa == 'nu':

                    #     nus = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [12,14]] # electron or muon neutrinos (or antis)

                    #     # Number of electrons. Depends on decay channel.
                    #     # Fully leptonic: 2
                    #     # Semi leptonic: 1 
                    #     if len(nus) == 2:
                    #         for hi,nu in enumerate(nus):
                    #             #print 'Fully leptonic decay detected'
                    #             val = eval('nu.' + v[0] + '()')
                    #             histos[pi][0].Fill(val) 

                    # # pi == 5
                    # elif pa == 'mu': # maybe change to leptons then subcat for flavor 

                    #     mus = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [13]]

                    #     # Can make function to do the same thing with either es or mus as input..

                    #     # Number of electrons. Depends on decay channel.
                    #     # Fully leptonic: 2
                    #     # Semi leptonic: 1 
                    #     if len(mus) == 2:

                    #         # if pt 
                    #         if (v[0] == 'pt'):
                    #             # if plot leading and subleading separately for later combination 
                    #             if (v[4] == 'ls'):
                    #                 # get values 1 and 2 
                    #                 val1 = eval('mus[0].' + v[0] + '()')
                    #                 val2 = eval('mus[1].' + v[0] + '()')
                    #                 # value 1 is leading 
                    #                 if val1 > val2:
                    #                     histos[pi][0].Fill(val1)
                    #                     histos[pi][3].Fill(val2)
                    #                 # value 2 is leading
                    #                 elif val2 > val1:
                    #                     histos[pi][0].Fill(val2)
                    #                     histos[pi][3].Fill(val1)
                    #                 # value 1 = value 2
                    #                 else:
                    #                     print 'Values are equal'
                    #                     histos[pi][0].Fill(val1)
                    #                     histos[pi][3].Fill(val2)

                    #             else:
                    #                 print 'Don\'t know what to plot for pt'

                    #         # if both together
                    #         else: 

                    #             for hi,mu in enumerate(mus):
                    #                 #print 'Fully leptonic decay detected'
                    #                 val = eval('mu.' + v[0] + '()')
                    #                 histos[pi][0].Fill(val) 

                                
                                                    
                    # else:
                    #     print 'I am not prepared for any of the particles in your desired single particles list'
                    #     print 'Please either choose a different desired particle, or write something to deal with your desired particle'
            print 'Finished going through events in file: ', path
            # Check path index 
            if (ip+1 == max_files): break 
               
        # Finished going through all events in directory
        # Save single file histos 
        print 'Finished going through all files in directory: ',direc
        print '   Saving ', DID, ' histos'
        pn = 0 # particle number 
        # number of histograms in histos is number of particles
        #print 'histos = ',histos  
        for hi,hinfo in enumerate(histos):
            print '      Saving histo ',hi 
            # if h contains leading and subleading histos
            #print 'h = ',h
            #print 'v_histos = ',v_histos
            #h[0].SetDirectory(0)
            c1 = TCanvas('c1', 'c1', 800, 600)
            h[0].SetDirectory(0)
            #print 'h[0] = ',h[0]
            h[0].SetLineColor(lc)
            h[0].SetFillColor(fc)
            h[0].GetYaxis().SetTitle('Events')
            particle_ = h[2]
            if v[0] == 'invm':
                #if particle_ == 'q':
                    #h[0].GetXaxis().SetTitle( 'm_{' + particle_ + '}')
                #else:
                h[0].GetXaxis().SetTitle( 'm_{' + particle_ + particle_ + '}')
            else:
                h[0].GetXaxis().SetTitle( v[0] + '_{' + particle_ + '}')
            
            h[0].Draw()
            #c1.Update()
            file_path1 = outputLoc + h[1] + '.png'
            file_path2 = outputLoc + h[1] + '.root'
            file_exists1 = False 
            file_exists2 = False 
            file_exists1 = os.path.isfile(file_path1)
            file_exists2 = os.path.isfile(file_path2)
            if file_exists1:
                #print 'file_path = ',file_path 
                os.system("rm " + file_path1)
            if file_exists2:
                #print 'file_path = ',file_path2 
                os.system("rm " + file_path2)
                #subprocess.Popen("rm " + file_path) # if file already exists, remove it before saving 
            h[0].SaveAs(file_path2)
            c1.SaveAs(file_path1)

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
            elif h[2] == 'q':
                v_histos[iv][2].append(h)
            # elif h[2] == 'e':
            #     v_histos[iv][3].append(h)
            elif h[2] == 'l':
                v_histos[iv][3].append(h)
            elif h[2] == 'nu':
                v_histos[iv][4].append(h)
            elif h[2] == 'mu':
                v_histos[iv][5].append(h)
            else:
                'Can\'t find this plot\'s particle:', h[2] ,' in list of expected particles'
            # If there's a second histogram to save, it's the subleading one
            # This code is terrible right now. This should be a function: plot_h(h[0],h[1],h[2])
            if len(h) == 6:

                this_histo = h[3]
                particle_ = h[5]

                c1 = TCanvas('c1', 'c1', 800, 600)
                this_histo.SetDirectory(0)
                #print 'h[0] = ',h[0]
                #this_histo.SetLineColor(f[2])
                #this_histo.SetFillColor(f[3])
                this_histo.SetLineColor(colors[dn]) # kGreen+/-4 -4 then +4 
                this_histo.SetFillColor(colors[dn])
                this_histo.GetYaxis().SetTitle('Events')
                
                if v[0] == 'invm':
                    #if particle_ == 'q':
                        #h[0].GetXaxis().SetTitle( 'm_{' + particle_ + '}')
                    #else:
                    this_histo.GetXaxis().SetTitle( 'm_{' + particle_ + particle_ + '}')
                else:
                    this_histo.GetXaxis().SetTitle( v[0] + '_{' + particle_ + '}')
                
                this_histo.Draw()
                #c1.Update()
                file_path1 = outputLoc + h[4] + '.png'
                file_path2 = outputLoc + h[4] + '.root'
                file_exists1 = False 
                file_exists2 = False 
                file_exists1 = os.path.isfile(file_path1)
                file_exists2 = os.path.isfile(file_path2)
                if file_exists1:
                    #print 'file_path = ',file_path 
                    os.system("rm " + file_path1)
                if file_exists2:
                    #print 'file_path = ',file_path2 
                    os.system("rm " + file_path2)
                    #subprocess.Popen("rm " + file_path) # if file already exists, remove it before saving 
                this_histo.SaveAs(file_path2)
                c1.SaveAs(file_path1)

                #h[0].SetDirectory(0) # This avoids problem later on when introducing legend 
                #c1.Destructor()
                #h.SaveAs("histopath.root")
                #v_histos[iv].append([]) # For each particle
                #v_histos[iv][hi].append(h)
                # Check which particle, add to its list of plots for this variable 

                # # This method puts (variable, particle) ('iv','i') plots in v_histos[iv][i]
                # if particle_ == 'H': # Currently [iv][0] associated with H, [iv][1] with W. 
                #     v_histos[iv][0].append(h)
                # elif particle_ == 'W':
                #     v_histos[iv][1].append(h)
                # elif particle_ == 'q':
                #     v_histos[iv][2].append(h)
                # elif particle_ == 'e':
                #     v_histos[iv][3].append(h)
                # elif particle_ == 'nu':
                #     v_histos[iv][4].append(h)
                # elif particle_ == 'mu':
                #     v_histos[iv][5].append(h)
                # else:
                #     'Can\'t find this plot\'s particle:', particle_ ,' in list of expected particles'


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
    print 'v_histos[',iv,'] = ',v_histos[iv]
    for phists in v_histos[iv]:

        print 'phists = ',phists
        print 'len(phists) = ',len(phists)

        if len(phists) == 0: continue # skip 

        #print 'phists[2][0] = ',phists[2][0]
        c0 = TCanvas('c0', 'c0', 800, 600)
        #leg = TLegend(0.6, 0.7, 0.89, 0.89) # might want destructors later to be more memory efficient 

        for hi,hinfo in enumerate(phists):
            #histo = hinfo[0]
            print 'hi = ',hi # directory/files. Need to add both leading and subleading 
            #histo = hinfo[hi*3] # leading first 
            #title_info = hinfo[hi*3+2] # subleading second 
            #histo = hinfo[hi*(-3)+3]
            #title_info = hinfo[hi*(-3)+5]
            histo1=hinfo[0]
            histo2=hinfo[3]
            title_info1=hinfo[1]
            title_info2=hinfo[4]
            #these_hists_[hi].SetFillColor(kWhite)
            histo1.SetTitle( title_info1 + v[0] + ' Combined ') # <particle> <variable> combined 
            histo2.SetTitle( title_info2 + v[0] + ' Combined ') # <particle> <variable> combined 
            histo1.SetFillColor(kWhite)
            histo2.SetFillColor(kWhite)

            if hi == 0:
            #if hi == 1: # draw subleading first so y axis will contain all entries 
                #histo.SetStats(0)
                #histo.Draw('h')
                #print'histo = ',histo
                histo1.SetStats(0)
                histo1.GetYaxis().SetRangeUser(0,130)
                histo1.Draw('h')
                print'histo1 = ',histo1
                
                histo2.SetStats(0)
                histo2.Draw('h same')
                print'histo2 = ',histo2
            if hi > 0:
            #if hi == 0:
                #histo.SetStats(0)
                #histo.Draw('h same')
                #print'histo = ',histo

                histo1.SetStats(0)
                histo1.Draw('h same')
                print'histo1 = ',histo1
                histo2.SetStats(0)
                histo2.Draw('h same')
                print'histo2 = ',histo2

        leg = TLegend(0.6, 0.7, 0.89, 0.89)
        #j=0
        for i in range(0,len(phists)):
            for j in range(0,2):
                leg.AddEntry(phists[i][j*3],phists[i][j*3+1], 'lf') # histo object, legend entry (ID) # add first and second 
            #j=0
            # This is going to need to be fixed because it's currently configured for leading-subleading plots
            #leg.AddEntry(phists[i][i*3],phists[i][i*3+1], 'lf') # histo object, legend entry (ID)
            #leg.AddEntry(phists[i][j],phists[i][j+1], 'lf') # histo object, legend entry (ID) # add first and second 
            #leg.AddEntry(phists[i][j*3],phists[i][j*3+1], 'lf') # histo object, legend entry (ID)
            #j+=1
            #leg.SetTextSize(0.02)
        #gStyle.SetOptStat(0) # No Stats Box
        leg.Draw('same')

        file_path1 = outputLoc + 'GEN_' + hinfo[2] + '_' + v[0] + '_combined' + '.png'
        #file_path2 = outputLoc + h[1] + '.root'
        file_exists1 = False 
        #file_exists2 = False 
        file_exists1 = os.path.isfile(file_path1)
        #file_exists2 = os.path.isfile(file_path2)
        if file_exists1:
            os.system("rm " + file_path1)
        # if file_exists2:
        #     os.system("rm " + file_path2)


        c0.SaveAs(file_path1)
        #leg.~TLegend()

print 'All variables plotted. My work here is done' 