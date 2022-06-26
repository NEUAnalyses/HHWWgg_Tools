import os 
import uproot 
import numpy as np 

# direcs = [
    # "{d}/2016/Semileptonic_SingleHiggs/".format(d=d)

# files = [
#     # # 2016 
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/2016/Semileptonic_SingleHiggs/GluGluHToGG/GluGluHToGG_2016.root",
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/2016/Semileptonic_SingleHiggs/VBFHToGG/VBFHToGG_2016.root",
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/FullSingleHiggsSamples/2016/Semileptonic_SingleHiggs/VHToGG/VHToGG_2016.root",
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/FullSingleHiggsSamples/2016/Semileptonic_SingleHiggs/ttHJetToGG/ttHJetToGG_2016.root",

#     # # 2017
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/2017/Semileptonic_SingleHiggs/GluGluHToGG/GluGluHToGG_2017.root",
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/2017/Semileptonic_SingleHiggs/VBFHToGG/VBFHToGG_2017.root",    
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/FullSingleHiggsSamples/2017/Semileptonic_SingleHiggs/VHToGG/VHToGG_2017.root",
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/FullSingleHiggsSamples/2017/Semileptonic_SingleHiggs/ttHJetToGG/ttHJetToGG_2017.root",

#     # # 2018 
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/2018/Semileptonic_SingleHiggs/GluGluHToGG/GluGluHToGG_2018.root",
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/2018/Semileptonic_SingleHiggs/VBFHToGG/VBFHToGG_2018.root",       
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/FullSingleHiggsSamples/2018/Semileptonic_SingleHiggs/VHToGG/VHToGG_2018.root",
#     # "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_SMResults/FullSingleHiggsSamples/2018/Semileptonic_SingleHiggs/ttHJetToGG/ttHJetToGG_2018.root",        

# ]

d = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_EFTResults/20_Benchmark_Results/"
years = ["2016", "2017", "2018"]
procs = ["GluGluHToGG", "VBFHToGG", "VHToGG", "ttHJetToGG"]
# nodes = [str(i) for i in range(1,21)]
nodes = [str(i) for i in range(1,2)]

for node in nodes:
    for year in years:
        for proc in procs:
            direc = "%s/%s/Semileptonic_SingleHiggs/%s/"%(d, year, proc)
            files = ["%s/%s"%(direc, f) for f in os.listdir(direc) if f.endswith(".root")]

            ##-- Begin Table
            print("\\begin{table}[H]")
            print("  \\begin{center}")
            print("    \\begin{tabular}{c|c|c|c|c}")
            print("    Proc & SLDNN\_3 & SLDNN\_2 & SLDNN\_1 & SLDNN\_0 \\\ \\hline")    

            for f_i, f in enumerate(files):
                fName = f.split('/')[-1].split('.')[0]
                fName = fName.replace("_", "\_") # for latex table 
                # get number of unweighted entries per category 
                f_u = uproot.open(f)
                trees = f_u.keys()
                catStrings = ["HHWWggTag_SL_0_v1", "HHWWggTag_SL_1_v1", "HHWWggTag_SL_2_v1", "HHWWggTag_SL_3_v1"]
                savedTreeNames = []
                for tree in trees:
                    for catStr in catStrings:
                        if(catStr in str(tree)):
                            #print("Saving tree:",tree)
                            savedTreeNames.append(tree)

                unweighted_yields = []

                for savedTree in savedTreeNames:
                    vals = f_u[savedTree]["CMS_hgg_mass"].array() 
                    N_entries = len(vals)
                    unweighted_yields.append(str(N_entries))
                    #print("%s, %s, %s"%(fName, str(savedTree), N_entries))

                print("    %s & %s & %s & %s & %s \\\ "%(fName, unweighted_yields[0], unweighted_yields[1], unweighted_yields[2], unweighted_yields[3]))

            ##-- Finish table
            print("    \\end{tabular}")
            print("  \\end{center}")
            print("\\caption{")
            print("    %s, year %s"%(proc, year))
            print("}")
            print("\\label{tab:label}")
            print("\\end{table}")
            print(" ")