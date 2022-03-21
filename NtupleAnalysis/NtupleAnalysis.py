#########################################################################################################################################################################################################
# Abraham Tishelman-Charny
# 13 May 2020
#
# The purpose of this module is to analyze HHWWgg ntuples. The current options are:
# - Cut flow efficiencies
# - Data / MC comparison
#
# Example Usage:
#
# ##-- Efficiency Analysis
# python NtupleAnalysis.py --Efficiency --folder HHWWgg_v2-4_NMSSM_CutFlow_Hadded/ --note NMSSM_Test --NMSSM --SumTags
# python NtupleAnalysis.py --Efficiency --folder HHWWgg_v2-4_CutFLow_Hadded/ --note EFT_Test --EFT --SumTags
#
# ##-- Efficiency Ratio
# python NtupleAnalysis.py --Efficiency --folders HHWWgg_v2-3_Trees_Hadded_some/,HHWWgg_v2-6_Trees_Hadded/ --campaigns HHWWgg_v2-3,HHWWgg_v2-6 --massPoints X1000 --Res --ratio
#
# ##-- Data / MC Analysis
# python NtupleAnalysis.py --DataMC --ol /eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/January2021-Production/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ --dataFile /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/Data_2017_HHWWggTag_0_MoreVars.root --signalFile /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root --bkgDirec /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ --VarBatch DNN --CutsType TrainingSelections --Lumi 41.5 --verbose --SigScale 1 --SB  --DNNbinWidth 0.1 --log --ratioMin 0.5 --ratioMax 1.5 --SidebandScale
# python NtupleAnalysis.py --DataMC --ol /eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/January2021-Production/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ --dataFile /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/Data_2017_HHWWggTag_0_MoreVars.root --signalFile /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root --bkgDirec /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ --VarBatch TrainingVariables --CutsType testingSelections --Lumi 41.5 --verbose --SigScale 1 --SB  --DNNbinWidth 0.0333 --log --ratioMin 0.1 --ratioMax 2 --SidebandScale
# python NtupleAnalysis.py --DataMC --ol /eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/January2021-Production/WithHggTraining_withSidebandScaling_ANv3/ --dataFile /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_withHgg_BalanceYields_allBkgs_LOSignals_noPtOverM/Data_2017_HHWWggTag_0_MoreVars.root --signalFile /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_noHgg_BalanceYields_allBkgs_oddSignal_v3/GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root --bkgDirec /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_withHgg_BalanceYields_allBkgs_LOSignals_noPtOverM/ --VarBatch TrainingVariables --CutsType testingSelections --Lumi 41.5 --verbose --SigScale 1 --SB  --DNNbinWidth 0.0333 --log --ratioMin 0.1 --ratioMax 2 --SidebandScale --log
# python NtupleAnalysis.py --DataMC --ol /eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/January2021-Production/WithHggTraining_withSidebandScaling_ANv3/ --dataFile /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_withHgg_BalanceYields_allBkgs_LOSignals_noPtOverM/Data_2017_HHWWggTag_0_MoreVars.root --signalFile /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_noHgg_BalanceYields_allBkgs_oddSignal_v3/GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root --bkgDirec /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_withHgg_BalanceYields_allBkgs_LOSignals_noPtOverM/ --VarBatch TrainingVariables --CutsType TrainingSelections --Lumi 41.5 --verbose --SigScale 1 --SB  --DNNbinWidth 0.0333 --log --ratioMin 0.1 --ratioMax 2 --SidebandScale --log 
# python NtupleAnalysis.py --DataMC --ol /eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/January2021-Production/WithHggTraining_withSidebandScaling/ --dataFile /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_withHgg_BalanceYields_allBkgs_LOSignals_noPtOverM/Data_2017_HHWWggTag_0_MoreVars.root --signalFile /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_noHgg_BalanceYields_allBkgs_oddSignal_v3/GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root --bkgDirec /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_withHgg_BalanceYields_allBkgs_LOSignals_noPtOverM/ --VarBatch TrainingVariables --CutsType TrainingSelections --Lumi 41.5 --verbose --SigScale 1 --SB  --DNNbinWidth 0.0333 --log --ratioMin 0.1 --ratioMax 5 --SidebandScale
# python NtupleAnalysis.py --DataMC --ol /eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/January2021-Production/ --dataFile /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_withHgg_BalanceYields_allBkgs_LOSignals_noPtOverM/Data_2017_HHWWggTag_0_MoreVars.root --signalFile /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_noHgg_BalanceYields_allBkgs_oddSignal_v3/GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root --bkgDirec /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_withHgg_BalanceYields_allBkgs_LOSignals_noPtOverM/ --VarBatch RestOfTrainingVars --CutsType TrainingSelections --Lumi 41.5 --verbose --SigScale 1 --SB  --DNNbinWidth 0.0333 --SidebandScale --log 
# python NtupleAnalysis.py --DataMC --ol /eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/January2021-Production/ --dataFile /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_withHgg_BalanceYields_allBkgs_LOSignals_noPtOverM/Data_2017_HHWWggTag_0_MoreVars.root --signalFile /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_noHgg_BalanceYields_allBkgs_oddSignal_v3/GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_MoreVars.root --bkgDirec /eos/user/b/bmarzocc/HHWWgg/January_2021_Production/HHWWyyDNN_binary_withHgg_BalanceYields_allBkgs_LOSignals_noPtOverM/ --VarBatch Jet --CutsType TrainingSelections --Lumi 41.5 --verbose --SigScale 1 --SB  --DNNbinWidth 0.0333 --SidebandScale
#
# ##-- Gen / Reco Analysis 
# python NtupleAnalysis.py --GenReco
#########################################################################################################################################################################################################

##-- Import python modules
from python.Options import *
from python.NtupleAnalysisTools import *
from ROOT import gPad, TAxis, TTree, TChain, TLine, TGraph, TMultiGraph, TFile, TCanvas, gROOT, TH2F, TH1F, kPink, kGreen, kCyan, TLegend, kRed, kOrange, kBlack, TLegend, gStyle, TObjArray, kBlue, TGraphErrors
from array import array
import os

##-- Define flags and variables based on user input
args = GetOptions()

print("Start of program...")

if __name__ == '__main__':
    gROOT.SetBatch(1) # Do not output upon draw statement 
    if(args.Efficiency): ol = '/eos/user/r/rasharma/www/doubleHiggs/NtupleAnalysis-v2/cutFlow/'
    elif(args.DataMC):
        print("Data/MC comparison...")
        if(args.testFeatures): ol = '/eos/user/r/rasharma/www/doubleHiggs/New_2021/NtupleAnalysis_v1/'
        #nTupleDirec = '/eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/'
        else: 
            ol = args.ol  # '/eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/DNN_addWjets/'    
            if(not os.path.exists(ol)):
                print"Path %s does not exist, so creating it now"
                print'mkdir %s'%(ol)
                os.system('mkdir %s'%(ol))
                print'cp %s/../index.php %s'%(ol,ol)
                os.system('cp %s/../index.php %s'%(ol,ol))
    if(args.Efficiency):
        print"Performing cut flow efficiency analysis"
        if(args.ratio):
            nMassPoints = len(args.massPoints.split(','))
            ratio_x_vals = []
            for i in range(5):
                exec("c1_y_vals_%s = array( 'd' )"%(i)) # campaign 1 efficiencies
                exec("c2_y_vals_%s = array ( 'd' )"%(i)) # campaign 2 efficiencies

        folders = args.folders.split(',')
        campaigns = args.campaigns.split(',')
        massPoints = args.massPoints.split(',')

        for iFolder,folder in enumerate(folders):
            campaign = campaigns[iFolder]

            # folder = str(args.folder)

            direc = nTupleDirec + folder
            colors = GetColors()

            x_values = array( 'd' )
            x_errors = array( 'd' )
            y_errors = array( 'd' )
            y_sigeff00 = array( 'd' ) # MicroAOD (efficiency of 1). Need # of events.
            for i in range(5):
                exec("y_sigeff%s = array( 'd' )"%(i))
            Npoints = 0

            # For files in directory. Containing all combined for each mass point
            # unorderedFiles = []
            # for path in enumerate(os.listdir(direc)):
                # unorderedFiles.append(path)
            # orderedFiles = []
            # orderedFiles = Tcl().call('lsort', '-dict', os.listdir(direc))
            files = []
            for file in os.listdir(direc):
                files.append(file)

            orderedFiles_ = Tcl().call('lsort', '-dict', files)

            # print"files:",files
            orderedFiles = []
            print"orderedFiles:",orderedFiles_
            for i in orderedFiles_:
                # print"i:",i
                i = i.replace(",","")
                i = i.replace("[","")
                i = i.replace("]","")
                i = i.replace("'","")
                print"i:",i
                orderedFiles.append(i)

            # print"orderedFiles:",orderedFiles

            # badMasses = ['X750','SM'] # masses to not include in the plot
            badMasses = []
            plotLabels = []

            # for fi,file in enumerate(os.listdir(direc)):
            # for fi,path in enumerate(files):
            for fi,path in enumerate(orderedFiles):
                print"path:",path
                Npass_0_tot, Npass_1_tot, Npass_2_tot, Npass_3_tot, Npass_4_tot = 0,0,0,0,0
                badmass = 0
                if(args.Res):
                    mass = path.split('_')[1]
                    print'On mass:',mass
                    for bM in badMasses:
                        if mass == bM: badmass = 1
                    if (badmass): continue
                    # print"massPoints:",massPoints
                    if(mass not in massPoints): continue
                    x_values.append(float(mass[1:]))
                    if(iFolder==0): ratio_x_vals.append(float(mass[1:]))

                    nTotEvents = GetEvents(mass,campaign)

                elif(args.EFT):
                    SM_point = 0
                    print "thing:",path.split('_')[0]
                    if path.split('_')[0] == "SM":
                        SM_point = 1
                        x_values.append(fi)
                        nTotEvents = GetEvents("SM")
                        plotLabels.append("SM")

                    else:
                        BM = path.split('_')[3][4]
                        print("BM:",BM)
                        print"appending:",float(BM) + 1
                        # x_values.append(float(BM) + 1)
                        x_values.append(fi)
                        nodeStr = "node%s"%(float(BM)+1)
                        nTotEvents = GetEvents("node%s"%BM)
                        print("nTotEvents:",nTotEvents)
                        nodeStr = nodeStr.replace("node","node ")
                        nodeStr = nodeStr.replace(".0","")
                        plotLabels.append(nodeStr)

                elif(args.NMSSM):
                    mx = path.split('_')[2]
                    my = path.split('_')[3]
                    massPair = "%s_%s"%(mx,my)
                    print"massPair:",massPair
                    x_values.append(fi) # file i
                    nTotEvents = GetEvents(massPair)
                    massPairString = massPair.replace("_",", ")
                    plotLabels.append(massPairString)

                y_sigeff00.append(1) # Max efficiency
                Npoints += 1
                x_errors.append(0.5)
                y_errors.append(0)
                # if(SM_point): ntags = 1
                # else: ntags = 2
                ntags = 3
                if(campaign=="HHWWgg_v2-3"): ntags = 3
                elif(campaign=="HHWWgg_v2-6"): ntags = 3

                print"ntags:",ntags

                # if(args.SumTags): ntags = 3
                # if(args.SumTags): ntags = 2
                # else: ntags = 1
                for tag in range(0,ntags):
                    # if(not args.SumTags and tag == 1): continue
                    # print'path:',path
                    # print'fi =',fi
                    # print'len(orderedFiles):',len(orderedFiles)
                    # if fi == len(orderedFiles) - 2: continue
                    color = colors[fi]

                    print'Num events in MicroAOD:',nTotEvents

                    signal_path = direc + '/' + str(path)
                    signal_file = TFile.Open(signal_path)
                    if(args.Res): treeEnd = 'ggF_' + mass + '_WWgg_qqlnugg_13TeV_HHWWggTag_%s'%(tag)
                    elif(args.EFT):
                        if(SM_point): treeEnd = 'ggF_SM_WWgg_qqlnugg_13TeV_HHWWggTag_%s'%(tag)
                        else: treeEnd = 'GluGluToHHTo_WWgg_qqlnu_node%s_13TeV_HHWWggTag_%s'%(BM,tag)

                    elif(args.NMSSM): treeEnd = 'NMSSM_XYHWWggqqlnu_%s_13TeV_HHWWggTag_%s'%(massPair,tag)

                    # sig_tree = signal_file.Get('tagsDumper/trees/' + treeEnd)
                    sig_tree = signal_file.Get(treeEnd)

                    # outputName = mass + '_CutFlow_efficiencies.txt' # output text file path
                    # EfficienciesTxt = "bthresh\tsigeff\tttHeff\n"

                    sig_h_0 = TH1F('sig_h_0','sig_h_0',2,0,2)
                    sig_h_1 = TH1F('sig_h_1','sig_h_1',2,0,2)
                    sig_h_2 = TH1F('sig_h_2','sig_h_2',2,0,2)
                    sig_h_3 = TH1F('sig_h_3','sig_h_3',2,0,2)
                    sig_h_4 = TH1F('sig_h_4','sig_h_4',2,0.,2)

                    sig_tree.Draw("passPS >> sig_h_0", "passPS == 1")
                    sig_tree.Draw("passPhotonSels >> sig_h_1","passPhotonSels == 1 && passPS == 1")
                    sig_tree.Draw("passbVeto >> sig_h_2","passPhotonSels == 1 && passPS && passbVeto == 1")
                    sig_tree.Draw("ExOneLep >> sig_h_3","passPhotonSels == 1 && passPS && passbVeto == 1 && ExOneLep == 1 ")
                    sig_tree.Draw("goodJets >> sig_h_4","passPhotonSels == 1 && passPS && passbVeto == 1 && ExOneLep == 1 && goodJets == 1")

                    Npass_0, Npass_1, Npass_2, Npass_3, Npass_4 = sig_h_0.GetEntries(), sig_h_1.GetEntries(), sig_h_2.GetEntries(), sig_h_3.GetEntries(), sig_h_4.GetEntries()
                    Npass_0_tot, Npass_1_tot, Npass_2_tot, Npass_3_tot, Npass_4_tot
                    for i in range(0,5):
                        # print("Npass:",eval("Npass_%s"%(i)))
                        exec("Npass_%s_tot += Npass_%s"%(i,i))
                    # Neff_0, Neff_1, Neff_2, Neff_3, Neff_4 = float(Npass_0) / float(nTotEvents), float(Npass_1) / float(nTotEvents), float(Npass_2) / float(nTotEvents), float(Npass_3) / float(nTotEvents), float(Npass_4) / float(nTotEvents)
                    # print'efficiencies,',Neff_0,Neff_1,Neff_2,Neff_3,Neff_4

                for i in range(0,5):
                    # print("Total pass:",eval("Npass_%s_tot"%(i)))
                    # print("Neff:",eval("Npass_%s_tot"%(i)))
                    exec("Neff_%s = float(Npass_%s_tot) / float(nTotEvents)"%(i,i))

                y_sigeff0.append(Neff_0)
                y_sigeff1.append(Neff_1)
                y_sigeff2.append(Neff_2)
                y_sigeff3.append(Neff_3)
                y_sigeff4.append(Neff_4)

                for i in range(5):
                    if(iFolder == 0): exec("c1_y_vals_%s.append(Neff_%s)"%(i,i)) # campaign 1 efficiencies
                    if(iFolder == 1): exec("c2_y_vals_%s.append(Neff_%s)"%(i,i)) # campaign 1 efficiencies

                # sig_tree.Draw(hasHighbjet + ' >> sig_h',hasHighbjet)
                # NsigPass = float(Nsig) - float(sig_h.GetEntries())
                # print'NsigPass: ',NsigPass
                # sig_eff = float(NsigPass) / float(Nsig)
                # print'Signal efficiency = ',sig_eff
                # y_sigeff.append(sig_eff)

                # EfficienciesTxt += str(bthresh) + "\t" +  str(sig_eff) + "\t" + str(ttH_eff) + "\n"
                # EfficienciesTxt += str(bthresh) + "\t" +  str(sig_eff) + "\t" + str(ttH_eff) + "\n"

                # with open(outputName, "w") as output:
                        # output.write(EfficienciesTxt) # write txt file

            if(args.NMSSM) or (args.EFT):
                sig_eff_g_00 = TGraphErrors(Npoints,x_values,y_sigeff00,x_errors,y_errors)
                # SetBinLabels(sig_eff_g_00,Npoints,plotLabels)
                for i in range(0,5):
                    exec("sig_eff_g_%s = TGraphErrors(Npoints,x_values,y_sigeff%s,x_errors,y_errors)"%(i,i))
                    # exec("SetBinLabels(sig_eff_g_%d,Npoints,plotLabels)"%(i))

            else:
                sig_eff_g_00 = TGraph(Npoints,x_values,y_sigeff00)
                for i in range(0,5):
                    exec("sig_eff_g_%s = TGraph(Npoints,x_values,y_sigeff%s)"%(i,i))

            SetGraphStyle(sig_eff_g_00,1,kRed, 20)
            SetGraphStyle(sig_eff_g_0,10,kBlue, 21)
            SetGraphStyle(sig_eff_g_1,9,kGreen, 22)
            SetGraphStyle(sig_eff_g_2,6,kPink, 23)
            SetGraphStyle(sig_eff_g_3,2,95,34) # orange
            SetGraphStyle(sig_eff_g_4,7,9,33) # purple

            if(args.NMSSM) or (args.EFT):
                SetGraphStyle(sig_eff_g_00,1,kRed,20)
                SetGraphStyle(sig_eff_g_0,1,kBlue, 21)
                SetGraphStyle(sig_eff_g_1,1,kGreen, 22)
                SetGraphStyle(sig_eff_g_2,1,kPink, 23)
                SetGraphStyle(sig_eff_g_3,1,95,34) # orange
                SetGraphStyle(sig_eff_g_4,1,9,33) # purple

            sig_eff_g_00.SetTitle("MicroAOD")
            sig_eff_g_0.SetTitle("Pass #gamma#gamma cuts")
            sig_eff_g_1.SetTitle("Pass #gamma cuts")
            sig_eff_g_2.SetTitle("passbVeto")
            sig_eff_g_3.SetTitle("Lepton")
            sig_eff_g_4.SetTitle("Jets")

            mg = TMultiGraph()
            if(args.Res): mg.SetTitle("Resonant Signal Efficiency Cut Flow;Radion Mass (GeV);Efficiency")
            elif(args.EFT): mg.SetTitle("Non-Resonant Signal Efficiency Cut Flow;;Efficiency")
            elif(args.NMSSM): mg.SetTitle("NMSSM Signal Efficiency Cut Flow;;Efficiency")

            if(args.NMSSM) or (args.EFT): drawOption = "P2"
            else: drawOption = "PL"

            mg.Add(sig_eff_g_00)
            for i in range(5):
                # eval("mg.Add(sig_eff_g_%d,'%s')"%(i,drawOption))
                eval("mg.Add(sig_eff_g_%d,)"%(i))

            mg.SetMinimum(0)

            # outName = ol + 'CutFlow' + '_' + args.campaign
            outName = ol + 'CutFlow' + '_' + campaign
            if args.log: outName += 'Log'
            if args.note is not "": outName += '_' + str(args.note)
            outName += '.png'
            os.system("mkdir -p "+outName)

            if(args.NMSSM) or (args.EFT):
                DrawNonResHistogram(mg,"AP",outName,args.log,Npoints,plotLabels)
                outName = outName.replace("png","pdf")
                DrawNonResHistogram(mg,"AP",outName,args.log,Npoints,plotLabels)
            else:
                Draw_Histogram(mg,"APL",outName,args.log)
                outName = outName.replace("png","pdf")
                Draw_Histogram(mg,"APL",outName,args.log)

        if(args.ratio):
            print"Plotting ratio of efficiencies"
            print"ratio_x_vals:"
            print ratio_x_vals
            for i in range(5):
                print"c1_y_vals_%s"%(i)
                exec("print c1_y_vals_%s"%(i))
                print"c2_y_vals_%s"%(i)
                exec("print c2_y_vals_%s"%(i))

            x_values = array( 'd' )
            y_ratioEff00 = array ( 'd' )
            for entry in ratio_x_vals:
                x_values.append(entry)
                y_ratioEff00.append(1)

            for i in range(5):
                exec("y_ratioEff%s = array( 'd' )"%(i))
            for i in range(len(args.massPoints.split(','))):
                for j in range(5):
                    ratio = eval("c1_y_vals_%s[%s] / c2_y_vals_%s[%s]"%(j,i,j,i))
                    eval("y_ratioEff%s.append(%s)"%(j,ratio))

            Nmasses = len(args.massPoints.split(','))
            sig_ratioEff_g_00 = TGraph(Nmasses,x_values,y_ratioEff00)
            for i in range(0,5):
                exec("sig_ratioEff_g_%s = TGraph(Nmasses,x_values,y_ratioEff%s)"%(i,i))

            SetGraphStyle(sig_ratioEff_g_00,1,kRed, 20)
            SetGraphStyle(sig_ratioEff_g_0,10,kBlue, 21)
            SetGraphStyle(sig_ratioEff_g_1,9,kGreen, 22)
            SetGraphStyle(sig_ratioEff_g_2,6,kPink, 23)
            SetGraphStyle(sig_ratioEff_g_3,2,95,34) # orange
            SetGraphStyle(sig_ratioEff_g_4,7,9,33) # purple

            sig_ratioEff_g_00.SetTitle("MicroAOD")
            sig_ratioEff_g_0.SetTitle("Pass #gamma#gamma cuts")
            sig_ratioEff_g_1.SetTitle("Pass #gamma cuts")
            sig_ratioEff_g_2.SetTitle("passbVeto")
            sig_ratioEff_g_3.SetTitle("Lepton")
            sig_ratioEff_g_4.SetTitle("Jets")

            ratio_mg = TMultiGraph()

            if(args.Res): ratio_mg.SetTitle("Resonant Signal Efficiency Cut Flow;Radion Mass (GeV);Efficiency")
            # elif(args.EFT): mg.SetTitle("Non-Resonant Signal Efficiency Cut Flow;;Efficiency")
            # elif(args.NMSSM): mg.SetTitle("NMSSM Signal Efficiency Cut Flow;;Efficiency")

            if(args.NMSSM) or (args.EFT): drawOption = "P2"
            else: drawOption = "PL"

            ratio_mg.Add(sig_ratioEff_g_00)
            for i in range(5):
                # eval("mg.Add(sig_eff_g_%d,'%s')"%(i,drawOption))
                eval("ratio_mg.Add(sig_ratioEff_g_%d,)"%(i))

            # ratio_mg.SetMinimum(0)
            # ratio_mg.SetMaximum(1.01)
            # ratio_mg.SetMinimum(0.5)
#
            # outName = ol + 'CutFlow' + '_' + args.campaign
            outName = ol + 'CutFlow' + '_' + campaign
            if args.log: outName += 'Log'
            if args.note is not "": outName += '_' + str(args.note)
            outName += '.png'
            if(not os.path.exists(outName)):
                os.system("mkdir -p "+outName)

            if(args.NMSSM) or (args.EFT):
                DrawNonResHistogram(ratio_mg,"AP",outName,args.log,Npoints,plotLabels)
                outName = outName.replace("png","pdf")
                DrawNonResHistogram(ratio_mg,"AP",outName,args.log,Npoints,plotLabels)
            else:
                Draw_Histogram(ratio_mg,"APL",outName,args.log)
                outName = outName.replace("png","pdf")
                Draw_Histogram(ratio_mg,"APL",outName,args.log)

    ##-- Perform Data / MC analysis
    elif(args.DataMC):
        print"Performing Data / MC Analysis"

        ##-- Get Data File
        dataFile = args.dataFile 

        ##-- Get Background Files 
        bkgDirec = args.bkgDirec 
        bkgFiles = GetFiles(bkgDirec)
        print"Background files: ",bkgFiles
        # exit(1) 

        ##-- Get Signal File 
        signalFile = args.signalFile 

        ##-- Run Main Module 
        if(not args.SB and not args.SR):
            print "No phase space regions selected"
            print "To run on the signal region pass the flag --SR"
            print "To run on the signal sidebands region, pass the flag --SB"
            print "You can pass both flags "

        ##-- Data, MC and Signal Together. Data and MC in sidebands
        if(args.SB): region = "SB"
        elif(args.SR): region = "SR"
        cuts, cutNames = GetCuts(args.CutsType)
        for i in range(0,len(cuts)):
            cut_ = cuts[i] ## using only first cut.
            cutName_ = cutNames[i] ## using only first cut.     
            print"cut_:",cut_
            print"cutName_:",cutName_       
            chi2 = PlotDataMC(dataFile,bkgFiles,signalFile,ol,args,region,cut_,cutName_,args.DNNbinWidth, args.ratioMin, args.ratioMax)
            print "chi2:",chi2

        # ##-- MC and Signal in Signal Region 
        # if(args.SR): 
        #     region = "SR"
        #     cuts, cutNames = GetCuts(args.CutsType)
        #     for i in range(0,len(cuts)):
        #         cut_ = cuts[i] ## using only first cut.
        #         cutName_ = cutNames[i] ## using only first cut.     
        #         print"cut_:",cut_
        #         print"cutName_:",cutName_       
        #         chi2 = PlotDataMC(dataFile,bkgFiles,signalFile,ol,args,region,cut_,cutName_)
        #         print "chi2:",chi2        
        # if(args.SR): 
        #     region = "SR"
        #     PlotDataMC(dataFile,bkgFiles,signalFile,ol,args,region)
        print"DONE"
