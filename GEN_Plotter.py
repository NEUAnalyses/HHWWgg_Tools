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
#import ROOT
gROOT.SetBatch(True)
#PyConfig.IgnoreCommandLineOptions = True
from DataFormats.FWLite import Handle, Runs, Lumis, Events
import sys

genHandle = Handle('vector<reco::GenParticle>')
outputLoc = '/eos/user/a/atishelm/www/analysis_plots/'

# Files 
fi = []
# [fileID,path,linecolor,fillcolor]
fi.append(['X250_qqenugg','root://cmsxrootd.fnal.gov//store/user/atishelm/postGEN_Outputs/ggF_X250_WWgg_jjenugg_1000events_MINIAOD/190202_205801/0000/ggF_X250_WWgg_jjenugg_1000events_MINIAOD_1.root',kGreen,kGreen])
#fi.append(['X1000_munumunugg','root://cmsxrootd.fnal.gov//store/user/atishelm/postGEN_Outputs/ggF_X1000_WWgg_munumunugg1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190129_081915/0000/ggF_X1000_WWgg_munumunugg1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root',kViolet,kViolet])
#fi.append(['X1000_enuenugg','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root',kCyan,kCyan])
#fi.append(['csenugg','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190121_130646/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root',kRed,kRed]) # This only has 999 entries for some reason. This could be important to understand/fix before submitting fragment. 

#fi.append('root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root')

# Let's check out enuenu, munumunu, qqenu, qqmunu files. 
#events = Events(['1.root','2.root'])

# Variables 
# https://root.cern.ch/doc/v612/namespaceROOT_1_1Math_1_1VectorUtil.html

#dphi = ROOT.Math.VectorUtil.DeltaPhi
#deltaR = ROOT.Math.VectorUtil.DeltaR
#Wphi = ROOT.Math.VectorUtil.Phi_0_2pi
invmass = ROOT.Math.VectorUtil.InvariantMass
#invmass = Math.VectorUtil.InvariantMass

# Histograms 
#hdrpt = ROOT.TH1F("deltaphiHH", "deltaphiHH", 32, 0, 3.2)
#HHdphivsRadionpT

# Variables 
# need to be methods of reco::GenParticle 
# need to do something different if it requires full vectors like angle between or invariant mass 
vs = []
#vs.append(['px',100,-1000,1000]) 
#vs.append(['py',100,-1000,1000])
#vs.append(['pz',100,-1000,1000])
#vs.append(['pt',100,0,1000])
vs.append(['invm',100,0,500])
#vs.append(['eta',50,-5,5])
#vs.append(['phi',50,-5,5])

# Can implement two vector dependent variables like dphi in any part where length of particle vector is two. 

#vs.append(['',50,-5,5])

#vs.append([])

# Single Particles
sp = []
#sp.append('H') # order of appended variables here might matter at first 
#sp.append('W') 
sp.append('qq') # diquark pair 
#sp.append('e') # electron(s)
sp.append('nu') # neutrino(s)

# number of particles, files 
nps = len(sp)
nfi = len(fi)

# Max events 
me = 1000

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
        
    for fn,f in enumerate(fi):
        print '   Filling histos for file: ',f[0] 
        events = Events(f[1])

        # Make histograms just before looping file events for given file 
        histos = []
        for spar in sp:
            ID = 'GEN_' + spar + '_' + v[0] + '_' + f[0]
            h = TH1F(ID,ID,v[1],v[2],v[3])
            histos.append([h,ID,spar])
            #histos = [particle1,particle2,...] 

        # Loop events 
        # fills histos appropriately each time 
        for iev, event in enumerate(events):
            if iev >= me: break # Max events 
            event.getByLabel('prunedGenParticles', genHandle)
            genParticles = genHandle.product()

            # Plot for each desired particle 
            for pi,pa in enumerate(sp):
                # H first 
                # pi == 0
                if pa == 'H':

                    higgs = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [25]]
                    if len(higgs) == 2:
                        for hi,h in enumerate(higgs):
                            val = eval('h.' + v[0] + '()')
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
                    else:
                        print 'Not exactly 2 quarks in this event'

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

        # Finished going through all events 
        # Save single file histos 
        print '   Saving ', f[0], ' histos'
        pn = 0 # particle number 
        # number of histograms in histos is number of particles 
        for hi,h in enumerate(histos):
            print '      Saving histo ',hi 
            #print 'h = ',h
            c1 = TCanvas('c1', 'c1', 800, 600)
            h[0].SetLineColor(f[2])
            h[0].SetFillColor(f[3])
            h[0].Draw()
            #c1.Update()
            c1.SaveAs(outputLoc + h[1] + '.png')
            h[0].SetDirectory(0) # This avoids problem later on when introducing legend 
            #c1.Destructor()
            #h.SaveAs("histopath.root")
            #v_histos[iv].append([]) # For each particle
            #v_histos[iv][hi].append(h)
            # Check which particle, add to its list of plots for this variable 
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

    #v_h = TH1F()

    # Is it interesting to plot the same variable for different particles? 
    # Should it be separated by particle? 
    #for particle in v_histos[iv] 

    #for part in v_histos[iv]

    # for each particle 
    #phists = particle histograms. length = number of files 
    #for hi,phists in enumerate(v_histos[iv]):
    #print 'v_histos[iv] = ',v_histos[iv]
    #print 'v_histos[iv][0] = ',v_histos[iv][0]
    #print 'v_histos[iv][0][2][0] = ',v_histos[iv][0][2][0]
    #leg = TLegend(0.6, 0.7, 0.89, 0.89)
    #print 'v_histos[',iv,'] = ',v_histos[iv]
    for phists in v_histos[iv]:
        #print 'phists = ',phists
        #leg = TLegend(0.6, 0.7, 0.89, 0.89)
        #these_hists = []
        #these_hists_ = []

        # for i in range(0,nfi):
        #     print'i = ',i
        #     print 'phists[',i,'] = ',phists[i]
        #     print 'phists[',i,'][0] = ',phists[i][0]
        #     these_hists.append(phists[i])
        #     print'these_hists = ',these_hists 
        #     these_hists_.append(phists[i][0])

        #print'these_hists_ = ',these_hists_
        #print 'phists[2] = ',phists[2]

        #print 'phists[2][0] = ',phists[2][0]
        c0 = TCanvas('c0', 'c0', 800, 600)
        #leg = TLegend(0.6, 0.7, 0.89, 0.89) # might want destructors later to be more memory efficient 
        #for hi,h in enumerate(phists):
        #for hi,hinfo in enumerate(phists):
        #for hi in range(0,len(phists)):

        # Draw, add to legend 
        #print'these_hists = ',these_hists 

        # The legend was messing everything up 
        # This somehow caused the third histogram to be lost from memory 

        #print'these_hists_ before loop = ',these_hists_
        #for hi,hinfo in enumerate(these_hists):
        for hi,hinfo in enumerate(phists):
            histo = hinfo[0]
            # if hi == 0:
            #     leg = TLegend(0.6, 0.7, 0.89, 0.89) # might want destructors later to be more memory efficient 
            #print'these_hists_ in loop = ',these_hists_

            #print 'hinfo = ',hinfo 
            #print'these_hists_[',hi,'] = ',these_hists_[hi]
            # list for each particle [[],[],[],...] # item for each file 
            #print'v_histos = ',v_histos
            #print'v_histos[', iv ,  '] = ',v_histos[iv]
            #print'hi = ',hi
            #print'hinfo = ',hinfo
            #print'phists[hi] = ',phists[hi]
            #hinfo = phists[hi]
            #print'phists[hi][0] = ',phists[hi][0]
            #print'hinfo[0] = ',hinfo[0]

            #leg.AddEntry(these_hists_[hi],hinfo[1], 'lf') # histo object, legend entry (ID)
            #leg.SetTextSize(0.02)
            #these_hists_[hi].SetTitle(v[0] + ' Combined ')
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