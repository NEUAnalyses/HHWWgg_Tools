#!/usr/bin/env python
# Run from cmssw with cmsenv to access FWLite 
# Might need certain CMSSW version depending on data 
import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.PyConfig.IgnoreCommandLineOptions = True
from DataFormats.FWLite import Handle, Runs, Lumis, Events
import sys

genHandle = Handle('vector<reco::GenParticle>')

events = Events('root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root')

dphi = ROOT.Math.VectorUtil.DeltaPhi
deltaR = ROOT.Math.VectorUtil.DeltaR

hdrpt = ROOT.TH1D("deltaphiHH", "deltaphiHH", 32, 0, 3.2);

for iev, event in enumerate(events):
    if iev >= 1000: break #only look at 1000 events for now 
    event.getByLabel('prunedGenParticles', genHandle)
    genParticles = genHandle.product()

    higgs = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in [25]]
    if len(higgs) != 2:
        print "what is happening"
    else:
        print "Nice I found 2 Higgs particles"
        deltaphi = dphi(higgs[0].p4(), higgs[1].p4())
        hdrpt.Fill(deltaphi)

hdrpt.Draw("")
ROOT.gPad.Print("test.root")