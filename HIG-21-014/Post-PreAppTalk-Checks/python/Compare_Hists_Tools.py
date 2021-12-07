"""
2 December 2021
Abraham Tishelman-Charny 

The purpose of this module is to provide functions for Compare_Hists.py 
"""

import numpy as np 
import uproot 
from matplotlib import pyplot as plt 
import pandas as pd

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
    in_range_data = np.asarray([data[idx] for idx in in_range_index], dtype = float)

    if weights is None or np.array_equal(weights, np.ones(len(weights))):
        # Default to weights of 1 and thus uncertainty = sqrt(N)
        in_range_weights = np.ones(len(in_range_data))
    else:
        in_range_weights = np.asarray([weights[idx] for idx in in_range_index], dtype = float)

    # Bin the weights with the same binning as the data
    bin_index = np.digitize(in_range_data, bin_edges)
    # N.B.: range(1, bin_edges.size) is used instead of set(bin_index) as if
    # there is a gap in the data such that a bin is skipped no index would appear
    # for it in the set
    binned_weights = np.asarray( [in_range_weights[np.where(bin_index == idx)[0]] for idx in range(1, len(bin_edges))])
    bin_uncertainties = np.asarray(
        [np.sqrt(np.sum(np.square(w))) for w in binned_weights])
    return bin_uncertainties

reweightDict_LO = {
    "1"  : "weight_LO_1",
    "2"  : "weight_LO_2",
    "3"  : "weight_LO_3",
    "4"  : "weight_LO_4",
    "5"  : "weight_LO_5",
    "6"  : "weight_LO_6",
    "7"  : "weight_LO_7",
    "8"  : "weight_LO_8",
    "9"  : "weight_LO_9",
    "10"  : "weight_LO_10",
    "11"  : "weight_LO_11",
    "12"  : "weight_LO_12",
    "8a" : "weight_LO_8a",
    "1b" : "weight_LO_1b",
    "2b" : "weight_LO_2b",
    "3b" : "weight_LO_3b",
    "4b" : "weight_LO_4b",
    "5b" : "weight_LO_5b",
    "6b" : "weight_LO_6b",
    "7b" : "weight_LO_7b",        
}

def CompareGenAndReweightSamples(variables, nodes, years, varBinDict, AddRatioErrors):
    for variable in variables:
        for node in nodes:
            print("On Node:",node)

            for i_year, year in enumerate(years):
                print("On year:",year)

                if(len(varBinDict[variable]) == 3):
                    xmin, xmax, xbins = varBinDict[variable]
                    bins = np.linspace(xmin, xmax, xbins + 1)
                    binWidth = (xmax - xmin) / xbins
                else: 
                    bins = varBinDict[variable]
                    xmin = bins[0]
                    xmax = bins[-1]                    

                Reweighted_D = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/combined_allNodes/".format(year=year)
                Generated_D = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/{year}/Signal/SL_LO_{year}_noPdfWeight_hadded/".format(year=year)

                NLO_Reweighted_f = "{Reweighted_D}/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(Reweighted_D=Reweighted_D, year=year)
                Node_f = "{Generated_D}/GluGluToHHTo2G2Qlnu_node_{node}_{year}.root".format(Generated_D=Generated_D, node=node, year=year)
                NLO_Reweighted_ntuple = uproot.open(NLO_Reweighted_f)
                NLO_Reweighted_tree = NLO_Reweighted_ntuple["GluGluToHHTo2G2Qlnu_node_All_NLO_{year}_Normalized_13TeV_HHWWggTag_0".format(year=year)]
                NLO_Reweighted_variable = NLO_Reweighted_tree[variable].array()
                reweightName = reweightDict_LO[node]
                NLO_weight = NLO_Reweighted_tree["weight"].array()
                NLO_weight_NLO_Node = NLO_Reweighted_tree[reweightName].array()

                # get second file values 
                Node_ntuple = uproot.open(Node_f)
                Node_tree = Node_ntuple["tagsDumper/trees"]["GluGluToHHTo2G2Qlnu_node_{node}_13TeV_HHWWggTag_0".format(node=node)] # need to use v1 whenever available for semileptonic 
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

                if(len(varBinDict[variable]) == 3):
                    binCenters = np.array([float(a) + (float(binWidth)/2.) for a in NLO_Reweighted_edges[:-1]], dtype = float) # use one histogram's since they should all be the same anyway --- this assumes equally distanced bins 
                else:
                    binCenters = np.array( [ ((bins[i+1] - bins[i])/2.) + bins[i] for i,bin_edge in enumerate(bins) if i < (len(bins) - 1)]  , dtype=float)   # (bin_i+1 - bin_i) / 2 + bin_i

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
                upper.legend(loc = 'upper right', fontsize = 14)
                upper.grid()

                ol = "/eos/user/a/atishelm/www/HHWWgg/HIG-21-014/PostPreAppTalkChecks/SemileptonicEFTReweighting/CompareGenAndReweight/"
                plt.savefig("{ol}/{node}_{year}_{variable}.pdf".format(ol=ol, node=node, year=year, variable=variable))
                plt.savefig("{ol}/{node}_{year}_{variable}.png".format(ol=ol, node=node, year=year, variable=variable))
                plt.close()