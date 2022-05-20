# The purpose of this module is to save useful snippets or commands for potential future use


##-- add color to best event yield 
##-- color max / min label / cell in a grid 

    # for ml in massLabels: # for pair of cutName, HHWWggTag 
    # print'ml:',ml

    # lowestMedianVal, lowestMedianLabel, lowestMedianIndex = 9999999, "", -99
    # highestMedianVal, highestMedianLabel, highestMedianIndex = -9999999, "", -99

    # for gl_i,gl in enumerate(args.GridLabels):
    #     h_grid.GetXaxis().SetBinLabel(gl_i+1,gl)
    #     # file_name = gl + "_limits/HHWWgg_v2-3_2017_" + ml + "_" + gl + "_HHWWgg_qqlnu.root"
    #     # limit = getLimits(file_name)
    #     # m2sig, m1sig, median, p1sig, p2sig = limit[0], limit[1], limit[2], limit[3], limit[4] 
    #     limits = [m2sig, m1sig, median, p1sig, p2sig]
    #     for il,l in enumerate(limits):
    #         h_grid.Fill(gl_i,il,l)
    #     if(median < lowestMedianVal): 
    #         lowestMedianVal = median 
    #         lowestMedianLabel = gl 
    #         lowestMedianIndex = gl_i
    #     if(median > highestMedianVal): 
    #         highestMedianVal = median 
    #         highestMedianLabel = gl 
    #         highestMedianIndex = gl_i                    

    # lowestLabel = "#color[3]{%s}"%(lowestMedianLabel) # color label with lowest median limit 
    # highestLabel = "#color[2]{%s}"%(highestMedianLabel) # color label with lowest median limit 

    # h_grid.GetXaxis().SetBinLabel(lowestMedianIndex+1,lowestLabel)
    # h_grid.GetXaxis().SetBinLabel(highestMedianIndex+1,highestLabel)

    # h_grid.SetMarkerSize(1.8)
    # label = TLatex()
    # label.SetNDC()
    # label.SetTextAngle(0)
    # label.SetTextColor(kBlack)
    # label.SetTextFont(42)
    # label.SetTextSize(0.045)
    # label.SetLineWidth(2)

    # outNamepng = "%s/%s_grid.png"%(ol_,ml)
    # outNamepdf = "%s/%s_grid.pdf"%(ol_,ml)
    # outNamepng = "%s/EventsTable_%s.png"%(ol_,selections)
    # outNamepdf = "%s/EventsTable_%s.pdf"%(ol_,selections)    

## -- old data / mc code

    ##-- SB: Produce table with number of events for each MC, total MC, and data 
    # CreateYieldsTable(region_,cutName,)
    # CreateYieldsTables(cutBatchTag_pairs, dataNevents_list, MC_names, MC_Nevents_lists, MC_Nevents_noweight_lists,
    #                     ol_, S_list, args_.removeBackgroundYields, B_lists, SidebandSF)







    # ##-- For each data file (can just be one)
    # for dF_ in dataFiles_:
    #     cutBatchTag_pairs = [] 
    #     dataNevents_list = []
    #     MC_names = [] 
    #     MC_Nevents_lists = []
    #     MC_Nevents_noweight_lists = []
    #     S_list = [] ##--assumes one signal!
    #     B_lists = [] # list of number of background events in the signal region (using MC)

    #     ##-- For each category (Ex: HHWWggTag_0, HHWWggTag_1, HHWWggTag_2, combined)
    #     for itag,HHWWggTag in enumerate(HHWWggTags):
    #         if(args_.verbose): 
    #             print"tag:",HHWWggTag                      
    #         dPath = "%s/%s"%(dataDirec_,dF_)
    #         dFile = TFile.Open(dPath)
    #         if(HHWWggTag=="combined"):
    #             ch = TChain('%sData_13TeV_HHWWggTag_0'%(args_.prefix))
    #             ch.Add("%s/%sData_13TeV_HHWWggTag_0"%(dPath,args_.prefix))
    #             ch.Add("%s/%sData_13TeV_HHWWggTag_1"%(dPath,args_.prefix))
    #             ch.Add("%s/%sData_13TeV_HHWWggTag_2"%(dPath,args_.prefix))
    #         else:
    #             ch = TChain('%sData_13TeV_%s'%(args_.prefix,HHWWggTag))
    #             ch.Add(dPath)
    #         BLIND_CUT = "(CMS_hgg_mass < 115 || CMS_hgg_mass > 135)"
    #         SR_CUT = "(CMS_hgg_mass >=115 && CMS_hgg_mass <= 135)"
    #         MC_WEIGHT = "1*weight"
    #         ZERO_CUT = "ZERO_CUT"
    #         MC_CUT = "%s*(%s)*(%s)"%(MC_WEIGHT,BLIND_CUT,ZERO_CUT)
    #         DATA_CUT = "%s*(%s)"%(BLIND_CUT,ZERO_CUT)  
    #         SIGNAL_CUT = "%s*(%s)"%(MC_WEIGHT,ZERO_CUT) # no blind cut on signal
 
    #         # For S and B computations
    #         S_CUT = "%s*(%s)*(%s)"%(MC_WEIGHT,SR_CUT,ZERO_CUT) 
    #         B_CUT = "%s*(%s)*(%s)"%(MC_WEIGHT,SR_CUT,ZERO_CUT)

	#         ##-- For each cut 
    #         for ic,cut in enumerate(cuts):                
    #             #if(args_.verbose): print"Plotting with selection:",cut                  
    #             cutName = cutNames[ic]
    #             cutBatchTag = "%s_%s"%(cutName,HHWWggTag)
    #             cutBatchTag_pairs.append(cutBatchTag)
    #             dataNevents = -999
    #             these_MC_Nevents = []
    #             these_MC_Nevents_noweights = [] 
    #             B_list = []
    #             outputFolder = "%s/%s"%(ol_,cutName)
    #             if(not os.path.exists(outputFolder)):
    #                 os.system('mkdir %s'%(outputFolder))
    #                 os.system('cp %s/index.php %s'%(ol_,outputFolder))
    #             MC_CUT += "*(%s)"%(cut)
    #             DATA_CUT += "*(%s)"%(cut)
    #             SIGNAL_CUT += "*(%s)"%(cut)
    #             S_CUT += "*(%s)"%(cut)
    #             B_CUT += "*(%s)"%(cut)

    #             SIGNAL_CUT = SIGNAL_CUT.replace("goodJets","AtLeast2GoodJets")
    #             S_CUT = S_CUT.replace("goodJets","AtLeast2GoodJets")
                
    #             ##-- For each variable 
    #             for iv,v in enumerate(Variables): 
    #                 if(args_.VarBatch == "Loose"): varTitle = varNames[iv]
    #                 else: varTitle = GetVarTitle(v)
    #                 if(args_.verbose): print"Plotting variable:",varTitle

    #                 MC_CUT = MC_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
    #                 DATA_CUT = DATA_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
    #                 SIGNAL_CUT = SIGNAL_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
    #                 MC_CUT_NOWEIGHT = MC_WEIGHT.replace(MC_WEIGHT,"(1)")      
    #                 S_CUT = S_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
    #                 B_CUT = B_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
    #                 B_CUT_NOWEIGHT = B_CUT.replace(MC_WEIGHT,"(1)")
    #                 S_CUT_NOWEIGHT = SIGNAL_CUT.replace(MC_WEIGHT,"(1)")

    #                 # if(args_.verbose):
    #                 #   print
    #                 #   print"SIGNAL_CUT:",SIGNAL_CUT
    #                 #   print"S_CUT:",S_CUT 
    #                 #   print"MC_CUT:",MC_CUT
    #                 #   print"B_CUT:",B_CUT 
    #                 #   print 

    #                 if(varTitle == "weight"): MC_CUT = MC_CUT.replace(MC_WEIGHT,"(1)") # if you want to plot the "weight" variable, you should not scale it by weight!             
                    
    #                 ##-- Can add printing of cuts to debug 
    #                 # if(args_.verbose): 
    #                     # print"MC_CUT:",MC_CUT         
    #                     # print"DATA_CUT:",DATA_CUT
    #                 ##-- 

    #                 legend = TLegend(0.55,0.65,0.89,0.89)
    #                 legend.SetTextSize(0.025)
    #                 legend.SetBorderSize(0)
    #                 legend.SetFillStyle(0)
    #                 xbins, xmin, xmax = GetBins(varTitle)

    #                 ##-- Fill histogram with data  
    #                 Data_h_tmp = TH1F('Data_h_tmp',varTitle,xbins,xmin,xmax)
    #                 Data_h_tmp.SetTitle("%s"%(varTitle))
    #                 Data_h_tmp.SetMarkerStyle(8)
    #                 exec('ch.Draw("%s >> Data_h_tmp","%s")'%(v,DATA_CUT))

    #                 ##-- Only save number of events for first variable. Should be same for all because same cut is used 
    #                 if(iv == 0): 
    #                     dataNevents = Data_h_tmp.GetEntries()
    #                     dataNevents_list.append(dataNevents)
    #                 # print"Blinded Data numEvents:",Data_h_tmp.GetEntries()                    
    #                 DataHist = Data_h_tmp.Clone("DataHist")
    #                 DataHist.SetDirectory(0)
    #                 legend.AddEntry(DataHist,"Data","P")

    #                 ##-- Get histograms with MC Backgrounds 
    #                 bkgStack = THStack("bkgStack","bkgStack")
    #                 histos = []
    #                 histCategories = [] 
    #                 for i,mcF_ in enumerate(mcFiles_):
    #                     mcPath = "%s/%s"%(mcDirec_,mcF_)
    #                     mcFile = TFile.Open(mcPath)
    #                     treeName = GetMCTreeName(mcF_)
    #                     MC_Category = GetMCCategory(mcF_)
    #                     if(args_.verbose): 
    #                         #print"Background File:",mcPath
    #                         print"Background:",MC_Category
    #                         # print"file:",mcPath  

    #                     ##-- If noQCD set to true, skip QCD 
    #                     if((MC_Category == "QCD") and (args_.noQCD)): 
    #                         print"Skipping QCD"
    #                         these_MC_Nevents_noweights.append(0) # Set yields to 0 for table 
    #                         these_MC_Nevents.append(0) # Set yields to 0 for table
    #                         B_list.append(0) 
    #                         if(itag == 0 and ic == 0 and iv == 0): 
    #                             MCname = GetMCName(mcF_)
    #                             MC_names.append(MCname) # Skipping QCD, but still save name for yields because tag_2 may not be 0                           
    #                         continue 

    #                     ##-- Define TChain based on categories 
    #                     if(HHWWggTag=="combined"):
    #                         mc_ch = TChain('%s%s_13TeV_HHWWggTag_0'%(args_.prefix,treeName))
    #                         mc_ch.Add("%s/%s%s_13TeV_HHWWggTag_0"%(mcPath,args_.prefix,treeName))
    #                         mc_ch.Add("%s/%s%s_13TeV_HHWWggTag_1"%(mcPath,args_.prefix,treeName))
    #                         mc_ch.Add("%s/%s%s_13TeV_HHWWggTag_2"%(mcPath,args_.prefix,treeName))
    #                         #mc_ch.Add("%s/%s%s_13TeV_HHWWggTag_3"%(mcPath,args_.prefix,treeName))
    #                         #mc_ch.Add("%s/%s%s_13TeV_HHWWggTag_4"%(mcPath,args_.prefix,treeName))
    #                     else:
    #                         mc_ch = TChain('%s%s_13TeV_%s'%(args_.prefix,treeName,HHWWggTag))
    #                         mc_ch.Add(mcPath)
    #                     xbins, xmin, xmax = GetBins(varTitle)
    #                     exec("MC_h_tmp_%s = TH1F('MC_h_tmp_%s',varTitle,xbins,xmin,xmax)"%(i,i))
    #                     exec("MC_h_tmp_noweight_%s = TH1F('MC_h_tmp_noweight_%s',varTitle,xbins,xmin,xmax)"%(i,i))
    #                     exec("B_h_%s = TH1F('B_h_%s',varTitle,xbins,xmin,xmax)"%(i,i)) # histogram specifically for computing B in signal region
    #                     exec("B_h_noweight_%s = TH1F('B_h_noweight_%s',varTitle,xbins,xmin,xmax)"%(i,i)) # histogram specifically for computing B in signal region
                        
    #                     thisHist = eval("MC_h_tmp_%s"%(i))
    #                     mcColor = GetMCColor(MC_Category)

    #                     ##-- If GJet or QCD sample, need to remove prompt-prompt events 
    #                     if(MC_Category == "GJet" or MC_Category == "QCD"):
    #                         if(args_.verbose): print"Remove prompt-prompt"
    #                         removePromptPromptCut = "(!((Leading_Photon_genMatchType == 1) && (Subleading_Photon_genMatchType == 1)))" # selection: remove events where both photons are prompt
    #                         original_B_CUT = "%s"%(B_CUT)
    #                         original_MC_CUT = "%s"%(MC_CUT)
    #                         this_MC_CUT = "%s*(%s)"%(original_MC_CUT,removePromptPromptCut)
    #                         this_B_CUT = "%s*(%s)"%(original_B_CUT,removePromptPromptCut)
    #                         this_MC_CUT_NOWEIGHT = this_MC_CUT.replace(MC_WEIGHT,"(1)")
    #                         this_B_CUT_NOWEIGHT = this_B_CUT.replace(MC_WEIGHT,"(1)")

    #                     eval("MC_h_tmp_%s.SetFillColor(eval(mcColor))"%(i))
    #                     eval("MC_h_tmp_%s.SetLineColor(eval(mcColor))"%(i))

    #                     if(MC_Category == "GJet" or MC_Category == "QCD"): 
    #                         exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,this_MC_CUT))
    #                         exec('mc_ch.Draw("%s >> B_h_%s","%s")'%(v,i,this_B_CUT))
    #                     else: 
    #                         exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,MC_CUT))    
    #                         exec('mc_ch.Draw("%s >> B_h_%s","%s")'%(v,i,B_CUT))                                       

    #                     eval("MC_h_tmp_%s.Scale(float(args_.Lumi))"%(i))
    #                     eval("B_h_%s.Scale(float(args_.Lumi))"%(i))

    #                     ##-- MC reweighting for HHWWgg backgrounds (turned off for now)
    #                     # reWeightVals = ReWeightMC(mcF_)
    #                     # doReWeight, reWeightScale = reWeightVals[0], reWeightVals[1]
    #                     # print"doReWeight,reWeightScale:",doReWeight, reWeightScale
    #                     # if(doReWeight): 
    #                     #     if(args_.verbose):
    #                     #         print"ReWeighting MC"
    #                     #         print"With scale: ",reWeightScale
    #                     #     eval("MC_h_tmp_%s.Scale(float(reWeightScale))"%(i))
    #                     ## 

    #                     ##-- Only save for 1st variable. Should be same for all variables
    #                     if(iv == 0): 
    #                         if(MC_Category == "GJet" or MC_Category == "QCD" ): 
    #                           exec('mc_ch.Draw("%s >> MC_h_tmp_noweight_%s","%s")'%(v,i,this_MC_CUT_NOWEIGHT))
    #                           exec('mc_ch.Draw("%s >> B_h_noweight_%s","%s")'%(v,i,this_B_CUT_NOWEIGHT))
    #                         else: 
    #                           exec('mc_ch.Draw("%s >> MC_h_tmp_noweight_%s","%s")'%(v,i,MC_CUT_NOWEIGHT))
    #                           exec('mc_ch.Draw("%s >> B_h_noweight_%s","%s")'%(v,i,B_CUT_NOWEIGHT))
    #                         these_MC_Nevents_noweights.append(eval("MC_h_tmp_noweight_%s.Integral()"%(i)))   
    #                         these_MC_Nevents.append(eval("MC_h_tmp_%s.Integral()"%(i)))
    #                         B = eval("B_h_%s.Integral()"%(i))
    #                         B_noweight = eval("B_h_noweight_%s.Integral()"%(i))
    #                         # print "B = ",B
    #                         # print "B_noweight ",B_noweight
    #                         B_list.append(B)                            

    #                         ##-- Only need to get MC names once 
    #                         if(itag == 0 and ic == 0 and iv == 0): 
    #                             MCname = GetMCName(mcF_)
    #                             MC_names.append(MCname) # get shorter MC name here

    #                     newHist = thisHist.Clone("newHist")
    #                     ##-- Set title based on treeName 
    #                     newHist.SetTitle(MC_Category)
    #                     newHist.GetXaxis().SetTitle(mcF_)
    #                     newHist.SetDirectory(0)
    #                     histos.append(newHist)
    #                     histCategories.append(MC_Category)

    #                 sig_histos = []
    #                 sig_histCategories = []             

    #                 ##-- Add Signal to plots 
    #                 for i,sigF_ in enumerate(signalFiles_):
    #                     sigPath = "%s/%s"%(signalDirec_,sigF_)
    #                     sigFile = TFile.Open(sigPath)
    #                     treeName = GetMCTreeName(sigF_)
    #                     MC_Category = GetMCCategory(sigF_)
    #                     if(args_.verbose):
    #                         # print"Signal File:",sigPath 
    #                         print"Signal:",MC_Category
    #                     if(HHWWggTag=="combined"):
    #                         mc_ch = TChain('%s%s_13TeV_HHWWggTag_0'%(args_.prefix,treeName))
    #                         mc_ch.Add("%s/%s%s_13TeV_HHWWggTag_0"%(sigPath,args_.prefix,treeName))
    #                         mc_ch.Add("%s/%s%s_13TeV_HHWWggTag_1"%(sigPath,args_.prefix,treeName))
    #                         mc_ch.Add("%s/%s%s_13TeV_HHWWggTag_2"%(sigPath,args_.prefix,treeName))
    #                         mc_ch.Add("%s/%s%s_13TeV_HHWWggTag_3"%(sigPath,args_.prefix,treeName))
    #                         mc_ch.Add("%s/%s%s_13TeV_HHWWggTag_4"%(sigPath,args_.prefix,treeName))
    #                     else:
    #                         mc_ch = TChain('%s%s_13TeV_%s'%(args_.prefix,treeName,HHWWggTag))
    #                         mc_ch.Add(sigPath)
    #                     xbins, xmin, xmax = GetBins(varTitle)
    #                     exec("MC_h_tmp_%s = TH1F('MC_h_tmp_%s',v,xbins,xmin,xmax)"%(i,i))
    #                     exec("S_h_%s = TH1F('S_h_%s',v,xbins,xmin,xmax)"%(i,i)) # Specifically for computing S in signal region 
    #                     thisHist = eval("MC_h_tmp_%s"%(i))
    #                     mcColor = GetMCColor(MC_Category) 
    #                     ##-- Style options for signal to distinguish from Data, Background 
    #                     # eval("MC_h_tmp_%s.SetFillColor(eval(mcColor))"%(i))
    #                     # eval("MC_h_tmp_%s.SetFillStyle(3004)"%(i))
    #                     ##-- 
	# 		            #S_CUT = "weight*(CMS_hgg_mass >= 115 && CMS_hgg_mass <= 135)"
    #                     eval("MC_h_tmp_%s.SetFillColorAlpha(eval(mcColor),0.1)"%(i))
    #                     eval("MC_h_tmp_%s.SetLineColor(eval(mcColor))"%(i))
    #                     exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,SIGNAL_CUT))
    #                     eval("MC_h_tmp_%s.Scale(float(args_.Lumi))"%(i)) # should scale to luminosity by default 
    #                     SigXS_Scale = GetXScale("HHWWgg_SM") # how to scale the XS which is by default in flashgg 1fb
    #                     if(args_.verbose): print"SigXS_Scale: ",SigXS_Scale
    #                     eval("MC_h_tmp_%s.Scale(float(SigXS_Scale))"%(i)) # should scale to luminosity by default
    #                     eval("mc_ch.Draw('%s >> S_h_%s','%s')"%(v,i,S_CUT))
    #                     eval("S_h_%s.Scale(float(args_.Lumi))"%(i))
    #                     eval("S_h_%s.Scale(float(SigXS_Scale))"%(i)) 
    #                     S = eval("S_h_%s.Integral()"%(i)) # want number of signal events in the signal region: 115 -> 135 GeV 
    #                     ##-- Only save for 1st variable. Should be same for all variables
    #                     if(iv == 0):    
    #                         # print("S = ",S)                     
    #                         S_list.append(S) ##-- assumes one signal model! 

    #                     newHist = thisHist.Clone("newHist")

    #                     ##-- Set title based on treeName 
    #                     newHist.SetTitle(MC_Category)
    #                     newHist.GetXaxis().SetTitle(sigF_)
    #                     newHist.SetLineStyle(1)
    #                     newHist.SetLineWidth(5)

    #                     newHist.SetDirectory(0)
    #                     sig_histos.append(newHist)
    #                     sig_histCategories.append(MC_Category)              
                        
    #                 MC_AddedtoLegend = {
    #                     "QCD" : 0,
    #                     "SMhgg" : 0,
    #                     "GJet" : 0,
    #                     "DiPhoJets" : 0,
    #                     "DiPhoJetsBox" : 0,
    #                     # "W1JetsToLNu" : 0,
    #                     # "W2JetsToLNu" : 0,
    #                     # "W3JetsToLNu" : 0,
    #                     # "W4JetsToLNu" : 0,
    #                     "WJets" : 0,
    #                     "WW" : 0,
    #                     "tt" : 0,
    #                     "DY" : 0,
    #                     "WGGJets" : 0,
    #                     "WGJJ" : 0,
    #                     "ttW" : 0
    #                 }

    #                 Signals_AddedtoLegend = {
    #                     "HHWWgg_SM" : 0
    #                 }

    #                 ##-- Order histograms by MC category 
    #                 orderedHistos = OrderHistos(histos,histCategories)
    #                 sig_orderedHistos = OrderHistos(sig_histos,sig_histCategories)

    #                 ##-- Add backgrounds to background stack 
    #                 for h in orderedHistos:
    #                     bkgStack.Add(h,'hist')
    #                     bkgName = h.GetTitle()
    #                     added = MC_AddedtoLegend[bkgName]
    #                     if(added): continue 
    #                     else:
    #                         legend.AddEntry(h,bkgName,"F")
    #                         MC_AddedtoLegend[bkgName] = 1


    #                 ##-- By default draw background save background contributions. Later delete if not wanted 
    #                 outName = "%s/BackgroundsTest_%s.png"%(outputFolder,HHWWggTag)
    #                 bkgOutName = "%s/BackgroundsPADS_%s_%s.png"%(outputFolder,varTitle,HHWWggTag)
    #                 SimpleDrawHisto(bkgStack,"PADS",bkgOutName,varTitle)
    #                 bkgOutName = bkgOutName.replace(".png",".pdf")
    #                 SimpleDrawHisto(bkgStack,"PADS",bkgOutName,varTitle)  

    #                 ##-- Add text box with selection type 
    #                 offset = 0
    #                 selText = TLatex(0.129,0.85,cutName)
    #                 selText.SetNDC(1)
    #                 selText.SetTextSize(0.04)   
    #                 CatText = TLatex(0.129,0.8,HHWWggTag)
    #                 CatText.SetNDC(1)
    #                 CatText.SetTextSize(0.04)                                                 
    #                 stackSum = bkgStack.GetStack().Last() #->Draw(); # for computing ratio 
    #                 stackSum.Sumw2() 
    #                 stackSum.SetLineColor(kBlack)
    #                 stackSum.SetLineStyle(7) # to distinguish from data uncertainty 
    #                 DataHist.SetLineColor(kBlack)
    #                 DataHist.Sumw2()
    #                 xTitle = GetXaxisTitle(varTitle)
    #                 DataHist.GetXaxis().SetTitle(xTitle)
    #                 if(args_.log): 
    #                     if(args_.verbose): print "Setting histogram minimums"
    #                     DataHist.SetMinimum(0.0001)
    #                     stackSum.SetMinimum(0.0001)
    #                     bkgStack.SetMinimum(0.0001)

    #                 ##-- Optional: Scale Backgrounds to SF: Data sidebands sum / Background sidebands sum
    #                 SidebandSF = 1 
    #                 if(args_.SidebandScale):
    #                     data_sidebands_sum = DataHist.Integral() ##-- data hist is already in sidebands only 
    #                     background_sidebands_sum = stackSum.Integral()
    #                     if(background_sidebands_sum > 0): SidebandSF = float(data_sidebands_sum / background_sidebands_sum)
    #                     else: 
    #                         print "background sidebands sum <= 0. Setting sideband scale factor to 1"
    #                         SidebandSF = 1
    #                     print "data sum in sidebands:",data_sidebands_sum
    #                     print "backgrounds sum in sidebands:",background_sidebands_sum
    #                     print "Sideband scale factor:",SidebandSF
    #                     for background in bkgStack.GetStack():
    #                         background.Scale(SidebandSF)
    #                     stackSum = bkgStack.GetStack().Last() #->Draw(); # for computing ratio 
    #                     # stackSum.Scale(SidebandSF)                        
	 	        
    #                 ##-- Compute chi squared 
    #                 chi2 = GetChiSquared(DataHist,stackSum)
    #                 # print"chi2 = ",chi2 
    #                 chi2Text = TLatex(0.129,0.75,"#Chi^{2} = %.5g"%(chi2))       
    #                 chi2Text.SetNDC(1)
    #                 chi2Text.SetTextSize(0.04)                         
    #                 ##-- Define ratio plot for computing Data / MC ratio 
    #                 rp = TRatioPlot(DataHist,stackSum)
    #                 rp.SetH1DrawOpt("P")
    #                 rp.SetH2DrawOpt("hist")
    #                 # rp.SetGraphDrawOpt("PE2")
    #                 dMax = DataHist.GetMaximum()
    #                 bMax = stackSum.GetMaximum()

    #                 maxHeight = max(dMax,bMax) 

    #                 ##-- Create the entire picture: Combine Data, MC, Data / MC ratio and signal in one plot 

    #                 for fileType in ["pdf"]:
    #                     gStyle.SetErrorX(0.0001)
    #                     # varTitle = GetVarTitle(v)
    #                     outName = "%s/DataMC_%s_%s.%s"%(outputFolder,varTitle,HHWWggTag,fileType)
    #                     if(args_.log): outName = "%s/DataMC_%s_%s_log.%s"%(outputFolder,varTitle,HHWWggTag,fileType)
    #                     else: outName = "%s/DataMC_%s_%s_nonLog.%s"%(outputFolder,varTitle,HHWWggTag,fileType)                        
    #                     DataMCRatio_c = TCanvas("DataMCRatio_c","DataMCRatio_c",600,800)
    #                     rp.Draw("nogrid")
    #                     rp.GetLowYaxis().SetNdivisions(5)
    #                     DataMCRatio_c.Update()

    #                     ratioGraph = rp.GetCalculationOutputGraph()
    #                     ratioGraph.SetMarkerStyle(8)
    #                     ratioGraph.SetMarkerSize(0.5)

    #                     # rp.SetGraphDrawOpt("EP")
    #                     # rp.SetGraphDrawOpt("EPZ2")
    #                     # rp.GetLowerRefYaxis().SetTitle("Data / MC")

    #                     rp.GetUpperRefYaxis().SetTitle("Entries")   
    #                     rp.GetLowerRefYaxis().SetTitle("Data / MC")
    #                     rp.GetLowerPad().Update()
    #                     if(args_.log): rp.GetUpperRefYaxis().SetRangeUser(0.1,maxHeight*100.)   
    #                     else: rp.GetUpperRefYaxis().SetRangeUser(0,maxHeight*1.4) # to make room for plot text 
                                
    #                     UpperPad = rp.GetUpperPad()
    #                     UpperPad.cd()
    #                     bkgStack.Draw("same")
    #                     stackSum.Draw("sameE")
    #                     DataHist.Draw("samePE")
    #                     for sig_hist in sig_histos:
    #                         sigMax = sig_hist.GetMaximum()
    #                         if sigMax == 0: sigMax = 1 

    #                         ##-- No user input signal scale 
    #                         if(args_.SigScale == -999): 
    #                             sigScale = (float(maxHeight)/10.) / float(sigMax) # in order to scale signal to 10th of max of plot 
    #                             sig_hist.Scale(sigScale)  

    #                         ##-- User input signal scale 
    #                         else:
    #                             if(args_.verbose): print"user sig scale:",args_.SigScale
    #                             sigScale = args_.SigScale
    #                             sig_hist.Scale(sigScale) 
                                                        
    #                         for sig_h in sig_orderedHistos:
    #                             # sigName = "%s X %d"%(sig_h.GetTitle(),sigScale)
    #                             sigName = sig_h.GetTitle()
    #                             added = Signals_AddedtoLegend[sigName]
    #                             if(added): continue 
    #                             else:
    #                                 legend.AddEntry(sig_h,"%s * %.5g"%(sig_h.GetTitle(),sigScale),"FL")
    #                                 Signals_AddedtoLegend[sigName]                            
    #                         sig_hist.Draw("samehist")
    #                     legend.Draw("same")
    #                     selText.Draw("same")
    #                     CatText.Draw("same")
    #                     chi2Text.Draw("same")
    #                     rp.GetLowerRefGraph().SetMinimum(0.5)
    #                     rp.GetLowerRefGraph().SetMaximum(1.5)     
    #                     Npoints = rp.GetLowerRefGraph().GetN()
    #                     for ip in range(0,Npoints):
    #                         rp.GetLowerRefGraph().SetPointEXhigh(ip,0)  
    #                         rp.GetLowerRefGraph().SetPointEXlow(ip,0)  
    #                     if(args_.log): 
    #                         UpperPad.SetLogy()
    #                         UpperPad.Update() 
    #                     rp.GetLowerPad().cd()
    #                     lowerPad = rp.GetLowerPad()
    #                     rp.GetLowerRefYaxis().SetTitle("Data / MC")
    #                     lineAtOne = TLine(lowerPad.GetUxmin(),1,lowerPad.GetUxmax(),1)
    #                     lineAtOne.SetLineStyle(3)
    #                     lineAtOne.Draw("same")
    #                     rp.GetLowerPad().Update()                        
    #                     DataMCRatio_c.Update()                
    #                     DataMCRatio_c.SaveAs(outName) 
    #                     outName = outName.replace(".pdf",".png")                    
    #                     DataMCRatio_c.SaveAs(outName)                     
    #                 if(not args_.drawPads):
    #                     bkgOutName = "%s/BackgroundsPADS_%s_%s.png"%(outputFolder,varTitle,HHWWggTag)
    #                     os.system('rm %s'%(bkgOutName))
    #                     bkgOutName = bkgOutName.replace(".png",".pdf")
    #                     os.system('rm %s'%(bkgOutName))
    #                 MC_CUT = MC_CUT.replace("(%s != 0) && (%s != -999)"%(v,v),"ZERO_CUT")
    #                 DATA_CUT = DATA_CUT.replace("(%s != 0) && (%s != -999)"%(v,v),"ZERO_CUT")

    #                 # chi2 value for each end of this loop (finished tag,cut,variable pair)

    #             ## -- append for every cut/tag combination
    #             B_lists.append(B_list) 
    #             MC_Nevents_lists.append(these_MC_Nevents)
    #             MC_Nevents_noweight_lists.append(these_MC_Nevents_noweights)  

    #     ##-- Produce table with number of events for each MC, total MC, and data 
    #     CreateYieldsTables(cutBatchTag_pairs, dataNevents_list, MC_names, MC_Nevents_lists, MC_Nevents_noweight_lists,
    #                        ol_, S_list, args_.removeBackgroundYields, B_lists, SidebandSF)
    #     # CreateChiSquaredTable(variables,cutBatch,chiSquaredVals) # Want chi squared z value. x: variable, y: cut batch
