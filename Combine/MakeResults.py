import os 
import argparse
import uproot 
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# Example Usage: 
# python MakeResults.py --CheckYearCombos 
# python MakeResults.py --CheckChannelCombos
# python MakeResults.py --CombineYears
# python MakeResults.py --CombineChannels
# python MakeResults.py --Plot 
# python MakeResults.py --IndividualImpacts
# python MakeResults.py --CombinedImpacts

parser = argparse.ArgumentParser()

parser.add_argument("--CheckYearCombos", action="store_true", default=False, help="Check results same for all orders of channel_year datacard combination")
parser.add_argument("--CheckChannelCombos", action="store_true", default=False, help="Check results same for all orders of channel datacard combination")
parser.add_argument("--CombineYears", action="store_true", default=False, help="Run combine on each channel/year datacard")
parser.add_argument("--CombineChannels", action="store_true", default=False, help="Run combine on each channel for Run 2 and combine")
parser.add_argument("--Plot", action="store_true", default=False, help="Plot limits")
parser.add_argument("--IndividualImpacts", action="store_true", default=False, help="Produce impact plots for each year / channel")
parser.add_argument("--CombinedImpacts", action="store_true", default=False, help="Produce impact plots for each channel and combination")

args = parser.parse_args()

if(args.CheckYearCombos):
    ##-- Year pairs for each channel
    channels = ["SL","FH","FL"]
    pairs = ["2016-2017-2018", "2016-2018-2017", "2017-2016-2018", "2017-2018-2016", "2018-2016-2017", "2018-2017-2016"]
    for channel in channels:
        for pair in pairs:
            y1, y2, y3 = pair.split('-')
            dc1, dc2, dc3 = "%s%s.txt"%(channel,y1), "%s%s.txt"%(channel,y2), "%s%s.txt"%(channel,y3)
            pairName = "%s_%s.txt"%(channel, pair)
            COMBINECARDS_COMMAND = "combineCards.py %s %s %s >> %s "%(dc1, dc2, dc3, pairName)
            print"COMBINECARDS_COMMAND:",COMBINECARDS_COMMAND
            os.system(COMBINECARDS_COMMAND)
            COMBINE_COMMAND = "combine %s -m 125.38 -M AsymptoticLimits --run=blind -t -1 --setParameters  MH=125.38 --freezeParameters MH --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 >> CheckCombos/%s.log "%(pairName, pairName)
            print"COMBINE_COMMAND:",COMBINE_COMMAND
            print"Running..." 
            os.system(COMBINE_COMMAND)

if(args.CheckChannelCombos):
    ##-- Channel pairs for run 2 
    pairs = ["SL-FH-FL","SL-FL-FH","FH-SL-FL","FH-FL-SL","FL-SL-FH","FL-FH-SL"]
    channel = "Run2"
    for pair in pairs:
        y1, y2, y3 = pair.split('-')
        dc1, dc2, dc3 = "%s_Run2.txt"%(y1), "%s_Run2.txt"%(y2), "%s_Run2.txt"%(y3)
        pairName = "%s_%s.txt"%(channel, pair)
        COMBINECARDS_COMMAND = "combineCards.py %s %s %s >> %s "%(dc1, dc2, dc3, pairName)
        print"COMBINECARDS_COMMAND:",COMBINECARDS_COMMAND
        os.system(COMBINECARDS_COMMAND)
        COMBINE_COMMAND = "combine %s -m 125.38 -M AsymptoticLimits --run=blind -t -1 --setParameters  MH=125.38 --freezeParameters MH --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 >> CheckCombos_OneFLBkgModel/%s.log "%(pairName, pairName)
        print"COMBINE_COMMAND:",COMBINE_COMMAND
        print"Running..." 
        os.system(COMBINE_COMMAND)    

if(args.CombineYears):
    years = ["2016","2017","2018"]
    channels = ["SL","FH","FL"]

    mH = "125.38"
    for channel in channels:
        for year in years:
            DataCard = "%s%s"%(channel, year)
            logFile = "%s.log"%(DataCard) #--setParameterRanges  MH=120,130
            print"Datacard: ",DataCard
            COMBINE_COMMAND = "combine %s.txt -m %s -M AsymptoticLimits --run=blind -t -1 --setParameters MH=%s --freezeParameters MH --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 -n %s > %s"%(DataCard,mH,mH,DataCard,logFile)
            print"COMBINE COMMAND: ",COMBINE_COMMAND
            os.system(COMBINE_COMMAND)
            os.system("mv higgsCombine.%s.AsymptoticLimits.mH%s.root CombineOutputs"%(DataCard,mH))
            os.system("mv %s CombineLogs"%(logFile))

if(args.CombineChannels):
    channels = ["SL","FH","FL"]
    mH = "125.38"
    for channel in channels:
        DataCard = "%s_Run2"%(channel)
        logFile = "%s.log"%(DataCard) #--setParameterRanges  MH=120,130
        print"Datacard: ",DataCard
        COMBINE_COMMAND = "combine %s.txt -m %s -M AsymptoticLimits --run=blind -t -1 --setParameters MH=%s --freezeParameters MH --cminDefaultMinimizerStrategy 0 --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 -n %s > %s"%(DataCard,mH,mH,DataCard,logFile)
        print"COMBINE COMMAND: ",COMBINE_COMMAND
        os.system(COMBINE_COMMAND)
        os.system("mv higgsCombine%s.AsymptoticLimits.mH%s.root CombineOutputs"%(DataCard,mH))
        os.system("mv higgsCombine%s.AsymptoticLimits.mH%s.root CombineOutputs/higgsCombine.%s.AsymptoticLimits.mH%s.root"%(DataCard,mH,DataCard,mH))
        os.system("mv %s CombineLogs"%(logFile))  

if(args.Plot):
    Direc = "CombineOutputs"
    FinalStates = ["All"]
    # years = ["2016","2017","2018","Run2"]
    years = ["Run2"]

    file_text = """
    \\begin{table}[H]
        \\begin{center}
          \\begin{tabular}{ccccccc}
            \hline
              & $-2\sigma$ & $-1\sigma$ & Median & $+1\sigma$ & $+2\sigma$ \\\ \hline
                Fully-Hadronic     &   {FH_Results}    \\\ \hline
                Fully-Leptonic     &   {FL_Results}    \\\ \hline
                Semi-Leptonic      &   {SL_Results}    \\\ \hline
                Combination        &   {Combined_Results}   \\\ \hline
                \end{tabular}
        \end{center}
        \caption{Full Run2 Combination results, including Semi-Leptonic, Fully-Leptonic and Fully-Hadronic categories, 
        on $\\frac{\sigma(HH)}{\sigma_{SM}(HH)}$, assuming an NLO standard model cross section of about 31.05 fb}
        \label{tab:Run2Results}
    \end{table}
    """

    FH_Results = []
    FL_Results = []
    SL_Results = []
    Combined_Results = []

    # print(file_text)

    # exit(1) 

    ##-- Make a plot for each final state 
    for fs in FinalStates:
        files = [] 
        if(fs == "All"):
            fs_Label = "All"
            files = ["CombineOutputs/higgsCombine.FH_Run2.AsymptoticLimits.mH125.38.root",
                     "CombineOutputs/higgsCombine.FL_Run2.AsymptoticLimits.mH125.38.root",
                     "CombineOutputs/higgsCombine.SL_Run2.AsymptoticLimits.mH125.38.root",
                     "CombineOutputs/higgsCombine.Combined_Run2.AsymptoticLimits.mH125.38.root"
            ]
        else: 
            fs_Label = fs.split('_')[-1]
            for year in years:
                fileName = "CombineOutputs/higgsCombineHHWWgg_%s_%s.AsymptoticLimits.mH125.38.root"%(fs,year)
                files.append(fileName)         

        y_pos = np.arange(len(files))
        y_pos_labels = np.arange(len(files)) + 0.5
        
        fig, ax = plt.subplots() 
        # fig.set_figheight(15)
        # fig.set_figwidth(15)        
        limits_quantiles = ["down2","down1","median","up1","up2"]
        down2, down1, median, up1, up2 = [], [], [], [], [] 
        limitPairs = []
        for file in files:
            print"file:",file
            file_uproot = uproot.open(file)
            limitVals = file_uproot["limit/limit"].array()
            if("SL" in file): SL_Results = limitVals.copy().round(decimals = 2)
            if("FH" in file): FH_Results = limitVals.copy().round(decimals = 2)
            if("FL" in file): FL_Results = limitVals.copy().round(decimals = 2)
            if("Combined" in file): Combined_Results = limitVals.copy().round(decimals = 2)
            print"limitVals:",limitVals
            for i, quant in enumerate(limits_quantiles):
                exec("%s.append(limitVals[%s])"%(quant, i))
        if(fs_Label == "All"):
            channels = [file.split('.')[1].split('_')[0] for file in files]
            years = [file.split('.')[1].split('_')[1] for file in files]
        else:
            channels = [file.split('_')[4] for file in files]
            years = [file.split('_')[5].split('.')[0] for file in files]            
        # channels = [file.split('_')[4] for file in files]
        # years = [file.split('_')[5].split('.')[0] for file in files]
        labels = ["%s %s"%(channel,years[i]) for i, channel in enumerate(channels)]
        for quantile in ["down2","down1","up1","up2"]:
            exec("%s_vals = [abs(median[i] - %s[i]) for i, val in enumerate(median)]"%(quantile,quantile))
        # lineWidth = 87 ##-- 115 + 1: just about perfect fit for 3 files. 86.25 + 0.75: for 4 files. 
        # m = -28.75
        # nFilesFloat = float(len(files))
        # pad = 1 * 3 / nFilesFloat
        # lineWidth = ( m * nFilesFloat + 201.25 ) + pad 
        lineWidth = 87.5
        yerr = 0.5
        ax.barh(y_pos, median, xerr = [down2_vals, up2_vals], ecolor='gold', align='center', alpha=0, error_kw=dict(ls='--', lw=lineWidth, capsize=0, capthick=0))
        ax.barh(y_pos, median, xerr = [down1_vals, up1_vals], ecolor='g', align='center', alpha=0, error_kw=dict(ls='--', lw=lineWidth, capsize=0, capthick=0))
        # ax.barh(y_pos, median, yerr = yerr, ecolor='black', align='center', alpha=0, error_kw=dict(ls='dashed')) ##-- Expected limits 
        # ax.barh(y_pos, median, yerr = yerr, ecolor='black', align='center', alpha=0, label='Expected 95% C.L. Limit', error_kw=dict(ls='--')) ##-- Expected limits 
        eb = plt.errorbar(median, y_pos, marker="o", yerr = yerr, linestyle="", color="black", capsize=0, label="Expected 95% C.L. Limit")
        eb[-1][0].set_linestyle('dashed')
        # ax.errorbar.set_linestyle('--')
        plt.text(
            # 0.05, 0.9, u"CMS $\it{Preliminary}$",
            0., 1., u"CMS ",
            fontsize=18, fontweight='bold',
            horizontalalignment='left', 
            verticalalignment='bottom', 
            transform=ax.transAxes
        )    
        plt.text(
            # 0.05, 0.9, u"CMS $\it{Preliminary}$",
            0.12, 1., u"Preliminary",
            fontsize=18,
            horizontalalignment='left', 
            verticalalignment='bottom', 
            transform=ax.transAxes
        )            

        plt.text(
                1., 1., r"%1.0f fb$^{-1}$ (13 TeV)" % 137,
                fontsize=14, horizontalalignment='right', 
                verticalalignment='bottom', 
                transform=ax.transAxes     
        )       
        # for i,val in enumerate(y_pos):
            # y_pos[i] = val - 0.5 
        # ax.set_yticks(y_pos,va="center")
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.tick_params(axis='y', which=u'both',length=0)
        # plt.yticks(y_pos,va='bottom')
        # plt.yticklabels(labels)
        # ax.set_yticks(y_pos, va='bottom')
        # ax.set_yticklabels(labels, va='center')
        ax.invert_yaxis()  # labels read top-to-bottom
        # locs_spots, labels_names = plt.yticks()

        # for axis in [ax.yaxis]:
            # axis.set(ticks=np.arange(0.5, len(labels)), ticklabels=labels)

        # for tick in ax.yaxis.get_majorticklabels():
            # tick.set_verticalalignment("top")
        # print"ax.get_ylim():",ax.get_ylim()
        # locs_spots, labels_names = plt.yticks()
        # print"locs_spots:",locs_spots      
        # print"labels_names:",labels_names          
        ax.set_xlabel(r'95% CL Upper Limit on $\sigma$ / $\sigma_{SM}^{NLO}$')
        # ax.set_title('%s Limits'%(fs_Label))  
        ax.set_xscale('log') 
        plt.subplots_adjust(left=0.175)
        xmin, xmax = plt.xlim()
        plt.hlines([0.5, 1.5, 2.5], xmin=xmin, xmax=xmax, linestyles='solid')

        legend_elements = [Line2D([0], [0], color='black', marker="o", lw=1, ls='--', label='Expected 95% C.L. Limit'),
                        Patch(facecolor='g', edgecolor='black',
                                 label=r'Expected $\pm$1 s.d.'),
                        Patch(facecolor='gold', edgecolor='black',
                                 label=r'Expected $\pm$2 s.d.')                                                         
                                 ]

        # plt.legend('upper left')
        plt.legend(handles=legend_elements, numpoints=1, loc='upper left', prop={'size': 12})
        plt.grid(True, axis='x')
        plt.savefig("/eos/user/a/atishelm/www/HHWWgg/January-2021-Production/Results/%s_limits.png"%(fs_Label))
        plt.savefig("/eos/user/a/atishelm/www/HHWWgg/January-2021-Production/Results/%s_limits.pdf"%(fs_Label))
        plt.close()
    
    file_text = file_text.replace("{FH_Results}", "%s & %s & %s & %s & %s"%(FH_Results[0], FH_Results[1], FH_Results[2], FH_Results[3], FH_Results[4]))
    file_text = file_text.replace("{FL_Results}", "%s & %s & %s & %s & %s"%(FL_Results[0], FL_Results[1], FL_Results[2], FL_Results[3], FL_Results[4]))
    file_text = file_text.replace("{SL_Results}", "%s & %s & %s & %s & %s"%(SL_Results[0], SL_Results[1], SL_Results[2], SL_Results[3], SL_Results[4]))
    file_text = file_text.replace("{Combined_Results}", "%s & %s & %s & %s & %s"%(Combined_Results[0], Combined_Results[1], Combined_Results[2], Combined_Results[3], Combined_Results[4]))

    print file_text

if((args.IndividualImpacts) or (args.CombinedImpacts)):
    mass = "125.38"

    #if(args.IndividualImpacts): datacardLabels = ["%s%s"%(channel,year) for channel in ["SL","FH","FL"] for year in ["2016","2017","2018"] ]
    # if(args.CombinedImpacts): datacardLabels = ["SL_Run2","FH_Run2","FL_Run2","FullRun2"]
    # if(args.CombinedImpacts): datacardLabels = ["FL_Run2","FullRun2"]
    #if(args.CombinedImpacts): datacardLabels = ["FullRun2"]
    # if(args.CombinedImpacts): datacardLabels = ["SL_Run2","FH_Run2"]

    datacardLabels=["SL2016"]

    for i,datacardLabel in enumerate(datacardLabels):
        print"Datacard: ",datacardLabel
        datacard = "%s.txt"%(datacardLabel)
        workspace = "%s.root"%(datacardLabel)
        outDirec = "Impacts/%s"%(datacardLabel)
        os.system('mkdir -p %s '%(outDirec))
        TEXTTOWORKSPACE_COMMAND = "text2workspace.py %s -o %s/%s"%(datacard,outDirec,workspace)
        print"TEXTTOWORKSPACE_COMMAND:",TEXTTOWORKSPACE_COMMAND
        os.system(TEXTTOWORKSPACE_COMMAND)

        os.chdir(outDirec)

        IMPACT_COMMAND_ONE = "combineTool.py -M Impacts -d %s -m %s --rMin -5 --rMax 10 --robustFit 1 --doInitialFit  -t -1 --expectSignal 1 --cminDefaultMinimizerStrategy 0 --setParameters  MH=%s --freezeParameters MH  --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2"%(workspace, mass, mass)
        IMPACT_COMMAND_TWO = "combineTool.py -M Impacts -d %s -m %s --rMin -5 --rMax 10 --robustFit 1 --doFits  -t -1 --expectSignal 1 --cminDefaultMinimizerStrategy 0 --setParameters  MH=%s --freezeParameters MH  --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2"%(workspace, mass, mass)
        IMPACT_COMMAND_THREE = "combineTool.py -M Impacts -d %s -m %s --rMin -5 --rMax 10 --robustFit 1 --output Impacts_%s.json -t -1 --expectSignal 1 --cminDefaultMinimizerStrategy 0 --setParameters  MH=%s --freezeParameters MH  --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2"%(workspace, mass, datacardLabel, mass)
        IMPACT_COMMAND_FOUR = "plotImpacts.py -i Impacts_%s.json -o Impacts_%s"%(datacardLabel,datacardLabel)

        print"IMPACT_COMMAND_ONE:",IMPACT_COMMAND_ONE
        os.system(IMPACT_COMMAND_ONE)
        print"IMPACT_COMMAND_TWO:",IMPACT_COMMAND_TWO
        os.system(IMPACT_COMMAND_TWO)
        print"IMPACT_COMMAND_THREE:",IMPACT_COMMAND_THREE
        os.system(IMPACT_COMMAND_THREE)
        print"IMPACT_COMMAND_FOUR:",IMPACT_COMMAND_FOUR
        os.system(IMPACT_COMMAND_FOUR)
        
        COPY_COMMAND = "cp Impacts_%s.pdf /eos/user/a/atishelm/www/HHWWgg/January-2021-Production/Results/"%(datacardLabel)
        print"COPY_COMMAND:",COPY_COMMAND
        os.system(COPY_COMMAND)

        os.chdir('../..')        
