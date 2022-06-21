"""
Abraham Tishelman-Charny
13 May 2020

The purpose of this module is to provide variables and definitions for NtupleAnalysis.py 
"""

from ROOT import TCanvas, TColor, TStyle, gROOT, gPad, TH1F, TFile, TChain, TPaveStats, gStyle, THStack, kBlue, kCyan, kRed, kGreen, TLegend, kYellow, TRatioPlot, kBlack, TLine, kPink, TLatex, kOrange, gErrorIgnoreLevel, kWarning, TGraphErrors, kGray
import ROOT 
import os 
from MCTools import * 
from VariableTools import * 
from PlotTools import * 
from CutsTools import * 
from array import array
from tdrstyle import * 
from CMS_lumi import * 


"""
Custom colors 

thank you to the following pages:
https://github.com/yhaddad/Heppi/blob/master/images/colors.png
https://root-forum.cern.ch/t/how-to-form-a-color-t-from-a-tcolor/25013/2
"""

class Color(int):
    """Create a new ROOT.TColor object with an associated index"""
    __slots__ = ["object", "name"]

    def __new__(cls, r, g, b, name=""):
        self = int.__new__(cls, ROOT.TColor.GetFreeColorIndex())
        self.object = ROOT.TColor(self, r, g, b, name, 1.0)
        self.name = name
        return self

colors = [Color(0, 0, 0, "black"),
          Color(26/255., 188/255., 156/255., "turqoise"),
          Color( 46/255., 204/255., 113/255.,"emerland"      ),
          Color( 52/255., 152/255., 219/255.,"peterriver"   ),
          Color(155/255.,  89/255., 182/255.,"amethyst"      ),
          Color( 52/255.,  73/255.,  94/255.,"wet-asphalt"   ),
          Color( 22/255., 160/255., 133/255.,"green-sea"     ),
          Color( 39/255., 174/255.,  96/255.,"nephritis"     ),
          Color( 41/255., 128/255., 185/255.,"belize-hole"   ),
          Color(142/255.,  68/255., 173/255.,"wisteria"      ),
          Color( 44/255.,  62/255.,  80/255.,"midnight-blue" ),
          Color(241/255., 196/255.,  15/255.,"sunflower"    ),
          Color(230/255., 126/255.,  34/255.,"carrot"        ),
          Color(231/255.,  76/255.,  60/255.,"alizarin"      ),
          Color(236/255., 240/255., 241/255.,"clouds"        ),
          Color(149/255., 165/255., 166/255.,"concrete"      ),
          Color(243/255., 156/255.,  18/255.,"orange"        ),
          Color(211/255.,  84/255.,   0/255.,"pumpkin"       ),
          Color(192/255.,  57/255.,  43/255.,"pomegranate"   ),
          Color(189/255., 195/255., 199/255.,"silver"        ),
          Color(127/255., 140/255., 141/255.,"asbestos"      ),          
          ]
for color in colors:
    setattr(ROOT, color.name, color)

def GetFiles(direc, cutName):
    files = [] 
    ##-- training 
    MCendsTraining = [

        'DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'GJet_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'TTGG_0Jets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'TTGJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'ttWJets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'TTJets_TuneCP5_extra_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'W1JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'W1JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'W1JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'W1JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'W2JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'W2JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'W2JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'W2JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'WGGJets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',
        'WGJJToLNu_EWK_QCD_HHWWggTag_0_MoreVars_kinWeight_noHgg_v3.root',

        # 'GluGluHToGG_HHWWggTag_0_MoreVars.root', ##--  which is used for training? check training .py file 

        # 'GluGluHToGG_2017_HHWWggTag_0_MoreVars.root',
        # 'VBFHToGG_2017_HHWWggTag_0_MoreVars.root',
        # 'VHToGG_2017_HHWWggTag_0_MoreVars.root',
        # 'ttHJetToGG_2017_HHWWggTag_0_MoreVars.root',
        # 'VBFHToGG_HHWWggTag_0_MoreVars.root',
        # 'VHToGG_HHWWggTag_0_MoreVars.root',
        # 'ttHJetToGG_HHWWggTag_0_MoreVars.root'


        # # "DYJetsToLL_M-50_HHWWggTag_0_MoreVars.root",
        # # "DiPhotonJetsBox_M40_80_HHWWggTag_0_MoreVars.root",
        # "DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars.root",
        # # "GJet_Pt-20to40_HHWWggTag_0_MoreVars.root",
        # # "GJet_Pt-20toInf_HHWWggTag_0_MoreVars.root",
        # "GJet_Pt-40toInf_HHWWggTag_0_MoreVars.root",
        # # "GluGluHToGG_HHWWggTag_0_MoreVars_noSyst.root",
        # # "QCD_Pt-30to40_HHWWggTag_0_MoreVars.root",
        # # "QCD_Pt-30toInf_HHWWggTag_0_MoreVars.root",
        # # "QCD_Pt-40toInf_HHWWggTag_0_MoreVars.root",
        # # "THQ_ctcvcp_HHWWggTag_0_MoreVars.root",
        # "TTGG_0Jets_HHWWggTag_0_MoreVars.root",
        # "TTGJets_TuneCP5_HHWWggTag_0_MoreVars.root",
        # # "TTJets_HT-1200to2500_HHWWggTag_0_MoreVars.root",
        # # "TTJets_HT-2500toInf_HHWWggTag_0_MoreVars.root",
        # # "TTJets_HT-600to800_HHWWggTag_0_MoreVars.root",
        # # "TTJets_HT-800to1200_HHWWggTag_0_MoreVars.root",
        # "TTJets_TuneCP5_extra_HHWWggTag_0_MoreVars.root",
        # # "TTToHadronic_HHWWggTag_0_MoreVars.root",
        # # "VBFHToGG_HHWWggTag_0_MoreVars_noSyst.root",
        # # "VHToGG_HHWWggTag_0_MoreVars_noSyst.root",
        # # "W1JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars.root",
        # # "W1JetsToLNu_LHEWpT_100-150_extra_HHWWggTag_0_MoreVars.root",
        # "W1JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars.root",
        # "W1JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars.root",
        # "W1JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars.root",
        # "W1JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars.root",
        # # "W2JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars.root",
        # # "W2JetsToLNu_LHEWpT_100-150_extra_HHWWggTag_0_MoreVars.root",
        # "W2JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars.root",
        # "W2JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars.root",
        # "W2JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars.root",
        # "W2JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars.root",
        # # "W3JetsToLNu_HHWWggTag_0_MoreVars.root",
        # # "W4JetsToLNu_HHWWggTag_0_MoreVars.root",
        # "WGGJets_HHWWggTag_0_MoreVars.root",
        # "WGJJToLNuGJJ_EWK_HHWWggTag_0_MoreVars.root",
        # # "WGJJToLNu_EWK_QCD_HHWWggTag_0_MoreVars.root",
        # # "WWTo1L1Nu2Q_HHWWggTag_0_MoreVars.root",
        # # "WW_TuneCP5_HHWWggTag_0_MoreVars.root",
        # # "ttHJetToGG_HHWWggTag_0_MoreVars_noSyst.root",
        # # "ttWJets_HHWWggTag_0_MoreVars.root"

    ]


    if((cutName == "Unblinded") or (cutName == "Unblinded_noDNNCut")):
        MCendsTraining.append("GluGluHToGG_2017_HHWWggTag_0_MoreVars_v2.root")
        MCendsTraining.append("VBFHToGG_2017_HHWWggTag_0_MoreVars_v2.root")
        MCendsTraining.append("VHToGG_2017_HHWWggTag_0_MoreVars_v2.root")
        MCendsTraining.append("ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2.root")
        MCendsTraining.append("GluGluToHHTo2G2Qlnu_node_cHHH1_2017.root")

    MCends = [
        "DYJetsToLL_M-50_HHWWggTag_0_MoreVars.root",
        "DiPhotonJetsBox_M40_80_HHWWggTag_0_MoreVars.root",
        "DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars.root",
        "GJet_Pt-20to40_HHWWggTag_0_MoreVars.root",
        "GJet_Pt-20toInf_HHWWggTag_0_MoreVars.root",
        "GJet_Pt-40toInf_HHWWggTag_0_MoreVars.root",
        "GluGluHToGG_HHWWggTag_0_MoreVars_noSyst.root",
        # "QCD_Pt-30to40_HHWWggTag_0_MoreVars.root",
        # "QCD_Pt-30toInf_HHWWggTag_0_MoreVars.root",
        # "QCD_Pt-40toInf_HHWWggTag_0_MoreVars.root",
        "THQ_ctcvcp_HHWWggTag_0_MoreVars.root",
        "TTGG_0Jets_HHWWggTag_0_MoreVars.root",
        "TTGJets_TuneCP5_HHWWggTag_0_MoreVars.root",
        # "TTJets_HT-1200to2500_HHWWggTag_0_MoreVars.root",
        # "TTJets_HT-2500toInf_HHWWggTag_0_MoreVars.root",
        # "TTJets_HT-600to800_HHWWggTag_0_MoreVars.root",
        # "TTJets_HT-800to1200_HHWWggTag_0_MoreVars.root",
        "TTJets_TuneCP5_extra_HHWWggTag_0_MoreVars.root",
        "TTToHadronic_HHWWggTag_0_MoreVars.root",
        "VBFHToGG_HHWWggTag_0_MoreVars_noSyst.root",
        "VHToGG_HHWWggTag_0_MoreVars_noSyst.root",
        "W1JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars.root",
        # "W1JetsToLNu_LHEWpT_100-150_extra_HHWWggTag_0_MoreVars.root",
        "W1JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars.root",
        "W1JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars.root",
        "W1JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars.root",
        "W1JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars.root",
        "W2JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars.root",
        # "W2JetsToLNu_LHEWpT_100-150_extra_HHWWggTag_0_MoreVars.root",
        "W2JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars.root",
        "W2JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars.root",
        "W2JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars.root",
        "W2JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars.root",
        "W3JetsToLNu_HHWWggTag_0_MoreVars.root",
        "W4JetsToLNu_HHWWggTag_0_MoreVars.root",
        "WGGJets_HHWWggTag_0_MoreVars.root",
        "WGJJToLNuGJJ_EWK_HHWWggTag_0_MoreVars.root",
        "WGJJToLNu_EWK_QCD_HHWWggTag_0_MoreVars.root",
        "WWTo1L1Nu2Q_HHWWggTag_0_MoreVars.root",
        "WW_TuneCP5_HHWWggTag_0_MoreVars.root",
        "ttHJetToGG_HHWWggTag_0_MoreVars_noSyst.root",
        "ttWJets_HHWWggTag_0_MoreVars.root"

    ]

    for fileEnd in os.listdir(direc): 
        # if ((".root" in fileEnd) and ( (fileEnd == "GluGluToHHTo2G2Qlnu_node_cHHH1_2017_HHWWggTag_0_even_MoreVars.root") or (fileEnd in MCends) ) ):
        # if ( fileEnd in MCends ):
        # if ( fileEnd in MCends ):
        if ( fileEnd in MCendsTraining ):
            fullPath = "%s/%s"%(direc,fileEnd)
            files.append(fullPath)
    return files   

# def GetFiles(nTupleDirec_, Folder_):
#     files = [] 
#     Direc = "%s/%s"%(nTupleDirec_,Folder_)
#     for file in os.listdir(Direc): files.append(file)
#     return files 

def AppendNtuples(dataFiles_, mcFiles_, signalFiles_):
    print "In AppendNtuples"
    # for each input file, make a new output file with an added branch

def CalcEff(h_,cut_):
    ##-- return percentage of events that pass cut 
    pctPass_ = 0
    numPass = 0 
    N = h_.GetEntries()
    nBins = h_.GetNbinsX()
    for ix,y in enumerate(h_):
        if ix == 0: continue # skip underflow bin 
        elif ix == nBins + 1: break # skip overflow bin 
        x = h_.GetBinLowEdge(ix)
        if x < cut_: numPass += y # if the x value of the bin is less than the cut, all jets pass 
        elif x >= cut_: break # if the x value of the bin is greater than or equal to the cut, no more jets will pass 
    pctPass_ = float(numPass) / float(N)
    return pctPass_ 

def GetBinVals(h_):
    binVals_ = [] 
    nBins = h_.GetNbinsX()
    for i in range(0,nBins):
        bin_val = h_.GetBinContent(i+1)
        binVals_.append(bin_val)
    return binVals_

def GetDataHist(dPath,prefix,cut,cutName,iv,v,varTitle,VarBatch,verbose,DNNbinWidth_,region_):
    # print "Getting data histogram" 
    dFile = TFile.Open(dPath)
    # print "Data file path: ",dPath
    # ch = TChain('%sData_13TeV_HHWWggTag_0'%(prefix))
    # data_trees = TChain('%sData_13TeV_HHWWggTag_0'%(prefix))
    data_trees = TChain('data_trees')
    # data_trees.Add("%s/%sData"%(dPath,prefix))
    # data_trees.Add("%s/%sData_13TeV_HHWWggTag_0"%(dPath,prefix))
    data_trees.Add("%s/%sData_13TeV_HHWWggTag_0_v1"%(dPath,prefix))

    ##-- Hardcoding the addition of 2016 and 2018 data for AN-20-165 v5 checks

    # data_trees.Add("/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/Data_2016_HHWWggTag_0_MoreVars.root/%sData_13TeV_HHWWggTag_0_v1"%(prefix))
    # data_trees.Add("/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/Data_2018_HHWWggTag_0_MoreVars.root/%sData_13TeV_HHWWggTag_0_v1"%(prefix))

    # data_trees.Add("%s/%stagsDumper/trees/Data_13TeV_HHWWggTag_0"%(dPath,prefix))
    # data_trees.Add("%s/%sData_13TeV_HHWWggTag_1"%(dPath,prefix))
    # data_trees.Add("%s/%sData_13TeV_HHWWggTag_2"%(dPath,prefix))
    SB_CUT = "(CMS_hgg_mass <= 115 || CMS_hgg_mass >= 135)"
    MASS_RANGE_CUT = "(CMS_hgg_mass >= 100 && CMS_hgg_mass <= 180)"
    ZERO_CUT = "ZERO_CUT" ## to cut empty entries 

    if(region_ == "FullRegion"):
        DATA_CUT = "%s*(%s)"%(MASS_RANGE_CUT, ZERO_CUT) # unblinded - do not apply sideband cut 
    else:
        DATA_CUT = "%s*(%s)"%(SB_CUT,ZERO_CUT) # not unblinded - should apply sideband cut 

    DATA_CUT += "*(%s)"%(cut)  

    ##-- Replace zero cut with variable name 
    if(VarBatch == "Loose"): varTitle = varNames[iv]
    else: varTitle = GetVarTitle(v)
    # if(verbose): print"Plotting variable:",varTitle
    DATA_CUT = DATA_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v)) 
    # if(varTitle == "weight"): MC_CUT = MC_CUT.replace(MC_WEIGHT,"(1)") # if you want to plot the "weight" variable, you should not scale it by weight!             
    xbins, xmin, xmax = GetBins(varTitle,DNNbinWidth_)

    ##-- Fill histogram with data  

    # special binning for evalDNN_HH

    # edges = array('d',[0.1000,0.2,0.3,0.4,0.5,0.630000,0.7,0.84000,0.89000,1.0001])
    edges = array('d',[0.1000,0.15, 0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.630000,0.7,0.75,0.84000,0.89000,1.0001])
    N_bins_special = len(edges) -1 
    
    if(varTitle == "evalDNN_HH"): 
        Data_h_tmp = TH1F('Data_h_tmp',varTitle,N_bins_special,edges)
    else: Data_h_tmp = TH1F('Data_h_tmp',varTitle,xbins,xmin,xmax)

    # Data_h_tmp = TH1F('Data_h_tmp',varTitle,xbins,xmin,xmax)
    Data_h_tmp.SetTitle("%s"%(varTitle))
    Data_h_tmp.SetMarkerStyle(8)

    # print("xnax:",Data_h_tmp.GetXaxis().GetXmax())

    # print"v:",v
    # print"DATA_CUT:",DATA_CUT
    exec('data_trees.Draw("%s >> Data_h_tmp","%s")'%(v,DATA_CUT))
    # exec('data_trees.Draw("%s >> Data_h_tmp","%s")'%(v,DATA_CUT))
    # print"filled histogram"

    ##-- Only save number of events for first variable. Should be same for all because same cut is used 
    # if(iv == 0): 
        # dataNevents = Data_h_tmp.GetEntries()
        # dataNevents_list.append(dataNevents)
    # print"Blinded Data numEvents:",Data_h_tmp.GetEntries()   
                     
    DataHist_ = Data_h_tmp.Clone("DataHist")
    DataHist_.SetDirectory(0)

    return DataHist_

def GetBackgroundHists(bkgFiles_,noQCD,verbose,prefix,varTitle,region,v,Lumi,cut,cutName,DNNbinWidth_,withKinWeight_):
    print "Getting background stack"

    ##-- Define cut 
    REGION_CUT = ""
    if(region == "SB"): REGION_CUT = "(CMS_hgg_mass <= 115 || CMS_hgg_mass >= 135)"
    elif(region == "SR"): REGION_CUT = "(CMS_hgg_mass > 115 && CMS_hgg_mass < 135)"
    elif(region == "FullRegion"): REGION_CUT = "(CMS_hgg_mass >= 100 && CMS_hgg_mass <= 180)"
    else: 
        print"Input region ",region,"is not defined"
        print"Exiting"
        exit(1)

    if(cutName == "Unblinded"):
        REGION_CUT = "(CMS_hgg_mass >= 100 && CMS_hgg_mass <= 180)"

    # B_WEIGHT = "1*weight"
    if(withKinWeight_): 
        print("Including semileptonic kinematic weights into MC weighting")
        B_WEIGHT = "1*weight*kinWeight*(fabs(weight*kinWeight) < 10.)" ##-- Used in training 
    else: 
        print("NOT Including semileptonic kinematic weights into MC weighting")
        B_WEIGHT = "1*weight*(fabs(weight*kinWeight) < 10.)" 
    # B_WEIGHT = "1*weight" ##-- to plot with no kin weight

    print("Background MC weight applied:", B_WEIGHT)
    print("PLEASE NOTE if you want this weight. Check if it includes kinematic reweighting or not.")

    ZERO_CUT = "ZERO_CUT"
    B_CUT = "%s*(%s)*(%s)"%(B_WEIGHT,REGION_CUT,ZERO_CUT)
    B_CUT += "*(%s)"%(cut)  
    B_CUT = B_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
    B_CUT_NOWEIGHT = "%s"%(B_CUT)
    B_CUT_NOWEIGHT = B_CUT_NOWEIGHT.replace(B_WEIGHT,"(1)")

    ##-- Get Background Histograms 
    bkgHistos_ = []
    bkgHistCategories_ = [] 
    Bkg_Names_ = [] 
    Bkg_Nevents_ = [] 
    Bkg_Nevents_unweighted_ = [] 
    # for i,mcF_ in enumerate(mcFiles):

    # YacineStyle = TStyle("YacineStyle", "Yacine Style")
    # NRGBs = 3 
    # NCont = 255 
    # TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
    # ci = TColor.GetFreeColorIndex()

    for i,mcPath in enumerate(bkgFiles_):
        # mcPath = "%s/%s"%(mcDirec,mcF_)
        mcEnd = mcPath.split('/')[-1]
        mcFile = TFile.Open(mcPath)
        treeName = GetMCTreeName(mcEnd)
        treeName += "_13TeV_HHWWggTag_0"
        # treeName += "_13TeV_HHWWggTag_0_v1"
        MC_Category = GetMCCategory(mcEnd)
        print("MC_Category:",MC_Category)
        v1_mcs = ["VBFH","ttHJetToGG","ggH","VH", "H$\gamma\gamma$", "H\\rightarrow\gamma\gamma"]   
        if(MC_Category in v1_mcs):
            treeName += "_v1"
        MCname = GetMCName(mcEnd)
        Bkg_Names_.append(MCname) # get shorter MC name here        
        if(verbose): 
            # print"Background File:",mcPath
            print"Background:",MC_Category
            print"file:",mcPath  

        ##-- If noQCD set to true, skip QCD 
        if((MC_Category == "QCD") and (noQCD)): 
            print"Skipping QCD"
            Bkg_Nevents_.append(0)
            Bkg_Nevents_unweighted_.append(0)
            # these_MC_Nevents_noweights.append(0) # Set yields to 0 for table 
            # these_MC_Nevents.append(0) # Set yields to 0 for table
            # B_list.append(0) 
            # if(itag == 0 and ic == 0 and iv == 0): 
                # MCname = GetMCName(mcF_)
                # MC_names.append(MCname) # Skipping QCD, but still save name for yields because tag_2 may not be 0                           
            continue 

        ##-- Get Background Trees 
        Bkg_Trees = TChain("Bkg_Trees")
        # mc_ch = TChain('%s%s_13TeV_HHWWggTag_0'%(args_.prefix,treeName))
        Bkg_Trees.Add("%s/%s%s"%(mcPath,prefix,treeName))
        # Bkg_Trees.Add("%s/%s%s_13TeV_HHWWggTag_1"%(mcPath,prefix,treeName))
        # Bkg_Trees.Add("%s/%s%s_13TeV_HHWWggTag_2"%(mcPath,prefix,treeName))

        ##-- Fill Histogram
        xbins, xmin, xmax = GetBins(varTitle, DNNbinWidth_)
        # exec("MC_h_tmp_%s = TH1F('MC_h_tmp_%s',varTitle,xbins,xmin,xmax)"%(i,i))
        # exec("MC_h_tmp_noweight_%s = TH1F('MC_h_tmp_noweight_%s',varTitle,xbins,xmin,xmax)"%(i,i))

        # exec("B_h_%s = TH1F('B_h_%s',varTitle,xbins,xmin,xmax)"%(i,i)) # histogram specifically for computing B in signal region

        # edges = array('d',[0.1000,0.2,0.3,0.4,0.5,0.630000,0.7,0.84000,0.89000,1.0001])
        edges = array('d',[0.1000,0.15, 0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.630000,0.7,0.75,0.84000,0.89000,1.0001])
        N_bins_special = len(edges) - 1  

        if(varTitle == "evalDNN_HH"): 
            exec("B_h_%s = TH1F('B_h_%s',varTitle,N_bins_special,edges)"%(i,i)) # histogram specifically for computing B in signal region
        else: 
            exec("B_h_%s = TH1F('B_h_%s',varTitle,xbins,xmin,xmax)"%(i,i)) # histogram specifically for computing B in signal region

        # exec("B_h_noweight_%s = TH1F('B_h_noweight_%s',varTitle,xbins,xmin,xmax)"%(i,i)) # histogram specifically for computing B in signal region

        # print("xmax_bkg:",Data_h_tmp.GetXaxis().GetXmax())

        ##-- no weights 
        if(varTitle == "evalDNN_HH"): 
            exec("B_h_%s_noweights = TH1F('B_h_%s_noweights',varTitle,N_bins_special,edges)"%(i,i)) # histogram specifically for computing B in signal region
        else: exec("B_h_%s_noweights = TH1F('B_h_%s_noweights',varTitle,xbins,xmin,xmax)"%(i,i)) # histogram specifically for computing B in signal region
        
        # thisHist = eval("MC_h_tmp_%s"%(i))
        thisHist = eval("B_h_%s"%(i))
        thisHist.Sumw2()
        # declare_colors()
        mcColor = GetMCColor(MC_Category)

        ##-- If GJet or QCD sample, need to remove prompt-prompt events 
        if(MC_Category == "GJet" or MC_Category == "QCD"):
            if(verbose): print"Removing prompt-prompt"
            removePromptPromptCut = "(!((Leading_Photon_genMatchType == 1) && (Subleading_Photon_genMatchType == 1)))" # selection: remove events where both photons are prompt
            original_B_CUT = "%s"%(B_CUT)
            # original_MC_CUT = "%s"%(MC_CUT)
            # this_MC_CUT = "%s*(%s)"%(original_MC_CUT,removePromptPromptCut)
            this_B_CUT = "%s*(%s)"%(original_B_CUT,removePromptPromptCut)
            # this_MC_CUT_NOWEIGHT = this_MC_CUT.replace(MC_WEIGHT,"(1)")
            this_B_CUT_NOWEIGHT = this_B_CUT.replace(B_WEIGHT,"(1)")

        # eval("MC_h_tmp_%s.SetFillColor(eval(mcColor))"%(i))
        # eval("MC_h_tmp_%s.SetLineColor(eval(mcColor))"%(i))

        eval("B_h_%s.SetFillColor(eval(mcColor))"%(i))
        eval("B_h_%s.SetLineColor(eval(mcColor))"%(i))       
        # 
        # eval("B_h_%s.SetFillColor(mcColor)"%(i))
        # eval("B_h_%s.SetLineColor(mcColor)"%(i))                 

        if(MC_Category == "GJet" or MC_Category == "QCD"): 
            # exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,this_MC_CUT))
            exec('Bkg_Trees.Draw("%s >> B_h_%s","%s")'%(v,i,this_B_CUT))
            exec('Bkg_Trees.Draw("%s >> B_h_%s_noweights","%s")'%(v,i,this_B_CUT_NOWEIGHT))
            
        else: 
            # exec('mc_ch.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,MC_CUT))    
            exec('Bkg_Trees.Draw("%s >> B_h_%s","%s")'%(v,i,B_CUT))                                       
            exec('Bkg_Trees.Draw("%s >> B_h_%s_noweights","%s")'%(v,i,B_CUT_NOWEIGHT))                                       

        # eval("MC_h_tmp_%s.Scale(float(args_.Lumi))"%(i))
        eval("B_h_%s.Scale(float(Lumi))"%(i))

        Bkg_Nevents_.append(eval("B_h_%s.Integral()"%(i))) 

        ##-- Check for negative bins 
        for bi in range(eval("B_h_%s.GetNbinsX()"%(i))):
            bin_i = bi + 1 # skip underflow bin 
            Nbkg = eval("B_h_%s.GetBinContent(%s)"%(i,bin_i)) 
            if(Nbkg < 0):
                Nbkg_unweighted = eval("B_h_%s_noweights.GetBinContent(%s)"%(i,bin_i)) 
                print"bin ",bin_i," Background Yield is < 0: ",Nbkg
                print"number of unweighted events: ",Nbkg_unweighted
            # if(bin_i == 5 and Nbkg > 0):
            #     print"bin_i == 5"
            #     Nbkg_unweighted = eval("B_h_%s_noweights.GetBinContent(%s)"%(i,bin_i)) 
            #     # print"bin ",bin_i," Background Yield is < 0: ",Nbkg
            #     print"Weighted Background Yield: ",Nbkg
            #     print"number of unweighted events: ",Nbkg_unweighted                

        ##-- without weights
        Bkg_Nevents_unweighted_.append(eval("B_h_%s_noweights.Integral()"%(i))) 

        newHist = thisHist.Clone("newHist")

        ##-- Set title based on treeName 
        newHist.SetTitle(MC_Category)
        newHist.GetXaxis().SetTitle(mcEnd)
        newHist.SetDirectory(0)
        newHist.Sumw2()
        bkgHistos_.append(newHist)
        bkgHistCategories_.append(MC_Category)

    return bkgHistos_, bkgHistCategories_, Bkg_Names_, Bkg_Nevents_, Bkg_Nevents_unweighted_

def GetSignalHists(signalFile_,prefix,v,region,varTitle,Lumi,verbose,cut,DNNbinWidth_):
    print "Getting Signal histogram(s)"
    sig_histos_ = []
    sig_histCategories_ = []          

    ##-- Get cut
    REGION_CUT = ""
    if(region == "SB"): REGION_CUT = "(CMS_hgg_mass <= 115 || CMS_hgg_mass >= 135)"
    elif(region == "SR"): REGION_CUT = "(CMS_hgg_mass > 115 && CMS_hgg_mass < 135)"
    elif(region == "FullRegion"): REGION_CUT = "(CMS_hgg_mass >= 100 && CMS_hgg_mass <= 180)"
    else: 
        print"Input region ",region,"is not defined"
        print"Exiting"
        exit(1)

    S_WEIGHT = "1*weight"
    ZERO_CUT = "ZERO_CUT"
    S_CUT = "%s*(%s)*(%s)"%(S_WEIGHT,REGION_CUT,ZERO_CUT)    
    S_CUT += "*(%s)"%(cut)  
    # S_CUT = S_CUT.replace("goodJets","AtLeast2GoodJets") ## for the case where the data and background ntuples have a different variable name than signal here for the same thing 
    S_CUT = S_CUT.replace("ZERO_CUT","(%s != 0) && (%s != -999)"%(v,v))
    S_CUT_NOWEIGHTS = "%s"%(S_CUT)
    S_CUT_NOWEIGHTS = S_CUT_NOWEIGHTS.replace(S_WEIGHT,"(1)")

    ##-- Get Signal Histogram(s) 
    signalFiles = [] 
    signalFiles.append(signalFile_)
    for i,sigPath in enumerate(signalFiles):
        # sigPath = "%s/%s"%(signalDirec,sigF_)
        sigEnd = sigPath.split('/')[-1]
        sigFile = TFile.Open(sigPath)
        treeName = GetMCTreeName(sigEnd)
        # treeName += "_13TeV_HHWWggTag_0"
        treeName += "_13TeV_HHWWggTag_0"
        MC_Category = GetMCCategory(sigEnd)
        if(verbose):
            # print"Signal File:",sigPath 
            print"Signal:",MC_Category

        # Signal_Trees = TChain('%s%s_13TeV_HHWWggTag_0'%(args_.prefix,treeName))
        Signal_Trees = TChain("Signal_Trees")
        Signal_Trees.Add("%s/%s%s"%(sigPath,prefix,treeName))
        # Signal_Trees.Add("%s/%s%s_13TeV_HHWWggTag_1"%(sigPath,prefix,treeName))
        # Signal_Trees.Add("%s/%s%s_13TeV_HHWWggTag_2"%(sigPath,prefix,treeName))
        # Signal_Trees.Add("%s/%s%s_13TeV_HHWWggTag_3"%(sigPath,prefix,treeName))
        # Signal_Trees.Add("%s/%s%s_13TeV_HHWWggTag_4"%(sigPath,prefix,treeName)) ## - tags 3 and 4 may be here in signal but not data and background

        xbins, xmin, xmax = GetBins(varTitle,DNNbinWidth_)
        # exec("S_h_%s = TH1F('S_h_%s',v,xbins,xmin,xmax)"%(i,i)) 
        # exec("S_h_%s_unweighted = TH1F('S_h_%s_unweighted',v,xbins,xmin,xmax)"%(i,i)) 

        # edges = array('d',[0.1000,0.2,0.3,0.4,0.5,0.630000,0.7,0.84000,0.89000,1.0001])
        edges = array('d',[0.1000,0.15, 0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.630000,0.7,0.75,0.84000,0.89000,1.0001])
        N_bins_special = len(edges) - 1

        if(varTitle == "evalDNN_HH"):
            exec("S_h_%s = TH1F('S_h_%s',v,N_bins_special,edges)"%(i,i)) 
            exec("S_h_%s_unweighted = TH1F('S_h_%s_unweighted',v,N_bins_special,edges)"%(i,i))             
        else:
            exec("S_h_%s = TH1F('S_h_%s',v,xbins,xmin,xmax)"%(i,i)) 
            exec("S_h_%s_unweighted = TH1F('S_h_%s_unweighted',v,xbins,xmin,xmax)"%(i,i))             


        thisHist = eval("S_h_%s"%(i))
        mcColor = GetMCColor(MC_Category) 
        ##-- Style options for signal to distinguish from Data, Background 
        # eval("MC_h_tmp_%s.SetFillColor(eval(mcColor))"%(i))
        # eval("MC_h_tmp_%s.SetFillStyle(3004)"%(i))
        ##-- 
        #S_CUT = "weight*(CMS_hgg_mass >= 115 && CMS_hgg_mass <= 135)"
        # eval("MC_h_tmp_%s.SetFillColorAlpha(eval(mcColor),0.1)"%(i))
        # eval("MC_h_tmp_%s.SetLineColor(eval(mcColor))"%(i))
        eval("S_h_%s.SetFillColorAlpha(eval(mcColor),0.1)"%(i))
        eval("S_h_%s.SetLineColor(eval(mcColor))"%(i))        
        # exec('Signal_Trees.Draw("%s >> MC_h_tmp_%s","%s")'%(v,i,SIGNAL_CUT))
        exec('Signal_Trees.Draw("%s >> S_h_%s","%s")'%(v,i,S_CUT))
        exec('Signal_Trees.Draw("%s >> S_h_%s_unweighted","%s")'%(v,i,S_CUT_NOWEIGHTS))
        SigXS_Scale = GetXScale("Signal") # how to scale the XS which is by default in flashgg 1fb
        if(verbose): print"SigXS_Scale: ",SigXS_Scale
        eval("S_h_%s.Scale(float(Lumi))"%(i))
        eval("S_h_%s.Scale(float(SigXS_Scale))"%(i))       

        S_ = eval("S_h_%s.Integral()"%(i))
        S_unweighted_ = eval("S_h_%s_unweighted.Integral()"%(i))

        newHist = thisHist.Clone("newHist")

        ##-- Set title based on treeName 
        newHist.SetTitle(MC_Category)
        newHist.GetXaxis().SetTitle(sigPath)
        newHist.SetLineStyle(1)
        newHist.SetLineWidth(5)

        newHist.SetDirectory(0)
        sig_histos_.append(newHist)
        sig_histCategories_.append(MC_Category)     

    return sig_histos_, sig_histCategories_, S_, S_unweighted_

##-- Main Data / MC module 
# def PlotDataMC(dataFiles_,mcFiles_,signalFiles_,dataDirec_,mcDirec_,signalDirec_,Tags_,ol_,args_,region_,DNNbinWidth_):
def PlotDataMC(dataFile_,bkgFiles_,signalFile_,ol_,args_,region_,cut,cutName,DNNbinWidth_, ratioMin, ratioMax, withKinWeight_):
    ##-- Misc 
    print"Plotting Data / MC and Signal"
    gROOT.ProcessLine("gErrorIgnoreLevel = kError") # kPrint, kInfo, kWarning, kError, kBreak, kSysError, kFatal
    gStyle.SetOptStat(0)     


    # turqoise = TColor(9999, 26/255., 188/255., 156/255.)
    # gROOT.ForceStyle() 
    # gStyle.ls()

    #gStyle.SetErrorX(0.0001)  
    chi2 = 0

    ##-- Output
    outputFolder = "%s/%s"%(ol_,cutName)
    if(not os.path.exists(outputFolder)):
        os.system('mkdir %s'%(outputFolder))
        os.system('cp %s/index.php %s'%(ol_,outputFolder))  

    ##-- Get Variables
    # If var batch is loose, need separate titles for variables since it will be sum of vars * bools 
    if(args_.VarBatch == "Loose"):
        Variables, varNames = GetVars(args_.VarBatch) # get vars from var batch 
        if(args_.verbose):
            print"Variables = ",Variables 
            print"varNames = ",varNames
    else: Variables = GetVars(args_.VarBatch) # get vars from var batch 
        
    if(args_.verbose): 
        print "cut:",cut   
        print "cutName:",cutName        
        print "vars:",Variables   

    ##-- For each Variable 
    for iv,v in enumerate(Variables):
        # legend = TLegend(0.55,0.65,0.89,0.89)
        if(v == "evalDNN_HH"):
            leg_xmin, leg_ymin, leg_xmax, leg_ymax = 0.25, 0.55, 0.65, 0.89
        else:
            leg_xmin, leg_ymin, leg_xmax, leg_ymax = 0.55, 0.55, 0.89, 0.89
        legend = TLegend(leg_xmin, leg_ymin, leg_xmax, leg_ymax)
        legend.SetNColumns(1)
        legend.SetTextSize(0.025)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)        
        if(args_.VarBatch == "Loose"): varTitle = varNames[iv]
        else: varTitle = GetVarTitle(v)    

        # specialVarTitles = {"Scaled_Leading_Photon_pt" : "",
        #                     "Scaled_Subleading_Photon_pt" : ""
        #                 }
        # if(varTitle in specialVarTitles.keys()):
        #     varTitleLabel = specialVarTitles[varTitle]
        # else:
        #     varTitleLabel = varTitle

        if(args_.verbose): print"Plotting variable:",varTitle
        xbins, xmin, xmax = GetBins(varTitle,DNNbinWidth_)
        # xbins, xmin, xmax = GetBins(varTitle)

        ##-- In either case, SB or SR, get backgrounds and signal(s)
        bkgStack = THStack("bkgStack","bkgStack")
        bkgHistos, bkgHistCategories, Bkg_Names, Bkg_Nevents, Bkg_Nevents_unweighted = GetBackgroundHists(bkgFiles_,args_.noQCD,args_.verbose,args_.prefix,varTitle,region_,v,args_.Lumi,cut,cutName,DNNbinWidth_,withKinWeight_)         
        sig_histos, sig_histCategories,  S_, S_unweighted_ = GetSignalHists(signalFile_,args_.prefix,v,region_,varTitle,args_.Lumi,args_.verbose,cut,DNNbinWidth_)

        MC_AddedtoLegend = {
           "\gamma+jet" : 0,
           "\gamma\gamma+jets" : 0,
           "W\gamma(s)+jets" : 0,
           "tt\gamma(s)+jets" : 0,
           "H\\rightarrow\gamma\gamma": 0,
           "Signal" : 0, # if "1", do not add to legend (this is a hardcoded hack :) )
        }

        Signals_AddedtoLegend = {
            "Signal" : 0 # if "1", do not add to legend
            # "Signal" : 1 # if "1", do not add to legend
        }

        ##-- Order histograms by MC category 
        orderedHistos = OrderHistos(bkgHistos,bkgHistCategories)
        sig_orderedHistos = OrderHistos(sig_histos,sig_histCategories)

        ##-- Add backgrounds to background stack 
        for h in orderedHistos:
            h.Sumw2()
            bkgStack.Add(h,'hist')
            bkgName = h.GetTitle()
            print"Adding MC:",bkgName
            added = MC_AddedtoLegend[bkgName]
            if(bkgName == "Signal"): continue 
            if(added): continue 
            else:
                legend.AddEntry(h,bkgName,"F")
                MC_AddedtoLegend[bkgName] = 1        

        ##-- Add text box with selection type 
        region_labels = {
            "SB" : "Sidebands",
            "SR" : "Signal Region",
            "FullRegion" : "FullRegion"
        }

        region_label = region_labels[region_]
        offset = 0
        selText = TLatex(0.129,0.85,cutName)
        selText.SetNDC(1)
        selText.SetTextSize(0.04)   
        CatText = TLatex(0.129,0.8,region_label)
        CatText.SetNDC(1)
        CatText.SetTextSize(0.04)                                                 
        stackSum = bkgStack.GetStack().Last() #->Draw(); # for computing ratio 
        stackSum.Sumw2() 
        stackSum.SetLineColor(kBlack)
        #stackSum.SetLineWidth(3)
        #stackSum.SetFillStyle(0)
        #stackSum.SetLineStyle(7) # to distinguish from data uncertainty 

        # # the purpose of this clone is to try and plot shaded error bands on the background stack sum 
        # stackSum_clone_forError = stackSum.Clone("stackSum_clone_forError")

        # #binWidth = stackSum_clone_forError.GetXaxis().GetBinWidth(0)
        # #print("binWidth:",int(binWidth))

        # stackSum_clone_forError.SetFillStyle(0)
        # stackSum_clone_forError.SetLineColorAlpha(kBlack, 0.5)
        # stackSum_clone_forError.SetLineStyle(2)
        # stackSum_clone_forError.SetLineWidth(10)

        stackSum_clone_forError = stackSum.Clone("stackSum_clone_forError")

        #binWidth = stackSum_clone_forError.GetXaxis().GetBinWidth(0)
        #print("binWidth:",int(binWidth))
        #nhatchsp = gStyle.GetHatchesSpacing()
        #print("nhatchsp:",nhatchsp)
        gStyle.SetHatchesSpacing(0.5)
        # stackSum_clone_forError.SetLineColorAlpha(kBlack,0)
        stackSum_clone_forError.SetFillStyle(3353)
        stackSum_clone_forError.SetFillColorAlpha(kYellow+4, 1)
        # stackSum_clone_forError.SetLineStyle(0.)
        stackSum_clone_forError.SetLineWidth(0)
        stackSum_clone_forError.SetMarkerSize(0)

        # for i,bin in enumerate(stackSum_clone_forError):
            # stackSum_clone_forError.SetBinError(i,0.000001)
        #print("stack type:",type(stackSum_clone_forError))
        #stackSum_clone_forError.SetLineColorAlpha(kBlack, 0.5)
        #stackSum_clone_forError.SetLineStyle(2)
        #stackSum_clone_forError.SetLineWidth(10)        

        stackSum_clone = stackSum.Clone("stackSum_clone")
        stackSum_clone.SetDirectory(0)

        # B_vals_ = GetBinVals(stackSum_clone)
        S_vals_ = GetBinVals(sig_orderedHistos[0]) ## assuming 1 signal 

        # for s_val in S_vals_:
            # print"s_val:",s_val

        # for b_val in B_vals_:
            # print"b_val:",b_val    

        # B = sum(Bkg_Nevents)
        # S = sum(S_vals_)
        # print("B = ",B)

        ##-- By default draw background save background contributions. Later delete if not wanted 
        bkgOutName = "%s/BackgroundsPADS_%s_%s.png"%(outputFolder,varTitle,region_)
        SimpleDrawHisto(bkgStack,"PADS",bkgOutName,varTitle)
        bkgOutName = bkgOutName.replace(".png",".pdf")
        SimpleDrawHisto(bkgStack,"PADS",bkgOutName,varTitle) 

        drawLabels = 0  

        ##-- If Plotting in the Sidebands or full region, Get Data and combine plots 
        if(region_ == "SB" or region_ == "FullRegion"):
            # define selections 
            # just use combined tag always. Define a category or look at cut based analysis categories by making selections 
            DataHist = GetDataHist(dataFile_,args_.prefix,cut,cutName,iv,v,varTitle,args_.VarBatch,args_.verbose,DNNbinWidth_,region_) ## assuming one data file!
            dataNevents = DataHist.GetEntries()
            # legend.AddEntry(DataHist,"Data","P")
            DataHist.SetLineColor(kBlack)
            DataHist.Sumw2()
            xTitle = GetXaxisTitle(varTitle)
            DataHist.GetXaxis().SetTitle(xTitle)

            DataHist.SetLineColorAlpha(kBlack, 0)

            if(args_.log): 
                if(args_.verbose): print "Setting histogram minimums"
                # print"Setting histogram minimums"
                #bkgStack.SetMinimum(1)
                DataHist.SetMinimum(1.)
                stackSum.SetMinimum(1.)
                bkgStack.SetMinimum(1.)
                #bkgStack.SetMinimum(0.0001)            
                #stackSum.SetMinimum(0.0001)
                #bkgStack.SetMinimum(0.0001)            

            # Convert DataHist into TGraphErrors in order to remove x errors 
            nBins = DataHist.GetNbinsX()
            # print("nBins:",nBins)
            x_ = []
            ex_= [] 
            y_ = []
            ey_ = []
            
            for i,bin in enumerate(DataHist):
                if(i == 0): continue # skip underflow bin 
                if(i == (nBins + 1)): continue # skip overflow bin 
                #print("i:",i)
                #print("bin:",bin)       
                #print("center_value:",DataHist.GetBinCenter(i))
                #print("yerr:",DataHist.GetBinError(i))   
                center_value = DataHist.GetBinCenter(i)
                yerr = DataHist.GetBinError(i)

                x_.append(center_value)
                ex_.append(0.0001) 
                y_.append(bin)
                ey_.append(yerr)
                
            x  = array( 'f', x_ )
            ex = array( 'f', ex_ )
            y  = array( 'f', y_ )
            ey = array( 'f', ey_ )

            print("Data x:",x)

            Data_gr = TGraphErrors( nBins, x, y, ex, ey )
            Data_gr.SetMarkerStyle(8)
            Data_gr.SetMarkerSize(1)

            ##-- Optional: Scale Backgrounds to SF: Data sidebands sum / Background sidebands sum
            SidebandSF_ = 1 
            if(args_.SidebandScale):
                data_sidebands_sum = DataHist.Integral() ##-- data hist is already in sidebands only 
                background_sidebands_sum = stackSum.Integral()
                if(background_sidebands_sum > 0): SidebandSF_ = float(data_sidebands_sum / background_sidebands_sum)
                else: 
                    print "background sidebands sum <= 0. Setting sideband scale factor to 1"
                    SidebandSF_ = 1
                print "data sum in sidebands:",data_sidebands_sum
                print "backgrounds sum in sidebands:",background_sidebands_sum
                print "Sideband scale factor:",SidebandSF_
                for background in bkgStack.GetStack():
                    background.Scale(SidebandSF_)
                stackSum = bkgStack.GetStack().Last() #->Draw(); # for computing ratio 

                # the purpose of this clone is to try and plot shaded error bands on the background stack sum 
                stackSum_clone_forError = stackSum.Clone("stackSum_clone_forError")

                #binWidth = stackSum_clone_forError.GetXaxis().GetBinWidth(0)
                #print("binWidth:",int(binWidth))
                #nhatchsp = gStyle.GetHatchesSpacing()
                #print("nhatchsp:",nhatchsp)
                gStyle.SetHatchesSpacing(0.5)
                #stackSum_clone_forError.SetLineColorAlpha(kBlack,0)
                stackSum_clone_forError.SetFillStyle(3353)
                stackSum_clone_forError.SetFillColorAlpha(kYellow+4, 1)
                # stackSum_clone_forError.SetLineStyle(0.)
                #stackSum_clone_forError.SetLineWidth(10)
                stackSum_clone_forError.SetMarkerSize(0)

                # for i,bin in enumerate(stackSum_clone_forError):
                    # stackSum_clone_forError.SetBinError(i,0.000001)
                #print("stack type:",type(stackSum_clone_forError))
                #stackSum_clone_forError.SetLineColorAlpha(kBlack, 0.5)
                #stackSum_clone_forError.SetLineStyle(2)
                #stackSum_clone_forError.SetLineWidth(10)

                # stackSum.Scale(SidebandSF)     

            # # if plotting full region unblinded, add signal
            # if(region_ == "FullRegion"):


            ##-- Compute chi squared 
            chi2 = GetChiSquared(DataHist,stackSum)
            # print"chi2 = ",chi2 
            chi2Text = TLatex(0.129,0.75,"#Chi^{2} = %.5g"%(chi2))       
            chi2Text.SetNDC(1)
            chi2Text.SetTextSize(0.04)    
            #for i,bin in enumerate(stackSum):
                #binUnc = bin**(1/2)
                #print("bin %s: yield equals: %s"%(i,bin))
                #print("contained uncertainty: ",stackSum.GetBinError(i))
                #print("uncer from sqrt:",binUnc)
                #stackSum.SetBinError(i,binUnc)

            # print bin errors:

            #for i, bin in enumerate(stackSum)

            ##-- Define ratio plot for computing Data / MC ratio 
            # print("")
            # print("~~~~~~~~~~~~~~DataHist:",DataHist)
            # print("~~~~~~~~~~~~~~stackSum:",stackSum)
            # print("DataHist xmax:",DataHist.GetXaxis().GetXmax())
            # print("stackSum xmax:",stackSum.GetXaxis().GetXmax())
            # print("")

            DataHist.SetTitle("")
            stackSum.SetTitle("")

            rp = TRatioPlot(DataHist,stackSum)
            #rp.SetH1DrawOpt("") # whether or not to draw data from datahist object 
            rp.SetH2DrawOpt("hist")
            # rp.SetH2DrawOpt("PE2")
            # rp.SetGraphDrawOpt("PE2")
            dMax = DataHist.GetMaximum()
            bMax = stackSum.GetMaximum()

            maxHeight = max(dMax,bMax) 

            ##-- Create the entire picture: Combine Data, MC, Data / MC ratio and signal in one plot 
            for fileType in ["pdf"]:
                #gStyle.SetErrorX(0.0001)
                # varTitle = GetVarTitle(v)
                outName = "%s/DataMC_%s_%s.%s"%(outputFolder,varTitle,region_,fileType)
                if(args_.log): outName = "%s/DataMC_%s_%s_log.%s"%(outputFolder,varTitle,region_,fileType)
                else: outName = "%s/DataMC_%s_%s_nonLog.%s"%(outputFolder,varTitle,region_,fileType)                        
                DataMCRatio_c = TCanvas("DataMCRatio_c","DataMCRatio_c",600,800)

                # rp.SetTitle("")

                rp.Draw("nogrid")
                
                rp.GetLowYaxis().SetNdivisions(5)

                DataMCRatio_c.Update()

                ratioGraph = rp.GetCalculationOutputGraph()
                ratioGraph.SetMarkerStyle(8)
                ratioGraph.SetMarkerSize(1)

                rp.GetUpperRefYaxis().SetTitle("Entries")   
                rp.GetLowerRefYaxis().SetTitle("Data / MC")
                rp.GetLowerPad().Update()
                if(args_.log): rp.GetUpperRefYaxis().SetRangeUser(0.01,maxHeight*1000.)   
                else: rp.GetUpperRefYaxis().SetRangeUser(0,maxHeight*1.4) # to make room for plot text 

                UpperPad = rp.GetUpperPad()
                UpperPad.cd()

                #"""
                # print("   ")
                # print("~~~~~~~~~~~~~~~bkgStack xmax:",bkgStack.GetXaxis().GetXmax())
                # print("   ")

                bkgStack.SetTitle("")

                bkgStack.Draw("same")
                stackSum_clone_forError.SetLineWidth(0)
                stackSum_clone_forError.Draw("sameE0E2")                
                #"""

                # print("   ")
                # print("~~~~~~~~~~~~~~~Data_gr xmax:",Data_gr.GetXaxis().GetXmax())
                # print("   ")

                #"""
                Data_gr.Draw("samePE1") 
                #"""

                for sig_hist in sig_histos:
                    sigMax = sig_hist.GetMaximum()
                    if sigMax == 0: sigMax = 1 

                    ##-- No user input signal scale 
                    if(args_.SigScale == -999): 
                        sigScale = (float(maxHeight)/10.) / float(sigMax) # in order to scale signal to 10th of max of plot 
                        sig_hist.Scale(sigScale)  

                    ##-- User input signal scale 
                    else:
                        if(args_.verbose): print"user sig scale:",args_.SigScale
                        sigScale = args_.SigScale
                        sig_hist.Scale(sigScale) 
                                                
                    for sig_h in sig_orderedHistos:
                        # sigName = "%s X %d"%(sig_h.GetTitle(),sigScale)
                        sigName = sig_h.GetTitle()
                        added = Signals_AddedtoLegend[sigName]
                        if(added): continue 
                        else:
                            legend.AddEntry(sig_h,"%s * %.5g"%(sig_h.GetTitle(),sigScale),"FL")
                            Signals_AddedtoLegend[sigName]  

                    # print("   ")
                    # print("~~~~~~~~~~~~~~~sig_hist xmax:",sig_hist.GetXaxis().GetXmax())
                    # print("   ")
                    

                    #"""
                    sig_hist.Draw("samehist")
                    #"""

                legend.AddEntry(DataHist,"Data","P")
                legend.Draw("same")
                if(drawLabels):
                    selText.Draw("same")
                    CatText.Draw("same")
                    chi2Text.Draw("same")
                rp.GetLowerRefGraph().SetMinimum(ratioMin)
                rp.GetLowerRefGraph().SetMaximum(ratioMax)     
                Npoints = rp.GetLowerRefGraph().GetN()
                # print(" ")
                # print("~~~~~~~~~~~~~~Npoints:",Npoints)
                # print(" " )
                #"""
                for ip in range(0,Npoints):
                    rp.GetLowerRefGraph().SetPointEXhigh(ip,0)  
                    rp.GetLowerRefGraph().SetPointEXlow(ip,0)  
                #"""

                if(args_.log): 
                    UpperPad.SetLogy()
                    UpperPad.Update() 

                UpperPad.cd()
                UpperPad.Update()

                # Add TLines if plotting DNN score
                if(varTitle == "evalDNN_HH"):

                        # exec("ThisLine = TLine(Boundary,UpperPad.GetUymin(),Boundary,maxHeight*100.)")
                        # ThisLine = TLine(Boundary,UpperPad.GetUymin(),Boundary,maxHeight*100.)
                        # ThisLine.SetLineStyle(3)
                        # ThisLine.Draw("same")

                        BoundaryLine_1 = TLine(0.63,UpperPad.GetUymin(),0.63,maxHeight*1000.)
                        BoundaryLine_2 = TLine(0.84,UpperPad.GetUymin(),0.84,maxHeight*1000.)
                        BoundaryLine_3 = TLine(0.89,UpperPad.GetUymin(),0.89,maxHeight*1000.)

                        BoundaryLine_1.SetLineStyle(3)
                        BoundaryLine_2.SetLineStyle(3)
                        BoundaryLine_3.SetLineStyle(3)

                        BoundaryLine_1.Draw("same")
                        BoundaryLine_2.Draw("same")
                        BoundaryLine_3.Draw("same")

                    # Boundaries = [0.63, 0.84, 0.89,1.0]
                    # for Boundary in Boundaries:
                    #     exec("ThisLine = TLine(Boundary,UpperPad.GetUymin(),Boundary,maxHeight*100.)")
                    #     ThisLine.SetLineStyle(3)
                    #     ThisLine.Draw("same")


                # rp.GetUpperRefXaxis().SetRangeUser(0.1,1)

                rp.GetLowerPad().cd()

                # lowerPad.SetUxmax(1)
                # rp.GetLowerRefXaxis().SetRangeUser(0.1,1)

                lowerPad = rp.GetLowerPad()
                # lowerPad.GetXAxis().SetRangeUser(0.1,1)
                # lowerPad.
                lowerPad.Update()
                lowerPad.cd()

                # print("lowerPad.GetUxmin():",lowerPad.GetUxmin())
                # print("lowerPad.GetUxmax():",lowerPad.GetUxmax())

                rp.GetLowerRefYaxis().SetTitle("Data / MC")
                lineAtOne = TLine(lowerPad.GetUxmin(),1,lowerPad.GetUxmax(),1)
                lineAtOne.SetLineStyle(3)
                lineAtOne.Draw("same")


                

                # writeExtraText = True       #// if extra text
                # extraText  = "Preliminary"#;  // default extra text is "Preliminary"
                # lumi_8TeV  = "19.1 fb^{-1}"#; // default is "19.7 fb^{-1}"
                # lumi_7TeV  = "4.9 fb^{-1}"#;  // default is "5.1 fb^{-1}"
                # lumi_sqrtS = "13 TeV"#;       // used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)   

                # CMS_lumi( DataMCRatio_c, 4,  20)


                rp.GetLowerPad().Update()       

                # setTDRStyle() # https://ghm.web.cern.ch/ghm/plots/

                DataMCRatio_c.Update()                
                DataMCRatio_c.SaveAs(outName) 
                outName = outName.replace(".pdf",".png")                    
                DataMCRatio_c.SaveAs(outName)   
                outName = outName.replace(".png",".C")          
                DataMCRatio_c.SaveAs("out.C")          

        ##-- If plotting in the signal region, Combine Background and Signal(s)
        elif(region_ == "SR"):
            print "Plotting Signal Region"

            # plotLog = 1 ##-- Plot signal region selected plots in log scale by default since HH->WWgg signal is small 
            # upperPlotymin = 0.001           
            plotLog = args_.log
            if(plotLog): upperPlotymin = 0.001
            else: upperPlotymin = 0 
            dataNevents = 0 
            ##-- Optional: Scale Backgrounds to SF: Data sidebands sum / Background sidebands sum
            SidebandSF_ = 1 
            if(args_.SidebandScale):
                DataHist = GetDataHist(dataFile_,args_.prefix,cut,cutName,iv,v,varTitle,args_.VarBatch,args_.verbose, DNNbinWidth_,region_) ## assuming one data file!
                data_sidebands_sum = DataHist.Integral() ##-- data hist is already in sidebands only..or not, depending on the region.

                ##-- If region is SR, need to draw background in SB in order to obtain proper SF 
                bkgStack_sidebands = THStack("bkgStack_sidebands","bkgStack_sidebands")
                bkgHistos_sidebands, bkgHistCategories_sidebands, Bkg_Names_sidebands, Bkg_Nevents_sidebands, Bkg_Nevents_unweighted_sidebands = GetBackgroundHists(bkgFiles_,args_.noQCD,args_.verbose,args_.prefix,varTitle,"SB",v,args_.Lumi,cut,cutName,DNNbinWidth_,withKinWeight_) ##-- Sidebands     
                orderedHistos_sidebands = OrderHistos(bkgHistos_sidebands,bkgHistCategories_sidebands)
                for h in orderedHistos_sidebands:
                    h.Sumw2()
                    bkgStack_sidebands.Add(h,'hist')
                stackSum_sidebands = bkgStack_sidebands.GetStack().Last() #->Draw(); # for computing ratio 
                background_sidebands_sum = stackSum_sidebands.Integral()
                if(background_sidebands_sum > 0): SidebandSF_ = float(data_sidebands_sum / background_sidebands_sum)
                else: 
                    print "background sidebands sum <= 0. Setting sideband scale factor to 1"
                    SidebandSF_ = 1
                print "data sum in sidebands:",data_sidebands_sum
                print "backgrounds sum in sidebands:",background_sidebands_sum
                print "Sideband scale factor:",SidebandSF_
                for background in bkgStack.GetStack():
                    background.Scale(SidebandSF_)
                stackSum = bkgStack.GetStack().Last() #->Draw(); # for computing ratio 

            Signal_h_clone = sig_histos[0].Clone("Signal_h_clone")  ##-- assuming you want the ratio with the first signal in the list 
            Signal_h_clone.SetDirectory(0)
            xTitle = GetXaxisTitle(varTitle)
            Signal_h_clone.GetXaxis().SetTitle(xTitle)
            # Signal_h_clone.SetTitle(varTitle)
            # Signal_h_clone.SetTitle("")

            stackSum_clone = stackSum.Clone("stackSum_clone")
            stackSum_clone.SetDirectory(0)
            # B_vals_ = GetBinVals(stackSum_clone)

            # ## get Signal values to later compute S / sqrt(B)
            # S_vals_ = GetBinVals(Signal_h_clone)
            # S_vals_ = []
            # for i in range(0,xbins):
            #     S_val = Signal_h_clone.GetBinContent(i+1) # i+1 to avoid underflow bin
            #     S_vals_.append(S_val)
            #     # if(S_val != 0.0): S_vals_.append(S_val)
            # print "S_vals_:",S_vals_ ## if any of these are zero or background is zero in a bin, you may have problems with the S / sqrt(B) plot 

            # B_vals_ = [] 
            # for i in range(0,xbins):
            #     B_val = stackSum_clone.GetBinContent(i+1)
            #     B_vals_.append(B_val)
            #     # if(B_val != 0.0): B_vals_.append(B_val)

            for i,bin in enumerate(stackSum):
                print("")
                print("~~~~~~~~~On stack sum bin:",i)
                print("")
                
                binUnc = bin**(1/2)
                # print"bin %s: yield equals: %s"%(i,bin) 
                # print"uncertainty: ",stackSum.GetBinError(i)
                stackSum.SetBinError(i,binUnc)

            rp = TRatioPlot(Signal_h_clone,stackSum) ## S / B

            rp.SetH1DrawOpt("hist")
            rp.SetH2DrawOpt("hist")
            # dMax = DataHist.GetMaximum()
            sMax = Signal_h_clone.GetMaximum()
            bMax = stackSum.GetMaximum()

            # maxHeight = max(sMax,bMax) 
            maxHeight = max(sMax,bMax) 

            ##-- Create the entire picture: Combine Data, MC, Data / MC ratio and signal in one plot 
            for fileType in ["pdf"]:
                #gStyle.SetErrorX(0.0001)
                # varTitle = GetVarTitle(v)
                outName = "%s/DataMC_%s_%s.%s"%(outputFolder,varTitle,region_,fileType)
                if(plotLog): outName = "%s/DataMC_%s_%s_log.%s"%(outputFolder,varTitle,region_,fileType)
                else: outName = "%s/DataMC_%s_%s_nonLog.%s"%(outputFolder,varTitle,region_,fileType)                        
                DataMCRatio_c = TCanvas("DataMCRatio_c","DataMCRatio_c",600,800)
                
                rp.SetTitle("")
                
                rp.Draw("nogrid")
                rp.GetLowYaxis().SetNdivisions(5)
                DataMCRatio_c.Update()

                ratioGraph = rp.GetCalculationOutputGraph()
                ratioGraph.SetMarkerStyle(8)
                ratioGraph.SetMarkerSize(0.5)

                # rp.SetGraphDrawOpt("EP")
                # rp.SetGraphDrawOpt("EPZ2")
                # rp.GetLowerRefYaxis().SetTitle("Data / MC")

                rp.GetUpperRefYaxis().SetTitle("Entries")   
                rp.GetLowerPad().Update()
                if(plotLog): rp.GetUpperRefYaxis().SetRangeUser(upperPlotymin,maxHeight*10000.)   
                # else: rp.GetUpperRefYaxis().SetRangeUser(0,maxHeight*1.4) # to make room for plot text 
                else: rp.GetUpperRefYaxis().SetRangeUser(0,maxHeight*2.0) # to make room for plot text 
                        
                bkgStack.SetTitle("")
                stackSum.SetTitle("")

                UpperPad = rp.GetUpperPad()
                UpperPad.cd()
                bkgStack.Draw("same")
                stackSum.Draw("sameE")
                # DataHist.Draw("samePE")
                for sig_hist in sig_histos:
                    sigMax = sig_hist.GetMaximum()
                    if sigMax == 0: sigMax = 1 

                    ##-- No user input signal scale 
                    if(args_.SigScale == -999): 
                        sigScale = (float(maxHeight)/10.) / float(sigMax) # in order to scale signal to 10th of max of plot 
                        sig_hist.Scale(sigScale)  

                    ##-- User input signal scale 
                    ##-- NOTE this will plot something that doesn't correspond to the ratio of S to B if sig scale != 1 
                    else:
                        if(args_.verbose): print"user sig scale:",args_.SigScale
                        sigScale = args_.SigScale
                        sig_hist.Scale(sigScale) 
                                                
                    for sig_h in sig_orderedHistos:
                        # sigName = "%s X %d"%(sig_h.GetTitle(),sigScale)
                        sigName = sig_h.GetTitle()
                        added = Signals_AddedtoLegend[sigName]
                        if(added): continue 
                        else:
                            legend.AddEntry(sig_h,"%s * %.5g"%(sig_h.GetTitle(),sigScale),"FL")
                            Signals_AddedtoLegend[sigName]                            
                    sig_hist.Draw("same hist")
                # legend.AddEntry(DataHist,"Data","P")
                legend.Draw("same")
                if(drawLabels):
                    selText.Draw("same")
                    CatText.Draw("same")
                # chi2Text.Draw("same")

                Npoints = rp.GetLowerRefGraph().GetN()
                SosqB_vals = []
                SosqB_min, SosqB_max = 0, 0

                # for ip in range(0,Npoints):
                #     binmin = rp.GetLowerRefGraph().GetPointX(ip)
                #     SoverB = rp.GetLowerRefGraph().GetPointY(ip)
                #     S = S_vals_[ip]
                #     ## calc s / sqrtB) from here and then just plot it on lower graph 
                #     # print "binmind: ",binmin
                #     # print "S:",S
                #     # print "SoverB:",SoverB  
                #     # sqrtB = (SoverB**-1)*S
                #     B = S*(1 / SoverB)
                #     if(B<=0): sqrtB = 0
                #     else: sqrtB = B**1/2
                #     if(sqrtB <= 0 or S == 0): SoversqrtB = 0
                #     else: SoversqrtB = S / sqrtB
                    
                #     # print "SoversqrtB:",SoversqrtB
                #     SosqB_vals.append(SoversqrtB)
                
                # SosqB_min, SosqB_max = min(SosqB_vals), max(SosqB_vals)
                # lowerPlotMin, lowerPlotMax = SosqB_min / 2 , SosqB_max * 2

                for ip in range(0,Npoints):
                    rp.GetLowerRefGraph().SetPointEXhigh(ip,0)  
                    rp.GetLowerRefGraph().SetPointEXlow(ip,0) 
                    # rp.GetLowerRefGraph().SetPointY(ip,SosqB_vals[ip]) 
                # rp.GetLowerRefGraph().SetMinimum(lowerPlotMin)
                # rp.GetLowerRefGraph().SetMaximum(lowerPlotMax)                      
                if(plotLog): 
                    UpperPad.SetLogy()
                    UpperPad.Update() 
                rp.GetLowerPad().cd()
                lowerPad = rp.GetLowerPad()
                # rp.GetLowerRefYaxis().SetTitle("S / #sqrt{B}") # this is what we want but not there yet     
                rp.GetLowerRefYaxis().SetTitle("S / B") # this is what we want but not there yet     
                lineAtOne = TLine(lowerPad.GetUxmin(),1,lowerPad.GetUxmax(),1)
                lineAtOne.SetLineStyle(3)
                lineAtOne.Draw("same")
                rp.GetLowerPad().Update()                        
                DataMCRatio_c.Update()                
                DataMCRatio_c.SaveAs(outName) 
                outName = outName.replace(".pdf",".png")                    
                DataMCRatio_c.SaveAs(outName)  

        if(not args_.drawPads):
            bkgOutName = "%s/BackgroundsPADS_%s_%s.png"%(outputFolder,varTitle,region_)
            os.system('rm %s'%(bkgOutName))
            bkgOutName = bkgOutName.replace(".png",".pdf")
            os.system('rm %s'%(bkgOutName))

        ##-- Only create yields table for 0th variable because yields are cut dependent, not variable dependent
        if(iv==0): 
            print"SidebandSF_:",SidebandSF_
            B_vals_ = [] 
            CreateYieldsTable(region_,cutName,Bkg_Names,args_.removeBackgroundYields,S_vals_,B_vals_,dataNevents,SidebandSF_,Bkg_Nevents,ol_,Bkg_Nevents_unweighted, S_, S_unweighted_) 
        
        ## For each variable loop ends here 

    return chi2
    
