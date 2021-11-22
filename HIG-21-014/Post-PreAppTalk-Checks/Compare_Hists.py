"""
10 November 2021 
Abraham Tishelman-Charny 

The purpose of this python module is to compare histograms, including their per bin agreement. 

Example command: 
python3 Compare_Hists.py --years 2017 --plotReweighted --nodes 8a --EFT_DNN
python3 Compare_Hists.py --years 2017 --plotReweighted --nodes 8a --EFT_DNN --variable CMS_hgg_mass

"""

import uproot 
from matplotlib import pyplot as plt 
import numpy as np
import pandas as pd
import argparse 

from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

# read input arguments 
parser = argparse.ArgumentParser()
parser.add_argument("--years", type = str, default = "2017", help = "Comma separated list of years to run ")
parser.add_argument("--nodes", type = str, default = "cHHH1", help = "Comma separated list of nodes to run ")
parser.add_argument("--variables", type = str, default = "evalDNN_HH", help = "Comma separated list of variables to plot")
parser.add_argument("--AddRatioErrors", action="store_true", default = True, help = "Add error bars on ratio values")
parser.add_argument("--compareFullandCategorized", action="store_true", help = "Compare full reweighted sample to categorized reweighted sample to verify categorization worked")
parser.add_argument("--compareFullandGenerated", action="store_true", help = "compare full NLO (all samples) reweighted to a generated node's DNN score")
parser.add_argument("--plotReweighted", action="store_true", help = "Plot reweighted DNN score")
parser.add_argument("--EFT_DNN", action="store_true", help = "When plotting DNN score, use files with DNN score from EFT binary DNN")
parser.add_argument("--Selections", type = str, default="None", help = "Comma separated list of selections to apply")
args = parser.parse_args()

years = args.years.split(',')
nodes = args.nodes.split(',')
AddRatioErrors = args.AddRatioErrors
compareFullandCategorized = args.compareFullandCategorized
compareFullandGenerated = args.compareFullandGenerated
plotReweighted = args.plotReweighted
EFT_DNN = args.EFT_DNN
variables = args.variables.split(',') 

def make_error_boxes(ax, xdata, ydata, xerror, yerror, facecolor='r',
                     edgecolor='None', alpha=0.5):

    # Loop over data points; create box from errors at each point
    errorboxes = [Rectangle((x - xe[0], y - ye[0]), xe.sum(), ye.sum())
                  for x, y, xe, ye in zip(xdata, ydata, xerror.T, yerror.T)]

    # Create patch collection with specified colour/alpha
    pc = PatchCollection(errorboxes, facecolor=facecolor, alpha=alpha,
                         edgecolor=edgecolor)

    # Add collection to axes
    ax.add_collection(pc)

    # Plot errorbars
    artists = ax.errorbar(xdata, ydata, xerr=xerror, yerr=yerror,
                          fmt='None', ecolor='k')

    return artists

def hist_bin_uncertainty(data, weights, bin_edges):
    """
    The statistical uncertainity per bin of the binned data.
    If there are weights then the uncertainity will be the root of the
    sum of the weights squared.
    If there are no weights (weights = 1) this reduces to the root of
    the number of events.

    Args:
        data: `array`, the data being histogrammed.
        weights: `array`, the associated weights of the `data`.
        bin_edges: `array`, the edges of the bins of the histogram.

    Returns:
        bin_uncertainties: `array`, the statistical uncertainity on the bins.

    Example:
    >>> x = np.array([2,9,4,8])
    >>> w = np.array([0.1,0.2,0.3,0.4])
    >>> edges = [0,5,10]
    >>> hist_bin_uncertainty(x, w, edges)
    array([ 0.31622777,  0.4472136 ])
    >>> hist_bin_uncertainty(x, None, edges)
    array([ 1.41421356,  1.41421356])
    >>> hist_bin_uncertainty(x, np.ones(len(x)), edges)
    array([ 1.41421356,  1.41421356])
    """
    # Bound the data and weights to be within the bin edges
    in_range_index = [idx for idx in range(len(data))
                      if data[idx] > min(bin_edges) and data[idx] < max(bin_edges)]
    in_range_data = np.asarray([data[idx] for idx in in_range_index])

    if weights is None or np.array_equal(weights, np.ones(len(weights))):
        # Default to weights of 1 and thus uncertainty = sqrt(N)
        in_range_weights = np.ones(len(in_range_data))
    else:
        in_range_weights = np.asarray([weights[idx] for idx in in_range_index])

    # Bin the weights with the same binning as the data
    bin_index = np.digitize(in_range_data, bin_edges)
    # N.B.: range(1, bin_edges.size) is used instead of set(bin_index) as if
    # there is a gap in the data such that a bin is skipped no index would appear
    # for it in the set
    binned_weights = np.asarray(
        [in_range_weights[np.where(bin_index == idx)[0]] for idx in range(1, len(bin_edges))])
    bin_uncertainties = np.asarray(
        [np.sqrt(np.sum(np.square(w))) for w in binned_weights])
    return bin_uncertainties

if (__name__ == '__main__'):

    varBinDict = {
        # variable : [xmin, xmax, nBins]
        "evalDNN_HH" : [0.1, 1, 30],
        "evalDNN_HH_0" : [0.935714285714, 1., 10],
        "evalDNN_HH_1" : [0.82, 0.935714285714, 10],
        "evalDNN_HH_2" : [0.64, 0.82, 10],
        "evalDNN_HH_3" : [0.1, 0.64, 10],
        "CMS_hgg_mass" : [105, 140, 35],
        "Leading_Photon_pt" : [0, 100, 20]
    }

    reweightDict = {
        "cHHH0" : "weight_NLO_cHHH0",
        "cHHH1" : "weight_NLO_SM",
        "cHHH2p45" : "weight_NLO_cHHH2", # typo in reweight branch names. "weight_NLO_cHHH2" corresponds to cHHH2p45 
        "cHHH5" : "weight_NLO_cHHH5",
        "cttHH3" : "weight_NLO_cttHH3",
        "cttHH0p35" : "weight_NLO_cttHH0p35",
        "3D3" : "weight_NLO_3D3",
        "8a" : "weight_NLO_8a",
        "1b" : "weight_NLO_1b",
        "2b" : "weight_NLO_2b",
        "3b" : "weight_NLO_3b",
        "4b" : "weight_NLO_4b",
        "5b" : "weight_NLO_5b",
        "6b" : "weight_NLO_6b",
        "7b" : "weight_NLO_7b",
        "1"  : "weight_NLO_1",
        "2"  : "weight_NLO_2",
        "3"  : "weight_NLO_3",
        "4"  : "weight_NLO_4",
        "5"  : "weight_NLO_5",
        "6"  : "weight_NLO_6",
        "7"  : "weight_NLO_7",
        "8"  : "weight_NLO_8",
        "9"  : "weight_NLO_9",
        "10"  : "weight_NLO_10",
        "11"  : "weight_NLO_11",
        "12"  : "weight_NLO_12",
    }

    cats = ["0", "1", "2", "3"]    

    if(compareFullandCategorized):
        for variable in variables:
            for node in nodes:
                print("On node:",node)
                for year in years:
                    print("On year:",year)
                    for cat in cats:
                        print("on category:",cat)
                        variable_bins = "evalDNN_HH_{cat}".format(cat=cat)
                        xmin, xmax, xbins = varBinDict[variable_bins]
                        bins = np.linspace(xmin, xmax, xbins + 1)
                        binWidth = (xmax - xmin) / xbins                

                        # file 1 
                        Full_NLO_f = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(year=year)
                        Full_NLO_ntuple = uproot.open(Full_NLO_f)
                        Full_NLO_tree = Full_NLO_ntuple["GluGluToHHTo2G2Qlnu_node_All_NLO_{year}_Normalized_13TeV_HHWWggTag_0".format(year=year)]
                        Full_NLO_variable = Full_NLO_tree[variable].array()
                        Full_NLO_weight = Full_NLO_tree["weight"].array()
                        reweightName = reweightDict[node]
                        Full_NLO_reweight = Full_NLO_tree[reweightName].array()

                        # file 2 
                        Categorized_NLO_f = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{node}/GluGluToHHTo2G2Qlnu_node_{node}_{year}_Categorized.root".format(year=year, node=node)
                        Categorized_NLO_ntuple = uproot.open(Categorized_NLO_f)
                        Categorized_NLO_tree = Categorized_NLO_ntuple["GluGluToHHTo2G2Qlnu_node_{node}_{year}_13TeV_HHWWggTag_SL_{cat}".format(node=node, year=year, cat=cat)]
                        Categorized_NLO_variable = Categorized_NLO_tree[variable].array()
                        Categorized_NLO_weight = Categorized_NLO_tree["weight"].array()

                        # get histogram bin values 
                        Full_NLO_binVals, Full_NLO_edges, _ = plt.hist(Full_NLO_variable, bins = bins, weights = np.multiply(Full_NLO_weight, Full_NLO_reweight)) 
                        plt.close() # to avoid showing intermediate histogram
                        Categorized_NLO_binVals, Categorized_NLO_edges, _ = plt.hist(Categorized_NLO_variable, bins = bins, weights = Categorized_NLO_weight) 
                        plt.close() # to avoid showing intermediate histogram             

                        # create ratio plot ###--- Make this a function which takes bin heights as input 
                        fig, axarr = plt.subplots(2, sharex=True, gridspec_kw={ 'hspace': 0.15, 'height_ratios': (0.7,0.3) } )

                        fig.set_dpi(100)
                        fig.set_size_inches(10, 7.5)
                        upper = axarr[0]
                        lower = axarr[1]      

                        binCenters = [float(a) + (float(binWidth)/2.) for a in Full_NLO_edges[:-1]] # use one histogram's since they should all be the same anyway --- this assumes equally distanced bins 
                        zero_errors = [0 for entry in binCenters]                  

                        # get uncertainties
                        Full_NLO_binned_MC_stat_uncertainties = hist_bin_uncertainty(Full_NLO_variable, np.multiply(Full_NLO_weight, Full_NLO_reweight), bins)
                        Categorized_NLO_binned_MC_stat_uncertainties = hist_bin_uncertainty(Categorized_NLO_variable, Categorized_NLO_weight, bins)

                        upper.hist(bins[:-1], bins = bins, weights = Full_NLO_binVals, histtype = 'step', linewidth = 2, label = "All NLO Reweighted to {node}".format(node=node), color = 'C0')
                        upper.hist(bins[:-1], bins = bins, weights = Categorized_NLO_binVals, histtype = 'step', linewidth = 2, label = "Categorized {node}".format(node=node), color = 'C1')

                        capthick = 0
                        capsize = 0
                        elinewidth = 3

                        upper.errorbar(x = binCenters, 
                                    y = Full_NLO_binVals, 
                                    yerr = Full_NLO_binned_MC_stat_uncertainties, 
                                    color = 'C0', 
                                    fmt = " ", 
                                    capthick = capthick, 
                                    capsize = capsize, 
                                    elinewidth = elinewidth
                                    )

                        upper.errorbar(x = binCenters, 
                                    y = Categorized_NLO_binVals, 
                                    yerr = Categorized_NLO_binVals, 
                                    color = 'C1' , 
                                    fmt = " ", 
                                    capthick = capthick, 
                                    capsize = capsize, 
                                    elinewidth = elinewidth
                                    )

                        sum_1_ = np.sum(Full_NLO_binVals)
                        sum_2_ = np.sum(Categorized_NLO_binVals)

                        roundPrecision = 4

                        sum_1 = round(sum_1_, roundPrecision)
                        sum_2 = round(sum_2_, roundPrecision)
                        sum_ratio = round(float(sum_1_/sum_2_), roundPrecision)

                        # Ratio 
                        lower.tick_params(axis = 'x', labelsize = 13)
                        upper.tick_params(axis = 'y', labelsize = 13)
                        upper.set_ylabel("Yield", fontsize = 20)
                        upper.ticklabel_format(style='plain') ##-- Remove scientific notation
                        lower.set_xlabel(variable, fontsize = 20)
                        lower.set_ylabel("Full / Categorized", fontsize = 15)
                        plt.yticks(fontsize=15)
                        plt.xticks(fontsize=15)        
                        lower.set_ylim(0.5, 1.5)
                        lower.plot([xmin, xmax],[1,1],linestyle=':', color = 'black')

                        ratio = np.true_divide(Full_NLO_binVals, Categorized_NLO_binVals, out = np.zeros_like(Categorized_NLO_binVals), where = Categorized_NLO_binVals != 0)

                        # Stat errors on ratio 
                        errors = []
                        for val_i, Full_NLO_val in enumerate(Full_NLO_binVals):
                            Categorized_NLO_val = Categorized_NLO_binVals[val_i]
                            r_val = ratio[val_i]
                            if(Categorized_NLO_val <= 0): 
                                errors.append(0.)
                            else:
                                # event weight = 1 uncertainty 
                                # rel_err = np.sqrt( (1 / NLO_reweighted_val) + (1 / Node_val) ) # statistical uncertainty assuming event weights of 1 
                                # err = float(rel_err) * r_val

                                # Taking weights into account
                                Full_NLO_w2 = Full_NLO_binned_MC_stat_uncertainties[val_i]
                                Categorized_w2 = Categorized_NLO_binned_MC_stat_uncertainties[val_i]
                                rel_err = np.sqrt( (Categorized_w2 / Categorized_NLO_val ) + (Full_NLO_w2 / Full_NLO_val)**2 ) # sqrt(sum(w^2)) per bin for MC stack uncertainty 
                                err = float(rel_err) * r_val 

                                errors.append(err)

                        if(AddRatioErrors): yErrors = errors 
                        else: yErrors = zero_errors

                        lower.errorbar(binCenters, ratio, xerr = zero_errors , yerr = yErrors, marker = '.', color = 'black', ls = '')  

                        # Decorate 
                        upper.set_title(year, fontsize = 30)
                        upper.text(
                            0., 1., r"HH$\rightarrow$WW$\gamma\gamma$",
                            fontsize=20, fontweight='bold',
                            horizontalalignment='left',
                            verticalalignment='bottom',
                            transform=upper.transAxes
                        )

                        upper.text(
                            0.5, 0.2, "\n".join((
                                    r"$\int$ Full = %s"%(sum_1),
                                    r"$\int$ Cat = %s"%(sum_2),
                                    "ratio = %s"%(sum_ratio)    
                                ),                        
                            ),
                            fontsize=15, fontweight='bold',
                            horizontalalignment='center',
                            verticalalignment='bottom',
                            transform=upper.transAxes                 
                        )

                #         # upper.legend(loc = 'best', fontsize = 18, title = "Comparison", title_fontsize = 20) # with title 
                        upper.legend(loc = 'upper right', fontsize = 18)
                        upper.grid()

                #         # axarr_node = fig
                #         # axarr_node[i_year] = axarr

                #         # exec("ax_%s = axarr_node[%s]"%(i_year))
                        ol = "/eos/user/a/atishelm/www/HHWWgg/HIG-21-014/PostPreAppTalkChecks/SemileptonicEFTReweighting/Categorized/"
                        plt.savefig("{ol}/{node}_{year}_{cat}_{variable}.pdf".format(ol=ol, node=node, year=year, cat=cat, variable=variable))
                        plt.savefig("{ol}/{node}_{year}_{cat}_{variable}.png".format(ol=ol, node=node, year=year, cat=cat, variable=variable))
                        plt.close()

    
    if(compareFullandGenerated):
        for variable in variables:
            for node in nodes:
                print("On Node:",node)

                for i_year, year in enumerate(years):
                    print("On year:",year)

                    xmin, xmax, xbins = varBinDict[variable]
                    bins = np.linspace(xmin, xmax, xbins + 1)
                    binWidth = (xmax - xmin) / xbins

                    if(EFT_DNN):
                        d = "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_EFT_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_withKinWeight_weightSel/"
                        NLO_Reweighted_f = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/BinaryDNN/HHWWyyDNN_binary_EFT_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_withKinWeight_weightSel/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(year=year)
                        Node_f = "{d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}_HHWWggTag_0_MoreVars.root".format(d=d, node=node, year=year)
                        NLO_Reweighted_ntuple = uproot.open(NLO_Reweighted_f)
                        NLO_Reweighted_tree = NLO_Reweighted_ntuple["GluGluToHHTo2G2Qlnu_node_All_NLO_{year}_Normalized_13TeV_HHWWggTag_0".format(year=year)]
                        NLO_Reweighted_variable = NLO_Reweighted_tree[variable].array()
                        reweightName = reweightDict[node]
                        NLO_weight = NLO_Reweighted_tree["weight"].array()
                        NLO_weight_NLO_Node = NLO_Reweighted_tree[reweightName].array()

                        # get second file values 
                        Node_ntuple = uproot.open(Node_f)
                        Node_tree = Node_ntuple["GluGluToHHTo2G2Qlnu_node_{node}_13TeV_HHWWggTag_0_v1".format(node=node)] # need to use v1 whenever available for semileptonic generated files 

                        if(variable == "evalDNN_HH"): 
                            variable = "evalDNN"
                        Node_variable = Node_tree[variable].array()
                        Node_weight = Node_tree["weight"].array()
                    else:
                        NLO_Reweighted_f = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(year=year)
                        Node_f = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_{node}_{year}_HHWWggTag_0_MoreVars.root".format(node=node, year=year)
                        NLO_Reweighted_ntuple = uproot.open(NLO_Reweighted_f)
                        NLO_Reweighted_tree = NLO_Reweighted_ntuple["GluGluToHHTo2G2Qlnu_node_All_NLO_{year}_Normalized_13TeV_HHWWggTag_0".format(year=year)]
                        NLO_Reweighted_variable = NLO_Reweighted_tree[variable].array()
                        reweightName = reweightDict[node]
                        NLO_weight = NLO_Reweighted_tree["weight"].array()
                        NLO_weight_NLO_Node = NLO_Reweighted_tree[reweightName].array()

                        # get second file values 
                        Node_ntuple = uproot.open(Node_f)
                        Node_tree = Node_ntuple["GluGluToHHTo2G2Qlnu_node_{node}_13TeV_HHWWggTag_0_v1".format(node=node)] # need to use v1 whenever available for semileptonic 
                        Node_variable = Node_tree[variable].array()
                        Node_weight = Node_tree["weight"].array()

                    NLO_Reweighted_binVals, NLO_Reweighted_edges, _ = plt.hist(NLO_Reweighted_variable, bins = bins, weights = np.multiply(NLO_weight, NLO_weight_NLO_Node)) 
                    plt.close() # to avoid showing intermediate histogram
                    Node_binVals, Node_edges, _ = plt.hist(Node_variable, bins = bins, weights = Node_weight) 
                    plt.close() # to avoid showing intermediate histogram 

                    # Create plot 
                    # exec("fig, axarr_%s = plt.subplots(2, sharex=True, gridspec_kw={ 'hspace': 0.15, 'height_ratios': (0.7,0.3) } )"%(year))
                    fig, axarr = plt.subplots(2, sharex=True, gridspec_kw={ 'hspace': 0.15, 'height_ratios': (0.7,0.3) } )

                    fig.set_dpi(100)
                    fig.set_size_inches(10, 7.5)
                    upper = axarr[0]
                    lower = axarr[1]

                    ratio = np.true_divide(NLO_Reweighted_binVals, Node_binVals, out = np.zeros_like(Node_binVals), where = Node_binVals != 0)

                    binCenters = [float(a) + (float(binWidth)/2.) for a in NLO_Reweighted_edges[:-1]] # use one histogram's since they should all be the same anyway --- this assumes equally distanced bins 
                    zero_errors = [0 for entry in binCenters]

                    # get uncertainties
                    Reweighted_binned_MC_stat_uncertainties = hist_bin_uncertainty(NLO_Reweighted_variable, np.multiply(NLO_weight, NLO_weight_NLO_Node), bins)
                    Node_binned_MC_stat_uncertainties = hist_bin_uncertainty(Node_variable, Node_weight, bins)

                    upper.hist(bins[:-1], bins = bins, weights = NLO_Reweighted_binVals, histtype = 'step', linewidth = 2, label = "All NLO Reweighted to {node}".format(node=node), color = 'C0')
                    upper.hist(bins[:-1], bins = bins, weights = Node_binVals, histtype = 'step', linewidth = 2, label = node, color = 'C1')

                    # xerr = [[binCenters[i] - (binWidth/2.), binCenters[i] + (binWidth/2.)] for i in range(0, len(binCenters))] 
                    # yerr = [[NLO_Reweighted_binVals[i] - (Reweighted_binned_MC_stat_uncertainties[i]), NLO_Reweighted_binVals[i] + (Reweighted_binned_MC_stat_uncertainties[i])] for i in range(0, len(binCenters))] 

                    # xerr = [[(binWidth/2.), (binWidth/2.)] for i in range(0, len(binCenters))] 
                    # yerr = [[(Reweighted_binned_MC_stat_uncertainties[i]), (Reweighted_binned_MC_stat_uncertainties[i])] for i in range(0, len(binCenters))]         
                    
                    # print("xerr:",xerr)
                    # print("binCenters:",binCenters)
                    # print("NLO_Reweighted_binVals:",NLO_Reweighted_binVals)
                    # print("Reweighted_binned_MC_stat_uncertainties:",Reweighted_binned_MC_stat_uncertainties)

                    # _ = make_error_boxes(upper, np.array(binCenters), np.array(NLO_Reweighted_binVals), np.array(xerr).T, np.array(yerr).T)

                    capthick = 0
                    capsize = 0
                    elinewidth = 3

                    upper.errorbar(x = binCenters, 
                                y = NLO_Reweighted_binVals, 
                                yerr = Reweighted_binned_MC_stat_uncertainties, 
                                color = 'C0', 
                                fmt = " ", 
                                capthick = capthick, 
                                capsize = capsize, 
                                elinewidth = elinewidth
                                )

                    upper.errorbar(x = binCenters, 
                                y = Node_binVals, 
                                yerr = Node_binned_MC_stat_uncertainties, 
                                color = 'C1' , 
                                fmt = " ", 
                                capthick = capthick, 
                                capsize = capsize, 
                                elinewidth = elinewidth
                                )

                    reweighted_sum = np.sum(NLO_Reweighted_binVals)
                    node_sum = np.sum(Node_binVals)

                    print("reweighted_sum:",reweighted_sum)
                    print("node_sum:",node_sum)
                    print("ratio: ",float(reweighted_sum/node_sum))

                    reweighted_sum = round(reweighted_sum, 3)
                    node_sum = round(node_sum, 3)
                    sum_ratio = round(float(reweighted_sum/node_sum), 3)

                    # Ratio 
                    lower.tick_params(axis = 'x', labelsize = 13)
                    upper.tick_params(axis = 'y', labelsize = 13)
                    upper.set_ylabel("Yield", fontsize = 20)
                    upper.ticklabel_format(style='plain') ##-- Remove scientific notation
                    lower.set_xlabel(variable, fontsize = 20)
                    lower.set_ylabel("Reweight / %s"%(node), fontsize = 15)
                    plt.yticks(fontsize=15)
                    plt.xticks(fontsize=15)        
                    lower.set_ylim(0.5, 1.5)
                    lower.plot([xmin, xmax],[1,1],linestyle=':', color = 'black')

                    # Stat errors 
                    errors = []
                    for val_i, NLO_reweighted_val in enumerate(NLO_Reweighted_binVals):
                        Node_val = Node_binVals[val_i]
                        r_val = ratio[val_i]
                        if(Node_val <= 0): 
                            errors.append(0.)
                        else:
                            # event weight = 1 uncertainty 
                            # rel_err = np.sqrt( (1 / NLO_reweighted_val) + (1 / Node_val) ) # statistical uncertainty assuming event weights of 1 
                            # err = float(rel_err) * r_val

                            # Taking weights into account
                            Reweighted_w2 = Reweighted_binned_MC_stat_uncertainties[val_i]
                            node_w2 = Node_binned_MC_stat_uncertainties[val_i]
                            rel_err = np.sqrt( (node_w2 / Node_val ) + (Reweighted_w2 / NLO_reweighted_val)**2 ) # sqrt(sum(w^2)) per bin for MC stack uncertainty 
                            err = float(rel_err) * r_val 

                            errors.append(err)

                    if(AddRatioErrors): yErrors = errors 
                    else: yErrors = zero_errors

                    lower.errorbar(binCenters, ratio, xerr = zero_errors , yerr = yErrors, marker = '.', color = 'black', ls = '')  

                    # Decorate 
                    upper.set_title(year, fontsize = 30)
                    upper.text(
                        0., 1., r"HH$\rightarrow$WW$\gamma\gamma$",
                        fontsize=20, fontweight='bold',
                        horizontalalignment='left',
                        verticalalignment='bottom',
                        transform=upper.transAxes
                    )

                    upper.text(
                        0.5, 0.2, "\n".join((
                                r"$\int$ reweight = %s"%(reweighted_sum),
                                r"$\int$ %s = %s"%(node, node_sum),
                                "ratio = %s"%(sum_ratio)    
                            ),                        
                        ),
                        fontsize=15, fontweight='bold',
                        horizontalalignment='center',
                        verticalalignment='bottom',
                        transform=upper.transAxes                 
                    )

                    # upper.legend(loc = 'best', fontsize = 18, title = "Comparison", title_fontsize = 20) # with title 
                    upper.legend(loc = 'upper right', fontsize = 18)
                    upper.grid()

                    ol = "/eos/user/a/atishelm/www/HHWWgg/HIG-21-014/PostPreAppTalkChecks/SemileptonicEFTReweighting/"
                    plt.savefig("{ol}/{node}_{year}_{variable}.pdf".format(ol=ol, node=node, year=year, variable=variable))
                    plt.savefig("{ol}/{node}_{year}_{variable}.png".format(ol=ol, node=node, year=year, variable=variable))
                    plt.close()
                

    if(plotReweighted):
        for variable in variables:
            for node in nodes:
                print("On node:",node)
                for year_i, year in enumerate(years):
                    print("On year:",year)

                    xmin, xmax, xbins = varBinDict[variable]
                    bins = np.linspace(xmin, xmax, xbins + 1)
                    binWidth = (xmax - xmin) / xbins

                    fig, ax = plt.subplots()
                    fig.set_dpi(100)
                    fig.set_size_inches(10, 7.5)

                    if(EFT_DNN):
                        d = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/BinaryDNN/HHWWyyDNN_binary_EFT_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_withKinWeight_weightSel/"
                    else:
                        d = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/"

                    NLO_Reweighted_f = "{d}/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(d=d, year=year)
                    NLO_Reweighted_ntuple = uproot.open(NLO_Reweighted_f)
                    NLO_Reweighted_tree = NLO_Reweighted_ntuple["GluGluToHHTo2G2Qlnu_node_All_NLO_{year}_Normalized_13TeV_HHWWggTag_0".format(year=year)]
                    NLO_Reweighted_variable = NLO_Reweighted_tree[variable].array()
                    reweightName = reweightDict[node]
                    NLO_weight = NLO_Reweighted_tree["weight"].array()
                    NLO_weight_NLO_Node = NLO_Reweighted_tree[reweightName].array()

                    NLO_Reweighted_binVals, NLO_Reweighted_edges, _ = plt.hist(NLO_Reweighted_variable, bins = bins, weights = np.multiply(NLO_weight, NLO_weight_NLO_Node)) 
                    plt.close() # to avoid showing intermediate histogram

                    binCenters = [float(a) + (float(binWidth)/2.) for a in NLO_Reweighted_edges[:-1]] # use one histogram's since they should all be the same anyway --- this assumes equally distanced bins 
                    zero_errors = [0 for entry in binCenters]

                    # get uncertainties
                    Reweighted_binned_MC_stat_uncertainties = hist_bin_uncertainty(NLO_Reweighted_variable, np.multiply(NLO_weight, NLO_weight_NLO_Node), bins)

                    ax.hist(bins[:-1], bins = bins, weights = NLO_Reweighted_binVals, histtype = 'step', linewidth = 2, label = "{year}: All NLO Reweighted to {node}".format(year=year, node=node), color = 'C%s'%(year_i))

                    capthick = 0
                    capsize = 0
                    elinewidth = 3

                    ax.errorbar(x = binCenters, 
                                y = NLO_Reweighted_binVals, 
                                yerr = Reweighted_binned_MC_stat_uncertainties, 
                                color = 'C%s'%(year_i), 
                                fmt = " ", 
                                capthick = capthick, 
                                capsize = capsize, 
                                elinewidth = elinewidth
                                )


                    # Decorate 
                    ax.set_title(node, fontsize = 30)
                    ax.text(
                        0., 1., r"HH$\rightarrow$WW$\gamma\gamma$",
                        fontsize=20, fontweight='bold',
                        horizontalalignment='left',
                        verticalalignment='bottom',
                        transform=ax.transAxes
                    )      

                    ax.tick_params(axis = 'x', labelsize = 13)
                    ax.tick_params(axis = 'y', labelsize = 13)
                    ax.set_ylabel("Yield", fontsize = 20)
                    ax.ticklabel_format(style='plain') ##-- Remove scientific notation
                    ax.set_xlabel(variable, fontsize = 20)
                    plt.yticks(fontsize=15)
                    plt.xticks(fontsize=15)        

                    ax.grid()

                    ol = "/eos/user/a/atishelm/www/HHWWgg/HIG-21-014/PostPreAppTalkChecks/SemileptonicEFTReweighting/"
                    fig.savefig("{ol}/{node}_{variable}_{year}.pdf".format(ol=ol, node=node, variable=variable, year=year))
                    fig.savefig("{ol}/{node}_{variable}_{year}.png".format(ol=ol, node=node, variable=variable, year=year))
                    plt.close()

"""

    # Make validation plots for each cHHH point 
    # years = ["2017"]
    years = ["2016", "2017", "2018"]
    # nodes = ["cttHH3", "cttHH0p35", "3D3"]
    nodes = ["8a", "1b", "2b", "3b", "4b", "5b", "6b", "7b"]

    for year_i, year in enumerate(years):
        print("On year:",year)
        fig_all, ax_all = plt.subplots()
        fig_all.set_dpi(100)
        fig_all.set_size_inches(10, 7.5)  
                
        for node_i, node in enumerate(nodes):
            print("On node:",node)

            xmin, xmax, xbins = varBinDict[variable]
            bins = np.linspace(xmin, xmax, xbins + 1)
            binWidth = (xmax - xmin) / xbins

            NLO_Reweighted_f = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(year=year)
            NLO_Reweighted_ntuple = uproot.open(NLO_Reweighted_f)
            NLO_Reweighted_tree = NLO_Reweighted_ntuple["GluGluToHHTo2G2Qlnu_node_All_NLO_{year}_Normalized_13TeV_HHWWggTag_0".format(year=year)]
            NLO_Reweighted_variable = NLO_Reweighted_tree[variable].array()
            reweightName = reweightDict[node]
            NLO_weight = NLO_Reweighted_tree["weight"].array()
            NLO_weight_NLO_Node = NLO_Reweighted_tree[reweightName].array()

            fig_tmp, ax_tmp = plt.subplots()
            NLO_Reweighted_binVals, NLO_Reweighted_edges, _ = plt.hist(NLO_Reweighted_variable, bins = bins, weights = np.multiply(NLO_weight, NLO_weight_NLO_Node)) 
            plt.close() # to avoid showing intermediate histogram

            binCenters = [float(a) + (float(binWidth)/2.) for a in NLO_Reweighted_edges[:-1]] # use one histogram's since they should all be the same anyway --- this assumes equally distanced bins 
            zero_errors = [0 for entry in binCenters]

            # get uncertainties
            Reweighted_binned_MC_stat_uncertainties = hist_bin_uncertainty(NLO_Reweighted_variable, np.multiply(NLO_weight, NLO_weight_NLO_Node), bins)

            ax_all.hist(bins[:-1], bins = bins, weights = NLO_Reweighted_binVals, histtype = 'step', linewidth = 2, label = node, color = 'C%s'%(node_i))
            # ax_all.hist(bins[:-1], bins = bins, weights = NLO_Reweighted_binVals, histtype = 'step', linewidth = 2, label = "{year}: All NLO Reweighted to {node}".format(year=year, node=node), color = 'C%s'%(year_i))
            # upper.hist(bins[:-1], bins = bins, weights = NLO_Reweighted_binVals, histtype = 'step', linewidth = 2, label = "All NLO Reweighted to {node}".format(node=node), color = 'C0')

            capthick = 0
            capsize = 0
            elinewidth = 3

            ax_all.errorbar(x = binCenters, 
                        y = NLO_Reweighted_binVals, 
                        yerr = Reweighted_binned_MC_stat_uncertainties, 
                        #    color = 'C%s'%(year_i), 
                        color = 'C%s'%(node_i), 
                        fmt = " ", 
                        capthick = capthick, 
                        capsize = capsize, 
                        elinewidth = elinewidth
                        )


        # Decorate 
        ax_all.set_title(year, fontsize = 30)
        ax_all.text(
            0., 1., r"HH$\rightarrow$WW$\gamma\gamma$",
            fontsize=20, fontweight='bold',
            horizontalalignment='left',
            verticalalignment='bottom',
            transform=ax_all.transAxes
        )      

        ax_all.tick_params(axis = 'x', labelsize = 13)
        ax_all.tick_params(axis = 'y', labelsize = 13)
        ax_all.set_ylabel("Yield", fontsize = 20)
        ax_all.ticklabel_format(style='plain') ##-- Remove scientific notation
        ax_all.set_xlabel(variable, fontsize = 20)
        # ax_all.set_ylabel("Reweight / %s"%(node), fontsize = 15)
        plt.yticks(fontsize=15)
        plt.xticks(fontsize=15)        

        # plt.legend(title = "Mass [GeV]", bbox_to_anchor=(1.01, 1.05), loc='upper left')
        ax_all.legend(loc = 'upper left', fontsize = 18, bbox_to_anchor=(1.01, 1.05))
        ax_all.grid()

        ol = "/eos/user/a/atishelm/www/HHWWgg/HIG-21-014/PostPreAppTalkChecks/SemileptonicEFTReweighting/"
        fig_all.savefig("{ol}/8BM_{year}.pdf".format(ol=ol, year=year))
        fig_all.savefig("{ol}/8BM_{year}.png".format(ol=ol, year=year))
        plt.close()

    print("DONE")

"""

print("DONE")
