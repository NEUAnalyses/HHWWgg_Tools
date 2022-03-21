"""
1 December 2021
Abraham Tishelman-Charny

The purpose of this module is to plot signal and background DNN scores, input from histograms.

Example usage: python3 Plot_DNN_Scores.py 
"""

import ROOT
import numpy as np 
from matplotlib import pyplot as plt

f = ROOT.TFile.Open("/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/evalDNN_HH/evalDNN_HH_Histos_smoothing_SmoothSuper_bins70_massMin122.0_massMax128.0.root")
Bkg_SR_h = f.Get("h_evalDNN_HH_bkg_SR_weighted_smooth")
Sig_SR_h = f.Get("h_evalDNN_HH_signal_SR")

Bkg_vals = []
Sig_vals = []

for bin in range(Bkg_SR_h.GetNbinsX()):
    val = Bkg_SR_h.GetBinContent(bin + 1)
    Bkg_vals.append(val)
for bin in range(Sig_SR_h.GetNbinsX()):
    val = Sig_SR_h.GetBinContent(bin + 1)
    Sig_vals.append(val)

bins = np.linspace(0.1, 1, 71)
    
# print("Bkg_vals:",Bkg_vals)    
# print("bins[:-1]:",bins[:-1])
    
fig, ax = plt.subplots()
plt.hist(bins[:-1], weights = Bkg_vals, bins = bins, label = "Background")
plt.hist(bins[:-1], weights = Sig_vals, bins = bins, label = "Signal")
plt.yscale('log')
plt.xlim(0.1, 1)
plt.xlabel("evalDNN_HH", fontsize = 15)
plt.ylabel("Number of Expected Events", fontsize = 15)
plt.legend(loc = 'best')
plt.tight_layout()
# plt.show()
outputName = "plot.png"
plt.savefig(outputName)
plt.close()

print("DONE")

