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
#gROOT.SetBatch(True)
#PyConfig.IgnoreCommandLineOptions = True
from DataFormats.FWLite import Handle, Runs, Lumis, Events
#import sys

genHandle = Handle('vector<reco::GenParticle>')
outputLoc = '/eos/user/a/atishelm/www/analysis_plots/'

# Use all of the files in this directory 
#/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_8/190212_095439/0000/*

# Files 
fi = []
# [fileID,path,linecolor,fillcolor]
#fi.append(['X250_qqenugg','root://cmsxrootd.fnal.gov//store/user/atishelm/postGEN_Outputs/ggF_X250_WWgg_jjenugg_1000events_MINIAOD/190202_205801/0000/ggF_X250_WWgg_jjenugg_1000events_MINIAOD_1.root',kGreen,kGreen])

#fi.append(['X1250_qqqqugg','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_3/190211_144340/0000/ggF_X1250_WWgg_qqqqgg_1000events_GEN_6.root',kGreen,kGreen])

# --------------

# Fully Leptonic
#   enuenu
fi.append(['X1250_enuenugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_enuenugg_1000events_GEN/190212_183953/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_enuenugg_1000events_GEN/190212_183953/0000/'],kMagenta,kMagenta-10])

#   munumunu 
fi.append(['X1250_munumunugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_munumunugg_1000events_GEN_1/190212_184207/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_munumunugg_1000events_GEN_1/190212_184207/0000/'],kGreen,kGreen-10])

# Semi Leptonic
#   qqenu
#fi.append(['X1250_qqenugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqenugg_1000events_GEN_1/190212_180745/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqenugg_1000events_GEN_1/190212_180745/0000/'],kMagenta,kMagenta-10])

#   qqmunu
#fi.append(['X1250_qqmunugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqmunugg_1000events_GEN/190212_183122/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqmunugg_1000events_GEN/190212_183122/0000/'],kGreen,kGreen-10])

# Fully hadronic

#fi.append(['X1250_qqqqgg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_2/190211_134802/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_2/190211_134802/0000/'],kBlue,kCyan-10])

# --------------

#fi.append(['X1250_qqqqugg','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_3/190211_144340/0000/ggF_X1250_WWgg_qqqqgg_1000events_GEN_6.root',kGreen,kGreen])


#fi.append(['X1000_munumunugg','root://cmsxrootd.fnal.gov//store/user/atishelm/postGEN_Outputs/ggF_X1000_WWgg_munumunugg1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190129_081915/0000/ggF_X1000_WWgg_munumunugg1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root',kViolet,kViolet])
#fi.append(['X1000_enuenugg','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root',kCyan,kCyan])
#fi.append(['csenugg','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190121_130646/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root',kRed,kRed]) # This only has 999 entries for some reason. This could be important to understand/fix before submitting fragment. 

#fi.append('root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root')

# Let's check out enuenu, munumunu, qqenu, qqmunu files. 
#events = Events(['1.root','2.root'])

# Variables 
# https://root.cern.ch/doc/v612/namespaceROOT_1_1Math_1_1VectorUtil.html

dphi = ROOT.Math.VectorUtil.DeltaPhi
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
vs.append(['pt',100,0,1000])
#vs.append(['invm',170,0,160]) # Invariant mass
#vs.append(['invm',200,1200,1300]) # Invariant mass 
#vs.append(['invm',100,120,160]) # Invariant mass 
#vs.append(['Tmass',100,0,500]) # Transverse mass
#vs.append(['dphi',100,-5,5]) # difference in phi 

#vs.append(['eta',50,-5,5])
#vs.append(['phi',50,-5,5])

# Can implement two vector dependent variables like dphi in any part where length of particle vector is two. 

#vs.append(['',50,-5,5])

#vs.append([])

# Single Particles
sp = []
#sp.append('H') # order of appended variables here might matter at first 
#sp.append('W') 
#sp.append('q') # quark 
#sp.append('e') # electron(s) (change to leptons?)
sp.append('nu') # neutrino(s)

# number of particles, files 
nps = len(sp)
nfi = len(fi)

# Max events 
me = -1 # per file 
max_files=-1