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
gROOT.SetBatch(True)
#PyConfig.IgnoreCommandLineOptions = True
from DataFormats.FWLite import Handle, Runs, Lumis, Events
import sys

genHandle = Handle('vector<reco::GenParticle>')
outputLoc = '/eos/user/a/atishelm/www/analysis_plots/'

# Files 
fi = []

fi.append(['enuenugg','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root',kBlue,kCyan])
#fi.append('root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root')

# Let's check out enuenu, munumunu, qqenu, qqmunu files. 
#events = Events(['1.root','2.root'])

# Variables 
# https://root.cern.ch/doc/v612/namespaceROOT_1_1Math_1_1VectorUtil.html

#dphi = ROOT.Math.VectorUtil.DeltaPhi
#deltaR = ROOT.Math.VectorUtil.DeltaR
#Wphi = ROOT.Math.VectorUtil.Phi_0_2pi
#invmass = ROOT.Math.VectorUtil.InvariantMass

# Histograms 
#hdrpt = ROOT.TH1F("deltaphiHH", "deltaphiHH", 32, 0, 3.2)
#HHdphivsRadionpT

# Variables 
# need to be methods of reco::GenParticle 
# need to do something different if it requires full vectors like angle between or invariant mass 
vs = []
vs.append(['px',100,-1000,1000]) 
vs.append(['py',100,-1000,1000])
vs.append(['pz',100,-1000,1000])
vs.append(['pt',100,0,1000])

# Single Particles
sp = []
sp.append('H') # order of appended variables here might matter at first 
sp.append('W')

# Max events 
me = 1000

# Plot each variable for each file, then together 
for v in vs:
    print 'Plotting variable: ',v[0]
        
    for f in fi:
        print 'Plotting file: ',f[0] 
        events = Events(f[1])

        # Make histograms just before looping file events 
        # number of histos to declare = One variable * One file * len(single particles) 
        histos = []
        for spar in sp:
            # Currently assuming there are two of each single particle (H and W)
            #if spar == 'H':
            #print 'Creating histo for single particle: '
            ID1 = spar + '1_' + v[0] + '_' + f[0]  
            s1 = ID1
            ID2 = spar + '2_' + v[0] + '_' + f[0] 
            s2 = ID2
            exec('ID1 = TH1F(s1,s1,v[1],v[2],v[3])')
            exec('ID2 = TH1F(s2,s2,v[1],v[2],v[3])')
            histos.append([ID1,s1,spar])
            histos.append([ID2,s2,spar])

        # Loop events 
        # fills histos appropriately each time 
        for iev, event in enumerate(events):
            if iev >= me: break # Max events 
            event.getByLabel('prunedGenParticles', genHandle)
            genParticles = genHandle.product()

            # Plot for each desired particle 
            for pa in sp:
                if pa == 'H':

                    higgs = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [25]]
                    if len(higgs) == 2:
                        for hi,h in enumerate(higgs):
                            val = eval('h.' + v[0] + '()')
                            histos[hi][0].Fill(val) 
                                                
                    elif len(higgs) != 2:
                        print "Length of higgs vector is not 2. Skipping event"

                    else:
                        print "Is it even possible for this condition to occur?"

                if pa == 'W':

                    Ws = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [24]]
                    if len(Ws) == 2:
                        for Wi,W in enumerate(Ws):
                            val = eval('W.' + v[0] + '()')
                            histos[Wi+2][0].Fill(val) #[histo_index][histo_object]
                            
                    elif len(Ws) != 2:
                        print "Length of W vector is not 2. Skipping event"

                    else:
                        print "Is it even possible for this condition to occur?"

        # Save histos 
        print 'Saving histos'
        for hi,h in enumerate(histos):
            print 'Saving histo ',hi 
            c1 = TCanvas('c1', 'c1', 800, 600)
            h[0].SetLineColor(f[2])
            h[0].SetFillColor(f[3])
            h[0].Draw()
            #c1.Update()
            c1.SaveAs(outputLoc + h[1] + '.png')



#---

# # Loop events 
# for iev, event in enumerate(events):
#     if iev >= 1000: break #only look at 1000 events for now 
#     event.getByLabel('prunedGenParticles', genHandle)
#     genParticles = genHandle.product()

#     # I want plots for:
#     # Radion, higgs, W's, (leptons + neutrinos, quarks)

#     #radion = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [25]] #pdgid? 

#     higgs = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [25]]
#     if len(higgs) != 2:
#         print "No higgs found"
#         #print "what is happening"
#     else:
#         #deltaphi = dphi(higgs[0].p4(), higgs[1].p4())
#         hXmval = invmass(higgs[0].p4(), higgs[1].p4())
#         #print 'two higgs found'
#         hXm.Fill(hXmval)

#     # W+- boson 
#     W = [p for p in genParticles if p.isHardProcess() and p.pdgId() in [24]] # Adds W plus and minus 
#     if len(W) != 1:
#         print "There is not exactly 1 W's in this event. Skipping."
#     else:
#         #print 'Found Ws' 
#         #val1 = invmass(W[0].p4(), W[1].p4())

#         val = W[0].px()
#         htest.Fill(val)

#         # How do you plot four momentum components? .p4(i)? 
#         #print W[0].px() 
#         #for i in W[0]:
#             #print 'i = ',i
#         # .px(), .py(), .energy(), 
#         #for i in W[0].p4():
#             #print'i ',i

#         #print'val1 = ',val1

#         #hHm.Fill(val1)
#         #hWphi.Fill(val2)

# htest.Draw("")
# ROOT.gPad.Print("test.root")

# # hHm.Draw("")
# # ROOT.gPad.Print("test2.root")

#---