"""
10 November 2021 
Abraham Tishelman-Charny 

The purpose of this python module is to compare histograms, including their per bin agreement. 

"""

import uproot 
from matplotlib import pyplot as plt 
import numpy as np
import pandas as pd

from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

# options 
AddRatioErrors = 1
variable = "evalDNN_HH"

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

# test uncertainty function 
# a = np.array([3, 5, 8, 3, 3, 3, 5, 5, 5])
# b = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
# c = np.array([2, 3,4,5,6,7,8,9])

# testBinUncs = hist_bin_uncertainty(a,b,c)
# print("testBinUncs:",testBinUncs)
# exit(1)

varBinDict = {
    "evalDNN_HH" : [0, 1, 30],
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
}

# # Make validation plots for each cHHH point 
# years = ["2016", "2017", "2018"]
# # nodes = ["cHHH0", "cHHH1", "cHHH2p45", "cHHH5"]
# nodes = ["cHHH5"]

# # years = ["2017"]
# # nodes = ["cHHH1"]
# # nodes = ["cHHH0", "cHHH1", "cHHH2p45", "cHHH5"]

# for node in nodes:
#     print("On Node:",node)

#     # For each node, make a plot with 3 subplots, one for each year 
#     # nrows, ncols = 1, 3
#     # fig_node, axarr_node = plt.subplots(nrows=nrows, ncols=ncols, figsize=(30,7.5)) #squeeze=True) 10, 7.5

#     for i_year, year in enumerate(years):
#         print("On year:",year)
#         # exec("this_ax = axarr_node[%s]"%(i_year))

#         xmin, xmax, xbins = varBinDict[variable]
#         bins = np.linspace(xmin, xmax, xbins + 1)
#         binWidth = (xmax - xmin) / xbins

#         NLO_Reweighted_f = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(year=year)
#         Node_f = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_{node}_{year}_HHWWggTag_0_MoreVars.root".format(node=node, year=year)
#         NLO_Reweighted_ntuple = uproot.open(NLO_Reweighted_f)
#         NLO_Reweighted_tree = NLO_Reweighted_ntuple["GluGluToHHTo2G2Qlnu_node_All_NLO_{year}_Normalized_13TeV_HHWWggTag_0".format(year=year)]
#         NLO_Reweighted_variable = NLO_Reweighted_tree[variable].array()
#         reweightName = reweightDict[node]
#         NLO_weight = NLO_Reweighted_tree["weight"].array()
#         NLO_weight_NLO_Node = NLO_Reweighted_tree[reweightName].array()

#         # get second file values 
#         Node_ntuple = uproot.open(Node_f)
#         Node_tree = Node_ntuple["GluGluToHHTo2G2Qlnu_node_{node}_13TeV_HHWWggTag_0_v1".format(node=node)] # need to use v1 whenever available for semileptonic 
#         Node_variable = Node_tree[variable].array()
#         Node_weight = Node_tree["weight"].array()

#         NLO_Reweighted_binVals, NLO_Reweighted_edges, _ = plt.hist(NLO_Reweighted_variable, bins = bins, weights = np.multiply(NLO_weight, NLO_weight_NLO_Node)) 
#         plt.close() # to avoid showing intermediate histogram
#         Node_binVals, Node_edges, _ = plt.hist(Node_variable, bins = bins, weights = Node_weight) 
#         plt.close() # to avoid showing intermediate histogram 

#         # Create plot 
#         # exec("fig, axarr_%s = plt.subplots(2, sharex=True, gridspec_kw={ 'hspace': 0.15, 'height_ratios': (0.7,0.3) } )"%(year))
#         fig, axarr = plt.subplots(2, sharex=True, gridspec_kw={ 'hspace': 0.15, 'height_ratios': (0.7,0.3) } )

#         fig.set_dpi(100)
#         fig.set_size_inches(10, 7.5)
#         upper = axarr[0]
#         lower = axarr[1]

#         # exec("upper = axarr_%s[0]"%(year))  
#         # exec("lower = axarr_%s[1]"%(year))  

#         ratio = np.true_divide(NLO_Reweighted_binVals, Node_binVals, out = np.zeros_like(Node_binVals), where = Node_binVals != 0)

#         binCenters = [float(a) + (float(binWidth)/2.) for a in NLO_Reweighted_edges[:-1]] # use one histogram's since they should all be the same anyway --- this assumes equally distanced bins 
#         zero_errors = [0 for entry in binCenters]

#         # get uncertainties
#         Reweighted_binned_MC_stat_uncertainties = hist_bin_uncertainty(NLO_Reweighted_variable, np.multiply(NLO_weight, NLO_weight_NLO_Node), bins)
#         Node_binned_MC_stat_uncertainties = hist_bin_uncertainty(Node_variable, Node_weight, bins)

#         upper.hist(bins[:-1], bins = bins, weights = NLO_Reweighted_binVals, histtype = 'step', linewidth = 2, label = "All NLO Reweighted to {node}".format(node=node), color = 'C0')
#         upper.hist(bins[:-1], bins = bins, weights = Node_binVals, histtype = 'step', linewidth = 2, label = node, color = 'C1')

#         # xerr = [[binCenters[i] - (binWidth/2.), binCenters[i] + (binWidth/2.)] for i in range(0, len(binCenters))] 
#         # yerr = [[NLO_Reweighted_binVals[i] - (Reweighted_binned_MC_stat_uncertainties[i]), NLO_Reweighted_binVals[i] + (Reweighted_binned_MC_stat_uncertainties[i])] for i in range(0, len(binCenters))] 

#         # xerr = [[(binWidth/2.), (binWidth/2.)] for i in range(0, len(binCenters))] 
#         # yerr = [[(Reweighted_binned_MC_stat_uncertainties[i]), (Reweighted_binned_MC_stat_uncertainties[i])] for i in range(0, len(binCenters))]         
        
#         # print("xerr:",xerr)
#         # print("binCenters:",binCenters)
#         # print("NLO_Reweighted_binVals:",NLO_Reweighted_binVals)
#         # print("Reweighted_binned_MC_stat_uncertainties:",Reweighted_binned_MC_stat_uncertainties)

#         # _ = make_error_boxes(upper, np.array(binCenters), np.array(NLO_Reweighted_binVals), np.array(xerr).T, np.array(yerr).T)

#         capthick = 0
#         capsize = 0
#         elinewidth = 3

#         upper.errorbar(x = binCenters, 
#                        y = NLO_Reweighted_binVals, 
#                        yerr = Reweighted_binned_MC_stat_uncertainties, 
#                        color = 'C0', 
#                        fmt = " ", 
#                        capthick = capthick, 
#                        capsize = capsize, 
#                        elinewidth = elinewidth
#                        )

#         upper.errorbar(x = binCenters, 
#                        y = Node_binVals, 
#                        yerr = Node_binned_MC_stat_uncertainties, 
#                        color = 'C1' , 
#                        fmt = " ", 
#                        capthick = capthick, 
#                        capsize = capsize, 
#                        elinewidth = elinewidth
#                        )

#         reweighted_sum = np.sum(NLO_Reweighted_binVals)
#         node_sum = np.sum(Node_binVals)

#         print("reweighted_sum:",reweighted_sum)
#         print("node_sum:",node_sum)
#         print("ratio: ",float(reweighted_sum/node_sum))

#         reweighted_sum = round(reweighted_sum, 3)
#         node_sum = round(node_sum, 3)
#         sum_ratio = round(float(reweighted_sum/node_sum), 3)

#         # Ratio 
#         lower.tick_params(axis = 'x', labelsize = 13)
#         upper.tick_params(axis = 'y', labelsize = 13)
#         upper.set_ylabel("Yield", fontsize = 20)
#         upper.ticklabel_format(style='plain') ##-- Remove scientific notation
#         lower.set_xlabel(variable, fontsize = 20)
#         lower.set_ylabel("Reweight / %s"%(node), fontsize = 15)
#         plt.yticks(fontsize=15)
#         plt.xticks(fontsize=15)        
#         lower.set_ylim(0.5, 1.5)
#         lower.plot([xmin, xmax],[1,1],linestyle=':', color = 'black')

#         # Stat errors 
#         errors = []
#         for val_i, NLO_reweighted_val in enumerate(NLO_Reweighted_binVals):
#             Node_val = Node_binVals[val_i]
#             r_val = ratio[val_i]
#             if(Node_val <= 0): 
#                 errors.append(0.)
#             else:
#                 # event weight = 1 uncertainty 
#                 # rel_err = np.sqrt( (1 / NLO_reweighted_val) + (1 / Node_val) ) # statistical uncertainty assuming event weights of 1 
#                 # err = float(rel_err) * r_val

#                 # Taking weights into account
#                 Reweighted_w2 = Reweighted_binned_MC_stat_uncertainties[val_i]
#                 node_w2 = Node_binned_MC_stat_uncertainties[val_i]
#                 rel_err = np.sqrt( (node_w2 / Node_val ) + (Reweighted_w2 / NLO_reweighted_val)**2 ) # sqrt(sum(w^2)) per bin for MC stack uncertainty 
#                 err = float(rel_err) * r_val 

#                 errors.append(err)

#         if(AddRatioErrors): yErrors = errors 
#         else: yErrors = zero_errors

#         lower.errorbar(binCenters, ratio, xerr = zero_errors , yerr = yErrors, marker = '.', color = 'black', ls = '')  

#         # Decorate 
#         upper.set_title(year, fontsize = 30)
#         upper.text(
#             0., 1., r"HH$\rightarrow$WW$\gamma\gamma$",
#             fontsize=20, fontweight='bold',
#             horizontalalignment='left',
#             verticalalignment='bottom',
#             transform=upper.transAxes
#         )

#         upper.text(
#             0.5, 0.2, "\n".join((
#                     r"$\int$ reweight = %s"%(reweighted_sum),
#                     r"$\int$ %s = %s"%(node, node_sum),
#                     "ratio = %s"%(sum_ratio)    
#                 ),                        
#             ),
#             fontsize=15, fontweight='bold',
#             horizontalalignment='center',
#             verticalalignment='bottom',
#             transform=upper.transAxes                 
#         )

#         # upper.legend(loc = 'best', fontsize = 18, title = "Comparison", title_fontsize = 20) # with title 
#         upper.legend(loc = 'upper right', fontsize = 18)
#         upper.grid()

#         # axarr_node = fig
#         # axarr_node[i_year] = axarr

#         # exec("ax_%s = axarr_node[%s]"%(i_year))
#         ol = "/eos/user/a/atishelm/www/HHWWgg/HIG-21-014/PostPreAppTalkChecks/SemileptonicEFTReweighting/"
#         plt.savefig("{ol}/{node}_{year}.pdf".format(ol=ol, node=node, year=year))
#         plt.close()
        
#     # axarr_node[0] = axarr_2016
#     # axarr_node[1] = axarr_2017
#     # axarr_node[2] = axarr_2018

#     # save node plot which has all three years plots 
#     # ol = "/eos/user/a/atishelm/www/HHWWgg/HIG-21-014/PostPreAppTalkChecks/SemileptonicEFTReweighting/"
#     # fig_node.savefig("{ol}/{node}_allYears.png".format(ol=ol, node=node))
#     # fig_node.savefig("{ol}/{node}_allYears.pdf".format(ol=ol, node=node))
#     # plt.close() 




# After comparison, plot distributions for NLO -> cttHH3, cttHH0p35, 3D3 (for the three years), 8 benchmarks

# # Make validation plots for each cHHH point 
# years = ["2017"]
# # years = ["2016", "2017", "2018"]
# # nodes = ["cttHH3", "cttHH0p35", "3D3"]
# nodes = ["8a", "1b", "2b", "3b", "4b", "5b", "6b", "7b"]

# for node in nodes:
#     print("On node:",node)
#     fig_all, ax_all = plt.subplots()
#     fig_all.set_dpi(100)
#     fig_all.set_size_inches(10, 7.5)    
#     for year_i, year in enumerate(years):
#         print("On year:",year)

#         xmin, xmax, xbins = varBinDict[variable]
#         bins = np.linspace(xmin, xmax, xbins + 1)
#         binWidth = (xmax - xmin) / xbins

#         NLO_Reweighted_f = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(year=year)
#         NLO_Reweighted_ntuple = uproot.open(NLO_Reweighted_f)
#         NLO_Reweighted_tree = NLO_Reweighted_ntuple["GluGluToHHTo2G2Qlnu_node_All_NLO_{year}_Normalized_13TeV_HHWWggTag_0".format(year=year)]
#         NLO_Reweighted_variable = NLO_Reweighted_tree[variable].array()
#         reweightName = reweightDict[node]
#         NLO_weight = NLO_Reweighted_tree["weight"].array()
#         NLO_weight_NLO_Node = NLO_Reweighted_tree[reweightName].array()

#         fig_tmp, ax_tmp = plt.subplots()
#         NLO_Reweighted_binVals, NLO_Reweighted_edges, _ = plt.hist(NLO_Reweighted_variable, bins = bins, weights = np.multiply(NLO_weight, NLO_weight_NLO_Node)) 
#         plt.close() # to avoid showing intermediate histogram

#         binCenters = [float(a) + (float(binWidth)/2.) for a in NLO_Reweighted_edges[:-1]] # use one histogram's since they should all be the same anyway --- this assumes equally distanced bins 
#         zero_errors = [0 for entry in binCenters]

#         # get uncertainties
#         Reweighted_binned_MC_stat_uncertainties = hist_bin_uncertainty(NLO_Reweighted_variable, np.multiply(NLO_weight, NLO_weight_NLO_Node), bins)

#         ax_all.hist(bins[:-1], bins = bins, weights = NLO_Reweighted_binVals, histtype = 'step', linewidth = 2, label = "{year}: All NLO Reweighted to {node}".format(year=year, node=node), color = 'C%s'%(year_i))
#         # upper.hist(bins[:-1], bins = bins, weights = NLO_Reweighted_binVals, histtype = 'step', linewidth = 2, label = "All NLO Reweighted to {node}".format(node=node), color = 'C0')

#         capthick = 0
#         capsize = 0
#         elinewidth = 3

#         ax_all.errorbar(x = binCenters, 
#                        y = NLO_Reweighted_binVals, 
#                        yerr = Reweighted_binned_MC_stat_uncertainties, 
#                        color = 'C%s'%(year_i), 
#                        fmt = " ", 
#                        capthick = capthick, 
#                        capsize = capsize, 
#                        elinewidth = elinewidth
#                        )


#     # Decorate 
#     ax_all.set_title(node, fontsize = 30)
#     ax_all.text(
#         0., 1., r"HH$\rightarrow$WW$\gamma\gamma$",
#         fontsize=20, fontweight='bold',
#         horizontalalignment='left',
#         verticalalignment='bottom',
#         transform=ax_all.transAxes
#     )      

#     ax_all.tick_params(axis = 'x', labelsize = 13)
#     ax_all.tick_params(axis = 'y', labelsize = 13)
#     ax_all.set_ylabel("Yield", fontsize = 20)
#     ax_all.ticklabel_format(style='plain') ##-- Remove scientific notation
#     ax_all.set_xlabel(variable, fontsize = 20)
#     # ax_all.set_ylabel("Reweight / %s"%(node), fontsize = 15)
#     plt.yticks(fontsize=15)
#     plt.xticks(fontsize=15)        

#     # ax_all.legend(loc = 'upper left', fontsize = 18)
#     ax_all.grid()

#     ol = "/eos/user/a/atishelm/www/HHWWgg/HIG-21-014/PostPreAppTalkChecks/SemileptonicEFTReweighting/"
#     fig_all.savefig("{ol}/{node}.pdf".format(ol=ol, node=node))
#     fig_all.savefig("{ol}/{node}.png".format(ol=ol, node=node))
#     plt.close()

# print("DONE")

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
