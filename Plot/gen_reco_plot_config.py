#!/usr/bin/env python

# 7 February 2019
# Abe Tishelman-Charny 

# Configuration for HHWWgg_Plotter.py 
from ROOT import TChain, TH1F, TCut, TCanvas, TLegend, TPad, TGaxis, TLine, gPad 
#from DataFormats.FWLite import Handle, Runs, Lumis, Events
import os 

#genHandle = Handle('vector<reco::GenParticle>')
#genHandle = Handle('vector<reco::GenParticle>')
output_Loc = '/eos/user/a/atishelm/www/analysis_plots/'
#print 'in config outputLoc = ',outputLoc 

#chosen_particles

# Use all of the files in this directory 
#/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_1000events_GEN_8/190212_095439/0000/*

# Depending on channel, specify number of particles? 
#ch = 'FL'
#ch = 'SL'
#ch = 'FH'

# Directories 
ds = []

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
#d.append(['SL','X1250_qqenugg',['/eos/cms/store/user/atishelm/RECO','root://cmsxrootd.fnal.gov//store/user/atishelm/RECO/'],'kMagenta','kMagenta-10'])

# [GEN],[RECO]
# . ['channel type','fileID',['path to directory','root path to directory'],'linecolor','fillcolor']
# 
# Get GEN info from flashgg microaods in /eos/cms/store/user/atishelm/Plot/MicroAOD
# Get RECO info from HHWWgg event dumper in /eos/cms/store/user/atishelm/Plot/EventDumper
# I currently don't need to root styled directory for the EventDumper file since this is only used for obtaining GEN information 

# kWhite  = 0,   kBlack  = 1,   kGray    = 920,  kRed    = 632,  kGreen  = 416,
# kBlue   = 600, kYellow = 400, kMagenta = 616,  kCyan   = 432,  kOrange = 800,
# kSpring = 820, kTeal   = 840, kAzure   =  860, kViolet = 880,  kPink   = 900

# d.append(
#     [
#         ['SL','X1250_qqenugg',['/eos/cms/store/user/atishelm/Plot/MicroAOD/test/','root://cmsxrootd.fnal.gov//store/user/atishelm/Plot/MicroAOD/test/'],'416','416-10'], # GEN
#         ['SL','X1250_qqenugg',['/eos/cms/store/user/atishelm/Plot/EventDumper/test_change/','root://cmsxrootd.fnal.gov//store/user/atishelm/Plot/EventDumper/test/'],'600','600-10'] # RECO 
#     ]
# )

ds.append(
        #['SL','X1250_qqenugg',['/eos/cms/store/user/atishelm/Plot/EventDumper/test_change/','root://cmsxrootd.fnal.gov//store/user/atishelm/Plot/EventDumper/test/'],'600','600-10']
        ['SL','testing','/eos/cms/store/user/atishelm/Plot/EventDumper/test_change/','600','600-10']
)

gen_colors = [416,416-10]
reco_colors = [600,600-10]

# d.append( 
#     ['SL','X1250_qqenugg',['/eos/cms/store/user/atishelm/Plot/EventDumper/test/','root://cmsxrootd.fnal.gov//store/user/atishelm/Plot/EventDumper/test/'],'600','600-10']
# ) 
#   qqmunu
#fi.append(['X1250_qqmunugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqmunugg_1000events_GEN/190212_183122/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqmunugg_1000events_GEN/190212_183122/0000/'],kGreen,kGreen-10])

# Fully hadronic

#d.append(['FH','X1250_qqenugg',['/eos/cms/store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_10000events_GEN_1/190214_151733/0000/','root://cmsxrootd.fnal.gov//store/user/atishelm/GEN_Outputs/ggF_X1250_WWgg_qqqqgg_10000events_GEN_1/190214_151733/0000/'],'kGreen','kGreen-10'])

# --------------

# # Particles to Plot
# # Need to set here for now 

# ptp = []

# #ptp.append('H')
# #ptp.append('l')
# ptp.append('le') # leading electron 
# #ptp.append('mu')
# #ptp.append('nu')
# #ptp.append('q')

# Variables 
# need to be methods of reco::GenParticle or pruned genparticle depending on what gen file has (can use minaod as well)
# need to do something different if it requires full vectors like angle between or invariant mass 
vs = []
# [<'variable name'>,<bins>,<min>,<max>]
#vs.append(['px',100,-1000,1000]) 
#vs.append(['py',100,-1000,1000])
#vs.append(['pz',100,-1000,1000])
#vs.append(['pt',10,0,10])
#vs.append(['pt',20,0,1000])
#vs.append(['n_jets',20,0,20])
vs.append(['invmass',50,0,400])
#vs.append(['pt',50,-1000,1000])

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
#nps = len(ptp)
nfi = len(ds)

colors=['kGreen','kGreen+2']

# Maximums 
me = -1 # max events per file 
max_files= -1 # max files per directory 

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
def import_ED(reco_path_,var_,hid_,xbins_,xmin_,xmax_):
    #print 'reco_path = ',reco_path_
    print 'var_ = ',var_
    # input files in directory. 
    # draw all onto same histogram to combine stats 

    # I would like a plot for each one... 
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_FullyLeptonic') 
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_SemiLeptonic') 
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_All_Events') 
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_Dipho_PS')
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_AtleastOneElec')  
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_AtleastOneMuon')
    ch = TChain('HHWWggCandidateDumper/trees/_13TeV_Dipho_PS') 
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_DiphoPSandTwoElec')  
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_DiphoPSandgteTwoElec') 
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_AtleastOneMuon')
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_1a3_1')
    #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_1a3_1')
    
    ch.Add(reco_path_)
    hname1 = hid_
    h1 = TH1F(hname1, hid_, xbins_, xmin_, xmax_)
    ch.Draw(var_+'>>'+hname1,TCut(''))

    print 'h1.GetEntries() = ',h1.GetEntries() # Tells you if the histogram was actually filled 
    return h1

# Draw and save canvas/histogram for input histogram 
#def custom_draw(input_histo_,save_path_):
def save_histo(hist_,label_,plabel_,variable_,lc__,fc__):

    #tmp_hist = hist_.Clone("tmp_hist") 

    c0_ = TCanvas('c0_', 'c0_', 800, 600)
    hist_.SetDirectory(0)
    hist_.SetLineColor(eval(str(lc__))) # eval because they are strings, need to recognize as root objects 
    hist_.SetFillColor(eval(str(fc__)))
    hist_.GetYaxis().SetTitle('Events')
    if variable_ == 'pt': hist_.GetXaxis().SetTitle( plabel_ + ' ' + 'p_{T}')
    else: hist_.GetXaxis().SetTitle( variable_ + '_{' + plabel_ + '}')
    #hist_.GetXaxis().SetTitle( variable_ + '_{' + plabel_ + '}')
    hist_.Draw()
    file_path3_ = output_Loc + label_ + '.png'
    file_path1_ = output_Loc + label_ + '.pdf'
    file_path2_ = output_Loc + label_ + '.root'
    file_exists1_ = False 
    file_exists2_ = False 
    file_exists1_ = path_exists(file_path1_)
    file_exists2_ = path_exists(file_path2_)
    if file_exists1_:   rm_path(file_path1_)
    if file_exists2_:   rm_path(file_path2_)
    hist_.SaveAs(file_path2_)
    c0_.SaveAs(file_path1_) #pdf 
    c0_.SaveAs(file_path3_)
    #return 0
    return hist_  

# Plot histograms on same canvas 
# Input: list of histograms (or hinfo)
# Output: canvas
def combine_histos(input_histo_infos_,var_copy_):
    c0_ = TCanvas('c0', 'c0', 800, 600)

    hists_ = []
    labels_ = []
    plabels_ = []
    colors_ = [] 

    for i in range(len(input_histo_infos_)):
        # for single plot 
        hist_ = input_histo_infos_[i][0]
        label_ = input_histo_infos_[i][1]
        plabel_ = input_histo_infos_[i][2]  
        h_lc = input_histo_infos_[i][3][0]
        h_fc = input_histo_infos_[i][3][0]

        hist_.SetDirectory(0)
        hist_.SetLineColor(eval(str(h_lc)))
        #hist_.SetLineColor(eval(str(lc_) + '-' + str(i*2) ) ) # eval because they are strings, need to recognize as root objects 
        #hist_.SetFillColor(eval(str(fc_) + '-' + str(i*2) ) )
        hist_.GetYaxis().SetTitle('Events')
        if var_copy_ == 'pt': hist_.GetXaxis().SetTitle( plabel_ + ' ' + 'p_{T}')
        else: hist_.GetXaxis().SetTitle( var_copy_ + '_{' + plabel_ + '}')

        # for combining 
        hists_.append(hist_)    
        labels_.append(label_)   
        plabels_.append(plabel_)

    # Check which histo has the highest max value to set y axis of combined plot accordingly to fit all values 

    mval = 0.
    for hi_,h_ in enumerate(hists_):
        hist_max = h_.GetMaximum()
        if hist_max > mval:
            mval = hist_max


    for hi_,h_ in enumerate(hists_):
        #h_.SetDirectory(0)
        #h_.SetFillColor(eval(str(clr)))
        h_.SetFillColor(0) # kWhite 
        h_.SetLineWidth(3)

        if hi_ == 0:
            h_.SetStats(0)
            h_.SetTitle(var_copy_ + '_' + plabel_ )
            h_.GetYaxis().SetRangeUser(0,mval)
            #h_.GetXaxis().SetTitle( var_copy_ + '_{all_' + plabel_ + '}') # Make combined histo have proper x axis 
            #h_.GetXaxis().SetTitle( var_copy_ + '_{all_' + plabel_ + '}') # Make combined histo have proper x axis 
            h_.Draw('h')
        
        if hi_ > 0:
            h_.SetStats(0)
            #h_.GetXaxis().SetTitle( var_copy_ + '_{all_' + plabel_ + '}') # Make combined histo have proper x axis 
            h_.Draw('h same')

    leg_ = TLegend(0.6, 0.7, 0.89, 0.89)
    for hi_,h_ in enumerate(hists_):
        leg_.AddEntry(h_,labels_[hi_],'lf') # histo object, ID 
    #leg.SetTextSize(0.02)
    leg_.Draw('same')

    file_path1_ = output_Loc + 'GEN_RECO_Combined_' + plabels_[0] + '_' + var_copy_ + '.png'
    file_path2_ = output_Loc + 'GEN_RECO_Combined_' + plabels_[0] + '_' + var_copy_ + '.pdf'
    #file_path1_ = 'test_path.png'
    file_exists1_ = False
    file_exists2_ = False 
    file_exists1_ = path_exists(file_path1_)
    #file_exists2_ = path_exists(file_path2_)
    if file_exists1_:
        rm_path(file_path1_)
    if file_exists2_:
        rm_path(file_path2_)
    c0_.SaveAs(file_path1_)
    c0_.SaveAs(file_path2_) #pdf 

    return mval

def plot_ratio(ih_,max_val_,xbins__,comb_ID_):

#    // Define two gaussian histograms. Note the X and Y title are defined
#    // at booking time using the convention "Hist_title ; X_title ; Y_title"
#    TH1F *h1 = new TH1F("h1", "Two gaussian plots and their ratio;x title; h1 and h2 gaussian histograms", 100, -5, 5);
#    TH1F *h2 = new TH1F("h2", "h2", 100, -5, 5);
#    h1.FillRandom("gaus");
#    h2.FillRandom("gaus");

#    // Define the Canvas
    #TCanvas *c = new TCanvas("c", "canvas", 800, 800);

    cc = TCanvas("cc", "canvas", 800, 800)

    h1 = ih_[0][0]
    h2 = ih_[1][0]

    #print 'h1 = ',h1
    #print 'h2 = ',h2 

    #print'h1.GetMaximum() = ' ,h1.GetMaximum() 

    #// Upper plot will be in pad1
    pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0) # Upper and lower plot are joined
    #pad1.SetGridx()         #Vertical grid, dashed lines 

    pad1.Draw()            #Draw the upper pad: pad1
    pad1.cd()               # pad1 becomes the current pad
    h1.SetStats(0)          # No statistics on upper plot
    h1.GetXaxis().SetNdivisions(xbins__)
    h1.Draw()               # Draw h1

    # pad1.Update()
    # lline = TLine(pad1.GetUxmin(),20,pad1.GetUxmax(),20)
    # #lline.SetNDC(1)
    # lline.SetLineStyle(3)
    # lline.Draw('same')

    h2.Draw("same")         # Draw h2 on top of h1

    #    // Do not draw the Y axis label on the upper plot and redraw a small
    #    // axis instead, in order to avoid the first label (0) to be clipped.
    h1.GetYaxis().SetLabelSize(0.)
    #TGaxis *axis = new TGaxis( -5, 20, -5, 220, 20,220,510,"");
    #axis = TGaxis( -5, 20, -5, 220, 20,220,510,"") #xmin ymin xmax ymax 
    axis = TGaxis( 0, 0, 0, max_val_, 0.001,max_val_,510,"")
    axis.SetLabelFont(43) #Absolute font size in pixel (precision 3)
    axis.SetLabelSize(15)
    axis.Draw()

    #lower plot will be in pad
    cc.cd()           # Go back to the main canvas before defining pad2
    #TPad *pad2 = new TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0) # can change to separate top and bottom 
    #pad2.SetBottomMargin(0.2)
    #pad2.SetBottomMargin(0)
    #pad2.SetGridx() # vertical grid, dashed lines 
    
    pad2.Draw()
    pad2.cd()      # pad2 becomes the current pad

    # Define the ratio plot
    #TH1F *h3 = (TH1F*)h1.Clone("h3");
    h3 = h2.Clone("h3")
    h3.SetLineColor(1)
    h3.SetMinimum(0.5)  # Define Y ..
    h3.SetMaximum(1.5) # .. range
    h3.Sumw2()
    h3.SetStats(0)     # No statistics on lower plot
    h3.Divide(h1)
    h3.SetMarkerStyle(21)

    #gPad.Modified()
    #gPad.Update()

    h3.Draw("ep")     # Draw the ratio plot

    pad2.Update()
    lline = TLine(pad2.GetUxmin(),1,pad2.GetUxmax(),1)
    #lline.SetNDC(1)
    lline.SetLineStyle(1)
    lline.Draw('same')


    #// h1 settings
    h1.SetLineColor(600+1)
    h1.SetLineWidth(2)

    #// Y axis h1 plot settings
    h1.GetYaxis().SetTitleSize(20)
    h1.GetYaxis().SetTitleFont(43)
    h1.GetYaxis().SetTitleOffset(1.55)

    #print 'xbins__ = ',xbins__ 
    
    h1.GetXaxis().SetNdivisions(xbins__)
    #h1.GetXaxis().SetNdivisions(0)

    #// h2 settings
    h2.SetLineColor(632)
    h2.SetLineWidth(2)

   # // Ratio plot (h3) settings
    h3.SetTitle("") # Remove the ratio title

    #// Y axis ratio plot settings
    h3.GetYaxis().SetTitle("Reco/Gen")
    h3.GetYaxis().SetNdivisions(505)
    h3.GetYaxis().SetTitleSize(20)
    h3.GetYaxis().SetTitleFont(43)
    h3.GetYaxis().SetTitleOffset(1.55)
    h3.GetYaxis().SetLabelFont(43) #Absolute font size in pixel (precision 3)
    h3.GetYaxis().SetLabelSize(15)

  #  // X axis ratio plot settings
    #h3.GetXaxis().SetNdivisions(xbins__)
    h3.GetXaxis().SetNdivisions(xbins__)
    #h3.GetXaxis().SetNdivisions(0)
    h3.GetXaxis().SetTitleSize(20)
    h3.GetXaxis().SetTitleFont(43)
    h3.GetXaxis().SetTitleOffset(4.)
    h3.GetXaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)
    h3.GetXaxis().SetLabelSize(15)

    

    pad1.cd()

    leg_ = TLegend(0.6, 0.75, 0.89, 0.89)
    #for hi_,h_ in enumerate(hists_):
    a = ih_[:]
    #print'a = ',a
    #for i,hist_info_ in enumerate(a):
    for hist_info_ in a:
        this_h = hist_info_[0]
        this_label = hist_info_[1]
        
        leg_.AddEntry(this_h,this_label,'lf') # histo object, ID 
    #leg.SetTextSize(0.02)
    leg_.Draw('same')
    
    #cc.SaveAs(output_Loc + "Gen_Reco_" + comb_ID_ + ".png")
    cc.SaveAs(output_Loc + "Gen_Reco_" + comb_ID_ + ".pdf")
    cc.SaveAs(output_Loc + "Gen_Reco_" + comb_ID_ + ".png")

    return 0 

# Variable Map
# Maps (v[0],plabel) . HHWWggTagVariables string 
def var_map(v0_,plab_,G_):
    #G_ = boolean of GEN. If gen, = 1. if reco, = 0 
    var_conv = {

    # "TagVarString": ['<v[0]>','<plabel>',GEN=1 RECO=0]
    # Configured for GEN/RECO. Should also have something for DATA/MC 
    # Do 

    ## RECO

    # Electrons
    "leading_elec_pt": ['pt','le',0],
    "subleading_elec_pt": ['pt','sle',0],

    # Muons
    "leading_muon_pt": ['pt','lm',0],
    "subleading_muon_pt": ['pt','slm',0],
    
    # Met

    # Jets
    "mdj_invmass": ['invmass','mjj',0],
    "nmdj_invmass": ['invmass','nmjj',0],

    ## GEN

    # Electrons
    "gen_leading_elec_pt": ['pt','le',1],
    "gen_subleading_elec_pt": ['pt','sle',1],

    # Muons 
    "gen_leading_muon_pt": ['pt','lm',1],
    "gen_subleading_muon_pt": ['pt','slm',1], 

    # Met 

    # Quarks 
    "mdq_invmass": ['invmass','mjj',1],
    "nmdq_invmass": ['invmass','nmjj',1],

    }

    reco_var = ''
    for key in var_conv:    
        if (var_conv[key][0] == v0_) and (var_conv[key][1] == plab_) and (var_conv[key][2] == G_):
            reco_var = key
            break 

    return reco_var


def rm_path(path_to_delete):
    os.system("rm " + path_to_delete)
    return 0 

def path_exists(path_to_check):
    return os.path.isfile(path_to_check)
