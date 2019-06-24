#!/usr/bin/env python
# Abe Tishelman-Charny 
# Configuration for Data_MC_Plot.py

from ROOT import TChain, TH1F, TCut, TCanvas, TLegend, TPad, TGaxis, TLine, gPad, kFullDotLarge, THStack, gStyle, kCandy, TFile, TTree, TList, TDirectory, kRainBow, kRed, kOrange, kYellow, kSpring, kGreen, kTeal, kCyan, kAzure, kBlue, kViolet, kMagenta, kWhite 
from MC_Categorize import MC_Cat
from MC_Sub_Categorize import MC_Sub_Cat
from Variable_Map import var_map 
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

# Data, MC Directories 
ds = []
ds = [[Data_direc,MC_direc],[Data_tree_prefix,MC_tree_prefix]]
#ds.append([[Data_direc,MC_direc],[Data_tree_prefix,MC_tree_prefix]])

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

# Cuts
cuts = []
for cut in obj["cuts"]:
    cuts.append(cut)

# Misc.
nfi = len(ds)
me = obj["maximums"]["me"] # max events per file 
mf = obj["maximums"]["mf"] # max files per directory 

# Get histograms from flashgg event dumper 
def import_ED(paths_,plotting_info_,tree_,vs_,ptp_,cuts_):
    E = '13TeV' # Energy 
    Cat = 'All_HLT_Events' # category

    # Data 
    if tree_ == 'Data':
        Data_hists_ = []
        # Chain files 
        ch = TChain('HHWWggCandidateDumper/trees/' + tree_ + '_' + E + '_' + Cat )
        for i,path_ in enumerate(paths_):
            if i%100 == 0: print'on Data path',i 
            ch.Add(path_) # combine files here 
            if i == mf: 
                print'Reached max desired files:',mf
                break 
        # Draw each v,p,c combination

        # hists = []
        # for v in vs_:
        #     variable, xbins, xmin, xmax = v[0], v[1], v[2], v[3]
        #     ED_variable = var_map(variable,particle,0) # Variable as called by the event dumper. Call it a non-gen variable to keep map consistent 
        #     for p in ptp:
        #             cut_number = cut.split('_')[1]
        #         for c in cuts_:
        #             if cut_number == '0': cut_name = var_map(c,'Data',0)
        #             else:   cut_name = var_map(c,'Dummy',0)  
        #             hist_name = 'Data_' + p + '_' + variable + '_' + cut_name 
        #             hist = TH1F(hist_name, hist_name, xbins, xmin, xmax)
        #             hists.append(hist)
        #             # once file is open, do ch.draw for all variables 
        # for h in hists:
        #     ch.Draw(ED_variable + '>>' + h., cut + ' == 1.0')

        for vi,pi in enumerate(plotting_info_):
            print'  Plotting variable',vi+1,'/',len(plotting_info_)
            v_info = pi[0]
            variable, xbins, xmin, xmax = v_info[0], v_info[1], v_info[2], v_info[3]
            particle = pi[1]
            cut = pi[2]
            cut_number = cut.split('_')[1]

            if cut_number == '0': cut_name = var_map(cut,'Data',0)
            else:   cut_name = var_map(cut,'Dummy',0)  

            # print'plot_data cut_name = ',cut_name 
            ED_variable = var_map(variable,particle,0) # Variable as called by the event dumper. Call it a non-gen variable to keep map consistent 
            hname = 'Data_' + particle + '_' + variable + '_' + cut_name
            h1 = TH1F(hname, hname, xbins, xmin, xmax)
            print'before draw'
            ch.Draw(ED_variable + '>>' + hname, cut + ' == 1.0')
            print'after draw'
            Data_hists_.append(h1)
            print'  Finished variable',vi+1,'/',len(plotting_info_)
            #ch.Draw(var_+'>>'+hname1,TCut('Cut_6 == 1.0'))
            #print 'h1.GetEntries() = ',h1.GetEntries() # Tells you if the histogram was actually filled 
        return Data_hists_

    # Backgrounds 
    # there are 17 unique draw statements. should only make that many 
    # need subcategories. this contains the unique draw statements
    # for each subcategory, draw, and then add to proper category 
    else:
        MC_hists_ = []
        num_cats = 6
        num_sub_cats = 17
        # Create list of files separated by cateogry 
        all_bkg_cats = []
        #bkg_sub_cats = [] 
        for i in range(0,num_cats):
            exec('bkg_cat_' + str(i) + ' = []')
        for i in range(0,num_sub_cats):
            exec('bkg_sub_cat_' + str(i) + ' = []')
        for i, path_ in enumerate(paths_): # all background paths 
            #print'path_ = ',path_
            if i%100 == 0: print'on MC path',i 
            if i == mf: 
                print'Reached max desired files:',mf
                break 
            tree_name = get_tree(path_)
            icategory = ''
            icategory = MC_Cat(tree_name)[1] 
            #isubcategory = MC_Sub_Cat(tree_name)
            eval('bkg_cat_' + icategory + '.append("' + path_ + '")')
            #eval('bkg_sub_cat_' + isubcategory + '.append("' + path_ + '")')
        # for i in range(0,num_sub_cats):
        #     bkg_sub_cats.append(eval('bkg_sub_cat_' + str(i)))
            #eval('bkg_cat_' + icategory + '.append("' + path_ + '")')
        for i in range(0,num_cats):
            if len(eval('bkg_cat_' + str(i))) > 0: 
                eval('all_bkg_cats.append(bkg_cat_' + str(i) + ')')
        #print'bkg_sub_cats = ',bkg_sub_cats 
        #print'Finished SubCategorizing MC files'
        print'Finished Categorizing MC files'
        print'Plotting variables ...'

        # # for each subcategory, draw for each vpc 
        # bsc_hists = []
        # for ibsc, bkg_sub_cat in enumerate(bkg_sub_cats):
        #     if len(bkg_sub_cat) == 0: continue 
        #     bkg_path_0 = bkg_sub_cat[0]
        #     tree_name = get_tree(bkg_path_0) # all paths in sub category should have same tree
        #     ch = TChain('HHWWggCandidateDumper/trees/' + tree_name )
        #     for bpath in bkg_sub_cat:
        #         ch.Add(bpath)
        #     for i,pi in enumerate(plotting_info_):
        #         print'  Plotting variable',i+1,'/',len(plotting_info_)
        #         v_info = pi[0]
        #         variable, xbins, xmin, xmax = v_info[0], v_info[1], v_info[2], v_info[3]
        #         particle = pi[1]
        #         cut = pi[2]
        #         cut_number = cut.split('_')[1]
        #         if cut_number == '0': cut_name = var_map(cut,'MC',0)
        #         else:   cut_name = var_map(cut,'Dummy',0) 
        #         ED_variable = var_map(variable,particle,0) # Variable as called by the event dumper. Call it a non-gen variable to keep map consistent 
        #         hname = 'MC_' + particle + '_' + variable + '_' + cut_name

        #         bsc_h_name = 'bsc_h_' + str(ibsc) + '_' + str(i)  # BSC_PI
        #         bsc_h = TH1F(bsc_h_name,bsc_h_name,xbins,xmin,xmax)

        #         ch.Draw(ED_variable + '*weight >>' + bsc_h_name , cut + ' == 1.0' )
        #         category = ''
        #         cateogry = MC_Cat(tree_name)[0]
        #         bsc_hists.append([bsc_h_name,category])
        # print'bsc_hists = ',bsc_hists
        # exit(0)
        # # Have a list of background subcategory histograms (bsc,pi)
        # # now need to sort into (c,pi)
        # c_hists = [] # will end up as num_cat*numvariables histograms 
        #for bsc_hist in bsc_hists:

        # Then sort into (pi)

        #### Old way below 

        for i, pi in enumerate(plotting_info_):
            print'  Plotting variable',i+1,'/',len(plotting_info_)
            v_info = pi[0]
            variable, xbins, xmin, xmax = v_info[0], v_info[1], v_info[2], v_info[3]
            particle = pi[1]
            cut = pi[2]
            cut_number = cut.split('_')[1]

            if cut_number == '0': cut_name = var_map(cut,'MC',0)
            else:   cut_name = var_map(cut,'Dummy',0)  

            ED_variable = var_map(variable,particle,0) # Variable as called by the event dumper. Call it a non-gen variable to keep map consistent 
            hname = 'MC_' + particle + '_' + variable + '_' + cut_name
            stk = THStack(hname,hname)

            for icat,cat in enumerate(all_bkg_cats):
                print'      Plotting category',icat+1
                bkg_name = cat[0].split('/')[-1].split('_')[1]
                cat_name = MC_Cat(bkg_name)[0]
                h_bkg_name = hname + '_' + cat_name 
                h_cat = TH1F(h_bkg_name,cat_name,xbins,xmin,xmax)
                db = (float(xmax) - float(xmin)) / float(xbins) 
                bkg_color = ''
                p_tree = get_tree(cat[0])
                bkg_color = MC_Cat(p_tree)[2] 
                # h_cat.SetFillColor(eval(bkg_color))            
                for ibp,bkg_path in enumerate(cat):
                    if ibp%50 == 0: print'          On path',ibp,'/',len(cat)
                    h_tmp_name = hname + '_' + str(ibp) 
                    h_tmp = TH1F(h_tmp_name, h_tmp_name, xbins, xmin, xmax)
                    tree_name = get_tree(bkg_path)
                    icategory, color = '' , ''
                    icategory = MC_Cat(tree_name)[1]
                    color = MC_Cat(tree_name)[2]
                    ch = TChain('HHWWggCandidateDumper/trees/' + tree_name )
                    ch.Add(bkg_path)
                    ch.Draw(ED_variable + '*weight >>' + h_tmp_name , cut + ' == 1.0' )
                    nbins = h_tmp.GetNbinsX()
                    
                    for ib,bv in enumerate(h_tmp): # bv = bin value 
                        if (ib == 0): # underflow bin 
                            continue 
                        elif (ib == nbins + 1): # overflow bin 
                            continue 
                        else:
                            h_cat.Fill(float(xmin + (ib - 1)*db), float(bv))
                # print'bkg_color = ',bkg_color 
                # h_cat.SetFillColor(eval(bkg_color))  
                # h_cat.SetDirectory(0)  
                h_cat.SetFillColor(eval(bkg_color))              
                stk.Add(h_cat,'hist') # Thank you so much: https://root-forum.cern.ch/t/th1f-fillcolor-not-working/27922/6
                print'      Finished category:',icat+1
            MC_hists_.append(stk)

        return MC_hists_

def Save_Data_Histos(hists_): #lc__,fc__):
    dec_Data_hists_ = []
    for hist_ in hists_:
        h_title = hist_.GetTitle() # get variable, particle and cut from htitle 
        plabel_, variable_ = h_title.split('_')[1], h_title.split('_')[2]
        cut_name = h_title.split('_')[3]
        c0_ = TCanvas('c0_', 'c0_', 800, 600)
        #hist_.SetDirectory(0)
        hist_.GetYaxis().SetTitle('Events')
        if variable_ == 'pt': hist_.GetXaxis().SetTitle( plabel_ + ' ' + 'p_{T}')
        else: hist_.GetXaxis().SetTitle( variable_ + '_{' + plabel_ + '}')
        hist_.SetMarkerStyle(kFullDotLarge)
        hist_.Draw("P0")
        # print'save data cut_name = ',cut_name 
        save_title = 'Data_' + plabel_ + '_' + variable_ + '_' + cut_name
        file_path3_ = output_Loc + save_title + '.png'
        file_path1_ = output_Loc + save_title + '.pdf'
        file_path2_ = output_Loc + save_title + '.root'
        file_exists1_ = False 
        file_exists2_ = False 
        file_exists3_ = False
        file_exists1_ = path_exists(file_path1_)
        file_exists2_ = path_exists(file_path2_)
        file_exists3_ = path_exists(file_path3_)
        if file_exists1_:   rm_path(file_path1_)
        if file_exists2_:   rm_path(file_path2_)
        hist_.SaveAs(file_path2_)
        #c0_.SaveAs(file_path1_) #pdf 
        c0_.SaveAs(file_path3_)
        dec_Data_hists_.append(hist_)
        #return 0
        # return hist_
    return dec_Data_hists_

def Save_Stack_Histos(hists_):
    dec_MC_hists_ = []
    for hist_ in hists_:
        h_title = hist_.GetTitle() # get variable, particle and cut from htitle 
        plabel_, variable_ = h_title.split('_')[1], h_title.split('_')[2]
        c0_ = TCanvas('c0_', 'c0_', 800, 600)
        file_type = h_title.split('_')[0]
        cut_name = h_title.split('_')[3]
        hist_.SetTitle('Backgrounds ' + plabel_ + ' ' + variable_ + ' ' + cut_name)      
        hist_.Draw()
        c0_.Modified()
        #gPad.BuildLegend(0.75,0.75,0.95,0.95,"")
        l1 = TLegend(0.75,0.75,0.95,0.95)
        for h in hist_.GetStack():
            l1.AddEntry(h,h.GetTitle().split('_')[-1],'f')
        l1.Draw('same')
        save_title = 'MC_' + plabel_ + '_' + variable_ + '_' + cut_name
        file_path3_ = output_Loc + save_title + '.png'
        file_path1_ = output_Loc + save_title + '.pdf'
        file_path2_ = output_Loc + save_title + '.root'
        file_exists1_ = False 
        file_exists2_ = False 
        file_exists3_ = False
        file_exists1_ = path_exists(file_path1_)
        file_exists2_ = path_exists(file_path2_)
        file_exists3_ = path_exists(file_path3_)
        if file_exists1_:   rm_path(file_path1_)
        if file_exists2_:   rm_path(file_path2_)
        if file_exists3_:   rm_path(file_path3_)
        hist_.SaveAs(file_path2_)
        #c0_.SaveAs(file_path1_) #pdf 
        c0_.SaveAs(file_path3_)
        dec_MC_hists_.append(hist_)

    return dec_MC_hists_
# Plot histograms on same canvas 
# Input: list of histograms (or hinfo)
# Output: canvas
# def combine_histos(input_histo_infos_,var_copy_):
def combine_histos(input_histo_infos_,plotting_info_):
    max_vals_ = []
    print'Getting max values'
    # for each plotting info entry, need to get a max value 
    for vi,pi in enumerate(plotting_info_):
        print'  Getting max value for variable',vi+1,'/',len(plotting_info_)
        c0_ = TCanvas('c0', 'c0', 800, 600)
        hists_ = []
        # turn THStack entry into sum of its histo entries 
        input_histo_infos_cpy = list(input_histo_infos_)
        # print'input_histo_infos_cpy = ',input_histo_infos_cpy
        h_data = input_histo_infos_cpy[0][vi] # Data 
        hstack = input_histo_infos_cpy[1][vi] # MC 
        hists_.append(h_data)
        hists_.append(hstack.GetStack().Last())
        # Check which histo has the highest max value to set y axis of combined plot accordingly to fit all values 
        mval = -99
        for hi_,h_ in enumerate(hists_): # hists_ should have data and MC plot for vpc
            hist_max = h_.GetMaximum()
            if hist_max > mval:
                mval = hist_max

        max_vals_.append(mval)

    return max_vals_

#def plot_ratio(ih_,max_val_,xbins__,comb_ID_,xmin_,variable_,p_,c_):
def plot_ratio(ih_,max_vals_,plotting_info_):
    for vi,pi in enumerate(plotting_info_):
        # Canvas for upper and lower plots 
        cc = TCanvas("cc", "canvas", 800, 800)

        # Get Data and MC histos 
        h_data = ih_[0][vi] # Data (TH1F) 
        h_MC = ih_[1][vi] # MC (THStack) 

        # print'h_data.GetTitle():',h_data.GetTitle()
        h_title = h_data.GetTitle()
        max_val_ = max_vals_[vi]
        p_, variable_, cut_name = h_title.split('_')[1], h_title.split('_')[2], h_title.split('_')[3] 

        v_info = pi[0]
        xmin_ = v_info[2]
        #variable, xbins_, xmin_, xmax_ = v_info[0], v_info[1], v_info[2], v_info[3]

        # Set range of MC y axis range to contain both data and MC when combined 
        h_MC.SetMinimum(0)
        h_MC.SetMaximum(max_val_*1.05)
        h_MC.GetYaxis().SetLabelOffset(999) # will create separate axis later 
        h_MC.SetTitle('Data/MC, ' + p_ + ', ' + variable_ + ', ' + cut_name) # particle, variable, cut 

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

        
        leg_ = TLegend(0.75,0.75,0.95,0.95)
        for h in h_MC.GetStack(): # bkg 
            leg_.AddEntry(h,h.GetTitle().split('_')[-1],'f')
        leg_.AddEntry(h_data,'Data','p')
        leg_.Draw('same')

        #cc.SaveAs(output_Loc + "Gen_Reco_" + comb_ID_ + ".png")
        #cc.SaveAs(output_Loc + "Gen_Reco_" + comb_ID_ + ".pdf")
        #print'comb_ID_ = ',comb_ID_ 
        Data_MC_ID = p_ + '_' + variable_ + '_' + cut_name
        cc.SaveAs(output_Loc + "Data_MC_" + Data_MC_ID + ".png")

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