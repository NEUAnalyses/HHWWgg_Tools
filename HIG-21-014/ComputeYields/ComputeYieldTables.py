"""
10 June 2022
Abraham Tishelman-Charny

The purpose of this python module is to produce yields tables for each WW final state before and after preselections.
"""

import uproot 
import numpy as np 

# d = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/2017/"
# f_ = "%s/Signal/SL_NLO_2017_hadded/GluGluToHHTo2G2Qlnu_node_cHHH1_2017.root"%(d)

"""
Parameters
"""
verbose = 0
round_digits = 4
Min_MC_Events = 100
bkg_d = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/2017/Backgrounds/"
process_types = ["HH"]
# process_types = ["Continuum_Background", "Single_Higgs", "HH"]

Continuum_Background_Files = [
    "DiPhotonJetsBox_M40_80.root",     
    "DiPhotonJetsBox_MGG-80toInf.root",
    "DYJetsToLL_M-50.root",
    "GJet_Pt-20to40.root",
    "GJet_Pt-20toInf.root",
    "GJet_Pt-40toInf.root",
    "QCD_Pt-30to40.root",
    "QCD_Pt-30toInf.root",
    "QCD_Pt-40toInf.root",
    "THQ_ctcvcp.root",
    "TTGG_0Jets.root",
    "TTGJets_TuneCP5.root",
    "TTJets_HT-1200to2500.root",       
    "TTJets_HT-2500toInf.root",        
    "TTJets_HT-600to800.root",
    "TTJets_HT-800to1200.root",        
    "TTToHadronic.root",
    "ttWJets.root",
    "W1JetsToLNu_LHEWpT_0-50.root",    
    "W1JetsToLNu_LHEWpT_150-250.root", 
    "W1JetsToLNu_LHEWpT_250-400.root", 
    "W1JetsToLNu_LHEWpT_400-inf.root", 
    "W1JetsToLNu_LHEWpT_50-150.root",  
    "W2JetsToLNu_LHEWpT_0-50.root",    
    "W2JetsToLNu_LHEWpT_150-250.root", 
    "W2JetsToLNu_LHEWpT_250-400.root", 
    "W2JetsToLNu_LHEWpT_400-inf.root", 
    "W2JetsToLNu_LHEWpT_50-150.root",  
    "W3JetsToLNu.root",
    "W4JetsToLNu.root",
    "WGGJets.root",
    "WGJJToLNu_EWK_QCD.root",
    "WGJJToLNuGJJ_EWK.root",
    "WWTo1L1Nu2Q.root",
    "WW_TuneCP5.root",
]

Single_Higgs_Files = [
    "GluGluHToGG.root",
    "ttHJetToGG.root",
    "VBFHToGG.root",
    "VHToGG.root",
]

HH_Files = [
    "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/2017/Signal/SL_NLO_2017_hadded/GluGluToHHTo2G2Qlnu_node_cHHH1_2017.root",
    "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/2017/Signal/FH_NLO_2017_hadded/GluGluToHHTo2G4Q_node_cHHH1_2017.root",
    "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/2017/Signal/FL_NLO_2017_hadded/GluGluToHHTo2G2l2nu_node_cHHH1_2017.root",
]

for process_type in process_types:
    print("On process type:",process_type)
    exec("process_files = %s_Files"%(process_type))

    files = []
    MiniAOD_Weighted_Yields = []
    Preselection_Weighted_Yields_0 = [] # semilep
    Preselection_Weighted_Yields_1 = [] # fullyhadr
    Preselection_Weighted_Yields_2 = [] # fullylep

    Preselection_Unweighted_Yields_0 = [] # semilep
    Preselection_Unweighted_Yields_1 = [] # fullyhadr
    Preselection_Unweighted_Yields_2 = [] # fullylep

    HH_Label_Dict = {
        "GluGluToHHTo2G2Qlnu\\_node\\_cHHH1\\_2017": ["Semi-leptonic HH$\\rightarrow WW\gamma\gamma$", "SL"],
        "GluGluToHHTo2G4Q\\_node\\_cHHH1\\_2017": ["Fully-hadronic HH$\\rightarrow WW\gamma\gamma$", "FH"],
        "GluGluToHHTo2G2l2nu\\_node\\_cHHH1\\_2017": ["Fully-leptonic HH$\\rightarrow WW\gamma\gamma$", "FL"],
    }

    XS_BR_Dict = {
        "SL" : (31.049 * 0.000970198 * 0.441),
        "FH" : (31.049 * 0.000970198 * 0.4544),
        "FL" : (31.049 * 0.000970198 * 0.1046),
    }

    # Continuum background 
    for f__ in process_files:
        if(process_type == "HH"): f_ = f__ # directory already there for HH files as defined in above lists 
        else: f_ = "%s/%s"%(bkg_d, f__)

        if(verbose):
            print("On background file:",f_)
        else:
            f_shortname = f_.split('/')[-1]
            print("On background process:",f_shortname)
        files.append(f__)

        if(process_type == "HH"): f = uproot.open(f_)["tagsDumper/trees"] # different TDirectory stucture 
        else: f = uproot.open(f_)

        TreeNames = f.keys()
        if(verbose):
            print("TreeNames:",TreeNames)

        t0, t1, t2, t3 = f[TreeNames[0]], f[TreeNames[1]], f[TreeNames[2]], f[TreeNames[3]]
        # t0, t1, t2, t3 = f["GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0"], f["GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_1"], f["GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_2"], f["GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_3"]

        # before preselections 

        for i in range(0,4):
            exec("weights%s = t%s['weight'].array()"%(i,i))
            exec("weighted_yield_%s = np.sum(weights%s)"%(i,i))
            exec("unweighted_yield_%s = len(weights%s)"%(i,i))

        MiniAOD_Weighted_Yield = weighted_yield_0 + weighted_yield_1 + weighted_yield_2 + weighted_yield_3

        if(verbose):
            print("MiniAOD_Weighted_Yield:",MiniAOD_Weighted_Yield)
            print("Yield_After_Preselections:",weighted_yield_0) # weighted_yield_0 = yield after SL preselections

        MiniAOD_Weighted_Yields.append(MiniAOD_Weighted_Yield)
        Preselection_Weighted_Yields_0.append(weighted_yield_0)
        Preselection_Weighted_Yields_1.append(weighted_yield_1)
        Preselection_Weighted_Yields_2.append(weighted_yield_2)

        Preselection_Unweighted_Yields_0.append(unweighted_yield_0)
        Preselection_Unweighted_Yields_1.append(unweighted_yield_1)
        Preselection_Unweighted_Yields_2.append(unweighted_yield_2)    

    ##-- TeX file table 
    fileName = "%s_Yields-Table.tex"%(process_type)
    file = open(fileName,"w")
    file.write("\\begin{table}[H]\n")
    file.write("\t\\begin{center}\n")
    file.write("\t\t\\begin{tabular}{c|c|c|c|c}\n")
    file.write("\t\t\tMC Sample & Before preselection & SL (efficiency) & FH (efficiency) & FL (efficiency) \\\ \\hline \n")

    # for i, name in enumerate(names):
    for file_i, MC_file in enumerate(files):
        MiniAOD_Yield = MiniAOD_Weighted_Yields[file_i]
        Preselection_Weighted_Yield_0 = Preselection_Weighted_Yields_0[file_i]
        Preselection_Weighted_Yield_1 = Preselection_Weighted_Yields_1[file_i]
        Preselection_Weighted_Yield_2 = Preselection_Weighted_Yields_2[file_i]

        Preselection_Unweighted_Yield_0 = Preselection_Unweighted_Yields_0[file_i]
        Preselection_Unweighted_Yield_1 = Preselection_Unweighted_Yields_1[file_i]
        Preselection_Unweighted_Yield_2 = Preselection_Unweighted_Yields_2[file_i]    

        MC_file = MC_file.replace("_","\_")
        MC_file = MC_file.replace(".root", "")
        MC_file = MC_file.replace("LHEWpT", "WpT")

        if(process_type == "HH"): 
            MC_file = MC_file.split('/')[-1]
            MC_file, finalstate = HH_Label_Dict[MC_file]

            HH_XSTimesBR = XS_BR_Dict[finalstate]

            #### For HH need to include XS and BR 

            MiniAOD_Yield *= HH_XSTimesBR
            Preselection_Weighted_Yield_0 *= HH_XSTimesBR 
            Preselection_Weighted_Yield_1 *= HH_XSTimesBR 
            Preselection_Weighted_Yield_2 *= HH_XSTimesBR             

            

        # Scale by 2017 lumi for 2017 MC 
        MiniAOD_Yield *= 41.5 
        Preselection_Weighted_Yield_0 *= 41.5 
        Preselection_Weighted_Yield_1 *= 41.5 
        Preselection_Weighted_Yield_2 *= 41.5 

        #### For HH need to include branching ratio. 

        ratio_0 = round(Preselection_Weighted_Yield_0 / MiniAOD_Yield, 5)
        ratio_0 *= 100.
        ratio_0 = round(ratio_0, 3)

        ratio_1 = round(Preselection_Weighted_Yield_1 / MiniAOD_Yield, 5)
        ratio_1 *= 100.
        ratio_1 = round(ratio_1, 3)

        ratio_2 = round(Preselection_Weighted_Yield_2 / MiniAOD_Yield, 5)
        ratio_2 *= 100.
        ratio_2 = round(ratio_2, 3)        

        MiniAOD_Yield = round(MiniAOD_Yield, round_digits)
        Preselection_Yield_0 = round(Preselection_Weighted_Yield_0, round_digits)
        Preselection_Yield_1 = round(Preselection_Weighted_Yield_1, round_digits)
        Preselection_Yield_2 = round(Preselection_Weighted_Yield_2, round_digits)


        if(Preselection_Unweighted_Yield_0 < Min_MC_Events): 
            Preselection_Yield_0 = "-"
            ratio_0 = "-"
        if(Preselection_Unweighted_Yield_1 < Min_MC_Events): 
            Preselection_Yield_1 = "-"
            ratio_1 = "-"
        if(Preselection_Unweighted_Yield_2 < Min_MC_Events): 
            Preselection_Yield_2 = "-"
            ratio_2 = "-"                

        file.write("\t\t\t {MC_file} & {MiniAOD_Yield} & {Preselection_Yield_0} ({ratio_0}\%) & {Preselection_Yield_1} ({ratio_1}\%) & {Preselection_Yield_2} ({ratio_2}\%) \\\ \n".format(
            MC_file = MC_file,MiniAOD_Yield=MiniAOD_Yield,
            Preselection_Yield_0=Preselection_Yield_0, ratio_0=ratio_0,
            Preselection_Yield_1=Preselection_Yield_1, ratio_1=ratio_1,
            Preselection_Yield_2=Preselection_Yield_2, ratio_2=ratio_2
            ))

    file.write("\t\t\end{tabular}\n")
    process_type_caption = process_type.replace("_", " ")
    file.write("\t\caption{2017 %s MC before and after preselections for each final state, and process efficiency. Note that for processes with less than %s unweighted MC events after a selection, a null value is shown.}\n"%(process_type_caption, Min_MC_Events))
    file.write("\t\\end{center}\n")
    file.write("\end{table}\n")  

    file.close()

    print("Saving yields table: ",fileName)

