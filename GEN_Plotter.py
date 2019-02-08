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
fi.append(['csenugg','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190121_130646/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root',kRed+4,kRed]) # This only has 999 entries for some reason. This could be important to understand/fix before submitting fragment. 




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
#vs.append([])

# Single Particles
sp = []
sp.append('H') # order of appended variables here might matter at first 
sp.append('W')

# number of particles
nps = len(sp)
nfi = len(fi)

# Max events 
me = 1000

print
print 'Time to plot some fun GEN variables'
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

    v_histos.append([]) # for variable iv 
    for i in range(0,nps): # for each particle
        #print 'i = ',i
        v_histos[iv].append([]) 

    #v_histos[0].append([]) # for plots of zeroeth particle 
        
    for fn,f in enumerate(fi):
        print ' Plotting file: ',f[0] 
        events = Events(f[1])

        # Make histograms just before looping file events for given file 
        histos = []
        for spar in sp:
            ## Currently assuming there are two of each single particle (H and W)
            # I don't think I can make plots of 'H1' and 'H2' variables, since the 'first' and 'second' higgs may change on an event by event basis
            # In case I eventually realize I can, I'll save the lines here: 
            # 
            # <<<

            #if spar == 'H':
            #print 'Creating histo for single particle: '
            #ID1 = spar + '1_' + v[0] + '_' + f[0]  
            #s1 = ID1
            #ID2 = spar + '2_' + v[0] + '_' + f[0] 
            #s2 = ID2
            #exec('ID1 = TH1F(s1,s1,v[1],v[2],v[3])')
            #exec('ID2 = TH1F(s2,s2,v[1],v[2],v[3])')

            #histos.append([ID1,s1,spar])
            #histos.append([ID2,s2,spar])

            #
            # >>>
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
                else:
                    print 'I am not prepared for any of the particles in your desired single particles list'
                    print 'Please either choose a different desired particle, or write something to deal with your desired particle'

        # Finished going through all events 
        # Save single file histos 
        print 'Saving file histos'
        pn = 0 # particle number 
        # number of histograms in histos is number of particles 
        for hi,h in enumerate(histos):
            print 'Saving histo ',hi 
            c1 = TCanvas('c1', 'c1', 800, 600)
            h[0].SetLineColor(f[2])
            h[0].SetFillColor(f[3])
            h[0].Draw()
            #c1.Update()
            c1.SaveAs(outputLoc + h[1] + '.png')
            #v_histos[iv].append([]) # For each particle
            v_histos[iv][hi].append(h)

            # total number of histos per file = num_particles = nps
            #if (hi%(nps/nfi) == 0) and (hi != 0): # on the next particle, increment v_histos to keep particle plots separate 
            #    v_histos[iv].append([]) 
            #    pn += 1
            #    v_histos[iv][pn].append(h)
            #else:
            #    v_histos[iv][pn].append(h)

    print 'Plotted variable: ', v[0], 'for all files'

    # For a given variable there are len(single_particles) plots 

    #v_h = TH1F()


      
    # Is it interesting to plot the same variable for different particles? 
    # Should it be separated by particle? 
    #for particle in v_histos[iv] 

    #for part in v_histos[iv]

    # for each particle 
    #phists = particle histograms. length = number of files 
    #for hi,phists in enumerate(v_histos[iv]):
    for phists in v_histos[iv]:
        print 'phists = ',phists
        c0 = TCanvas('c0', 'c0', 800, 600)
        leg = TLegend(0.6, 0.7, 0.89, 0.89) # might want destructors later to be more memory efficient 
        for hi,h in enumerate(phists):
            # list for each particle [[],[],[],...] # item for each file 
            #print'v_histos = ',v_histos
            #print'v_histos[', iv ,  '] = ',v_histos[iv]
            #print'h = ',h

            leg.AddEntry(h[0],h[1], 'lf') # histo object, legend entry (ID)
            #leg.SetTextSize(0.02)
            h[0].SetTitle(v[0] + ' Combined ')
            h[0].SetFillColor(kWhite)
            if hi == 0:
                #hh1[0].SetTitle(v[1] + ' Combined ')
                #gStyle.SetOptStat(0) # No Stats Box
                h[0].Draw('h')
            if hi > 0:
                #gStyle.SetOptStat(0) # No Stats Box
                h[0].Draw('h same')

        #gStyle.SetOptStat(0) # No Stats Box
        leg.Draw('same')
        c0.SaveAs( outputLoc + 'GEN_' + h[2] + '_' + v[0] + '_combined' + '.png')

print 'All variables plotted. My work here is done' 