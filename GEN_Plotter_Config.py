#!/usr/bin/env python

# 7 February 2019
# Abe Tishelman-Charny 

# Configuration for GEN_Plotter.py 
from ROOT import * 
from DataFormats.FWLite import Handle, Runs, Lumis, Events

genHandle = Handle('vector<reco::GenParticle>')
outputLoc = '/eos/user/a/atishelm/www/analysis_plots/'

#chosen_particles

# Use all of the files in this directory 
#/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_8/190212_095439/0000/*

# Depending on channel, specify number of particles? 
#ch = 'FL'
#ch = 'SL'
#ch = 'FH'

#channel setup definitions here 
# select certain particles after 

# Particles to Plot
# Need to set here for now 
ptp = []

#ptp.append('H')
ptp.append('l')


#ptp.append(all_particles["H"]) 
#ptp.append(all_particles["W"]) 
#ptp.append(all_particles["g"]) 
#ptp.append(all_particles["q"]) 
#ptp.append(all_particles["l"]) 
#ptp.append(all_particles["nu"]) 

# Files 
# Directories 
#fi = []

d = []

# [fileID,path,linecolor,fillcolor]

# --------------

# Fully Leptonic
#   enuenu
#d.append(['FL','X1250_enuenugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_enuenugg_1000events_GEN_1/190212_184044/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_enuenugg_1000events_GEN_1/190212_184044/0000/'],kMagenta,kMagenta-10])

#   munumunu 
#d.append(['FL','X1250_munumunugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_munumunugg_1000events_GEN_1/190212_184207/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_munumunugg_1000events_GEN_1/190212_184207/0000/'],kGreen,kGreen-10])

# Semi Leptonic
#   qqenu
d.append(['SL','X1250_qqenugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqenugg_1000events_GEN_1/190212_180745/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqenugg_1000events_GEN_1/190212_180745/0000/'],kMagenta,kMagenta-10])

#   qqmunu
#fi.append(['X1250_qqmunugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqmunugg_1000events_GEN/190212_183122/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqmunugg_1000events_GEN/190212_183122/0000/'],kGreen,kGreen-10])

# Fully hadronic

#fi.append(['X1250_qqqqgg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_2/190211_134802/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_2/190211_134802/0000/'],kBlue,kCyan-10])

# --------------

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
#vs.append(['pt',100,0,1000,'ls']) #ls = plot leading and subleading. l = leading. s = subleading 
#vs.append(['invm',170,0,160]) # Invariant mass
#vs.append(['invm',200,1200,1300]) # Invariant mass 
#vs.append(['invm',100,120,160]) # Invariant mass 
#vs.append(['invm',100,115,135]) # Invariant mass 
#vs.append(['Tmass',100,0,500]) # Transverse mass
#vs.append(['dphi',100,-5,5]) # difference in phi 

#vs.append(['eta',50,-5,5])
#vs.append(['phi',50,-5,5])

# Can implement two vector dependent variables like dphi in any part where length of particle vector is two. 

#vs.append(['',50,-5,5])

#vs.append([])

# number of particles, files 
nps = len(ptp)
nfi = len(d)

colors=[kGreen,kGreen+2]

# Max events 
me = 10 # per file 
max_files=1

def get_pparams(ch_,ptp_):

    # All possible particles
    all_particles = {
    # "particle": ['<particle>',number per event,pdgID's]
    "H": ['H',2,[25]], # Higgs boson
    "W": ['W',2,[24]], # W boson
    "g": ['g',2,[22]], # photon
    "q": ['q',0,[1,2,3,4,5]], # quark   # later make flavor subcategories
    "l": ['l',0,[11,13]], # lepton
    "nu": ['nu',0,[12,14]] # neutrino 
    }

    # Can make subcategories of Same Flavor, Different Flavors 
    if ch_ == 'FL':
        all_particles["q"][1] = 0
        all_particles["l"][1] = 2
        all_particles["nu"][1] = 2

    elif ch_ == 'SL':
        all_particles["q"][1] = 2
        all_particles["l"][1] = 1
        all_particles["nu"][1] = 1

    elif ch_ == 'FH':
        all_particles["q"][1] = 4
        all_particles["l"][1] = 0
        all_particles["nu"][1] = 0

    else:
        print 'Cannot find particle configuration for channel: ', ch
        print 'Exiting'
        sys.exit()

    pparams_ = []
    for p_ in ptp_: 
        for key in all_particles:
            if p_ == key:
                pparams_.append(all_particles[key])

    

    return pparams_ 

# def create_h():


def order_particles(ps_):
    max_pt = 0
    nparts = len(ps_)
    tmp_ps = []
    #for i in range(len(ps_)):
        #tmp_ps.append()
        #append 
    for p in ps_:
        fourvec = ps_.p4()
        pt = fourvec.pt()
        if pt > max_pt:
            print 'not setup yet'
            


    # pts_ = []
    # for p in ps_:
    #     fourvec = ps_.p4()
    #     pt = fourvec.pt()
    #     pts_.append(pt)
    # # order pts
    # for i in enumerate(pts_)

    return ops_