"""
15 December 2021
Abraham Tishelman-Charny

The purpose of this script is to quickly compare variables between NLO reweighted and generated cHHH1.
"""

import uproot 
import numpy as np 
from matplotlib import pyplot as plt 

lessVars = 1

f1 = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted_3Nodes/GluGluToHHTo2G2Qlnu_node_cHHH1_2017_Nominal.root"
f2 = "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production/2017/Signal/SL_NLO_2017_hadded/GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root"

f_u1 = uproot.open(f1)
f_u2 = uproot.open(f2)

tname1 = "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_13TeV_HHWWggTag_0"
tname2 = "GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0_v1"
 
w1 = f_u1[tname1]["weight"].array()
w2 = f_u2[tname2]["weight"].array()

t1 = f_u1[tname1]
t2 = f_u2[tname2]


ol = "/eos/user/a/atishelm/www/HHWWgg/Reweight_Validation_NLOToNLOForAN20165v7/"

variables = [
    
##-- Combination of branches 
                "Scaled_Leading_Photon_E",
                "Scaled_Subleading_Photon_E",
                "Leading_Jet_bscore",
                "Subleading_Jet_bscore",        
                "Scaled_Leading_Photon_pt",
                "Scaled_Subleading_Photon_pt",
    
##-- Existing Branches 
                "CMS_hgg_mass",
                "Leading_Photon_pt",
                "Subleading_Photon_pt",
                "Leading_Photon_E",
                "Subleading_Photon_E",
                "CMS_hgg_mass",
                "goodJets_0_pt",
                "goodLepton_pt",
                "Wmass_goodJets12",
                "goodJets_1_E",
                "goodJets_1_pt",
                "goodLepton_E",
                "METCor_pt",
                "goodJets_0_E",
                "goodLepton_phi",
                "Leading_Photon_MVA",
                "goodLepton_eta",
                "goodJets_1_eta",
                "goodJets_1_phi",
                "Subleading_Photon_eta",
                "Subleading_Photon_phi",
                "N_goodJets",
                "goodJets_0_phi",
                "Leading_Photon_phi",
                "Subleading_Photon_MVA",
                "goodJets_0_eta",
                "Leading_Photon_eta",
                "Wmt_L" 
    
]

if(lessVars):
    variables = [
        # "Leading_Photon_pt",
        # "Subleading_Photon_pt",
        # "Leading_Photon_E",
        # "Subleading_Photon_E",
        # "CMS_hgg_mass",
        # "Leading_Photon_MVA",
        # "Subleading_Photon_MVA",
        # "goodJets_1_eta", 
        # "goodJets_1_phi", 
        # "Leading_Photon_phi",
        # "goodJets_0_eta",
        # "Leading_Photon_eta", 
        # "Subleading_Photon_eta",
        # "Subleading_Photon_phi", 
        # "N_goodJets",
        # "goodJets_0_phi"

    # "Scaled_Leading_Photon_E" ,
    # "Scaled_Subleading_Photon_E" ,
    # "Scaled_Leading_Photon_pt",
    # "Scaled_Subleading_Photon_pt",


            "goodJets_0_pt",
            "goodJets_1_E",
            "goodJets_1_pt",
            "goodJets_0_E",

    ]


nbins_glob = 20
VarInfoDict = {
                    "Leading_Photon_pt": [nbins_glob,0,360, "GeV"],
                    "Subleading_Photon_pt": [nbins_glob,0,200, "GeV"],
                    "Leading_Photon_E": [nbins_glob,0,360, "GeV"],
                    "Subleading_Photon_E": [nbins_glob,0,360, "GeV"],    
                    "CMS_hgg_mass" : [nbins_glob, 115, 135, "GeV"],
                    "Leading_Photon_MVA": [nbins_glob,-1,1, "unitless"],
                    "Subleading_Photon_MVA": [nbins_glob,-1,1, "unitless"],
                    "goodJets_1_eta" : [nbins_glob,-2.5,2.5, 'radians'],
                    "goodJets_1_phi" : [nbins_glob,-3.14,3.15,'radians'],
                    "Leading_Photon_phi" : [nbins_glob,-3.14,3.15,'radians'],
                    "goodJets_0_eta" : [nbins_glob,-2.5,2.5, 'radians'],
                    "Leading_Photon_eta" : [nbins_glob,-2.5,2.5, 'radians'],
                    "Subleading_Photon_eta" : [nbins_glob,-2.5,2.5, 'radians'],
                    "Subleading_Photon_phi" : [nbins_glob,-3.14,3.15,'radians'],
                    "N_goodJets" : [5, 0, 5, "unitless"],
                    "goodJets_0_phi" : [nbins_glob,-3.14,3.15,'radians'],

                #     "CMS_hgg_mass": [nbins_glob,100,180],
                #     "weight":[nbins_glob,-10,10],
                #     "puweight":[nbins_glob,-2,2],
                #     "mjj" : [nbins_glob,0,300],
                #     "e_mT" : [nbins_glob,0,300],
                #     "mu_mT" : [nbins_glob,0,300],
                #     "dr_gg" : [nbins_glob,0,3],
                #     "dr_jj" : [nbins_glob,0,3],
                #     "pT_gg" : [nbins_glob,0,400],

                    "goodJets_0_pt" : [nbins_glob,0,500,"GeV"],
                    "goodLepton_pt" : [nbins_glob,0,360, "GeV"],
                    "Wmass_goodJets12": [nbins_glob,0,500, "GeV"],
                    # "Subleading_Photon_pt/CMS_hgg_mass",
                    "goodJets_1_E": [nbins_glob,0,300,"GeV"],
                    "goodJets_1_pt": [nbins_glob,0,200,"GeV"],
                    "goodLepton_E": [nbins_glob,0,360,"GeV"],
                    "METCor_pt": [nbins_glob,0,250,"GeV"],
                    "goodJets_0_E": [nbins_glob,0,360,"GeV"],
                    "Scaled_Leading_Photon_pt" : [nbins_glob,0.2,1.5,"unitless"],
                    "Scaled_Subleading_Photon_pt" : [nbins_glob,0.2,1.5,"unitless"],
                    "Scaled_Leading_Photon_E" : [nbins_glob,0,1.5,"unitless"],
                    "Scaled_Subleading_Photon_E" : [nbins_glob,0,1.5,"unitless"],
                    "Leading_Jet_bscore" : [nbins_glob,0,1,"unitless"],
                    "Subleading_Jet_bscore" : [nbins_glob,0,1,"unitless"],
                    "goodLepton_phi" : [nbins_glob,-3.14,3.15,'radians'],
                    "goodLepton_eta" : [nbins_glob,-2.5,2.5, 'radians'],
                    "Wmt_L" : [nbins_glob,0,300,"GeV"],
                    "Leading_Jet_bscore" : [nbins_glob, 0, 1, "unitless"],
                    "Subleading_Jet_bscore" : [nbins_glob, 0, 1, "unitless"],
}

# specialVars = [
#                 "Scaled_Leading_Photon_E",
#                 "Scaled_Subleading_Photon_E",
#                 "Leading_Jet_bscore",
#                 "Subleading_Jet_bscore",        
#                 "Scaled_Leading_Photon_pt",
#                 Scaled_Subleading_Photon_pt,    
# ]

specialVars = {
    "Scaled_Leading_Photon_E" : ["divide", "Leading_Photon_E", "CMS_hgg_mass"],
    "Scaled_Subleading_Photon_E" : ["divide", "Subleading_Photon_E", "CMS_hgg_mass"],
#     "Leading_Jet_bscore": ["add", "Leading_Photon_E", "CMS_hgg_mass"],
#     "Subleading_Jet_bscore": ["add", "Leading_Photon_E", "CMS_hgg_mass"],        
    "Scaled_Leading_Photon_pt": ["divide", "Leading_Photon_pt", "CMS_hgg_mass"],
    "Scaled_Subleading_Photon_pt": ["divide", "Subleading_Photon_pt", "CMS_hgg_mass"],      
}


for v in variables:
    print("On variable:",v)
    
    ##-- Check if multiple branches needed
    if v in specialVars.keys():
        operation, v1, v2 = specialVars[v]
        
        ##-- NLO Variable
        v1_vals_NLO = t1[v1].array()
        v2_vals_NLO = t1[v2].array()  
        exec("NLO_var = np.%s(v1_vals_NLO, v2_vals_NLO)"%(operation))
        
        ##-- LO Variable from sum of benchmarks
        v1_vals_LO_NLO = t2[v1].array()
        v2_vals_LO_NLO = t2[v2].array()          
        exec("LO_NLO_var = np.%s(v1_vals_LO_NLO, v2_vals_LO_NLO)"%(operation))

    elif v == "Leading_Jet_bscore":
        
        ##-- LO Variable from sum of benchmarks
        LO_NLO_var = np.array([])
        for node in nodes:
            path = "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production/2017/Signal/GluGluToHHTo2G2Qlnu_node_%s_2017_LO_withNLOweights_HHWWggTag_0_MoreVars.root"%(node)
            f = uproot.open(path)
            t = f["GluGluToHHTo2G2Qlnu_node_%s_13TeV_HHWWggTag_0_v1"%(node)]
        
        
            LO_NLO_var_thisNode_ = np.add(t["goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probb"].array(), 
                                t["goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probbb"].array())
            LO_NLO_var_thisNode = np.add(LO_NLO_var_thisNode_, t["goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_problepb"].array())   
            LO_NLO_var = np.append(LO_NLO_var, LO_NLO_var_thisNode)
        
        NLO_var_ = np.add(t1["goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probb"].array(), 
                            t1["goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probbb"].array())
        NLO_var = np.add(NLO_var_, t1["goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_problepb"].array())        
        
        
    elif v == "Subleading_Jet_bscore":
        
        ##-- LO Variable from sum of benchmarks
        LO_NLO_var = np.array([])
        for node in nodes:
            path = "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production/2017/Signal/GluGluToHHTo2G2Qlnu_node_%s_2017_LO_withNLOweights_HHWWggTag_0_MoreVars.root"%(node)
            f = uproot.open(path)
            t = f["GluGluToHHTo2G2Qlnu_node_%s_13TeV_HHWWggTag_0_v1"%(node)]
        
        
            LO_NLO_var_thisNode_ = np.add(t["goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probb"].array(), 
                                t["goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probbb"].array())
            LO_NLO_var_thisNode = np.add(LO_NLO_var_thisNode_, t["goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_problepb"].array())   
            LO_NLO_var = np.append(LO_NLO_var, LO_NLO_var_thisNode)        

        
        NLO_var_ = np.add(t1["goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probb"].array(), 
                            t1["goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probbb"].array())
        NLO_var = np.add(NLO_var_, t1["goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_problepb"].array())            
        
    else:
        LO_NLO_var = t2[v].array()
        NLO_var = t1[v].array()
    nbins, xmin, xmax, unit = VarInfoDict[v]
    bins = np.linspace(xmin, xmax, nbins + 1)
    
    ##-- Switch to dtype float for ratios avoiding zeros 
    LO_NLO_weighted_var_a = np.array(LO_NLO_var, dtype = float)
    NLO_weighted_var_a = np.array(NLO_var, dtype = float)
    
#     MASK_LO_NLO = np.logical_and(LO_NLO_weighted_var_a != -999, LO_NLO_weighted_var_a != -99)
#     MASK_NLO = np.logical_and(NLO_weighted_var_a != -999, NLO_weighted_var_a != -99)
    
#     LO_NLO_weighted_var_a = LO_NLO_weighted_var_a[MASK_LO_NLO]
#     NLO_weighted_var_a = NLO_weighted_var_a[MASK_NLO]
    
#     LO_NLO_Full_Weight = LO_NLO_Full_Weight[MASK_LO_NLO]
#     NLO_weight = NLO_weight[MASK_NLO]
    
    ##-- Bin into histograms to get bin heights 
    
    #hist

    LO_NLO_bin_vals, binedges = np.histogram(LO_NLO_weighted_var_a, bins = bins, weights = w2)
    NLO_bin_vals, binedges = np.histogram(NLO_weighted_var_a, bins = bins, weights = w1) 
    
    LO_NLO_bin_NOMCWEIGHTS_vals, binedges = np.histogram(LO_NLO_weighted_var_a, bins = bins)
    NLO_bin_NOMCWEIGHTS_vals, binedges = np.histogram(NLO_weighted_var_a, bins = bins)     
    
    LO_NLO_bin_NOMCWEIGHTS_vals_a = np.array(LO_NLO_bin_NOMCWEIGHTS_vals, dtype = float)
    NLO_bin_NOMCWEIGHTS_vals_a = np.array(NLO_bin_NOMCWEIGHTS_vals, dtype = float)
    
    ##-- Normalize histograms to max height = 1
#     LO_NLO_max = np.amax(LO_NLO_bin_vals)
#     NLO_max = np.amax(NLO_bin_vals)
#     LO_NLO_bin_vals_a_ = np.array([val/LO_NLO_max for val in LO_NLO_bin_vals])
#     NLO_bin_vals_a_ = np.array([val/NLO_max for val in NLO_bin_vals])

    ##-- Normalize histograms to sum = 1
    # LO_NLO_sum = np.sum(LO_NLO_bin_vals)
    # NLO_sum = np.sum(NLO_bin_vals)
    
    # LO_NLO_bin_vals_a_ = np.array([val/LO_NLO_sum for val in LO_NLO_bin_vals])
    # NLO_bin_vals_a_ = np.array([val/NLO_sum for val in NLO_bin_vals])
    
    # LO_NLO_bin_vals_a = np.array(LO_NLO_bin_vals_a_, dtype = float)
    # NLO_bin_vals_a = np.array(NLO_bin_vals_a_, dtype = float)

    ##-- No normalization 
    LO_NLO_bin_vals_a = np.array(LO_NLO_bin_vals, dtype = float)
    NLO_bin_vals_a = np.array(NLO_bin_vals, dtype = float)
    
    ratio = np.true_divide(LO_NLO_bin_vals_a , NLO_bin_vals_a, out = np.zeros_like(NLO_bin_vals_a), where = NLO_bin_vals_a != 0)
    
    ##-- Get error on each bin ratio 
    ratio_errors = []
    MCscaled_errors_1 = []
    MCscaled_errors_2 = []
    for i, ratio_val in enumerate(ratio):
            
        MCSCALED_val_1 = LO_NLO_bin_vals_a[i] 
        MCSCALED_val_2 = NLO_bin_vals_a[i]
        val_1 = LO_NLO_bin_NOMCWEIGHTS_vals_a[i]
        val_2 = NLO_bin_NOMCWEIGHTS_vals_a[i]
        
        if(val_2 == 0): 

            if(val_1 == 0):
                MCscaled_errors_1.append(0)
                
            else:
                relative_error_1 = float(NOMCWEIGHTS_error1)/float(val_1)
                scaled_error_1 = float(MCSCALED_val_1) * float(relative_error_1)
                MCscaled_errors_1.append(scaled_error_1)                
            
            MCscaled_errors_2.append(0)
            ratio_errors.append(0)
            continue 
        else:
            NOMCWEIGHTS_ratio = val_1 / val_2
            NOMCWEIGHTS_error1 = np.sqrt(val_1)
            NOMCWEIGHTS_error2 = np.sqrt(val_2)
            
#             if(val_1 == 0):
#                 MCscaled_errors_1.append(0)
                
#             else:
#                 relative_error_1 = float(NOMCWEIGHTS_error1)/float(val_1)
#                 scaled_error_1 = float(MCSCALED_val_1) * float(relative_error_1)
#                 MCscaled_errors_1.append(scaled_error_1)               
            
            if(val_1 == 0):
                relative_error_1 = 0
            else: 
                relative_error_1 = float(NOMCWEIGHTS_error1)/float(val_1)
            relative_error_2 = float(NOMCWEIGHTS_error2)/float(val_2)            
            
            relative_error = np.sqrt((relative_error_1)**2 + (relative_error_2)**2)
            
            scaled_error_1 = float(MCSCALED_val_1) * float(relative_error_1)
            scaled_error_2 = float(MCSCALED_val_2) * float(relative_error_2)
            
            ratio_error = float(ratio_val) * float(relative_error) 
            
            ratio_errors.append(ratio_error)  
            MCscaled_errors_1.append(scaled_error_1)
            MCscaled_errors_2.append(scaled_error_2)
    
            
    ##-- Overlay two plots and plot ratio 
    fig, axarr = plt.subplots(2, 
                                sharex=True, 
                                gridspec_kw={
                                    'hspace': 0.15,
#                                     'height_ratios': (0.8,0.2)
                                    'height_ratios': (0.7,0.3)
                                    }
                                )     
      
    upper = axarr[0]
    lower = axarr[1]
    lower.grid(True)    
    
    fig.set_size_inches(8, 6)
    
    bincenters = 0.5*(binedges[1:]+binedges[:-1])   

    upper.hist(bins[:-1], bins = bins, weights = LO_NLO_bin_vals_a, histtype = 'step', label = "Generated NLO", alpha = 1) 
    upper.hist(bins[:-1], bins = bins, weights = NLO_bin_vals_a, histtype = 'step', label = r'NLO$\rightarrow$SM NLO Reweight', alpha = 1)

    upper.errorbar(
                bincenters,
                LO_NLO_bin_vals_a,
#                 weights = LO_NLO_bin_vals_a,
                yerr=MCscaled_errors_1,
                ecolor = 'black',
                linestyle = '',
                fmt = 'none',
#                 zorder = zorder_nominal + 0.5 
#                     zorder = float(float(NUM_COLORS) - float(i)) ##-- For opposite mass point z-ordering in plot
#                     zorder = i + 0.5
    )  
    
    upper.errorbar(
                bincenters,
                NLO_bin_vals_a,
                yerr=MCscaled_errors_2,
                ecolor = 'black',
                linestyle = '',
                fmt = 'none',
#                 zorder = zorder_nominal + 0.5 
#                     zorder = float(float(NUM_COLORS) - float(i)) ##-- For opposite mass point z-ordering in plot
#                     zorder = i + 0.5
    )      
    
    plt.text(
        # 0.05, 0.9, u"CMS $\it{Preliminary}$",
        0., 1., u"CMS ",
        fontsize=18, fontweight='bold',
        horizontalalignment='left',
        verticalalignment='bottom',
        transform=upper.transAxes
    )
    plt.text(
        # 0.05, 0.9, u"CMS $\it{Preliminary}$",
        0.11, 1., r"$\it{Simulation}$ $\it{Preliminary}$",
        fontsize=18,
        horizontalalignment='left',
        verticalalignment='bottom',
        transform=upper.transAxes
    )    
    
    upper.set_ylabel("MC Scaled Yields", fontsize = 15)
    bin_centers = [ (((float(bins[i+1]) - float(bins[i])) / 2.) + float(bins[i])) for i in range(0, len(bins)-1)]
    lower.plot([xmin,xmax],[1,1],linestyle=':', color = 'black')
    xerr = [ ((float(bins[i+1]) - float(bins[i])) / 2.) for i in range(0, len(bins) - 1)]  
    
    zero_errors = [0 for entry in ratio_errors] ##-- for no errors 
    
    lower.errorbar(bin_centers, ratio, xerr = xerr , yerr = ratio_errors, marker = '.', color = 'black', ls = '') #drawstyle = 'steps-mid')
    lower.set_ylim(0.5,1.5)
    lower.set_ylabel("Reweight / NLO", fontsize = 10)
    lower.set_xlabel("%s [%s]"%(v, unit), fontsize = 15)   
#     upper.legend(loc = 'best', prop={'size': 10})
#     upper.legend(loc = 'best', prop={'size': 10})
    upper.grid(True)
    fig.tight_layout()
    upper.legend(loc = 'best', prop={'size': 10})

    plt.savefig("%s/nonLog/%s.png"%(ol, v))
    plt.savefig("%s/nonLog/%s.pdf"%(ol, v))
    upper.set_yscale('log')
    plt.savefig("%s/log/%s_log.png"%(ol, v))
    plt.savefig("%s/log/%s_log.pdf"%(ol, v))    
    
    plt.close()    


print("DONE")












# for v in vars:

#     print("On variable:",v)

#     xmin, xmax, xbins = varBinDict[v]
#     bins = np.linspace(xmin, xmax, xbins + 1)
#     binWidth = (xmax - xmin) / xbins       

#     v1 = f_u1[tname1][v].array()
#     v2 = f_u2[tname2][v].array()

#     # get histogram bin values 
#     binVals_1, edges_1, _ = plt.hist(v1, bins = bins, weights = np.multiply(v1, w1)) 
#     plt.close() # to avoid showing intermediate histogram
#     binVals_2, edges_2, _ = plt.hist(v2, bins = bins, weights = np.multiply(v2, w2)) 
#     plt.close() # to avoid showing intermediate histogram        

#     fig, axarr = plt.subplots(2, sharex=True, gridspec_kw={ 'hspace': 0.15, 'height_ratios': (0.7,0.3) } )
#     fig.set_dpi(100)
#     fig.set_size_inches(10, 7.5)
#     upper = axarr[0]
#     lower = axarr[1]  

#     upper.hist(bins[:-1], bins = bins, weights = binVals_1, histtype = 'step', linewidth = 2, label = "NLO Reweighted to cHHH1", color = 'C0')
#     upper.hist(bins[:-1], bins = bins, weights = binVals_2, histtype = 'step', linewidth = 2, label = "Generated cHHH1", color = 'C1')    

#     plt.savefig("{v}_plot.png".format(v=v))
#     plt.close()

# print("DONE")


# # parameters 
# upperRightText = "Pilot Beam 2021"
# text_xmin = 0.1

# ##-- Prepare figure and axes 
# fig, ax = plt.subplots()

# fig.set_dpi(100)
# fig.set_size_inches(10, 7.5)
# # cmap = plt.cm.Blues
# # cmap = plt.cm.RdBu_r # for sym log 
# cmap = plt.cm.jet
# cmap.set_under(color='white') 

# if("tagged" in selection):
#     vmax = vmaxAll
# else:
#     vmax = None
#     # plt.clim(0, vmaxAll)

# # plot with colormesh 
# if(isRatio): 
#     vmin = 0.00000001
# else: 
#     vmin = 1 
# if(doSymLog): 
#     norm = norm = SymLogNorm(linthresh=0.03, vmin = vmin)
# else: 
#     norm = None 

# if(zmax != -1):
#     vmax = zmax 

# pos = ax.pcolormesh(xbins, 
#                     ybins, 
#                     Values_array.transpose(1,0), 
#                     cmap = cmap, 
#                     vmin = vmin,
#                     vmax = vmax,
#                     norm = norm
#                     )
# cb = fig.colorbar(pos, 
#                 ax=ax,
#             )    


# xLabel, yLabel = GetPlotLabels(varLabel)

# plt.xlabel(xLabel, fontsize=25)
# plt.ylabel(yLabel, fontsize=25)

# Add_CMS_Header(plt, ax, upperRightText, text_xmin)

# plt.grid()
# plotText, addPlotText = plotText_params
# plotText = plotText.replace("clean_", "")

# if(addPlotText):
#     plt.text(
#         0.1, 0.75, plotText,
#         fontsize=30, fontweight='bold',
#         horizontalalignment='left',
#         verticalalignment='bottom',
#         transform=ax.transAxes
#     )

# ol = "/eos/user/a/atishelm/www/EcalL1Optimization/PilotBeam2021/"
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# fig.tight_layout()
# plt.savefig("{ol}/{varLabel}_{selection}.png".format(ol=ol, varLabel=varLabel, selection=selection))
# plt.savefig("{ol}/{varLabel}_{selection}.pdf".format(ol=ol, varLabel=varLabel, selection=selection))
# plt.close()    