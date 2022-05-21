import os 
import pickle 
import matplotlib.pyplot as plt
import numpy as np 
from python.VarTools import * 

def PlotDataFrames(args_):    
    print"Plotting dataframe(s)"
    df_types = args_.dfTypes.split(',')
    df_names = [] 
    for df_type in df_types:
        prefix = "Dataframes/%s"%(df_type)
        for file_i,file in enumerate(os.listdir(prefix)):
            df_path = "%s/%s"%(prefix,file)
            df_names.append(df_path)
    beforeOl = "/eos/user/a/atishelm/www/HHWWgg/"
    # beforeOl = "/eos/user/a/atishelm/www/HHWWgg/Phase_II/"
    ol = '%s/%s'%(beforeOl, args_.outDirectory)
    if(not os.path.exists(ol)):
        print"Creating output directory: %s"%(ol)
        os.system('mkdir %s'%(ol))
        os.system('cp %s/index.php %s'%(beforeOl,ol))    
    particles = args_.particles.split(',')
    variables = args_.variables.split(',')
    extraVars = args_.extraVariables.split(',')         

    # colors = ['C0','C1','C2','C3','C4','C5','C6']
    colors = ['C2','C0','C1','C3','C4','C5','C6']
    lineStyles = ['solid','dashed','dotted','dashdot'] # https://matplotlib.org/2.0.2/api/lines_api.html

    stylePairs = []

    for sty in range(0,4):
        color = colors[sty]
        lineStyle = lineStyles[sty]
        pair = [color,lineStyle]
        stylePairs.append(pair)

    # if(args_.ExtraStyles):
    #     for c in colors:
    #         for lS in lineStyles:
    #             pair = [c,lS]
    #             stylePairs.append(pair)

    # else:
    #     for c in colors: 
    #         pair = [c,'solid']
    #         stylePairs.append(pair)

    allVariables = []
    if(not extraVars == ['']):
        for v in extraVars: 
            allVariables.append(v)

    if not (particles == [''] and variables == ['']):
        for p in particles:
            for v in variables:
                varName = "%s_%s"%(p,v)
                allVariables.append(varName)  

    print("In PlotDataFrames.py")

    for v in allVariables:
        print"On variable:",v
        nbins, xmin, xmax, unit = GetVarParams(v,args_)

        ##-- Plot variable for each dataframe separately 
        if(args_.plotSingles):
            for dfi,df_name in enumerate(df_names):
                print"On dataframe:",df_name
                # stylePair = stylePairs[dfi]
                # thisColor, thisLineStyle = stylePair[0], stylePair[1]              
                # df = pickle.load( open( "%s"%(df_name), "rb" ) )                
                # plot = df.plot.hist(y=v,bins=nbins,alpha=0.5,color=thisColor,linestyle=('dashed'))
                # fig = plot.get_figure()
                dfEndPathName = df_name.split('/')[2].split('.')[0]
                # outName1 = "%s/%s_%s.png"%(ol,dfEndPathName,v)
                # outName2 = "%s/%s_%s.pdf"%(ol,dfEndPathName,v)
                # fig.savefig(outName1)
                # fig.savefig(outName2) 
                # plt.close() 

                fig, ax = plt.subplots()

                # plotLabel = "%s_%s"%(df_name.split('_')[3],df_name.split('_')[4])
                plotLabel = df_name.split('.')[-1].split('_')[0]
                plotLabel = plotLabel.replace("_df.p","")
                stylePair = stylePairs[dfi]
                thisColor, thisLineStyle = stylePair[0], stylePair[1]              
                df = pickle.load( open( "%s"%(df_name), "rb" ) ) 
                #print("length of df before:",len(df))
                #while(len(df) > args_.maxEvents): df = df.drop(df.index[-1]) # remove final entries until you have desired number of rows 
                #print("length of df after:",len(df))
                # print"df['pdgIds']:",df['pdgIds']
                if(v=='pdgIds'):
                    allVals = []
                    if(args_.nEvents != -1):
                        nEvents = int(args_.nEvents) 
                        for vals in df['pdgIds']:
                            for iv,val in enumerate(vals):
                                allVals.append(val)
                                if(iv >= nEvents): break 
                        nonNormyvals, binedges = np.histogram(allVals, bins=nbins, range=(xmin,xmax))
                        yvals, binedges = np.histogram(allVals, bins=nbins, range=(xmin,xmax),density=False)                        
                    else: 
                        for vals in df['pdgIds']:
                            for val in vals:
                                allVals.append(val)
                        nonNormyvals, binedges = np.histogram(allVals, bins=nbins, range=(xmin,xmax))
                        yvals, binedges = np.histogram(allVals, bins=nbins, range=(xmin,xmax),density=False)
                else: 
                    if(args_.nEvents != -1):
                        nEvents = int(args_.nEvents)
                        nonNormyvals, binedges = np.histogram(df[v][:nEvents], bins=nbins, range=(xmin,xmax))
                        yvals, binedges = np.histogram(df[v], bins=nbins, range=(xmin,xmax),density=True)                    
                    else: 
                        allVals_ = df[v]
                        allVals = np.array(allVals_)
                        MASK = [allVals != -99]     
                        allVals = allVals[MASK]                   
                        nonNormyvals, binedges = np.histogram(allVals, bins=nbins, range=(xmin,xmax))
                        yvals, binedges = np.histogram(allVals, bins=nbins, range=(xmin,xmax),density=True)

                entries = len(allVals)
                average = round(np.mean(allVals), 3)
                stdev = round(np.std(allVals), 3) 
                # average = 1
                # stdev = 1

                nonNormYerrors = np.sqrt(nonNormyvals)
                #print("nonNormyvals:",nonNormyvals)
                #print("nonNormYerrors:",nonNormYerrors)
                relErrors = np.divide(nonNormYerrors,nonNormyvals, out=np.zeros_like(nonNormYerrors),where=nonNormyvals!=0) 
                yerrors = yvals * relErrors
                bincenters = 0.5*(binedges[1:]+binedges[:-1])
                width = float(binedges[1])-float(binedges[0])
                #yerrors = np.sqrt(yvals)   

                if(v=='pdgIds'):

                    ##-- Save a latex style table with the number of particles of interest 
                    # pdgId_columns = [25, 22, -24, 24, -11, 11, -12, 12, -13, 13, -14, 14, -15, 15, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]

                    pdgId_column_possibilities = [
                        # [25],
                        # [22],
                        # [-24, 24],
                        # [-11, 11, -13, 13, -15, 15],
                        # [-12, 12, -14, 14, -16, 16],
                        # [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]

                        [25],
                        [22],
                        [23],
                        [-11, 11, -13, 13, -15, 15],
                        [-12, 12, -14, 14, -16, 16],
                        [-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]                        
                    ]

                    pdgId_column_labels = [
                        # "Higgs",
                        # "Photons",
                        # "W Bosons",
                        # "Leptons",
                        # "Neutrinos",
                        # "Quarks"

                        "Higgs",
                        "Photons",
                        "Z Bosons",
                        "Leptons",
                        "Neutrinos",
                        "Quarks"                        
                    ]                    

                    for pdgId_group, pdgId_columns in enumerate(pdgId_column_possibilities):

                        column_line_label = pdgId_column_labels[pdgId_group]

                        nPdgIds_forTable = len(pdgId_columns)
                        file_text = """
                        \\begin{table}[H]
                            \\begin{center}
                            \\begin{tabular}{c|{columnStyle}|c}
                                % \hline
                                    pdgId        &   {pdgId_columns_line} & all            \\\ \hline
                                    Total        &   {pdgId_Totals}       & {all_Total}    \\\ \hline
                                    Per Event    &   {pdgId_perEvent}     & {all_PerEvent}
                                    \end{tabular}
                            \end{center}
                            \caption{{column_line_label}}}
                            \label{tab:{column_line_label}_pdgIds}
                        \end{table} 
                        """     

                        particle_pdgID_dict = {}     

                        for ic,center in enumerate(bincenters):
                            val = yvals[ic]
                            # if(val!=0): 
                            pdgId_val = int(center - width / 2)
                            # print"pdgId:",pdgId_val,": ",val
                            particle_pdgID_dict[pdgId_val] = val 

                        columnStyle = ""
                        pdgId_columns_line = ""
                        pdgId_Totals = ""
                        pdgId_perEvent = ""

                        NEVENTS = 1000. ##-- Hardcoded :) 

                        for i in range(0, nPdgIds_forTable):
                            columnStyle += "c"

                        all_Total, all_PerEvent = 0, 0 

                        for pdgId_i, pdgId_val in enumerate(pdgId_columns):

                            ##-- Get values 
                            N_pdgId = particle_pdgID_dict[pdgId_val]
                            all_Total += N_pdgId 
                            N_perEvent = N_pdgId / NEVENTS

                            ##-- Append to strings 
                            pdgId_columns_line += str(pdgId_val) 
                            pdgId_Totals += str(N_pdgId)
                            pdgId_perEvent += str(N_perEvent)
                            
                            ##-- if not the final pdgId column, add a table column separator
                            if(pdgId_i < (nPdgIds_forTable - 1)):
                                pdgId_columns_line += " & "
                                pdgId_Totals += " & " 
                                pdgId_perEvent += " & "
                        
                        all_PerEvent = all_Total / NEVENTS

                        file_text = file_text.replace("{columnStyle}", columnStyle)
                        file_text = file_text.replace("{pdgId_columns_line}", pdgId_columns_line)
                        file_text = file_text.replace("{pdgId_Totals}", pdgId_Totals)
                        file_text = file_text.replace("{pdgId_perEvent}", pdgId_perEvent)
                        file_text = file_text.replace("{all_Total}", str(all_Total))
                        file_text = file_text.replace("{all_PerEvent}", str(all_PerEvent))
                        file_text = file_text.replace("{column_line_label}", str(column_line_label))

                        # print "Latex table of PdgIds:"
                        print 
                        print file_text

                xerrors = []
                for i in range(0,nbins): xerrors.append(width/2)
                xerrors_a = np.array(xerrors) # xerrors array 
                binedges = np.delete(binedges,0,0)

                # for yval in yvals: yvals_1.append(yval)
                # for error in yerrors: yerrors_1.append(error)

                # ax.hist(bincenters, weights = yvals)
                ax.bar(bincenters,
                            yvals,
                            width=width,
                            xerr=xerrors_a,
                            yerr=yerrors,
                            #  align='edge',
                            alpha=0,
                            #  linewidth=linewidth,
                            label=plotLabel,

                            # color=thisColor,
                            # error_kw = dict(
                            #     ecolor=thisColor
                            # )
                )     

                xlabel = "%s [%s]"%(v,unit)
                ax.set_ylabel("Entries [A.U.]")
                ax.set_title(v)
                ax.set_xlabel(xlabel)
                ax.set_xlim(xmin, xmax)
                # axarr[1].plot([xmin,xmax],[1,1],linestyle=':')
                # axarr[1].set_ylim(ymin=0.8,ymax=1.2)
                ax.tick_params(direction='in')
                ax.yaxis.set_ticks_position('both')
                ax.xaxis.set_ticks_position('both')

                # if(v=="qq_invmass" or v=="Sublead_H_pt"): legLoc = 'upper left'
                # else: legLoc = 'upper right'
                # legLoc = 'upper right'

                # if(args_.upLeftLegend): legLoc = 'upper left'

                # leg = ax.legend(loc=legLoc,fontsize='x-large')
                # for i,lh in enumerate(leg.legendHandles): 

                #     stylePair = stylePairs[i]
                #     thisColor, thisLineStyle = stylePair[0], stylePair[1] 
                #     lh.set_alpha(1)
                #     lh.set_color(thisColor)

                ##-- Prepare Text Box 
                textstr = '\n'.join((
                    "Entries: %s"%(entries),
                    "Average: %s"%(average),
                    "St. dev. : %s"%(stdev)
                    ))   
                props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)    

                # xpos, ypos = 0.7, 0.85
                xpos, ypos = 0.3, 0.85

                if(v == "qq_invmass"):
                    xpos, ypos = 0.3, 0.85 ##-- To avoid on-shell W peak 

                ax.text(xpos, ypos, textstr, transform=ax.transAxes, fontsize=14,
                        verticalalignment='top', bbox=props) 

                plt.grid()
                if(args_.nEvents != -1):
                    outName1 = "%s/%s_%s_%s-Events.png"%(ol,dfEndPathName,v,int(args_.nEvents))
                    outName2 = "%s/%s_%s_%s-Events.pdf"%(ol,dfEndPathName,v,int(args_.nEvents))
                else:
                    outName1 = "%s/%s_%s.png"%(ol,dfEndPathName,v)
                    outName2 = "%s/%s_%s.pdf"%(ol,dfEndPathName,v)                    
                fig.savefig(outName1)
                fig.savefig(outName2)
                plt.close()     

        # print"df names:",df_names
        # exit(1) 

        ##-- Combine plots for dataframes 
        if(args_.doRatioHists):
            print"Making ratio plots"
            props = dict(boxstyle='round', facecolor='aqua', alpha=0.2)
            fig, axarr = plt.subplots(2, 
                                    sharex=True, 
                                    gridspec_kw={
                                        'hspace': 0.15,
                                        'height_ratios': (0.8,0.2)
                                        }
                                    )

            n_dfs = len(df_names)
            for ii in range(n_dfs):
                exec("yvals_%s = []"%(ii))
                exec("yerrors_%s = []"%(ii))
                # make ratio values for each df after the first 
                if ii > 0:
                    exec("ratio_vals_%s = []"%(ii))
                    exec("ratio_errors_%s = []"%(ii))

            # yvals_1 = []
            # yerrors_1 = []
            # yvals_2 = [] 
            # yerrors_2 = [] 
            # ratio_vals = [] 
            # ratio_errors = []

            ##-- get individual lines 
            for dfi,df_name in enumerate(df_names):
                print"on dataframe",df_name
                # plotLabel = "%s_%s"%(df_name.split('_')[3],df_name.split('_')[4])
                plotLabel = df_name.split('_')[0]
                plotLabel = plotLabel.replace("_df.p","")
                stylePair = stylePairs[dfi]
                thisColor, thisLineStyle = stylePair[0], stylePair[1]              
                df = pickle.load( open( "%s"%(df_name), "rb" ) ) 
                #print("length of df before:",len(df))
                #while(len(df) > args_.maxEvents): df = df.drop(df.index[-1]) # remove final entries until you have desired number of rows 
                #print("length of df after:",len(df))
                nonNormyvals, binedges = np.histogram(df[v], bins=nbins, range=(xmin,xmax))
                yvals, binedges = np.histogram(df[v], bins=nbins, range=(xmin,xmax),density=True)
                nonNormYerrors = np.sqrt(nonNormyvals)
                #print("nonNormyvals:",nonNormyvals)
                #print("nonNormYerrors:",nonNormYerrors)
                relErrors = np.divide(nonNormYerrors,nonNormyvals, out=np.zeros_like(nonNormYerrors),where=nonNormyvals!=0) 
                yerrors = yvals * relErrors
                bincenters = 0.5*(binedges[1:]+binedges[:-1])
                width = float(binedges[1])-float(binedges[0])
                #yerrors = np.sqrt(yvals)
                xerrors = []
                for i in range(0,nbins): xerrors.append(width/2)
                xerrors_a = np.array(xerrors) # xerrors array 
                binedges = np.delete(binedges,0,0)

                if dfi == 0: 
                    # yvals = eval("yvals_%s"%(dfi))
                    # yerrors = eval("yvals_%s"%(dfi))
                    # for yval in yvals: yvals_1.append(yval)   
                    # for error in yerrors: yerrors_1.append(error)
                    for yval in yvals: yvals_0.append(yval)
                    for error in yerrors: yerrors_0.append(error)                    

                    axarr[0].bar(bincenters,
                                yvals,
                                width=width,
                                xerr=xerrors_a,
                                yerr=yerrors,
                                #  align='edge',
                                alpha=0,
                                #  linewidth=linewidth,


                                # label=plotLabel,
                                # color=thisColor,
                                # error_kw = dict(
                                #     ecolor=thisColor
                                # )


                    )
                    # if(args_.doRatioHists):
                    #     axarr[0].hist(histtype='step',
                    #                 bins=binedges,
                    #                 x = df[v],
                    #                 color=thisColor,
                            
                    #     )

                else:
                    # yvals = eval("yvals_%s"%(dfi))
                    # yerrors = eval("yerrors_%s"%(dfi))
                    # exec("yvals = yvals_%s"%(dfi))
                    # exec("yerrors = yerrors_%s"%(dfi))                    
                    # print"thisColor:",thisColor
                    ##-- add to lists for ratios later 
                    for yval in yvals:
                        eval("yvals_%s.append(yval)"%(dfi))
                    for yerror in yerrors:
                        eval("yerrors_%s.append(yerror)"%(dfi))
                    # for yval in yvals: yvals_2.append(yval)
                    # for error in yerrors: yerrors_2.append(error)
                    # for yval in yvals: yvals.append(yval)
                    # for error in yerrors: yerrors.append(error)                    
                    # for error in yerrors: yerrors.append(error)          
                    # 
                    # print"len(yvals): ",len(yvals)
                    # print"len(yerrors): ",len(yerrors)
                    # print"yvals: ",yvals
                    # print"yerrors: ",yerrors 

                    axarr[0].bar(bincenters,
                                yvals,
                                width=width,
                                xerr=xerrors_a,
                                yerr=yerrors,
                                # yerr=yerrors,
                                #  align='edge',
                                alpha=0,
                                #  linewidth=linewidth, 
                                label=plotLabel,


                                # color=thisColor,
                                # error_kw = dict(
                                #     ecolor=thisColor
                                # )

                                
                    )

            ##-- Add subsequent lines and make ratio lines 
            print"Adding subsequent lines and making ratio lines"
            for bin_i,yval_0 in enumerate(yvals_0):
                for df_i in range(1,n_dfs): ##-- skip first. don't need ratio with self. just add horizontal line at 1 
                    yval_denom = eval("yvals_%s[bin_i]"%(df_i))
                    if(yval_0==0 or yval_denom==0):
                        ratio_val, ratio_error = 0, 0 ##-- deal with zero values 
                    else: 
                        ratio_val = float(yval_0) / float(yval_denom)
                        error1 = yerrors_0[bin_i]
                        error2 = eval("yerrors_%s[bin_i]"%(df_i))
                        ratio_error = ratio_val*np.sqrt((error1/yval_0)**2 + (error2/yval_denom)**2)
                    exec("ratio_vals_%s.append(ratio_val)"%(df_i))
                    exec("ratio_errors_%s.append(ratio_error)"%(df_i))

            for df_i in range(1,n_dfs):
                ratio_vals_a = np.array(eval("ratio_vals_%s"%(df_i)))
                ratio_errors_a = np.array(eval("ratio_errors_%s"%(df_i)))                    
                stylePair = stylePairs[df_i]
                thisColor, thisLineStyle = stylePair[0], stylePair[1]      
                
                axarr[1].bar(bincenters,
                            ratio_vals_a,
                            width=width,
                            xerr=xerrors_a,
                            yerr=ratio_errors_a,
                            #  align='edge',
                            alpha=0,
                            ##-- add color and style corresponding to legend 

                            # color=thisColor,
                            # error_kw = dict(
                            #     ecolor=thisColor
                            # ),
                            # linestyle=thisLineStyle     

                            )

            xlabel = "%s [%s]"%(v,unit)
            axarr[0].set_ylabel("Entries [A.U.]")
            axarr[0].set_title(v)
            axarr[1].plot([xmin,xmax],[1,1],linestyle=':')
            axarr[1].set_xlabel(xlabel)
            axarr[1].set_ylabel("ratio")
            axarr[1].set_ylim(ymin=0.8,ymax=1.2)
            axarr[0].tick_params(direction='in')
            axarr[0].yaxis.set_ticks_position('both')
            axarr[0].xaxis.set_ticks_position('both')

            # if(v=="qq_invmass" or v=="Sublead_H_pt"): legLoc = 'upper left'
            # else: legLoc = 'upper right'
            legLoc = 'upper right'

            if(args_.upLeftLegend): legLoc = 'upper left'

            leg = axarr[0].legend(loc=legLoc,fontsize='x-large')


            # for i,lh in enumerate(leg.legendHandles): 
            #     stylePair = stylePairs[i]
            #     thisColor, thisLineStyle = stylePair[0], stylePair[1] 
            #     lh.set_alpha(1)
            #     lh.set_color(thisColor)

            outName1 = "%s/combined_%s.png"%(ol,v)
            outName2 = "%s/combined_%s.pdf"%(ol,v)
            fig.savefig(outName1)
            fig.savefig(outName2)
            plt.close() 


                # if dfi == len(df_names)-1: 

                #     for i,yval_1 in enumerate(yvals_0):
                #         yval_2 = yvals_2[i]
                #         if(yval_1==0 or yval_2==0):
                #             ratio_val, ratio_error = 0, 0
                #         else: 
                #             ratio_val = float(yval_1) / float(yval_2)
                #             error1 = yerrors_0[i] ## first df. take ratio wrt this one 
                #             error2 = yerrors_2[i]
                #             ratio_error = ratio_val*np.sqrt((error1/yval_1)**2 + (error2/yval_2)**2)
                #         ratio_vals.append(ratio_val)
                #         ratio_errors.append(ratio_error)

                #     ratio_vals_a = np.array(ratio_vals)
                #     ratio_errors_a = np.array(ratio_errors)

                    # axarr[1].bar(bincenters,
                    #             ratio_vals_a,
                    #             width=width,
                    #             xerr=xerrors_a,
                    #             yerr=ratio_errors_a,
                    #             #  align='edge',
                    #             alpha=0
                    #             )

                    # xlabel = "%s [%s]"%(v,unit)
                    # axarr[0].set_ylabel("Entries [A.U.]")
                    # axarr[0].set_title(v)
                    # axarr[1].plot([xmin,xmax],[1,1],linestyle=':')
                    # axarr[1].set_xlabel(xlabel)
                    # axarr[1].set_ylabel("ratio")
                    # axarr[1].set_ylim(ymin=0.8,ymax=1.2)
                    # axarr[0].tick_params(direction='in')
                    # axarr[0].yaxis.set_ticks_position('both')
                    # axarr[0].xaxis.set_ticks_position('both')

                    # # if(v=="qq_invmass" or v=="Sublead_H_pt"): legLoc = 'upper left'
                    # # else: legLoc = 'upper right'
                    # legLoc = 'upper right'

                    # if(args_.upLeftLegend): legLoc = 'upper left'

                    # leg = axarr[0].legend(loc=legLoc,fontsize='x-large')
                    # for i,lh in enumerate(leg.legendHandles): 

                    #     stylePair = stylePairs[i]
                    #     thisColor, thisLineStyle = stylePair[0], stylePair[1] 
                    #     lh.set_alpha(1)
                    #     lh.set_color(thisColor)

                    # outName1 = "%s/combined_%s.png"%(ol,v)
                    # outName2 = "%s/combined_%s.pdf"%(ol,v)
                    # fig.savefig(outName1)
                    # fig.savefig(outName2)
                    # plt.close()     

    print"DONE"