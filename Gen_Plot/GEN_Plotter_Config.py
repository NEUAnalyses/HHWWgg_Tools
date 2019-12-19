#!/usr/bin/env python

# Configuration for GEN_Plotter.py 
# from ROOT import * 
# from ROOT import kGreen 
import ROOT 
from DataFormats.FWLite import Handle, Runs, Lumis, Events

genHandle = Handle('vector<reco::GenParticle>')
summary = Handle('LumiSummary')
outputLoc = '/eos/user/a/atishelm/www/HHWWgg_Analysis/GEN' 

# Particles 
ptp = []

#ptp.append('R')
# ptp.append('b')
# ptp.append('g')
ptp.append('H')
# ptp.append('W')
#ptp.append(all_particles["H"]) 
#ptp.append(all_particles["W"]) 

d = []

# hadded files 
fs = []


# d.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/test/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/test/','SM','SL','ROOT.kRed'])
d.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X400_WWgg_qqlnugg/100000events_GEN-SIM/191128_153853/0000/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X400_WWgg_qqlnugg/100000events_GEN-SIM/191128_153853/0000/','X400','SL','ROOT.kRed'])
d.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X450_WWgg_qqlnugg/100000events_GEN-SIM/191128_153916/0000/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X450_WWgg_qqlnugg/100000events_GEN-SIM/191128_153916/0000/','X450','SL','ROOT.kRed'])
d.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_SM_WWgg_qqlnugg/100000events_GEN-SIM/191128_153938/0000/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_SM_WWgg_qqlnugg/100000events_GEN-SIM/191128_153938/0000/','SM','SL','ROOT.kRed'])

# 250 GeVggs/resonant_HH/RunII/MicroAOD/HHWWggSign
# d.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X250_WWgg_qqlnugg/100000events_GEN-SIM/190618_093349/0000/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X250_WWgg_qqlnugg/100000events_GEN-SIM/190618_093349/0000/','X250','SL','ROOT.kRed'])
# d.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X250_WWgg_lnulnugg/100000events_GEN-SIM/190618_093802/0000/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X250_WWgg_lnulnugg/100000events_GEN-SIM/190618_093802/0000/','X250','FL','ROOT.kRed'])
# d.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X250_WWgg_qqqqgg/100000events_GEN-SIM/190618_093433/0000/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X250_WWgg_qqqqgg/100000events_GEN-SIM/190618_093433/0000/','X250','FH','ROOT.kRed'])

# # 750 GeV
#d.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X750_WWgg_qqlnugg/100000events_GEN-SIM/190624_230014/0000/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X750_WWgg_qqlnugg/100000events_GEN-SIM/190624_230014/0000/','X750','SL','ROOT.kGreen'])
#d.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X750_WWgg_lnulnugg/100000events_GEN-SIM/190624_230034/0000/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X750_WWgg_lnulnugg/100000events_GEN-SIM/190624_230034/0000/','X750','FL','ROOT.kGreen'])
# d.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X750_WWgg_qqqqgg/100000events_GEN-SIM/190624_230054/0000/','root://cmsxrootd.fnal.gov//store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X750_WWgg_qqqqgg/100000events_GEN-SIM/190624_230054/0000/','X750','FH','ROOT.kGreen'])

# # 1250 GeV
#d.append(['/eos/cms/store/user/atishelm/ggF_X1250_WWgg_qqlnugg/100000events_GEN/190328_155257/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/ggF_X1250_WWgg_qqlnugg/100000events_GEN/190328_155257/0000/','X1250','SL','ROOT.kBlue'])
#d.append(['/eos/cms/store/user/atishelm/ggF_X1250_WWgg_lnulnugg/100000events_GEN/190328_155527/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/ggF_X1250_WWgg_lnulnugg/100000events_GEN/190328_155527/0000/','X1250','FL','ROOT.kBlue'])
# d.append(['/eos/cms/store/user/atishelm/ggF_X1250_WWgg_qqqqgg/100000events_GEN/190328_160120/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/ggF_X1250_WWgg_qqqqgg/100000events_GEN/190328_160120/0000/','X1250','FH','ROOT.kBlue'])

# Variables 
# https://root.cern.ch/doc/v612/namespaceROOT_1_1Math_1_1VectorUtil.htmlC

dphi = ROOT.Math.VectorUtil.DeltaPhi
#deltaR = ROOT.Math.VectorUtil.DeltaR
#Wphi = ROOT.Math.VectorUtil.Phi_0_2pi
invmass = ROOT.Math.VectorUtil.InvariantMass
#invmass = Math.VectorUtil.InvariantMass
# need to be methods of reco::GenParticle 
# need to do something different if it requires full vectors like angle between or invariant mass 
vs = []
# vs.append(['px',100,-1000,1000]) 
# vs.append(['py',100,-1000,1000])
# vs.append(['pz',100,-1000,1000])
# eta
# phi 
# E 
#vs.append(['pt',100,0,1000])
# vs.append(['pt',100,0,1000,'ls']) #ls = plot leading and subleading. l = leading. s = subleading 
# vs.append(['invm',75,250,1000]) # Invariant mass
vs.append(['invm',100,0,1000]) # Invariant mass
# vs.append(['invm',10,120,130]) # Invariant mass

# number of particles, files 
nps = len(ptp)
nfi = len(d)

colors=[ROOT.kGreen,ROOT.kGreen+2]

#def get_pparams(ch_,ptp_):
def get_pparams(ptp_):

    # All possible particles
    all_particles = {
    # "particle": ['<particle>',number per event,pdgID's]
    "H": ['H',2,[25]], # Higgs boson
    "b": ['b',0,[5]],
    "W": ['W',2,[24]], # W boson
    "g": ['g',2,[22]], # photon
    "R": ['R',1,[]], # radion 
    # "q": ['q',0,[1,2,3,4,5]], # quark   # later make flavor subcategories

    # "l": ['l',0,[11,13]], # lepton
    # "nu": ['nu',0,[12,14]] # neutrino 
    }

    # # Can make subcategories of Same Flavor, Different Flavors 
    # if ch_ == 'FL':
    #     all_particles["q"][1] = 0
    #     all_particles["l"][1] = 2
    #     all_particles["nu"][1] = 2

    # elif ch_ == 'SL':
    #     all_particles["q"][1] = 2
    #     all_particles["l"][1] = 1
    #     all_particles["nu"][1] = 1

    # elif ch_ == 'FH':
    #     all_particles["q"][1] = 4
    #     all_particles["l"][1] = 0
    #     all_particles["nu"][1] = 0

    # else:
    #     print 'Cannot find particle configuration for channel: ', ch
    #     print 'Exiting'
    #     sys.exit()

    pparams_ = []
    for p_ in ptp_: 
        for key in all_particles:
            if p_ == key:
                pparams_.append(all_particles[key])

    

    return pparams_ 

# def create_h():
me = -1 # max events 
max_files= 1 # max files

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
            
    return ops_