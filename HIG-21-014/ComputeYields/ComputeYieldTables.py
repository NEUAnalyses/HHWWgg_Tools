"""
10 June 2022
Abraham Tishelman-Charny

The purpose of this python module is to produce yields tables for each WW final state before and after preselections.

Example usage:
python3 ComputeYieldTables.py 

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

Min_MC_Events = 1
Min_MC_Events_FL = 1

# Min_MC_Events = 1000
# Min_MC_Events_FL = 100

bkg_d = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/2017/Backgrounds/"
# process_types = ["HH"]
process_types = ["Continuum_Background", "Single_Higgs", "HH"]

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

    file.write("\\begin{figure}[H]\n")
    file.write("\t\\resizebox{1\\textwidth}{!}{% \n")
    file.write("\t\t\\begin{tabular}{c|c|c|c|c}\n")
    file.write("\t\t\tMC Sample & Before preselection & SL (efficiency) & FH (efficiency) & FL (efficiency) \\\ \\hline \n")

    Total_MC_0 = 0. 
    Total_MC_1 = 0. 
    Total_MC_2 = 0. 
    Total_MC_3 = 0. 

    MC_Classes = {
        "GJet" : ["GJet\_Pt-20to40", "GJet\_Pt-20toInf", "GJet\_Pt-40toInf"],
        "QCD" : ["QCD\_Pt-30to40", "QCD\_Pt-30toInf", "QCD\_Pt-40toInf"],
        "TTJets" : ["TTJets\_HT-1200to2500", "TTJets\_HT-2500toInf", "TTJets\_HT-600to800", "TTJets\_HT-800to1200"],
        "W1Jet" : ["W1JetsToLNu\_WpT\_0-50", "W1JetsToLNu\_WpT\_150-250", "W1JetsToLNu\_WpT\_250-400", "W1JetsToLNu\_WpT\_400-inf", "W1JetsToLNu\_WpT\_50-150"],
        "W2Jets" : ["W2JetsToLNu\_WpT\_0-50", "W2JetsToLNu\_WpT\_150-250", "W2JetsToLNu\_WpT\_250-400", "W2JetsToLNu\_WpT\_400-inf", "W2JetsToLNu\_WpT\_50-150"]
    }

    MC_Classes_Yields = {
        "GJet" : [[0, 0],[0, 0],[0, 0],[0, 0]], # [unweighted, weighted] for MiniAOD, SL, FH, FL
        "QCD" : [[0, 0],[0, 0],[0, 0],[0, 0]], 
        "TTJets" : [[0, 0],[0, 0],[0, 0],[0, 0]],  
        "W1Jet" : [[0, 0],[0, 0],[0, 0],[0, 0]], 
        "W2Jets" : [[0, 0],[0, 0],[0, 0],[0, 0]],
    }

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
        # ratio_0 = "%s" % float('%.5g' % (Preselection_Weighted_Yield_0 / MiniAOD_Yield))
        ratio_0 *= 100.
        ratio_0 = round(ratio_0, 3)

        # ratio_1 = "%s" % float('%.5g' % (Preselection_Weighted_Yield_1 / MiniAOD_Yield))
        ratio_1 = round(Preselection_Weighted_Yield_1 / MiniAOD_Yield, 5)
        ratio_1 *= 100.
        ratio_1 = round(ratio_1, 3)

        # ratio_2 = "%s" % float('%.5g' % (Preselection_Weighted_Yield_2 / MiniAOD_Yield))
        ratio_2 = round(Preselection_Weighted_Yield_2 / MiniAOD_Yield, 5)
        ratio_2 *= 100.
        ratio_2 = round(ratio_2, 3)        

        MiniAOD_Yield = round(MiniAOD_Yield, round_digits)
        Preselection_Yield_0 = round(Preselection_Weighted_Yield_0, round_digits)
        Preselection_Yield_1 = round(Preselection_Weighted_Yield_1, round_digits)
        Preselection_Yield_2 = round(Preselection_Weighted_Yield_2, round_digits)

        # Preselection_Yield_0 = "%s" % float('%.5g' % (Preselection_Weighted_Yield_0)) # if you want to round based on total number of sig figs rather than decimal place.
        # Preselection_Yield_1 = "%s" % float('%.5g' % (Preselection_Weighted_Yield_1))
        # Preselection_Yield_2 = "%s" % float('%.5g' % (Preselection_Weighted_Yield_2))

        # Preselection_Yield_0_val = Preselection_Yield_0
        # Preselection_Yield_1_val = Preselection_Yield_1
        # Preselection_Yield_2_val = Preselection_Yield_2

        # if(Preselection_Unweighted_Yield_0 < Min_MC_Events): 
        #     Preselection_Yield_0 = "-"
        #     Preselection_Yield_0_val = 0.
        #     ratio_0 = "-"
        # if(Preselection_Unweighted_Yield_1 < Min_MC_Events): 
        #     Preselection_Yield_1 = "-"
        #     Preselection_Yield_1_val = 0.
        #     ratio_1 = "-"
        # if(Preselection_Unweighted_Yield_2 < Min_MC_Events_FL): 
        #     Preselection_Yield_2 = "-"
        #     Preselection_Yield_2_val = 0.
        #     ratio_2 = "-"                

        finalLineStr = ""
        inMCGroup = 0 
        for MC_Class in MC_Classes:
            types = MC_Classes[MC_Class]
            if(MC_file in types):
                inMCGroup = 1
                # MCGroup = MC_Classes[types]
                print("MC_Class:",MC_Class)

                # append to totals for groups 
                
                # MiniAOD unweighted and weighted events 
                MC_Classes_Yields[MC_Class][0][0] += 9999
                MC_Classes_Yields[MC_Class][0][1] += MiniAOD_Yield

                # After SL preselections 
                MC_Classes_Yields[MC_Class][1][0] += Preselection_Unweighted_Yield_0
                MC_Classes_Yields[MC_Class][1][1] += Preselection_Weighted_Yield_0

                # After FH preselections 
                MC_Classes_Yields[MC_Class][2][0] += Preselection_Unweighted_Yield_1
                MC_Classes_Yields[MC_Class][2][1] += Preselection_Weighted_Yield_1

                # After FL preselections 
                MC_Classes_Yields[MC_Class][3][0] += Preselection_Unweighted_Yield_2
                MC_Classes_Yields[MC_Class][3][1] += Preselection_Weighted_Yield_2                            


        # if this MC sample is part of a large group, do not add a new line yet (because going to sum them for a single line)
        if(inMCGroup):
            continue 
        else: 
            
            Preselection_Yield_0_val = Preselection_Yield_0
            Preselection_Yield_1_val = Preselection_Yield_1
            Preselection_Yield_2_val = Preselection_Yield_2

            if(Preselection_Unweighted_Yield_0 < Min_MC_Events): 
                Preselection_Yield_0 = "-"
                Preselection_Yield_0_val = 0.
                ratio_0 = "-"
            if(Preselection_Unweighted_Yield_1 < Min_MC_Events): 
                Preselection_Yield_1 = "-"
                Preselection_Yield_1_val = 0.
                ratio_1 = "-"
            if(Preselection_Unweighted_Yield_2 < Min_MC_Events_FL): 
                Preselection_Yield_2 = "-"
                Preselection_Yield_2_val = 0.
                ratio_2 = "-"    


            # If a process is part of an MCgroup, do not add to total - b/c have to check total number of unweighted events in the MCgroup
            if(process_type != "HH"):

                Total_MC_0 += MiniAOD_Yield
                Total_MC_1 += Preselection_Yield_0_val
                Total_MC_2 += Preselection_Yield_1_val
                Total_MC_3 += Preselection_Yield_2_val

            file.write("\t\t\t {MC_file} & {MiniAOD_Yield} & {Preselection_Yield_0} ({ratio_0}\%) & {Preselection_Yield_1} ({ratio_1}\%) & {Preselection_Yield_2} ({ratio_2}\%) \\\ {finalLineStr} \n".format(
                MC_file = MC_file,MiniAOD_Yield=MiniAOD_Yield,
                Preselection_Yield_0=Preselection_Yield_0, ratio_0=ratio_0,
                Preselection_Yield_1=Preselection_Yield_1, ratio_1=ratio_1,
                Preselection_Yield_2=Preselection_Yield_2, ratio_2=ratio_2,
                finalLineStr=finalLineStr
                ))

    # include grouped MC yields 
    if(process_type == "Continuum_Background"):
        for MCGroup_i, MCGroup in enumerate(MC_Classes_Yields):
            print("On MCGroup:",MCGroup)

            # weighted yields per MC group 
            MiniAOD_Yield = round(MC_Classes_Yields[MCGroup][0][1], round_digits)
            Preselection_Yield_0 = round(MC_Classes_Yields[MCGroup][1][1], round_digits)
            Preselection_Yield_1 = round(MC_Classes_Yields[MCGroup][2][1], round_digits)
            Preselection_Yield_2 = round(MC_Classes_Yields[MCGroup][3][1], round_digits)

            # unweighted yields 
            Preselection_Unweighted_Yield_0 = MC_Classes_Yields[MCGroup][1][0]
            Preselection_Unweighted_Yield_1 = MC_Classes_Yields[MCGroup][2][0]
            Preselection_Unweighted_Yield_2 = MC_Classes_Yields[MCGroup][3][0]

            ratio_0 = round(Preselection_Weighted_Yield_0 / MiniAOD_Yield, 5)
            ratio_0 *= 100.
            ratio_0 = round(ratio_0, 3)

            ratio_1 = round(Preselection_Weighted_Yield_1 / MiniAOD_Yield, 5)
            ratio_1 *= 100.
            ratio_1 = round(ratio_1, 3)

            ratio_2 = round(Preselection_Weighted_Yield_2 / MiniAOD_Yield, 5)
            ratio_2 *= 100.
            ratio_2 = round(ratio_2, 3)    

            Preselection_Yield_0_val = Preselection_Yield_0
            Preselection_Yield_1_val = Preselection_Yield_1
            Preselection_Yield_2_val = Preselection_Yield_2

            if(Preselection_Unweighted_Yield_0 < Min_MC_Events): 
                Preselection_Yield_0 = "-"
                Preselection_Yield_0_val = 0.
                ratio_0 = "-"
            if(Preselection_Unweighted_Yield_1 < Min_MC_Events): 
                Preselection_Yield_1 = "-"
                Preselection_Yield_1_val = 0.
                ratio_1 = "-"
            if(Preselection_Unweighted_Yield_2 < Min_MC_Events_FL): 
                Preselection_Yield_2 = "-"
                Preselection_Yield_2_val = 0.
                ratio_2 = "-"      


            # If a process is part of an MCgroup, do not add to total - b/c have to check total number of unweighted events in the MCgroup
            if(process_type != "HH"):
                Total_MC_0 += MiniAOD_Yield
                Total_MC_1 += Preselection_Yield_0_val
                Total_MC_2 += Preselection_Yield_1_val
                Total_MC_3 += Preselection_Yield_2_val



            if(MCGroup_i == len(MC_Classes_Yields) - 1):
                finalLineStr = "\\hline "
            else:
                finalLineStr = ""

            file.write("\t\t\t {MCGroup} & {MiniAOD_Yield} & {Preselection_Yield_0} ({ratio_0}\%) & {Preselection_Yield_1} ({ratio_1}\%) & {Preselection_Yield_2} ({ratio_2}\%) \\\ {finalLineStr} \n".format(
                MCGroup = MCGroup,MiniAOD_Yield=MiniAOD_Yield,
                Preselection_Yield_0=Preselection_Yield_0, ratio_0=ratio_0,
                Preselection_Yield_1=Preselection_Yield_1, ratio_1=ratio_1,
                Preselection_Yield_2=Preselection_Yield_2, ratio_2=ratio_2,
                finalLineStr=finalLineStr
                ))        

    if(process_type != "HH"):
        Total_ratio_1 = round(float(Total_MC_1) / float(Total_MC_0), round_digits)
        Total_ratio_2 = round(float(Total_MC_2) / float(Total_MC_0), round_digits)
        Total_ratio_3 = round(float(Total_MC_3) / float(Total_MC_0), round_digits)
        Total_MC_0 = round(Total_MC_0, round_digits)
        Total_MC_1 = round(Total_MC_1, round_digits)
        Total_MC_2 = round(Total_MC_2, round_digits)
        Total_MC_3 = round(Total_MC_3, round_digits)
        file.write("\t\t\t Total & {Total_MC_0} & {Total_MC_1} ({Total_ratio_1}\%) & {Total_MC_2} ({Total_ratio_2}\%) & {Total_MC_3} ({Total_ratio_3}\%) \\\ \\hline \n".format(
            Total_MC_0 = Total_MC_0,
            Total_MC_1 = Total_MC_1,
            Total_MC_2 = Total_MC_2,
            Total_MC_3 = Total_MC_3,
            Total_ratio_1 = Total_ratio_1,
            Total_ratio_2 = Total_ratio_2,
            Total_ratio_3 = Total_ratio_3,
        ))

    file.write("\t\t\end{tabular}}\n")
    process_type_caption = process_type.replace("_", " ")
    file.write("\t\caption{2017 %s MC before and after preselections for each final state, and process efficiency. Note that for processes with less than %s unweighted MC events after a selection (%s for the fully-leptonic preselections), a null value is shown.}\n"%(process_type_caption, Min_MC_Events, Min_MC_Events_FL))
    file.write("\t\label{fig:%s_Yield_Table} \n"%(process_type))
    file.write("\end{figure}\n")  

    file.close()

    print("Saving yields table: ",fileName)

    if(process_type != "HH"):

        # Second table which shows percentage of total after selections etc.
        fileName = "%s_Contributions-Table.tex"%(process_type)
        file = open(fileName,"w")

        file.write("\\begin{figure}[H]\n")
        file.write("\t\\resizebox{1\\textwidth}{!}{% \n")
        file.write("\t\t\\begin{tabular}{c|c|c|c|c}\n")
        file.write("\t\t\tMC Sample & Before preselection & SL & FH & FL \\\ \\hline \n")    
        
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

            # Now take ratio of all four to total of the specified column for this table 
            MiniAOD_Yield_Total = MiniAOD_Yield / Total_MC_0
            MiniAOD_Yield_Total *= 100.
            MiniAOD_Yield_Total = round(MiniAOD_Yield_Total, round_digits)

            Preselection_Weighted_Yield_Total_0 = (Preselection_Weighted_Yield_0 / Total_MC_1) * 100.
            Preselection_Weighted_Yield_Total_1 = (Preselection_Weighted_Yield_1 / Total_MC_2) * 100.
            Preselection_Weighted_Yield_Total_2 = (Preselection_Weighted_Yield_2 / Total_MC_3) * 100.

            Preselection_Weighted_Yield_Total_0 = round(Preselection_Weighted_Yield_Total_0, round_digits)
            Preselection_Weighted_Yield_Total_1 = round(Preselection_Weighted_Yield_Total_1, round_digits)
            Preselection_Weighted_Yield_Total_2 = round(Preselection_Weighted_Yield_Total_2, round_digits)

            if(Preselection_Unweighted_Yield_0 < Min_MC_Events):
                Preselection_Weighted_Yield_Total_0 = "-"

            if(Preselection_Unweighted_Yield_1 < Min_MC_Events): 
                Preselection_Weighted_Yield_Total_1 = "-"

            if(Preselection_Unweighted_Yield_2 < Min_MC_Events_FL): 
                Preselection_Weighted_Yield_Total_2 = "-"

            inMCGroup = 0 
            for MC_Class in MC_Classes:
                types = MC_Classes[MC_Class]
                if(MC_file in types):
                    inMCGroup = 1
                    # print("MC_Class:",MC_Class)

            if(inMCGroup): continue
            else:
                file.write("\t\t\t {MC_file} & {MiniAOD_Yield_Total}\% & {Preselection_Weighted_Yield_Total_0}\% & {Preselection_Weighted_Yield_Total_1}\% & {Preselection_Weighted_Yield_Total_2}\% \\\ \n".format(
                    MC_file = MC_file,MiniAOD_Yield_Total=MiniAOD_Yield_Total,
                    Preselection_Weighted_Yield_Total_0 = Preselection_Weighted_Yield_Total_0,
                    Preselection_Weighted_Yield_Total_1 = Preselection_Weighted_Yield_Total_1,
                    Preselection_Weighted_Yield_Total_2 = Preselection_Weighted_Yield_Total_2,
                    ))


        if(process_type == "Continuum_Background"):
            # Include MCGroup processes 
            for MCGroup_i, MCGroup in enumerate(MC_Classes_Yields):
                print("On MCGroup:",MCGroup)

                # weighted yields per MC group 
                MiniAOD_Yield = round(MC_Classes_Yields[MCGroup][0][1], round_digits)
                Preselection_Weighted_Yield_0 = round(MC_Classes_Yields[MCGroup][1][1], round_digits)
                Preselection_Weighted_Yield_1 = round(MC_Classes_Yields[MCGroup][2][1], round_digits)
                Preselection_Weighted_Yield_2 = round(MC_Classes_Yields[MCGroup][3][1], round_digits)

                # unweighted yields 
                Preselection_Unweighted_Yield_0 = MC_Classes_Yields[MCGroup][1][0]
                Preselection_Unweighted_Yield_1 = MC_Classes_Yields[MCGroup][2][0]
                Preselection_Unweighted_Yield_2 = MC_Classes_Yields[MCGroup][3][0]

                # Now take ratio of all four to total of the specified column for this table 
                MiniAOD_Yield_Total = MiniAOD_Yield / Total_MC_0
                MiniAOD_Yield_Total *= 100.
                MiniAOD_Yield_Total = round(MiniAOD_Yield_Total, round_digits)

                Preselection_Weighted_Yield_Total_0 = (Preselection_Weighted_Yield_0 / Total_MC_1) * 100.
                Preselection_Weighted_Yield_Total_1 = (Preselection_Weighted_Yield_1 / Total_MC_2) * 100.
                Preselection_Weighted_Yield_Total_2 = (Preselection_Weighted_Yield_2 / Total_MC_3) * 100.

                Preselection_Weighted_Yield_Total_0 = round(Preselection_Weighted_Yield_Total_0, round_digits)
                Preselection_Weighted_Yield_Total_1 = round(Preselection_Weighted_Yield_Total_1, round_digits)
                Preselection_Weighted_Yield_Total_2 = round(Preselection_Weighted_Yield_Total_2, round_digits)

                if(Preselection_Unweighted_Yield_0 < Min_MC_Events):
                    Preselection_Weighted_Yield_Total_0 = "-"

                if(Preselection_Unweighted_Yield_1 < Min_MC_Events): 
                    Preselection_Weighted_Yield_Total_1 = "-"

                if(Preselection_Unweighted_Yield_2 < Min_MC_Events_FL): 
                    Preselection_Weighted_Yield_Total_2 = "-"                

                if(MCGroup_i == len(MC_Classes_Yields) - 1):
                    finalLineStr = "\\hline "
                else:
                    finalLineStr = ""

                file.write("\t\t\t {MCGroup} & {MiniAOD_Yield_Total}\% & {Preselection_Weighted_Yield_Total_0}\% & {Preselection_Weighted_Yield_Total_1}\% & {Preselection_Weighted_Yield_Total_2}\% \\\ {finalLineStr} \n".format(
                    MCGroup = MCGroup,MiniAOD_Yield_Total=MiniAOD_Yield_Total,
                    Preselection_Weighted_Yield_Total_0 = Preselection_Weighted_Yield_Total_0,
                    Preselection_Weighted_Yield_Total_1 = Preselection_Weighted_Yield_Total_1,
                    Preselection_Weighted_Yield_Total_2 = Preselection_Weighted_Yield_Total_2,
                    finalLineStr=finalLineStr
                    ))

        file.write("\t\t\t Total & 100\% & 100\% & 100\% & 100\% \\\ \\hline \n")
        file.write("\t\t\end{tabular}}\n")
        process_type_caption = process_type.replace("_", " ")
        file.write("\t\caption{Contribution w.r.t total 2017 %s MC for various phase spaces: Before and after preselections for each final state. Note that for processes with less than %s unweighted MC events after a selection (%s for the fully-leptonic preselections), a null value is shown.}\n"%(process_type_caption, Min_MC_Events, Min_MC_Events_FL))
        file.write("\t\label{fig:%s_Contribution_Table} \n"%(process_type))
        file.write("\end{figure}\n")  

        file.close()

        print("Saving yields table: ",fileName)
