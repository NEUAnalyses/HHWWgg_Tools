#!/usr/bin/env python
# Abe Tishelman-Charny 
# 16 April 2019 
# Configuration for Data_MC_Plot.py

from ROOT import TChain, TH1F, TCut, TCanvas, TLegend, TPad, TGaxis, TLine, gPad, kFullDotLarge, THStack, gStyle, kCandy, TFile, TTree, TList, TDirectory, kRainBow, kRed, kOrange, kYellow, kSpring, kGreen, kTeal, kCyan, kAzure, kBlue, kViolet, kMagenta, kWhite 
from MC_Categorize import MC_Cat
import os 
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
ds.append([[Data_direc,MC_direc],[Data_tree_prefix,MC_tree_prefix],'416','416-10'])
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
# Cut
cut = ''
num_cuts = len(obj["cuts"])
for ic,c in enumerate(obj["cuts"]):
    cut += c 
    cut += ' == 1.0'
    if ( (ic + 1) != num_cuts): cut += ' && ' 
print'cut = ',cut 
nfi = len(ds)
me = obj["maximums"]["me"] # max events per file 
mf = obj["maximums"]["mf"] # max files per directory 

# Get histograms from flashgg event dumper 
def import_ED(paths_,var_,hid_,xbins_,xmin_,xmax_,tree_):
    pa_ = paths_[0]
    E = '13TeV' # Energy 
    Cat = 'All_HLT_Events' # category

    # Backgrounds 
    if tree_ != 'Data':
        num_cats = 3
        stk = THStack("stk","stacked_histo")
        histos = []
        all_bkg_cats = []
        for i in range(0,num_cats):
            exec('bkg_cat_' + str(i) + ' = []')
        for i, path_ in enumerate(paths_): # all background paths 
            tree_name = get_tree(path_)
            icategory = ''
            icategory = MC_Cat(tree_name)[1] 
            eval('bkg_cat_' + icategory + '.append("' + path_ + '")')
        for i in range(0,num_cats):
            if len(eval('bkg_cat_' + str(i))) > 0: 
                eval('all_bkg_cats.append(bkg_cat_' + str(i) + ')')
        for icat,cat in enumerate(all_bkg_cats):
            bkg_name = cat[0].split('/')[-1].split('_')[1]
            cat_name = MC_Cat(bkg_name)[0]
            h_bkg_name = hid_ + '_' + cat_name 
            h_cat = TH1F(h_bkg_name,cat_name,xbins_,xmin_,xmax_)
            db = (float(xmax_) - float(xmin_)) / float(xbins_) 
            bkg_color = ''
            p_tree = get_tree(cat[0])
            bkg_color = MC_Cat(p_tree)[2] 
            # h_cat.SetFillColor(eval(bkg_color))            
            for ibp,bkg_path in enumerate(cat):
                h_tmp_name = hid_ + '_' + str(ibp) 
                h_tmp = TH1F(h_tmp_name, h_tmp_name, xbins_, xmin_, xmax_)
                tree_name = get_tree(bkg_path)
                icategory, color = '' , ''
                icategory = MC_Cat(tree_name)[1]
                color = MC_Cat(tree_name)[2]
                ch = TChain('HHWWggCandidateDumper/trees/' + tree_name )
                ch.Add(bkg_path)
                #ch.Draw(var_ + '*weight >>' + h_tmp_name , TCut(cut))
                ch.Draw(var_ + ' >>' + h_tmp_name , TCut(cut))
                nbins = h_tmp.GetNbinsX()
                
                for ib,bv in enumerate(h_tmp): # bv = bin value 
                    if (ib == 0): 
                        #print'underflow bin'
                        continue 
                    elif (ib == nbins + 1): 
                        #print'overflow bin'
                        continue 
                    else:
                        # print'(x,y) =', xmin_ + (ib - 1)*db,',',bv
                        # print xmin_ + (ib - 1)*db # x value 
                        # print bv # y value 
                        # h_cat.Fill(-999,1)
                        h_cat.Fill(float(xmin_ + (ib - 1)*db), float(bv))
                    #print'b = ',b 
                # fill h_cat 
            # print'bkg_color = ',bkg_color 
            # h_cat.SetFillColor(eval(bkg_color))  
            # h_cat.SetDirectory(0)  
            h_cat.SetFillColor(eval(bkg_color))              
            stk.Add(h_cat,'hist') # Thank you so much: https://root-forum.cern.ch/t/th1f-fillcolor-not-working/27922/6
                
            #bkg_path = cat[0] 
            #tree_label = tree_name.split('_')[0]
            #print'tree_name = ',tree_name 
            #ch = TChain('HHWWggCandidateDumper/trees/' + tree_name ) 
            #for icf,f_path in enumerate(cat):
            #    ch.Add(cat[icf])
            #hname1 = hid_ + '_' + tree_label 
            #bkg_hist = TH1F(hname1, tree_label, xbins_, xmin_, xmax_)
            #bkg_color = ''
            #bkg_color = MC_Cat(tree_label)
            #bkg_hist.SetFillColor(eval(bkg_color))
            #ch.Draw(var_ + '*weight >>' + hname1 , TCut('') ) # MC weight 
            #ch.Draw(var_ + '*weight >>' + hname1 , TCut('Cut_6 == 1.0') ) # MC weight 
            #stk.Add(bkg_hist)
        return stk 

    # Data 
    else:
        ch = TChain('HHWWggCandidateDumper/trees/' + tree_ + '_' + E + '_' + Cat )
        for path_ in paths_:
            ch.Add(path_) # combine files here 
        hname1 = hid_
        h1 = TH1F(hname1, hid_, xbins_, xmin_, xmax_)
        ch.Draw(var_+'>>'+hname1,TCut(cut))
        #ch.Draw(var_+'>>'+hname1,TCut('Cut_6 == 1.0'))
        #print 'h1.GetEntries() = ',h1.GetEntries() # Tells you if the histogram was actually filled 
        return h1

def save_histo(hist_,label_,plabel_,variable_,lc__,fc__):
    #tmp_hist = hist_.Clone("tmp_hist") 
    c0_ = TCanvas('c0_', 'c0_', 800, 600)
    hist_.SetDirectory(0)
    hist_.SetLineColor(eval(str(lc__))) # eval because they are strings, need to recognize as root objects 
    #hist_.SetFillColor(eval(str(fc__)))
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

    c0_ = TCanvas('c0_', 'c0_', 800, 600)
    file_type = label_.split('_')[0]
    #hist_.GetXaxis().SetTitle(plabel_ + ' ' + variable_)
    hist_.SetTitle('Backgrounds ' + plabel_ + ' ' + variable_)
    # bkg_path = ''
    # bkg_path += hist_.GetTitle()
    # f_clr = MC_Cat(bkg_path)[1]
    # hist_.SetFillColor(eval(bkg_color))   
    # redo_stack = THStack("stk_2","stacked_histo_2")         
    hist_.Draw()
    c0_.Modified()
    #gPad.BuildLegend(0.75,0.75,0.95,0.95,"")
    l1 = TLegend(0.75,0.75,0.95,0.95)
    for h in hist_.GetStack():
        # print'h.GetFillColor() = ',h.GetFillColor() 
        # h.Draw()
        # h_c = h.Clone("h_c")
        # redo_stack.Add(h_c)
        l1.AddEntry(h,h.GetTitle().split('_')[-1],'f')
    #redo_stack.Draw('same')
    l1.Draw('same')
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
    return hist_  # it seems you need to draw a thstack before returning it. probably because it switches to its directory 
    # return redo_stack  # it seems you need to draw a thstack before returning it 

# Plot histograms on same canvas 
# Input: list of histograms (or hinfo)
# Output: canvas
def combine_histos(input_histo_infos_,var_copy_):
    c0_ = TCanvas('c0', 'c0', 800, 600)

    hists_ = []
    labels_ = []
    plabels_ = []
    colors_ = [] 

    # turn THStack entry into sum of its histo entries 
    input_histo_infos_cpy = list(input_histo_infos_)

    for i in range(len(input_histo_infos_cpy)):
        ID_ = input_histo_infos_cpy[i][1] 
        ID_start = ID_.split('_')[0] # this multistep process to get data/mc identifier could cause problems if things change 
        if (ID_start == 'MC'):
            hstack = input_histo_infos_cpy[i][0]
            #print'hstack = ',hstack 
            #print'hstack.GetStack() = ',hstack.GetStack()
            #print'hstack.GetStack().Last() = ',hstack.GetStack().Last() 
            del input_histo_infos_cpy[i] # remove hstack from histos 
            input_histo_infos_cpy.append([hstack.GetStack().Last(),'summed_h','test_p',[1,1]]) # append summed stack histogram to get maximum between that and data 
            #for bi, block in enumerate(hstack):
                #print'hstack thing = ',block
                #input_histo_infos_cpy.append([block,'block_' + str(bi),'test_p',[1,1]]) # append each histogram making up hstack 

    # input_histo_infos_ format 
    # input_histos_info.append([dec_Data_hist,Data_ID,p,[Data_colors[0],Data_colors[1]]])

    for i in range(len(input_histo_infos_cpy)):
        # for single plot 
        hist_ = input_histo_infos_cpy[i][0]
        label_ = input_histo_infos_cpy[i][1]
        plabel_ = input_histo_infos_cpy[i][2]  
        h_lc = input_histo_infos_cpy[i][3][0]
        h_fc = input_histo_infos_cpy[i][3][0]

        #hist_.SetDirectory(0)
        #hist_.SetLineColor(eval(str(h_lc)))
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


    #for hi_,h_ in enumerate(hists_):
        #h_.SetDirectory(0)
        #h_.SetFillColor(eval(str(clr)))
        #h_.SetFillColor(0) # kWhite 
        #h_.SetLineWidth(3)

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

def plot_ratio(ih_,max_val_,xbins__,comb_ID_,xmin_,variable_,p_):

    # Canvas for upper and lower plots 
    cc = TCanvas("cc", "canvas", 800, 800)

    # Get Data and MC histos 
    h_data = ih_[0][0] # Data (TH1F) 
    h_MC = ih_[1][0] # MC (THStack) 

    # Set range of MC y axis range to contain both data and MC when combined 
    h_MC.SetMinimum(0)
    h_MC.SetMaximum(max_val_*1.05)
    h_MC.GetYaxis().SetLabelOffset(999) # will create separate axis later 
    h_MC.SetTitle('Data/MC, ' + p_ + ', ' + variable_) # particle, variable

    # h_data.SetMinimum(0)
    # h_data.SetMaximum(max_val_*1.1)

    # Sum of MC stack. Will divide Data by this to get proper ratio 
    stack_sum_h = h_MC.GetStack().Last()

    # Upper plot will be in pad1
    pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0) # Upper and lower plot are joined
    #pad1.SetGridx()         #Vertical grid, dashed lines 

    pad1.Draw()            #Draw the upper pad: pad1
    pad1.cd()               # pad1 becomes the current pad
    h_data.SetStats(0)          # No statistics on upper plot
    #h1.GetXaxis().SetNdivisions(xbins__)
    h_data.SetMarkerStyle(kFullDotLarge)
    h_data.SetMinimum(0)
    h_data.SetMaximum(max_val_*1.1)

    #h_data.Draw("P0")
    #gStyle.SetPalette(kRainBow) # automatic color setting
    #h_MC.Draw("same pfc")   # pfc = pad fill color
    
    #gStyle.SetPalette(kRainBow) # automatic color setting
    #h_MC.Draw("pfc")
    h_MC.Draw()
    h_data.Draw("same P0")

    #    // Do not draw the Y axis label on the upper plot and redraw a small
    #    // axis instead, in order to avoid the first label (0) to be clipped.
    #h1.GetYaxis().SetLabelSize(0.)
    #h2.GetYaxis().SetLabelSize(0.)
    #h2.GetYaxis().SetNdivisions(0)
    #h2.GetYaxis().SetRangeUser(0.,0.)
    #h1.GetYaxis().SetNdivisions(0)
    #TGaxis *axis = new TGaxis( -5, 20, -5, 220, 20,220,510,"");
    #axis = TGaxis( -5, 20, -5, 220, 20,220,510,"") #xmin ymin xmax ymax 
    #axis = TGaxis( -5, 20, 0, max_val_*1.1, 0.001,max_val_*1.1,510,"")
    # print'max_val_ = ',max_val_
    # print'max_val_*1.05 = ',max_val_*1.05
    axis = TGaxis(xmin_, 0, xmin_, max_val_*1.05, 0.001,max_val_*1.05,510,"") # xmin ymin xmax ymax wmin wmax (lowest and higest tick mark values), ndiv    
    #axis = TGaxis( -5, 0, -5, max_val_*1.1, 0.001,max_val_*1.1,510,"") # xmin ymin xmax ymax wmin wmax (lowest and higest tick mark values), ndiv
    axis.SetLabelFont(43) #Absolute font size in pixel (precision 3)
    axis.SetLabelSize(15)
    #print'axis.GetLabelOffset() = ', axis.GetLabelOffset()
    #axis.Draw()
    axis.Draw("same")

    #lower plot will be in pad
    cc.cd()           # Go back to the main canvas before defining pad2
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
    
    h_ratio = h_data.Clone("h_ratio") # copy of data 
    h_ratio.GetYaxis().SetLabelOffset(0.005)
    h_ratio.GetYaxis().SetLabelSize(15)
    h_ratio.SetLineColor(1)
    h_ratio.SetMinimum(0.5)  # Define Y ..
    h_ratio.SetMaximum(1.5) # .. range
    h_ratio.Sumw2()
    h_ratio.SetStats(0)     # No statistics on lower plot
    #print'h1 = ',h1
    #print'h2 = ',h2
    #print'h3 = ',h3
    h_ratio.Divide(stack_sum_h) # Here is where h_ratio actually becomes a ratio 
    h_ratio.SetMarkerStyle(21)

    #gPad.Modified()
    #gPad.Update()

    h_ratio.Draw("ep")     # Draw the ratio plot

    pad2.Update()
    lline = TLine(pad2.GetUxmin(),1,pad2.GetUxmax(),1)
    #lline.SetNDC(1)
    lline.SetLineStyle(1)
    lline.Draw('same')


    #// h1 settings
    # h1.SetLineColor(600+1)
    # h1.SetLineWidth(2)

    #// Y axis h1 plot settings
    # h1.GetYaxis().SetTitleSize(20)
    # h1.GetYaxis().SetTitleFont(43)
    # h1.GetYaxis().SetTitleOffset(1.55)

    #h_MC.SetTitle('')
    #h_MC.GetYaxis().SetRangeUser(0,max_val_*1.1)
    #h_MC.GetYaxis().SetLabelOffset(999)
    #h_MC.GetYaxis().SetLabelSize(0)

    #print 'xbins__ = ',xbins__ 
    
    #h1.GetXaxis().SetNdivisions(xbins__)
    #h1.GetXaxis().SetNdivisions(0)

    #// h2 settings
    #h2.SetLineColor(632)
    #h2.SetLineWidth(2)

   # // Ratio plot (h3) settings
    h_ratio.SetTitle("") # Remove the ratio title

    #// Y axis ratio plot settings
    h_ratio.GetYaxis().SetTitle("Data/MC")
    h_ratio.GetYaxis().SetNdivisions(505) # with 0.5-1.5 ratio range, keeps y axis labels unobstructed 
    h_ratio.GetYaxis().SetTitleSize(20)
    h_ratio.GetYaxis().SetTitleFont(43)
    h_ratio.GetYaxis().SetTitleOffset(1.55)
    h_ratio.GetYaxis().SetLabelFont(43) #Absolute font size in pixel (precision 3)
    h_ratio.GetYaxis().SetLabelSize(15)

  #  // X axis ratio plot settings
    #h3.GetXaxis().SetNdivisions(xbins__)
    #h3.GetXaxis().SetNdivisions(xbins__)
    #h3.GetXaxis().SetNdivisions(0)
    h_ratio.GetXaxis().SetTitleSize(20)
    h_ratio.GetXaxis().SetTitleFont(43)
    h_ratio.GetXaxis().SetTitleOffset(4.)
    h_ratio.GetXaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)
    h_ratio.GetXaxis().SetLabelSize(15)

    pad1.cd()

    #### old legend 
    # leg_ = TLegend(0.6, 0.75, 0.89, 0.89)
    # #for hi_,h_ in enumerate(hists_):
    # a = ih_[:]
    # #print'a = ',a
    # #for i,hist_info_ in enumerate(a):

    # for i, hist_info_ in enumerate(a):
    #     this_h = hist_info_[0]
    #     this_label = hist_info_[1]
        
    #     if (i == 0): # data 
    #         leg_.AddEntry(this_h,this_label,'p')
    #     else:
    #         leg_.AddEntry(this_h,this_label,'lf') # histo object, ID 

    # #leg.SetTextSize(0.02)
    # leg_.Draw('same')
    ####
    
    leg_ = TLegend(0.75,0.75,0.95,0.95)
    for h in h_MC.GetStack(): # bkg 
        leg_.AddEntry(h,h.GetTitle().split('_')[-1],'f')
    leg_.AddEntry(h_data,'Data','p')
    leg_.Draw('same')

    #cc.SaveAs(output_Loc + "Gen_Reco_" + comb_ID_ + ".png")
    #cc.SaveAs(output_Loc + "Gen_Reco_" + comb_ID_ + ".pdf")
    #print'comb_ID_ = ',comb_ID_
    cc.SaveAs(output_Loc + "Data_MC_" + comb_ID_ + ".png")

    return 0 

# Variable Map
# Maps (v[0],plabel) . HHWWggTagVariables string 

def rm_path(path_to_delete):
    os.system("rm " + path_to_delete)
    return 0 

def path_exists(path_to_check):
    return os.path.isfile(path_to_check)

# Made this because I think it was messing up adding histograms to the THStack in the loop. Not fully understood,
# but I'm guessing it was changing the current directory or something 
def get_tree(fp): # file path 
    bck_f = TFile(fp) # background file
    d = TDirectory()
    d = bck_f.Get('HHWWggCandidateDumper/trees')
    a = TList()
    a = d.GetListOfKeys()
    tree_name__ = ''
    for thing in a:
        # print'thing.GetName() = ',thing.GetName()
        tree_name__ = thing.GetName()
    return tree_name__