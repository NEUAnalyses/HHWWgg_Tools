#!/usr/bin/env python

# 7 February 2019
# Abe Tishelman-Charny 

# Configuration for GEN_Plotter.py 
from ROOT import TChain, TH1F, TCut
from DataFormats.FWLite import Handle, Runs, Lumis, Events

#genHandle = Handle('vector<reco::GenParticle>')
genHandle = Handle('vector<reco::GenParticle>')
outputLoc = '/eos/user/a/atishelm/www/analysis_plots/'

#chosen_particles

# Use all of the files in this directory 
#/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_8/190212_095439/0000/*

# Depending on channel, specify number of particles? 
#ch = 'FL'
#ch = 'SL'
#ch = 'FH'

# Directories 
d = []

# [channel type, fileID, path, linecolor, fillcolor]

# --------------

# Fully Leptonic
#   enuenu
#d.append(['FL','X1250_enuenugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_enuenugg_1000events_GEN_1/190212_184044/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_enuenugg_1000events_GEN_1/190212_184044/0000/'],kMagenta,kMagenta-10])

#   munumunu 
#d.append(['FL','X1250_munumunugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_munumunugg_1000events_GEN_1/190212_184207/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_munumunugg_1000events_GEN_1/190212_184207/0000/'],kGreen,kGreen-10])
 
# Semi Leptonic
#   qqenu
#d.append(['SL','X1250_qqenugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqenugg_10000events_GEN_1/190214_151938/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqenugg_10000events_GEN_1/190214_151938/0000/'],'kMagenta','kMagenta-10'])
d.append(['SL','X1250_qqenugg',['/eos/cms/store/user/atishelm/RECO','root://cmsxrootd.fnal.gov//store/user/atishelm/RECO/'],'kMagenta','kMagenta-10'])

#   qqmunu
#fi.append(['X1250_qqmunugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqmunugg_1000events_GEN/190212_183122/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqmunugg_1000events_GEN/190212_183122/0000/'],kGreen,kGreen-10])

# Fully hadronic

#d.append(['FH','X1250_qqenugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_10000events_GEN_1/190214_151733/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_10000events_GEN_1/190214_151733/0000/'],'kGreen','kGreen-10'])

# --------------

# Particles to Plot
# Need to set here for now 
ptp = []

#ptp.append('H')
#ptp.append('l')
#ptp.append('q')
ptp.append('l')

# Variables 
# need to be methods of reco::GenParticle or pruned genparticle depending on what gen file has (can use minaod as well)
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
# https://root.cern.ch/doc/v612/namespaceROOT_1_1Math_1_1VectorUtil.html

#dphi = ROOT.Math.VectorUtil.DeltaPhi
#deltaR = ROOT.Math.VectorUtil.DeltaR
#Wphi = ROOT.Math.VectorUtil.Phi_0_2pi
#invmass = ROOT.Math.VectorUtil.InvariantMass
#invmass = Math.VectorUtil.InvariantMass

# Can implement two vector dependent variables like dphi in any part where length of particle vector is two. 

# number of particles, files 
nps = len(ptp)
nfi = len(d)

colors=['kGreen','kGreen+2']

# Maximums 
me = -1 # max events per file 
max_files= 1 # max files per directory 

def get_pparams(ch_,ptp_):

    # All possible particles
    all_particles = {
    # "particle": ['<particle>',<number per event>,[<pdgID1>,<pdgID2>,...]]
    "H": ['H',2,[25]], # Higgs boson
    "W": ['W',2,[24]], # W boson
    "g": ['g',2,[22]], # photon
    "q": ['q',0,[1,2,3,4,5]], # quark   # can make flavor subcategories
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
                # append ID number to match histos with particle filling 
                nparams_ = len(pparams_)
                all_particles[key].append(nparams_)

                pparams_.append(all_particles[key])
                
    return pparams_ 

# order particles 
def ordptcls(ps_):
    lead_pt = -1
    nparts = len(ps_)
    tmp_ps = []

    for i in range(len(ps_)):
        tmp_ps.append([])
        
    # Get leading pt value 
    for p in ps_:
        fourvec = p.p4()
        pt = fourvec.pt()
        #print 'pt = ',pt 
        #print 'lead_pt = ',lead_pt 
        # if new leading pt, push other elements back and set 0th to leading pt particle 
        if pt > lead_pt: 
            # Push all elements back one 
            rs = 0
            tmp_ps = p_back(tmp_ps,rs)

            # Set leading element to lead pt particle 
            lead_pt = pt 
            tmp_ps[0] = [p,lead_pt]

        # if the current pt is not leading, need to figure out where to place it 
        # Is it subleading? 
        # If there are only two particles, it's subleading 
        elif nparts == 2:
            tmp_ps[1] = [p,pt]
        elif nparts == 4:
            # If there are four particles
            # If particle is greater than current subleading, it's the new subleading. 
            if pt > tmp_ps[1][1]:
                rs = 1 # rs = replacement spot  
                tmp_ps = p_back(tmp_ps,rs)
                tmp_ps[rs] = [p,pt] 
            # If particle is greater than current subsubleading, it's the new subsubleading. 
            elif pt > tmp_ps[2][1]:
                rs = 2
                tmp_ps = p_back(tmp_ps,rs)
                tmp_ps[rs] = [p,pt]
            # If it's less than subsubleading, it's the subsubsubleading particle
            else: 
                tmp_ps[3] = [p,pt]

        else:
            print 'I don\'t know what to do with ', nparts, ' particles'
            print 'exiting'
            sys.exit()

    return tmp_ps

def p_back(tmp_ps_,rs_):

    nparts_ = len(tmp_ps_)
    for i in range(nparts_):
        eli_ = nparts_ - (i+1) #element index to change  
        #print'eli = ',eli 
        if eli_ == rs_: continue # is about to replace element we want to replace ourselves. 
        else: 
            #print'eli = ',eli 
            tmp_ps_[eli_] = tmp_ps_[eli_-1]
    return tmp_ps_

# Get RECO histograms from flashgg dumper to plot with GEN histograms 
# Tell it which 
def import_reco(reco_path_,var_):
    # f[] 
    #Files.append(['/afs/cern.ch/work/a/atishelm/2FebFlashgglxplus7/CMSSW_10_2_1/src/flashgg/abetest.root','qqenu_woPU_micro',kBlue,kWhite, 0, 1])
    #ch = ROOT.TChain('HHWWggCandidateDumper/trees/_13TeV_SemiLeptonic')
    ch = TChain('HHWWggCandidateDumper/trees/_13TeV_SemiLeptonic')
    ch.Add(reco_path_)
    #hname1_ = v[1]+'_'+f[1]
    hname1_ = 'histo_name'
    reco_h_ = TH1F(hname1_, 'test_histo', 100, 0, 1000)
    Cut = ''
    ch.Draw(var_+'>>'+hname1_,TCut(Cut))
    #ch.Draw(v[0]+'>>'+hname1,TCut( str(v[0]) + gtz_Cut))
    return reco_h_