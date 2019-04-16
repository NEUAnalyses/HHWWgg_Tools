#!/usr/bin/env python

# Abe Tishelman-Charny 
# 16 April 2019 
# Configuration for Data_MC_Plot.py

from ROOT import TChain, TH1F, TCut, TCanvas, TLegend, TPad, TGaxis, TLine, gPad, kFullDotLarge, THStack, gStyle, kCandy
import os 
#import rhinoscriptsyntax as rs
import json

# Read from json file 

with open('Data_MC_Input.json','r') as f:
    info = f.read()

obj = json.loads(info)

# directories containing all files to process
Data_direc = obj["directories"]["Data_direc_info"][0]
MC_direc = obj["directories"]["MC_direc_info"][0]

Data_tree_prefix = obj["directories"]["Data_direc_info"][1]
MC_tree_prefix = obj["directories"]["MC_direc_info"][1]

output_Loc = '/eos/user/a/atishelm/www/analysis_plots/'

# Directories 
ds = []

# kWhite  = 0,   kBlack  = 1,   kGray    = 920,  kRed    = 632,  kGreen  = 416,
# kBlue   = 600, kYellow = 400, kMagenta = 616,  kCyan   = 432,  kOrange = 800,
# kSpring = 820, kTeal   = 840, kAzure   =  860, kViolet = 880,  kPink   = 900

# [DirecID, path, linecolor, fillcolor]
ds.append([[Data_direc,MC_direc],[Data_tree_prefix,MC_tree_prefix],'416','416-10'])
#ds.append(['MC',MC_direc,'600','600-10'])

Data_colors = [416,416-10]
MC_colors = [600,600-10]

# Variables 
vs = []
# [<'variable name'>,<bins>,<min>,<max>]

for v in obj["variables"]:
    v_params = obj["variables"][str(v)]
    vs.append(v_params)

# Particles 
ptp = []
for p in obj["particles"]:
    ptp.append(p)

# ptp = []

#ptp.append('H')
#ptp.append('l')
#ptp.append('le') # leading electron 
#ptp.append('sle') # subleading electron 
#ptp.append('lm') # leading muon 
#ptp.append('slm') # subleading muon 
#ptp.append('nu')
#ptp.append('q')
#ptp.append('j')
#ptp.append('mjj') # Matching jj pair (qq for Data)
# ptp.append('nmjj') # Non-Matching jj pair (qq for Data)

#vs.append(['px',100,-1000,1000]) 
#vs.append(['py',100,-1000,1000])
#vs.append(['pz',100,-1000,1000])
#vs.append(['pt',10,0,10])
#vs.append(['pt',20,0,1000])
#vs.append(['n_jets',20,0,20])
#vs.append(['invmass',50,0,400])
#vs.append(['pt',50,-1000,1000])

#vs.append(['pt',100,0,1000,'ls']) #ls = plot leading and subleading. l = leading. s = subleading 
#vs.append(['invm',170,0,160]) # Invariant mass
#vs.append(['invm',200,1200,1300]) # Invariant mass 
#vs.append(['invm',100,120,160]) # Invariant mass 
#vs.append(['invm',100,115,135]) # Invariant mass 
#vs.append(['Tmass',100,0,500]) # Transverse mass
#vs.append(['dphi',100,-5,5]) # difference in phi 

# number of particles, files 
#nps = len(ptp)
nfi = len(ds)

me = obj["maximums"]["me"] # max events per file 
mf = obj["maximums"]["mf"] # max files per directory 

# def get_pparams(ch_,ptp_):

#     # All possible particles
#     all_particles = {
#     # "particle": ['<particle>',<number per event>,[<pdgID1>,<pdgID2>,...]]
#     "H": ['H',2,[25]], # Higgs boson
#     "W": ['W',2,[24]], # W boson
#     "g": ['g',2,[22]], # photon
#     "q": ['q',0,[1,2,3,4,5]], # quark   # can make flavor subcategories
#     "l": ['l',0,[11,13]], # lepton
#     "nu": ['nu',0,[12,14]] # neutrino 
#     }

#     # Can make subcategories of Same Flavor, Different Flavors 
#     if ch_ == 'FL':
#         all_particles["q"][1] = 0
#         all_particles["l"][1] = 2
#         all_particles["nu"][1] = 2

#     elif ch_ == 'SL':
#         all_particles["q"][1] = 2
#         all_particles["l"][1] = 1
#         all_particles["nu"][1] = 1

#     elif ch_ == 'FH':
#         all_particles["q"][1] = 4
#         all_particles["l"][1] = 0
#         all_particles["nu"][1] = 0

#     else:
#         print 'Cannot find particle configuration for channel: ', ch
#         print 'Exiting'
#         sys.exit()

#     pparams_ = []
    
#     for p_ in ptp_: 
#         for key in all_particles:
#             if p_ == key:
#                 # append ID number to match histos with particle filling 
#                 nparams_ = len(pparams_)
#                 all_particles[key].append(nparams_)

#                 pparams_.append(all_particles[key])
                
#     return pparams_ 

# # order particles 
# def ordptcls(ps_):
#     lead_pt = -1
#     nparts = len(ps_)
#     tmp_ps = []

#     for i in range(len(ps_)):
#         tmp_ps.append([])
        
#     # Get leading pt value 
#     for p in ps_:
#         fourvec = p.p4()
#         pt = fourvec.pt()
#         #print 'pt = ',pt 
#         #print 'lead_pt = ',lead_pt 
#         # if new leading pt, push other elements back and set 0th to leading pt particle 
#         if pt > lead_pt: 
#             # Push all elements back one 
#             rs = 0
#             tmp_ps = p_back(tmp_ps,rs)

#             # Set leading element to lead pt particle 
#             lead_pt = pt 
#             tmp_ps[0] = [p,lead_pt]

#         # if the current pt is not leading, need to figure out where to place it 
#         # Is it subleading? 
#         # If there are only two particles, it's subleading 
#         elif nparts == 2:
#             tmp_ps[1] = [p,pt]
#         elif nparts == 4:
#             # If there are four particles
#             # If particle is greater than current subleading, it's the new subleading. 
#             if pt > tmp_ps[1][1]:
#                 rs = 1 # rs = replacement spot  
#                 tmp_ps = p_back(tmp_ps,rs)
#                 tmp_ps[rs] = [p,pt] 
#             # If particle is greater than current subsubleading, it's the new subsubleading. 
#             elif pt > tmp_ps[2][1]:
#                 rs = 2
#                 tmp_ps = p_back(tmp_ps,rs)
#                 tmp_ps[rs] = [p,pt]
#             # If it's less than subsubleading, it's the subsubsubleading particle
#             else: 
#                 tmp_ps[3] = [p,pt]

#         else:
#             print 'I don\'t know what to do with ', nparts, ' particles'
#             print 'exiting'
#             sys.exit()

#     return tmp_ps

# def p_back(tmp_ps_,rs_):

#     nparts_ = len(tmp_ps_)
#     for i in range(nparts_):
#         eli_ = nparts_ - (i+1) #element index to change  
#         #print'eli = ',eli 
#         if eli_ == rs_: continue # is about to replace element we want to replace ourselves. 
#         else: 
#             #print'eli = ',eli 
#             tmp_ps_[eli_] = tmp_ps_[eli_-1]
#     return tmp_ps_

# Get histograms from flashgg event dumper 
def import_ED(paths_,var_,hid_,xbins_,xmin_,xmax_,tree_):

    # draw all onto same histogram to combine stats 
    # want to combine all paths 
    # for now just use first path

    pa_ = paths_[0]
    E = '13TeV' # Energy 
    Cat = 'All_Events' # category

    # Backgrounds. Stack files  
    if tree_ != 'Data':
        # Get tree_ somehow. Should be possible from file name 
        # For each file, get tree_ and draw to histogram
        # After done with all files, stack into new histogram 
        stk = THStack("stk","")

        for i, path_ in enumerate(paths_):
            # get tree_
            # tree_ = 
            ch = TChain('HHWWggCandidateDumper/trees/' + tree_ + '_13TeV_All_Events')
            ch.Add(path_)
            hname_tmp = hid_
            h_tmp = TH1F(hname_tmp, hid_, xbins_, xmin_, xmax_)
            ch.Draw(var_+'>>'+hname_tmp,TCut(''))
            print 'h_tmp.GetEntries() = ',h_tmp.GetEntries() # Tells you if the histogram was actually filled 
            #h_tmp.SetFillColor(1 + i) # custom color for each background 
            stk.Add(h_tmp)

        #print 'stk.GetEntries() = ',stk.GetEntries() # Tells you if the histogram was actually filled 
        return stk

    # Data. Just TChain files then draw  
    else:
        ch = TChain('HHWWggCandidateDumper/trees/' + tree_ + '_' + E + '_' + Cat )
        for path_ in paths_:
            ch.Add(path_) # combine files here 
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

    file_type = label_.split('_')[0]

    if file_type == 'Data':
        hist_.SetMarkerStyle(kFullDotLarge)
        hist_.Draw("P0")
    else:
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
    #c0_.SaveAs(file_path1_) #pdf 
    c0_.SaveAs(file_path3_)
    #return 0
    return hist_  


def save_histo_stack(hist_,label_,plabel_,variable_,lc__,fc__):

    #tmp_hist = hist_.Clone("tmp_hist") 

    c0_ = TCanvas('c0_', 'c0_', 800, 600)
    #hist_.SetDirectory(0)
    #hist_.SetLineColor(eval(str(lc__))) # eval because they are strings, need to recognize as root objects 
    #hist_.SetFillColor(eval(str(fc__)))
    #hist_.GetYaxis().SetTitle('Events')
    #if variable_ == 'pt': hist_.GetXaxis().SetTitle( plabel_ + ' ' + 'p_{T}')
    #else: hist_.GetXaxis().SetTitle( variable_ + '_{' + plabel_ + '}')
    #hist_.GetXaxis().SetTitle( variable_ + '_{' + plabel_ + '}')

    file_type = label_.split('_')[0]

    if file_type == 'Data':
        hist_.SetMarkerStyle(kFullDotLarge)
        hist_.Draw("P0")
    else:
        gStyle.SetPalette(kCandy) # automatic color setting
        hist_.Draw('pfc')
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
    #c0_.SaveAs(file_path1_) #pdf 
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

    # turn THStack entry into all its histo entries 
    input_histo_infos_cpy = list(input_histo_infos_)

    for i in range(len(input_histo_infos_cpy)):
        ID_ = input_histo_infos_cpy[i][1] 
        ID_start = ID_.split('_')[0] # this multistep process to get data/mc identifier could cause problems if things change 
        if (ID_start == 'MC'):
            hstack = input_histo_infos_cpy[i][0]
            del input_histo_infos_cpy[i] # remove hstack from histos 
            for bi, block in enumerate(hstack):
                #print'hstack thing = ',block
                input_histo_infos_cpy.append([block,'block_' + str(bi),'test_p',[1,1]]) # append each histogram making up hstack 

    # input_histo_infos_ format 
    # input_histos_info.append([dec_Data_hist,Data_ID,p,[Data_colors[0],Data_colors[1]]])

    for i in range(len(input_histo_infos_cpy)):
        # for single plot 
        hist_ = input_histo_infos_cpy[i][0]
        label_ = input_histo_infos_cpy[i][1]
        plabel_ = input_histo_infos_cpy[i][2]  
        h_lc = input_histo_infos_cpy[i][3][0]
        h_fc = input_histo_infos_cpy[i][3][0]

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

    file_path1_ = output_Loc + 'Data_MC_Combined_' + plabels_[0] + '_' + var_copy_ + '.png'
    file_path2_ = output_Loc + 'Data_MC_Combined_' + plabels_[0] + '_' + var_copy_ + '.pdf'
    #file_path1_ = 'test_path.png'
    file_exists1_ = False
    file_exists2_ = False 
    file_exists1_ = path_exists(file_path1_)
    #file_exists2_ = path_exists(file_path2_)
    if file_exists1_:
        rm_path(file_path1_)
    if file_exists2_:
        rm_path(file_path2_)
    #c0_.SaveAs(file_path1_)
    #c0_.SaveAs(file_path2_) #pdf 

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

    # In data/mc, one of these is the stacked mc. 
    # in ratio, need to divide data value by stacked mc value. 
    # on upper plot, will plot hstack. 
    h1 = ih_[0][0]
    h2 = ih_[1][0]

    hists_ = []
    hists_.append(h1)
    hists_.append(h2)

    for this_hist_i_, histo_ in enumerate(hists_):
        this_ID = ih_[this_hist_i_][1]
        this_ID_start = this_ID.split('_')[0] 
        if this_ID_start == 'MC':
            stack_sum_h = histo_.GetStack().Last()

    #ID_ = input_histo_infos_[i][1] 
    #ID_start = ID_.split('_')[0] # this multistep process to get data/mc identifier could cause problems if things change 

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
    #h1.GetXaxis().SetNdivisions(xbins__)
    h1.SetMarkerStyle(kFullDotLarge)
    h1.GetYaxis().SetRangeUser(0,max_val_*1.1)
    h1.Draw("P0")               # Draw h1

    # pad1.Update()
    # lline = TLine(pad1.GetUxmin(),20,pad1.GetUxmax(),20)
    # #lline.SetNDC(1)
    # lline.SetLineStyle(3)
    # lline.Draw('same')
    h2.GetYaxis().SetRangeUser(0,max_val_*1.1)
    gStyle.SetPalette(kCandy) # automatic color setting
    h2.Draw("same pfc")         # Draw h2 on top of h1

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
    #h3 = h2.Clone("h3")
    h3 = h1.Clone("h3")
    h3.SetLineColor(1)
    h3.SetMinimum(0.5)  # Define Y ..
    h3.SetMaximum(1.5) # .. range
    h3.Sumw2()
    h3.SetStats(0)     # No statistics on lower plot
    #print'h1 = ',h1
    #print'h2 = ',h2
    #print'h3 = ',h3
    h3.Divide(stack_sum_h)
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
    
    #h1.GetXaxis().SetNdivisions(xbins__)
    #h1.GetXaxis().SetNdivisions(0)

    #// h2 settings
    #h2.SetLineColor(632)
    #h2.SetLineWidth(2)

   # // Ratio plot (h3) settings
    h3.SetTitle("") # Remove the ratio title

    #// Y axis ratio plot settings
    h3.GetYaxis().SetTitle("Data/MC")
    h3.GetYaxis().SetNdivisions(505) # with 0.5-1.5 ratio range, keeps y axis labels unobstructed 
    h3.GetYaxis().SetTitleSize(20)
    h3.GetYaxis().SetTitleFont(43)
    h3.GetYaxis().SetTitleOffset(1.55)
    h3.GetYaxis().SetLabelFont(43) #Absolute font size in pixel (precision 3)
    h3.GetYaxis().SetLabelSize(15)

  #  // X axis ratio plot settings
    #h3.GetXaxis().SetNdivisions(xbins__)
    #h3.GetXaxis().SetNdivisions(xbins__)
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

    for i, hist_info_ in enumerate(a):
        this_h = hist_info_[0]
        this_label = hist_info_[1]
        
        if (i == 0): # data 
            leg_.AddEntry(this_h,this_label,'p')
        else:
            leg_.AddEntry(this_h,this_label,'lf') # histo object, ID 

    #leg.SetTextSize(0.02)
    leg_.Draw('same')
    
    #cc.SaveAs(output_Loc + "Gen_Reco_" + comb_ID_ + ".png")
    #cc.SaveAs(output_Loc + "Gen_Reco_" + comb_ID_ + ".pdf")
    #print'comb_ID_ = ',comb_ID_
    cc.SaveAs(output_Loc + "Data_MC_" + comb_ID_ + ".png")

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
    "leading_elec_eta": ['eta','le',0],
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
