# python ScanCatsBins.py --ComputeCats --filesLoc /eos/user/b/bmarzocc/HHWWgg/HHWWgg_DataSignalMCnTuples/PromptPromptApplied-TagsMerged/HHWWyyDNN_binary_weights_exp_allBkgs/ --note weightsExp
# python ScanCatsBins.py --ComputeCats --filesLoc /eos/user/a/atishelm/ntuples/HHWWgg_DataSignalMCnTuples/2017/ --note weightsExp
# python ScanCatsBins.py --ComputeCats --Cats 1,2,3,4 --BinWidths 0.09,0.1,0.11 --filesLoc /eos/user/a/atishelm/ntuples/HHWWgg_DataSignalMCnTuples/2017/ --note weightsExp

# python ScanCatsBins.py --ComputeCats --Cats 1,2,3,4,5  --Nbins 5,15,20,25 --filesLoc /eos/user/a/atishelm/ntuples/HHWWgg_DataSignalMCnTuples/2017/ --note weightsExp --year 2017 

##-- 24 November 2020
# python ScanCatsBins.py --ComputeCats --Cats 1  --BinWidths 0.1 --filesLoc /eos/user/b/bmarzocc/HHWWgg/HHWWgg_DataSignalMCnTuples/PromptPromptApplied-TagsMerged/HHWWyyDNN_binary_testnewfiles_allBkgs/ --note testnewfiles --year 2017

import os 
from matplotlib import pyplot as plt 
import pandas as pd 
import argparse 
import numpy as np 
import math 

parser = argparse.ArgumentParser()
parser.add_argument('--ComputeCats',action='store_true',help='Compute category boundaries')
parser.add_argument('--PlotSigs',action='store_true',help='Plot significance values')
parser.add_argument('--filesLoc',type=str,default="")
parser.add_argument('--Cats',type=str,default="Comma separated list of category numbers")
parser.add_argument('--BinWidths',type=str,default="Comma separated list of bin widths")
# parser.add_argument('--Nbins',type=str,default="Comma separated list of number of bins")
parser.add_argument('--note',type=str,default="output")
parser.add_argument('--year',type=str,default="2017")
args = parser.parse_args()

# nCatsVals_orig = [i for i in range(0,1)]

# nCatsVals_orig = [i for i in range(1,6)]
# binWidthVals_orig = [0.025, 0.05, 0.075, 0.1]

# binWidthVals_orig = [0.075]

# nCatsVals = [i for i in range(1,5)]
# binWidthVals = [0.09, 0.1, 0.011]

nCatsVals = args.Cats.split(',')
binWidthVals = args.BinWidths.split(',')
# NbinsVals = args.Nbins.split(',')

print "cats: ",nCatsVals
print "binWidths: ",binWidthVals
# print "NbinsVals: ",NbinsVals

# xInterval = float(float(nCatsVals_orig[1]) - float(nCatsVals_orig[0]))
# yInterval = float(float(binWidthVals_orig[1]) - float(binWidthVals_orig[0]))

# nCatbinWidthCombos = []
nCatnBinCombos = []
for i in range(0,len(nCatsVals)):
    for j in range(0,len(binWidthVals)):
    # for j in range(0,len(NbinsVals)):
        nCatVal = nCatsVals[i]
        binWidthVal = binWidthVals[j]
        # NbinsVal = NbinsVals[j]
        combo = [nCatVal,binWidthVal]
        # combo = [nCatVal,NbinsVal]
        # nCatbinWidthCombos.append(combo)
        nCatnBinCombos.append(combo)

if(args.ComputeCats):
    # for comb in nCatbinWidthCombos: 
    for comb in nCatnBinCombos: 
        # print comb 
        nCatVal, binWidthVal = comb 
        # nCatVal, NbinsVal = comb 
        os.system('root -l optimize_cats.C\\(\\%s\\,\\1\\,\\1\\,\\0.0\\,\\%s\\,\\"\\%s\\"\\,\\"%s/\\"\\) << EOF'%(nCatVal,binWidthVal,args.note,args.filesLoc))
        # os.system('root -l optimize_cats.C\\(\\%s\\,\\1\\,\\1\\,\\0.0\\,\\%s\\,\\"\\%s\\"\\,\\"%s/\\",\\"%s\\"\\) << EOF'%(nCatVal,NbinsVal,args.note,args.filesLoc,args.year))
# 'viridis'
# expected file names 
# "/eos/user/a/atishelm/www/HHWWgg/DNN_Tools/Categorization_evalDNN_%scats_TestNewFiles_withSidebandScale_xmin-0.000000_binWidth-%s_CatSignificances.txt"%(nCatVal,binWidth)
# 

if(args.PlotSigs):
    # colors = ['C0','C1','C2','C3','C4','C5']
    colors = ['b','g','r','c','m','k','orange','yellow']
    ax, fig = plt.subplots()
    direc = "/eos/user/a/atishelm/www/HHWWgg/DNN_Tools_again/"
    for ibin,binWidthVal in enumerate(binWidthVals):
    # for ibin,NbinsVal in enumerate(NbinsVals):
        color = colors[ibin]
        print"binWidthVal:",binWidthVal
        # print"NbinsVal:",NbinsVal
        nCats_all, Purities = [], [] 
        for file in os.listdir(direc):
            if(file.endswith('_CatSignificances.txt') and "%s"%(args.note) in file ):
                # Nbins = file.split('_')[-2]
                binWidth = file.split('_')[-2]
                binWidth = binWidth.replace('binWidth-','')
                # Nbins = Nbins.replace('Nbins-','')
                # Nbins = int(Nbins)
                # if(Nbins != int(NbinsVal)): continue 
                # binWidth = float(b/inWidth)
                # if(Nbins != float(NbinsVal)): continue 
                if(binWidth != float(binWidthVal)): continue 
                nCats = file.split('_')[-6]
                nCats = nCats.replace('cats', '') 
                nCats = int(nCats)
                filePath = "%s/%s"%("/eos/user/a/atishelm/www/HHWWgg/DNN_Tools_again/",file)
                print("file:",filePath)
                sigInfo_df = pd.read_csv(filePath, sep=" ", header=None)
                sigVals = sigInfo_df[3]
                sigVals_l = sigVals.tolist()
                sigTotal = 0
                for val in sigVals_l:
                    sigTotal += float(val)*float(val)
                sigTotal = math.sqrt(sigTotal)
                print"nCats:",nCats
                print"sigTotal:",sigTotal
                nCats_all.append(nCats)
                Purities.append(sigTotal)
        # make line for each bin width 
        plt.plot(nCats_all,Purities,'o-',color=color,label="bin width = %s"%(binWidthVal))
        # plt.plot(nCats_all,Purities,'o-',color=color,label="Nbins = %s"%(NbinsVal))
    
    ol = "/eos/user/a/atishelm/www/HHWWgg/DNN_Tools_again/Purities/"
    plt.title("Purity vs. Ncats, Per bin width: %s"%(args.note))
    plt.xlabel("Ncats")
    plt.ylabel("Purity")
    plt.legend(loc='best')
    print("saving:",'%s/SigMap_%s_%s.png'%(ol,args.note,args.year))
    plt.savefig('%s/SigMap_%s_%s.png'%(ol,args.note,args.year))
    print("saving:",'%s/SigMap_%s_%s.pdf'%(ol,args.note,args.year))
    plt.savefig('%s/SigMap_%s_%s.pdf'%(ol,args.note,args.year))
    plt.close()    
    

    # print("binWidthVals:",binWidthVals)
    # print("nCatsVals:",nCatsVals)
    # print("maxSigs:",maxSigs)

    # binWidthVals_npa, nCatsVals_npa, maxSigs_npa = np.array(binWidthVals), np.array(nCatsVals), np.array(maxSigs)
    # x_min, x_max = np.min(nCatsVals_npa), np.max(nCatsVals_npa)
    # y_min, y_max = np.min(binWidthVals_npa), np.max(binWidthVals_npa)

    # NxVals, NyVals = len(nCatsVals_orig), len(binWidthVals_orig)

    # x_bins = np.linspace(x_min - xInterval/2, x_max + xInterval/2, NxVals+1) 
    # y_bins = np.linspace(y_min - yInterval/2, y_max + yInterval/2, NyVals+1) 

    # print("x_bins:",x_bins)
    # print("y_bins:",y_bins)

    # plt.hist2d(nCatsVals_npa,
    #            binWidthVals_npa,
    #            bins=[x_bins,y_bins],
    #            weights=maxSigs,
    #         #    vmin=0,
    # )
    # ol = "/eos/user/a/atishelm/www/HHWWgg/DNN_Tools/"
    # plt.title("Max Significance: %s"%(args.note))
    # plt.xlabel("Ncats")
    # plt.ylabel("bin Width")
    # # psm = ax.pcolormesh()
    # # plt.colorbar(cmap = 'viridis')
    # plt.colorbar()
    # print("saving:",'%s/SigMap_%s.png'%(ol,args.note))
    # plt.savefig('%s/SigMap_%s.png'%(ol,args.note))
    # print("saving:",'%s/SigMap_%s.pdf'%(ol,args.note))
    # plt.savefig('%s/SigMap_%s.pdf'%(ol,args.note))
    # plt.close()

# if(args.PlotSigs):
#     ax, fig = plt.subplots()
#     direc = "/eos/user/a/atishelm/www/HHWWgg/DNN_Tools/"
#     binWidthVals, nCatsVals, maxSigs = [], [], []
#     for file in os.listdir(direc):
#         if(file.endswith('_CatSignificances.txt') and "%s"%(args.note) in file ):
#             binWidth = file.split('_')[-2]
#             binWidth = binWidth.replace('binWidth-','')
#             binWidth = float(binWidth)
#             nCats = file.split('_')[-6]
#             nCats = nCats.replace('cats', '') 
#             nCats = int(nCats)
#             print("nCats:",nCats)
#             # if(nCats==1 or nCats==6): continue 
#             # if (str(binWidth) not in binWidthVals_orig) or (str(nCats))
#             binWidthVals.append(binWidth)
#             nCatsVals.append(nCats)
#             filePath = "%s/%s"%("/eos/user/a/atishelm/www/HHWWgg/DNN_Tools/",file)
#             print("file:",filePath)
#             sigInfo_df = pd.read_csv(filePath, sep=" ", header=None)
#             sigVals = sigInfo_df[3]
#             maxSig = max(sigVals)
#             maxSigs.append(maxSig)

#     print("binWidthVals:",binWidthVals)
#     print("nCatsVals:",nCatsVals)
#     print("maxSigs:",maxSigs)

#     binWidthVals_npa, nCatsVals_npa, maxSigs_npa = np.array(binWidthVals), np.array(nCatsVals), np.array(maxSigs)
#     x_min, x_max = np.min(nCatsVals_npa), np.max(nCatsVals_npa)
#     y_min, y_max = np.min(binWidthVals_npa), np.max(binWidthVals_npa)

#     NxVals, NyVals = len(nCatsVals_orig), len(binWidthVals_orig)

#     x_bins = np.linspace(x_min - xInterval/2, x_max + xInterval/2, NxVals+1) 
#     y_bins = np.linspace(y_min - yInterval/2, y_max + yInterval/2, NyVals+1) 

#     print("x_bins:",x_bins)
#     print("y_bins:",y_bins)

#     plt.hist2d(nCatsVals_npa,
#                binWidthVals_npa,
#                bins=[x_bins,y_bins],
#                weights=maxSigs,
#             #    vmin=0,
#     )
#     ol = "/eos/user/a/atishelm/www/HHWWgg/DNN_Tools/"
#     plt.title("Max Significance: %s"%(args.note))
#     plt.xlabel("Ncats")
#     plt.ylabel("bin Width")
#     # psm = ax.pcolormesh()
#     # plt.colorbar(cmap = 'viridis')
#     plt.colorbar()
#     print("saving:",'%s/SigMap_%s.png'%(ol,args.note))
#     plt.savefig('%s/SigMap_%s.png'%(ol,args.note))
#     print("saving:",'%s/SigMap_%s.pdf'%(ol,args.note))
#     plt.savefig('%s/SigMap_%s.pdf'%(ol,args.note))
#     plt.close()
    
print("DONE")
