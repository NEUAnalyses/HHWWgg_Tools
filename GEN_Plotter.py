#!/usr/bin/env python

# Python only 

# 7 February 2019
# Abe Tishelman-Charny 

# This takes some inspiration from TreePlotter.py and PlotterTools.py
# Run from cmssw with cmsenv to access FWLite 
# Might need certain CMSSW version depending on data 
# Currently running from CMSSW_10

# The purpose of this plotter is to plot variables from GEN level files
# This is to study what the signal looks like with no detector bias
# The outputs of this can tell if the analysis strategy implemented in the flashgg HHWWggCandidateDumper logic is well-formed.
#https://indico.cern.ch/event/795443/contributions/3304650/attachments/1792639/2921042/2019-02-07-physicsPlenary.pdf

from ROOT import * 
import array as arr 
import numpy as np
#ROOT.gROOT.LoadMacro("GEN_Plotter_Config.py")
#gROOT.LoadMacro("./GEN_Plotter_Config.py")
from GEN_Plotter_Config import * 
import subprocess
#import ROOT
gROOT.SetBatch(True)
#PyConfig.IgnoreCommandLineOptions = True
from DataFormats.FWLite import Handle, Runs, Lumis, Events  #, ChainEvent 
import sys
#import os 
from os import listdir

print
print 'It\'s time to plot some fun GEN variables'
print

#print'myfunction() = ',myfunction()

# Will contain all histos so you can combine whichever you'd like, such as like variables for different particles
v_histos = [] # [variableindex][particleindex][histogramindex], len(histogramindices) = number of files 

# Plot each variable for each directory of files, then together 
for iv,v in enumerate(vs):
    print 'Plotting variable ', iv, ': ',v[0]

    v_histos.append([]) # add entry for variable iv 
    for i in range(0,nps): # add entry for each particle 
        v_histos[iv].append([]) # list for all plots for given particle 

    # For each directory of files 
    # Instead of a single file, just give its directory 
    for dn,d in enumerate(d):
        # Could make definition to take d, return all of these variables 
        ch = d[0]
        DID = d[1] # file ID
        direc = d[2][0] # full path of directory 
        rd = d[2][1] # direc path with root://cmsxrootd.fnal.gov/ prefix for 'Events' module  
        lc = d[3] # histo line color
        fc = d[4] # histo fill color 

        # Save paths of non-LHE files
        #direc = f[1][0] # full directory path 
        path_ends = [fp for fp in listdir(direc) if 'inLHE' not in fp] 
        paths = []
        for pa in path_ends:
            tmp_path = rd + pa
            paths.append(tmp_path)

        print '  Creating histos for file(s) of type: ',DID 

        # Get chosen particles to plot and number of them 
        pparams = []
        pparams = get_pparams(ch,ptp) #particle parameters 
        #print 'pparams = ',pparams 

        # Create histrograms to be filled in event loop 
        histos = []
        for params in pparams:
            pstring = params[0] # string of particle 
            nump = params[1] # number of this particle per event

            # For now, three cases for number of particles
            # 1,2,4 
            # if there is 1, just one histogram
            # 2, leading and subleading pT histograms 
            # 4, leading, subleading, subsubleading, and subsubsubleading pT histograms 

            # just make ID then run definition 

            if nump == 1:
                ID = 'GEN_' + pstring + '_' + v[0] + '_' + DID # unique histo ID 
                h = TH1F(ID,ID,v[1],v[2],v[3])
                histos.append([[h,ID,pstring]])

            elif nump == 2:
                LID = 'GEN_' + pstring + '_' + 'leading-' + v[0] + '_' + DID # unique histo ID 
                h1 = TH1F(LID,LID,v[1],v[2],v[3])

                SLID = 'GEN_' + pstring + '_' + 'subleading-' + v[0] + '_' + DID # unique histo ID 
                h2 = TH1F(SLID,SLID,v[1],v[2],v[3])
                histos.append([[h1,LID, pstring],[h2,SLID,'sl'+pstring]])
            
            elif nump == 4:
                LID = 'GEN_' + pstring + '_' + 'leading-' + v[0] + '_' + DID # unique histo ID 
                h1 = TH1F(LID,LID,v[1],v[2],v[3])

                SLID = 'GEN_' + pstring + '_' + 'subleading-' + v[0] + '_' + DID # unique histo ID 
                h2 = TH1F(SLID,SLID,v[1],v[2],v[3])

                SSLID = 'GEN_' + pstring + '_' + 'subsubleading-' + v[0] + '_' + DID # unique histo ID 
                h3 = TH1F(SSLID,SSLID,v[1],v[2],v[3])

                SSSLID = 'GEN_' + pstring + '_' + 'subsubsubleading-' + v[0] + '_' + DID # unique histo ID 
                h4 = TH1F(SSSLID,SSSLID,v[1],v[2],v[3])
                #histos.append([h4,SSSLID,pstring])
                histos.append([[h1,LID,pstring],[h2,SLID,'sl'+pstring],[h3,SSLID,'ssl'+pstring],[h4,SSSLID,'sssl'+pstring]])

            else:
                print 'Don\'t have a way to deal with ', nump, ' ', pstring, ' particles'
                print 'Exiting'
                sys.exit()

        #print 'histos = ',histos 

        # Might want to look into eventchain  

        # For each file in directory
        #print 'paths = ',paths 
        for ip,path in enumerate(paths):
            print '    Processing file ', ip, ': ',path 
            events = Events(path) # needs to be file with root prefix 

            # Loop events
            for iev, event in enumerate(events):
                if iev == me: break # Max events 
                event.getByLabel('flashggPrunedGenParticles', genHandle)
                #event.getByLabel('prunedGenParticles', genHandle)
                #events.getByLabel('genParticles', genHandle)
                genParticles = genHandle.product()

                # Fill histograms with current variable 

                # If you want a plot of transverse mass, you need to grab two genparticles
                # for example, grab an electron and neutrino to get transverse mass of W 

                for params in pparams:
                    #print 'params = ',params 
                    particle = params[0]
                    #nparticles = params[1]
                    pdgIDs = params[2]
                    histoentry=params[3]
                    
                    ps = [p for p in genParticles if p.isHardProcess() and abs(p.pdgId()) in pdgIDs]

                    # Get particles in order of pT 

                    # If one particle, just add entry 
                    if len(ps) == 1:
                        val = eval('ps[0].' + v[0] + '()')
                        #print 'val = ',val 
                        histos[histoentry][0][0].Fill(val) 
                        # histoentry based on particle, [0] because only 1 hinfo set b/c only one particle, [0] because this is the histogram entry   
                                 
                    elif len(ps) == 2:
                        ops = []
                        ops = ordptcls(ps)
                        for i,pinfo in enumerate(ops):
                            #print 'pinfo = ',pinfo 
                            val = eval('ops[i][0].' + v[0] + '()') # ops[i] = [genparticle,pt]
                            #print 'val = ',val 
                            histos[histoentry][i][0].Fill(val) 

                    elif len(ps) == 4:
                        ops = []
                        ops = ordptcls(ps)
                        for i,pinfo in ops:
                            print 'pinfo = ',pinfo 
                            val = eval('ops[i][0].' + v[0] + '()') # ops[i] = [genparticle,pt]
                            histos[histoentry][i][0].Fill(val) 

                    else:
                        print 'Not prepared for ', len(ps), ' ', particle, ' particles'
                        print 'Exiting'
                        sys.exit()

                        #ops = order_particles(ps) # particles ordered by pT
                                                             
                    # else:
                    #     print 'I am not prepared for any of the particles in your desired single particles list'
                    #     print 'Please either choose a different desired particle, or write something to deal with your desired particle'
            print 'Finished going through events in file: ', path
            # Check path index 
            if (ip+1 == max_files): break 
               
        # Finished going through all events in directory
        # Save single file histos 
        print 'Finished going through all (or desired number of) files in directory: ',direc
        print '   Saving ', DID, ' histos'

        # Plot each histogram separately 
        for hi,hinfo in enumerate(histos):

            print '      Saving histo ',hi 
            #print '      hinfo = ',hinfo 
            #print '      len(hinfo) = ',len(hinfo)

            # For each hinfo, I want to plot histograms separately. 
            # If there is more than one particle, I want to plot them together 

            # function probably 
            if len(hinfo) == 1:
                print '      Only a leading pt particle'
                # maybe make function for this 
                hist = hinfo[0][0]
                label = hinfo[0][1]
                plabel = hinfo[0][2]
                c1 = TCanvas('c1', 'c1', 800, 600)
                hist.SetDirectory(0)
                hist.SetLineColor(eval(lc)) # eval because they are strings, need to recognize as root objects 
                hist.SetFillColor(eval(fc))
                hist.GetYaxis().SetTitle('Events')
                hist.GetXaxis().SetTitle( v[0] + '_{' + plabel + '}')
                hist.Draw()
                file_path1 = output_Loc + label + '.png'
                file_path2 = output_Loc + label + '.root'
                file_exists1 = False 
                file_exists2 = False 
                file_exists1 = path_exists(file_path1)
                file_exists2 = path_exists(file_path2)
                #file_exists1 = os.path.isfile(file_path1)
                #file_exists2 = os.path.isfile(file_path2)
                if file_exists1:
                    #print 'file_path = ',file_path 
                    rm_path(file_path1)
                    #os.system("rm " + file_path1)
                if file_exists2:
                    #print 'file_path = ',file_path2 
                    #os.system("rm " + file_path2)
                    rm_path(file_path2)
                    #subprocess.Popen("rm " + file_path) # if file already exists, remove it before saving 
                hist.SaveAs(file_path2)
                c1.SaveAs(file_path1)

                # If you want to plot this with a reco file, can do it here
                # Should have function for plotting GEN with RECO. Input arguments are the histos or histo information
                reco_path = '/afs/cern.ch/work/a/atishelm/2FebFlashgglxplus7/CMSSW_10_2_1/src/flashgg/abetest.root'
                vbtp = 'elec1_pt'
                reco_hist = import_reco(reco_path,vbtp)
                #a = import_reco(reco_path,vbtp)
                #print 'a = ',a
                #print 'a.GetEntries() = ',a.GetEntries()
                #reco_h.SetDirectory(0)
                reco_save_title = output_Loc + 'RECO'
                #print'reco_h = ',reco_h
                #custom_draw(a,reco_save_title)
                custom_draw(reco_hist,reco_save_title)

                #print 'reco_h = ',reco_h 
                #reco_h.SetDirectory(0)
                #print 'reco_h = ',reco_h 
                reco_label = 'reco_label'
                reco_plabel = 'reco_plabel'
               # print 'reco_h = ',reco_h 
                #c2 = TCanvas('c2', 'c2', 800, 600)
                #c2.SetDirectory(0)
                #print 'reco_h = ',reco_h 
                #reco_h.Draw()
                
                #reco_h.SaveAs(reco_save_title + '.root')
                #c1.SaveAs(reco_save_title + '.png')
                #c2.SaveAs(reco_save_title + '.png')

                input_histos_info = []
                input_histos_info.append([hist,label,plabel])
                input_histos_info.append([reco_hist,reco_label,reco_plabel])

                var_copy = v[0][:]
                combine_histos(input_histos_info,eval(lc),eval(fc),var_copy) # Saves combined GEN/RECO canvas 
                #combined_title = output_Loc + 'Combined.png'
                #combined_canvas.SaveAs(combined_title)

                
            elif len(hinfo) == 2:
                #print 'hinfo = ',hinfo 
                num = len(hinfo)
                # plot separately and together
                print '      There is a leading and subleading pt particle'
                #print 'hinfo = ',hinfo 
                hists = []
                labels = []
                plabels = []
                for i in range(len(hinfo)):
                    # for single plot 
                    hist = hinfo[i][0]
                    label = hinfo[i][1]
                    plabel = hinfo[i][2]  

                    c1 = TCanvas('c1', 'c1', 800, 600) 
                    hist.SetDirectory(0)
                    #hist.SetLineColor(eval(lc + '+' + str(i*10) ) ) # eval because they are strings, need to recognize as root objects 
                    #hist.SetFillColor(eval(fc + '+' + str(i*10) ) )
                    hist.SetLineColor(eval(lc + '-' + str(i*2) ) ) # eval because they are strings, need to recognize as root objects 
                    hist.SetFillColor(eval(fc + '-' + str(i*2) ) )
                    hist.GetYaxis().SetTitle('Events')
                    hist.GetXaxis().SetTitle( v[0] + '_{' + plabel + '}')



                    # This is where you should import RECO histograms 
                    # Append them 



                    # for combining 
                    hists.append(hist)    
                    labels.append(label)   
                    plabels.append(plabel)

                    hist.Draw()
                    file_path1 = output_Loc + label + '.png'
                    file_path2 = output_Loc + label + '.root'
                    file_exists1 = False 
                    file_exists2 = False 
                    file_exists1 = path_exists(file_path1)
                    file_exists2 = path_exists(file_path2)
                    #file_exists1 = os.path.isfile(file_path1)
                    #file_exists2 = os.path.isfile(file_path2)
                    if file_exists1:
                        #print 'file_path = ',file_path 
                        rm_path(file_path1)
                        #os.system("rm " + file_path1)
                    if file_exists2:
                        #print 'file_path = ',file_path2 
                        rm_path(file_path2)
                        #os.system("rm " + file_path2)
                        #subprocess.Popen("rm " + file_path) # if file already exists, remove it before saving 
                    hist.SaveAs(file_path2)
                    c1.SaveAs(file_path1)
                
                # Combine 
                c0 = TCanvas('c0', 'c0', 800, 600)
                #leg = TLegend(0.6, 0.7, 0.89, 0.89) # might want destructors later to be more memory efficient 
                hists_copy = hists[:]
                labels_copy = labels[:]
                plabels_copy = plabels[:]
                hists_copy.reverse() # want to plot from lowest pt to fit all entries
                labels_copy.reverse() # want to plot from lowest pt to fit all entries
                plabels_copy.reverse() # want to plot from lowest pt to fit all entries

                for hi,h in enumerate(hists_copy):
                    h.SetFillColor(kWhite)

                    if hi == 0:
                        h.SetStats(0)
                        h.Draw('h')
                    
                    if hi > 0:
                        h.SetStats(0)
                        h.GetXaxis().SetTitle( v[0] + '_{all_' + plabel + '}') # Make combined histo have proper x axis 
                        h.Draw('h same')

                leg = TLegend(0.6, 0.7, 0.89, 0.89)
                for hi,h in enumerate(hists_copy):
                    leg.AddEntry(h,labels_copy[hi],'lf') # histo object, ID 
                #leg.SetTextSize(0.02)
                leg.Draw('same')

                file_path1 = output_Loc + 'GEN_' + plabels[0] + '_' + v[0] + '_combined' + '.png' # first plabel should be leading 
                file_exists1 = False 
                file_exists1 = path_exists(file_path1)
                #file_exists1 = os.path.isfile(file_path1)
                if file_exists1:
                    rm_file(file_path1)
                    #os.system("rm " + file_path1)
                c0.SaveAs(file_path1)
                #leg.~TLegend()

    print '   Plotted variable: ', v[0], 'for all files'
    print '   Now combining results for each particle'

    # For a given variable there are len(single_particles) plots 

    # Is it interesting to plot the same variable for different particles? 
    # Should it be separated by particle? 
    #for particle in v_histos[iv] 




    # print 'v_histos[',iv,'] = ',v_histos[iv]
    # for phists in v_histos[iv]:

    #     print 'phists = ',phists
    #     print 'len(phists) = ',len(phists)

    #     if len(phists) == 0: continue # skip 

    #     #print 'phists[2][0] = ',phists[2][0]
    #     c0 = TCanvas('c0', 'c0', 800, 600)
    #     #leg = TLegend(0.6, 0.7, 0.89, 0.89) # might want destructors later to be more memory efficient 

    #     for hi,hinfo in enumerate(phists):
    #         #histo = hinfo[0]
    #         print 'hi = ',hi # directory/files. Need to add both leading and subleading 
    #         #histo = hinfo[hi*3] # leading first 
    #         #title_info = hinfo[hi*3+2] # subleading second 
    #         #histo = hinfo[hi*(-3)+3]
    #         #title_info = hinfo[hi*(-3)+5]
    #         histo1=hinfo[0]
    #         histo2=hinfo[3]
    #         title_info1=hinfo[1]
    #         title_info2=hinfo[4]
    #         #these_hists_[hi].SetFillColor(kWhite)
    #         histo1.SetTitle( title_info1 + v[0] + ' Combined ') # <particle> <variable> combined 
    #         histo2.SetTitle( title_info2 + v[0] + ' Combined ') # <particle> <variable> combined 
    #         histo1.SetFillColor(kWhite)
    #         histo2.SetFillColor(kWhite)

    #         if hi == 0:
    #         #if hi == 1: # draw subleading first so y axis will contain all entries 
    #             #histo.SetStats(0)
    #             #histo.Draw('h')
    #             #print'histo = ',histo
    #             histo1.SetStats(0)
    #             histo1.GetYaxis().SetRangeUser(0,130)
    #             histo1.Draw('h')
    #             print'histo1 = ',histo1
                
    #             histo2.SetStats(0)
    #             histo2.Draw('h same')
    #             print'histo2 = ',histo2
    #         if hi > 0:
    #         #if hi == 0:
    #             #histo.SetStats(0)
    #             #histo.Draw('h same')
    #             #print'histo = ',histo

    #             histo1.SetStats(0)
    #             histo1.Draw('h same')
    #             print'histo1 = ',histo1
    #             histo2.SetStats(0)
    #             histo2.Draw('h same')
    #             print'histo2 = ',histo2

    #     leg = TLegend(0.6, 0.7, 0.89, 0.89)
    #     #j=0
    #     for i in range(0,len(phists)):
    #         for j in range(0,2):
    #             leg.AddEntry(phists[i][j*3],phists[i][j*3+1], 'lf') # histo object, legend entry (ID) # add first and second 
    #         #j=0
    #         # This is going to need to be fixed because it's currently configured for leading-subleading plots
    #         #leg.AddEntry(phists[i][i*3],phists[i][i*3+1], 'lf') # histo object, legend entry (ID)
    #         #leg.AddEntry(phists[i][j],phists[i][j+1], 'lf') # histo object, legend entry (ID) # add first and second 
    #         #leg.AddEntry(phists[i][j*3],phists[i][j*3+1], 'lf') # histo object, legend entry (ID)
    #         #j+=1
    #         #leg.SetTextSize(0.02)
    #     #gStyle.SetOptStat(0) # No Stats Box
    #     leg.Draw('same')

    #     file_path1 = output_Loc + 'GEN_' + hinfo[2] + '_' + v[0] + '_combined' + '.png'
    #     #file_path2 = output_Loc + h[1] + '.root'
    #     file_exists1 = False 
    #     #file_exists2 = False 
    #     file_exists1 = os.path.isfile(file_path1)
    #     #file_exists2 = os.path.isfile(file_path2)
    #     if file_exists1:
    #         os.system("rm " + file_path1)
    #     # if file_exists2:
    #     #     os.system("rm " + file_path2)


    #     c0.SaveAs(file_path1)
    #     #leg.~TLegend()

print 'All variables plotted. My work here is done' 



### extra 



            # # if h contains leading and subleading histos
            # #print 'h = ',h
            # #print 'v_histos = ',v_histos
            # #h[0].SetDirectory(0)
            # c1 = TCanvas('c1', 'c1', 800, 600)
            # hinfo[0].SetDirectory(0)
            # #print 'h[0] = ',h[0]
            # h[0].SetLineColor(lc)
            # h[0].SetFillColor(fc)
            # h[0].GetYaxis().SetTitle('Events')
            # particle_ = h[2]
            # if v[0] == 'invm':
            #     #if particle_ == 'q':
            #         #h[0].GetXaxis().SetTitle( 'm_{' + particle_ + '}')
            #     #else:
            #     h[0].GetXaxis().SetTitle( 'm_{' + particle_ + particle_ + '}')
            # else:
            #     h[0].GetXaxis().SetTitle( v[0] + '_{' + particle_ + '}')
            
            # h[0].Draw()
            # #c1.Update()
            # file_path1 = output_Loc + h[1] + '.png'
            # file_path2 = output_Loc + h[1] + '.root'
            # file_exists1 = False 
            # file_exists2 = False 
            # file_exists1 = os.path.isfile(file_path1)
            # file_exists2 = os.path.isfile(file_path2)
            # if file_exists1:
            #     #print 'file_path = ',file_path 
            #     os.system("rm " + file_path1)
            # if file_exists2:
            #     #print 'file_path = ',file_path2 
            #     os.system("rm " + file_path2)
            #     #subprocess.Popen("rm " + file_path) # if file already exists, remove it before saving 
            # h[0].SaveAs(file_path2)
            # c1.SaveAs(file_path1)

            # #h[0].SetDirectory(0) # This avoids problem later on when introducing legend 
            # #c1.Destructor()
            # #h.SaveAs("histopath.root")
            # #v_histos[iv].append([]) # For each particle
            # #v_histos[iv][hi].append(h)
            # # Check which particle, add to its list of plots for this variable 

            # # This method puts (variable, particle) ('iv','i') plots in v_histos[iv][i]
            # if h[2] == 'H': # Currently [iv][0] associated with H, [iv][1] with W. 
            #     v_histos[iv][0].append(h)
            # elif h[2] == 'W':
            #     v_histos[iv][1].append(h)
            # elif h[2] == 'q':
            #     v_histos[iv][2].append(h)
            # # elif h[2] == 'e':
            # #     v_histos[iv][3].append(h)
            # elif h[2] == 'l':
            #     v_histos[iv][3].append(h)
            # elif h[2] == 'nu':
            #     v_histos[iv][4].append(h)
            # elif h[2] == 'mu':
            #     v_histos[iv][5].append(h)
            # else:
            #     'Can\'t find this plot\'s particle:', h[2] ,' in list of expected particles'
            # If there's a second histogram to save, it's the subleading one
            # This code is terrible right now. This should be a function: plot_h(h[0],h[1],h[2])
            # if len(h) == 6:

            #     this_histo = h[3]
            #     particle_ = h[5]

            #     c1 = TCanvas('c1', 'c1', 800, 600)
            #     this_histo.SetDirectory(0)
            #     #print 'h[0] = ',h[0]
            #     #this_histo.SetLineColor(f[2])
            #     #this_histo.SetFillColor(f[3])
            #     this_histo.SetLineColor(eval(colors[dn])) # kGreen+/-4 -4 then +4 
            #     this_histo.SetFillColor(eval(colors[dn]))
            #     this_histo.GetYaxis().SetTitle('Events')
                
            #     if v[0] == 'invm':
            #         #if particle_ == 'q':
            #             #h[0].GetXaxis().SetTitle( 'm_{' + particle_ + '}')
            #         #else:
            #         this_histo.GetXaxis().SetTitle( 'm_{' + particle_ + particle_ + '}')
            #     else:
            #         this_histo.GetXaxis().SetTitle( v[0] + '_{' + particle_ + '}')
                
            #     this_histo.Draw()
            #     #c1.Update()
            #     file_path1 = output_Loc + h[4] + '.png'
            #     file_path2 = output_Loc + h[4] + '.root'
            #     file_exists1 = False 
            #     file_exists2 = False 
            #     file_exists1 = os.path.isfile(file_path1)
            #     file_exists2 = os.path.isfile(file_path2)
            #     if file_exists1:
            #         #print 'file_path = ',file_path 
            #         os.system("rm " + file_path1)
            #     if file_exists2:
            #         #print 'file_path = ',file_path2 
            #         os.system("rm " + file_path2)
            #         #subprocess.Popen("rm " + file_path) # if file already exists, remove it before saving 
            #     this_histo.SaveAs(file_path2)
            #     c1.SaveAs(file_path1)

            #     #h[0].SetDirectory(0) # This avoids problem later on when introducing legend 
            #     #c1.Destructor()
            #     #h.SaveAs("histopath.root")
            #     #v_histos[iv].append([]) # For each particle
            #     #v_histos[iv][hi].append(h)
            #     # Check which particle, add to its list of plots for this variable 

            #     # # This method puts (variable, particle) ('iv','i') plots in v_histos[iv][i]
            #     # if particle_ == 'H': # Currently [iv][0] associated with H, [iv][1] with W. 
            #     #     v_histos[iv][0].append(h)
            #     # elif particle_ == 'W':
            #     #     v_histos[iv][1].append(h)
            #     # elif particle_ == 'q':
            #     #     v_histos[iv][2].append(h)
            #     # elif particle_ == 'e':
            #     #     v_histos[iv][3].append(h)
            #     # elif particle_ == 'nu':
            #     #     v_histos[iv][4].append(h)
            #     # elif particle_ == 'mu':
            #     #     v_histos[iv][5].append(h)
            #     # else:
            #     #     'Can\'t find this plot\'s particle:', particle_ ,' in list of expected particles'


            # # total number of histos per file = num_particles = nps
            # #if (hi%(nps/nfi) == 0) and (hi != 0): # on the next particle, increment v_histos to keep particle plots separate 
            # #    v_histos[iv].append([]) 
            # #    pn += 1
            # #    v_histos[iv][pn].append(h)
            # #else:
            # #    v_histos[iv][pn].append(h)