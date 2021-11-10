"""
10 November 2021 
Abraham Tishelman-Charny 

The purpose of this python module is to compare histograms, including their per bin agreement. 

"""

import uproot 
from matplotlib import pyplot as plt 
import numpy as np
import pandas as pd

# options 
AddRatioErrors = 0
variable = "evalDNN_HH"

varBinDict = {
    "evalDNN_HH" : [0, 1, 30],
}

reweightDict = {
    "cHHH0" : "weight_NLO_cHHH0",
    "cHHH1" : "weight_NLO_SM",
    "cHHH2p45" : "weight_NLO_cHHH2",
    "cHHH5" : "weight_NLO_cHHH5"
}

# Make validation plots for each cHHH point 
nodes = ["cHHH0", "cHHH1", "cHHH2p45", "cHHH5"]

for node in nodes:
    print("On Node:",node)

    xmin, xmax, xbins = varBinDict[variable]
    bins = np.linspace(xmin, xmax, xbins + 1)
    binWidth = (xmax - xmin) / xbins

    NLO_Reweighted_f = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_All_NLO_2017.root"
    Node_f = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_{node}_2017_HHWWggTag_0_MoreVars.root".format(node=node)
    NLO_Reweighted_ntuple = uproot.open(NLO_Reweighted_f)
    NLO_Reweighted_tree = NLO_Reweighted_ntuple["GluGluToHHTo2G2Qlnu_node_All_NLO_2017_Normalized_13TeV_HHWWggTag_0"]
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
    fig, axarr = plt.subplots(2, 
                                sharex=True, 
                                gridspec_kw={
                                    'hspace': 0.15,
                                    'height_ratios': (0.7,0.3)
                                    }
                                )    
    fig.set_size_inches(10, 7.5)
    upper = axarr[0]
    lower = axarr[1]  

    ratio = np.true_divide(NLO_Reweighted_binVals, Node_binVals, out = np.zeros_like(Node_binVals), where = Node_binVals != 0)

    binCenters = [float(a) + (float(binWidth)/2.) for a in NLO_Reweighted_edges[:-1]] # use one histogram's since they should all be the same anyway --- this assumes equally distanced bins 
    zero_errors = [0 for entry in binCenters]

    upper.hist(bins[:-1], bins = bins, weights = NLO_Reweighted_binVals, histtype = 'step', linewidth = 3, label = "All NLO Reweighted")
    upper.hist(bins[:-1], bins = bins, weights = Node_binVals, histtype = 'step', linewidth = 3, label = node)

    reweighted_sum = np.sum(NLO_Reweighted_binVals)
    node_sum = np.sum(Node_binVals)

    print("reweighted_sum:",reweighted_sum)
    print("node_sum:",node_sum)
    print("ratio: ",float(reweighted_sum/node_sum))

    # Ratio 
    lower.tick_params(axis = 'x', labelsize = 13)
    upper.tick_params(axis = 'y', labelsize = 13)
    upper.set_ylabel("Entries", fontsize = 20)
    upper.ticklabel_format(style='plain') ##-- Remove scientific notation
    lower.set_xlabel(variable, fontsize = 20)
    lower.set_ylabel("Reweight / SM", fontsize = 20)
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
            rel_err = np.sqrt( (1 / NLO_reweighted_val) + (1 / Node_val) ) # statistical uncertainty assuming event weights of 1 
            err = float(rel_err) * r_val
    #         MC_stack_w2 = binned_MC_stat_uncertainties[val_i]
    #         rel_err = np.sqrt( (1 / d_val) + (MC_stack_w2 / MC_Stack_val)**2 ) sqrt(sum(w^2)) per bin for MC stack uncertainty 
            errors.append(err)

    if(AddRatioErrors): yErrors = errors 
    else: yErrors = zero_errors

    lower.errorbar(binCenters, ratio, xerr = zero_errors , yerr = yErrors, marker = '.', color = 'black', ls = '')  

    # Decorate 
    # upper.set_title("Hgg coffea, flashgg comparison", fontsize = 20) 
    upper.text(
        # 0.05, 0.9, u"CMS $\it{Preliminary}$",
        0., 1., r"HH$\rightarrow$WW$\gamma\gamma$",
        fontsize=20, fontweight='bold',
        horizontalalignment='left',
        verticalalignment='bottom',
        transform=upper.transAxes
    )

    # upper.legend(loc = 'best', fontsize = 18, title = "Comparison", title_fontsize = 20) # with title 
    upper.legend(loc = 'upper right', fontsize = 18)
    upper.grid()
    plt.savefig("{node}.png".format(node=node))
    plt.close()

print("DONE")