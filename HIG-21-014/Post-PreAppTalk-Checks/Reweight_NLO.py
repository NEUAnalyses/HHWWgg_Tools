"""
9 November 2021 
Abraham Tishelman-Charny 

The purpose of this module is to combine NLO samples while maintaining normalization, in order to use for reweighting to additional EFT benchmarks for HIG-21-014. 

Example Commands:

# Combine NLO samples 
python Reweight_NLO.py --syst Nominal  --TDirec "tagsDumper/trees" --GENnorm --year 2016 --node cHHH1

# Reweight to a node 

# Reweight to a node and include node branch
# 2016 / 2018

python Reweight_NLO.py --reweightNode 13 --syst Nominal --runLowEvents --TDirec "" --addNodeBranch --inDir /eos/user/c/chuw/ForAbe/HIG-21-014_Reweighting_Semileptonic/2017/combined_allNodes/ --year 2017
python Reweight_NLO.py --reweightNode 1 --syst Nominal --runLowEvents --TDirec "" --addNodeBranch --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2016/Signal/SL_allNLO_Reweighted/combined_allNodes/ --year 2016
python Reweight_NLO.py --reweightNode 1 --syst Nominal --runLowEvents --TDirec "" --addNodeBranch --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2018/Signal/SL_allNLO_Reweighted/combined_allNodes/ --year 2018
python Reweight_NLO.py --reweightNode 1 --syst Nominal --runLowEvents --TDirec "" --addNodeBranch --inDir /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted/combined_allNodes/ --year 2017

# Categorize by DNN score 

# Split into even/odd events for DNN training 

python3 Reweight_NLO.py  --syst Nominal  --TDirec "" --evenOddSplit --Single_Higgs --Single_Higgs_File VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2 --additionalSF 

python3 Reweight_NLO.py  --syst Nominal  --TDirec "" --evenOddSplit --Single_Higgs --Single_Higgs_File ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2

python3 Reweight_NLO.py --reweightNode 6 --syst MCSmearHighR9EBPhiDown01sigma --TDirec "" --evenOddSplit --additionalSF
python Reweight_NLO.py --reweightNode 2 --syst Nominal --runLowEvents --TDirec "" --evenOddSplit

# Categorize by DNN score

python Reweight_NLO.py --reweightNode 1 --year 2017 --syst Nominal --TDirec "" --categorize --isHH

python Reweight_NLO.py --reweightNode 2 --year 2016 --syst MCSmearLowR9EERhoDown01sigma --TDirec "" --categorize  --Single_Higgs   --Single_Higgs_File VBFHToGG
python Reweight_NLO.py --reweightNode 5 --year 2018 --syst PUJIDShiftDown01sigma --TDirec "" --categorize  --Single_Higgs   --Single_Higgs_File GluGluHToGG

"""

import argparse 

# export PYTHONPATH=$CERNBOX_HOME/.local/lib/python3.8/site-packages:$PYTHONPATH

import ROOT 
import os 
from array import array 
from Reweight_Tools import addVariables, Reweight, Categorize, EvenOddSplit

# Normalization factor per sample (Semileptonic)
def GetNorm(year, node):

    # sum of gen weights from flashgg catalogues (semileptonic, assuming you're including cHHH0,1,2p45,5)
    Sum_2016 = (24041.67591 + 10263.27003 + 4392.211129 + 31501.80227)
    Sum_2017 = (21264.42409 + 10588.6642 + 4413.499586 + 17686.79584)
    Sum_2018 = (21358.25083 + 9564.085541 + 3331.597595 + 18889.14688)

    # For semileptonic case 
    NormVals = {
        "2016" : {
                    "cHHH0" : 24041.67591 / Sum_2016,
                    "cHHH1" : 10263.27003 / Sum_2016, 
                    "cHHH2p45" : 4392.211129 / Sum_2016, 
                    "cHHH5" : 31501.80227 / Sum_2016
        },

        "2017" : {
                    "cHHH0" : 21264.42409 / Sum_2017,
                    "cHHH1" : 10588.6642 / Sum_2017,
                    "cHHH2p45" : 4413.499586 / Sum_2017,
                    "cHHH5" : 17686.79584 / Sum_2017
        },

        "2018" : {
                    "cHHH0" : 21358.25083 / Sum_2018,
                    "cHHH1" : 9564.085541 / Sum_2018,
                    "cHHH2p45" : 3331.597595 / Sum_2018,
                    "cHHH5" : 18889.14688 / Sum_2018
        }
    }

    return float(NormVals[year][node]) 

if __name__ == '__main__':
    print("Starting Reweight_NLO.py module")
    # input arguments 
    parser =  argparse.ArgumentParser()
    parser.add_argument('--node', default = "cHHH1", required=False, type=str, help = "Input Node to run")
    parser.add_argument('--year', default = "2017", required=False, type=str, help = "Year to run")
    parser.add_argument('--runLowEvents', action="store_true", required=False, help = "Run on a low number of events (for testing)")
    parser.add_argument('--evenOddSplit', action="store_true", required=False, help = "Split trees into two files: One with even event IDs, one with odd event IDs")
    parser.add_argument('--addNodeBranch', action="store_true", required=False, help = "Add branch Node_Number to be used for parametric DNN training")
    parser.add_argument('--additionalSF', action="store_true", required=False, help = "Apply SFs when producing even / odd trees in order to rescale to nominal yield")
    parser.add_argument('--syst', default = "Nominal", required=False, type=str, help = "Systematic tree to process")
    parser.add_argument('--reweightNode', default = "", required=False, type=str, help = "Node to reweight to, e.g. (updates weight branch)")
    parser.add_argument('--TDirec', default = "tagsDumper/trees", required=False, type=str, help = "TDirectory strucuture of input root file")
    parser.add_argument('--inDir', default = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/", type=str, help = "Directory containing output files with DNN scores.")
    parser.add_argument('--GENnorm', action="store_true", required=False, help = "Normalize weight branch based on relative GEN sums")
    parser.add_argument('--isMC', default = 1, required=False, type=int, help = "Flag if the sample is MC or not. Matters when applying MET correction")
    parser.add_argument('--isHH', action="store_true", required=False, help = "Run over HH")
    parser.add_argument('--isData', action="store_true", required=False, help = "Run over Data")
    parser.add_argument('--Single_Higgs', action="store_true", required=False, help = "Run over single higgs")
    parser.add_argument('--Single_Higgs_File', default = "", required=False, type=str, help = "Single higgs file")

    # Categorization 
    parser.add_argument('--categorize', action="store_true", required=False, help = "Split trees into categories based on DNN score")
    
    args = parser.parse_args()
    arguments = [
            "node", "year", "runLowEvents", "syst", "reweightNode", "TDirec", "GENnorm", "categorize", "inDir", "addNodeBranch", 
            "evenOddSplit", "additionalSF", "isMC", "Single_Higgs", "Single_Higgs_File", "isHH", "isData"
    ]
    
    print("=====")
    for a in arguments: 
        exec("{a} = args.{a}".format(a=a))
        print("{a}:".format(a=a),eval(a))
    print("=====")
    
    if(categorize):
        node = reweightNode

        print("isData:",isData)
        print("isHH:",isHH)
        print("isH:",Single_Higgs)

        if( (int(isData) + int(isHH) + int(Single_Higgs)) != 1 ):
            raise Exception("ERROR - Must select exactly one of the following: isData, isHH, isH")

        # Start with DNN evaluated file
        # /eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted/EFT_DNN_Training/HHWWyyDNN_binary_EFT_noHgg_noNegWeights_BalanceYields_allBkgs_NLO_Reweighted_20nodes_noPtOverM_withKinWeight_weightSel_Parametrized_CorMET/

        # Data 
        # Data_{year}_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root # 60 files 

        # H 
        # GluGluHToGG_M125_2016_HHWWggTag_0_MoreVars_v2_nodeNumber20.root
        # GluGluHToGG_2017_HHWWggTag_0_MoreVars_v2_nodeNumber20.root
        # GluGluHToGG_M125_2018_HHWWggTag_0_MoreVars_v2_nodeNumber18.root
        #
        # VBFHToGG_M125_2016_HHWWggTag_0_MoreVars_v2_nodeNumber18.root
        # VBFHToGG_2017_HHWWggTag_0_MoreVars_v2_nodeNumber20.root
        # VBFHToGG_M125_2018_HHWWggTag_0_MoreVars_v2_nodeNumber18.root
        #
        # VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2_nodeNumber18.root
        # VHToGG_2017_HHWWggTag_0_MoreVars_v2_nodeNumber20.root
        # VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2_nodeNumber12.root
        #
        # ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2_nodeNumber18.root
        # ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2_nodeNumber20.root
        # ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2_nodeNumber2.root

        # HH 
        # GluGluToHHTo2G2Qlnu_node_{reweightNode}_{year}_odd.root 

        SingleHiggsProcessStrDict = {

            "2016" : {
                "GluGluHToGG" : "GluGluHToGG_M125_2016_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode),
                "VBFHToGG" :    "VBFHToGG_M125_2016_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode),
                "VHToGG" :      "VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode),
                "ttHJetToGG" :  "ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode)
            },

            "2017" : {
                "GluGluHToGG" : "GluGluHToGG_2017_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode),
                "VBFHToGG" :    "VBFHToGG_2017_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode),
                "VHToGG" :      "VHToGG_2017_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode),
                "ttHJetToGG" :  "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode)
            }, 

            "2018" : {
                "GluGluHToGG" : "GluGluHToGG_M125_2018_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode),
                "VBFHToGG" :    "VBFHToGG_M125_2018_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode),
                "VHToGG" :      "VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode),
                "ttHJetToGG" :  "ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(reweightNode=reweightNode)
            } 
        }

        outSubDir = "NONE"
        if(isData): 
            outSubDir = "Semileptonic_Data"
            processStr = "Data"
            processStrInFile = processStr
        elif(isHH): 
            outSubDir = "Semileptonic_Signal"
            processStr = "GluGluToHHTo2G2Qlnu"
            processStrInFile = processStr
        elif(Single_Higgs): 
            outSubDir = "Semileptonic_SingleHiggs/{Single_Higgs_File}/".format(Single_Higgs_File=Single_Higgs_File)
            processStr = Single_Higgs_File
            processStrInFile = SingleHiggsProcessStrDict[year][Single_Higgs_File]
        else: raise Exception("ERROR - Need to select isData, isHH or isH if categorizing")

        signalEndStr = ""
        if( (year == "2017") and (isHH)): signalEndStr = "_odd"

        # parametric DNN output location 
        d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted/EFT_DNN_Training/HHWWyyDNN_binary_EFT_noHgg_noNegWeights_BalanceYields_allBkgs_NLO_Reweighted_20nodes_noPtOverM_withKinWeight_weightSel_Parametrized_CorMET/"
        
        if(Single_Higgs):
            f = "{d}/{processStrInFile}".format(d=d, processStrInFile=processStrInFile)
        elif(isData):
            f = "{d}/Data_{year}_HHWWggTag_0_MoreVars_v2_nodeNumber{reweightNode}.root".format(d=d, year=year, reweightNode=reweightNode)
        else:
            f = "{d}/{processStrInFile}_node_{reweightNode}_{year}{signalEndStr}.root".format(d=d, year=year, reweightNode=reweightNode, syst=syst, signalEndStr=signalEndStr, processStrInFile=processStrInFile)  

        #out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{reweightNode}_trees_categorized/".format(year=year, reweightNode=reweightNode)
        

        if(not isData): out_d = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_EFTResults/20_Benchmark_Results/{year}/{outSubDir}/{reweightNode}_trees_categorized/".format(year=year, outSubDir=outSubDir, reweightNode=reweightNode)
        else: out_d = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/HIG_21_014_PostPreApprovalTalk_EFTResults/20_Benchmark_Results/{year}/{outSubDir}/".format(year=year, outSubDir=outSubDir)

        if(not os.path.isdir(out_d)):
            print("Creating output directory:",out_d)
            os.system("mkdir -p {out_d}".format(out_d=out_d))

        if(not isData): outName = "{out_d}{processStr}_node_{reweightNode}_{year}_{syst}_Categorized.root".format(out_d=out_d, reweightNode=reweightNode, year=year, syst=syst, processStr=processStr) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards  
        else: outName = "{out_d}/Data_node_{reweightNode}_{year}_Categorized.root".format(out_d=out_d, reweightNode=reweightNode, year=year) # no systematics for data 

               

    elif(evenOddSplit):
        if(additionalSF): additionalSF_str = "_withAdditionalScaling"
        else: additionalSF_str = ""
        # d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{reweightNode}/".format(year=year, reweightNode=reweightNode)
        # d = "/eos/user/c/chuw/ForAbe/HIG-21-014_Reweighting_Semileptonic/{year}/{reweightNode}/".format(year=year, reweightNode=reweightNode)

        # H 
        if(Single_Higgs):

            H_Y_Direc_dict = {
                "VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "VH_2016",
                "ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "ttH_2016",

                "VHToGG_2017_HHWWggTag_0_MoreVars_v2" : "VH_2017",
                "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2" : "ttH_2017",

                "VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2" : "VH_2018",
                "ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2" : "ttH_2018"
            }

            H_Y_Direc = H_Y_Direc_dict[Single_Higgs_File]

            d = "/eos/user/c/chuw/ForAbe/Single_H_hadded/"
            f = "{d}/{Single_Higgs_File}.root".format(d=d, Single_Higgs_File=Single_Higgs_File)

            # direcs 
            thisDirec = "{d}/{H_Y_Direc}_even{additionalSF_str}".format(d=d, H_Y_Direc=H_Y_Direc, additionalSF_str=additionalSF_str)
            if(not os.path.isdir(thisDirec)):
                print("Creating output directory:",thisDirec)
                os.system("mkdir {thisDirec}".format(thisDirec=thisDirec))  

            thisDirec = "{d}/{H_Y_Direc}_odd{additionalSF_str}".format(d=d, H_Y_Direc=H_Y_Direc, additionalSF_str=additionalSF_str)
            if(not os.path.isdir(thisDirec)):
                print("Creating output directory:",thisDirec)
                os.system("mkdir {thisDirec}".format(thisDirec=thisDirec))    

            outName_even = "{d}/{H_Y_Direc}_even{additionalSF_str}/{Single_Higgs_File}_{syst}_even.root".format(d=d, Single_Higgs_File=Single_Higgs_File, syst=syst, H_Y_Direc=H_Y_Direc, additionalSF_str=additionalSF_str)
            outName_odd = "{d}/{H_Y_Direc}_odd{additionalSF_str}/{Single_Higgs_File}_{syst}_odd.root".format(d=d, Single_Higgs_File=Single_Higgs_File, syst=syst, H_Y_Direc=H_Y_Direc, additionalSF_str=additionalSF_str)

        # HH 
        else:
            d = "/eos/user/c/chuw/ForAbe/HIG-21-014_Reweighting_Semileptonic/{year}/".format(year=year, reweightNode=reweightNode)
            f = "{d}/{reweightNode}/GluGluToHHTo2G2Qlnu_node_{reweightNode}_{year}.root".format(d=d, year=year, reweightNode=reweightNode, syst=syst)  
            out_d_even = "{d}/{reweightNode}_trees_even{additionalSF_str}/".format(d=d, year=year, reweightNode=reweightNode, additionalSF_str=additionalSF_str)
            out_d_odd = "{d}/{reweightNode}_trees_odd{additionalSF_str}/".format(d=d, year=year, reweightNode=reweightNode, additionalSF_str=additionalSF_str)
            
            for out_d in [out_d_even, out_d_odd]:
                if(not os.path.isdir(out_d)):
                    print("Creating output directory:",out_d)
                    os.system("mkdir {out_d}".format(out_d=out_d)) # if you only have write access to the final directory 
                    # os.system("mkdir -p {out_d}".format(out_d=out_d)) # if you have write access to the full directory 
            
            outName_even = "{out_d_even}GluGluToHHTo2G2Qlnu_node_{reweightNode}_{year}_{syst}_Even.root".format(out_d_even=out_d_even, reweightNode=reweightNode, year=year, syst=syst) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards          
            outName_odd = "{out_d_odd}GluGluToHHTo2G2Qlnu_node_{reweightNode}_{year}_{syst}_Odd.root".format(out_d_odd=out_d_odd, reweightNode=reweightNode, year=year, syst=syst) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards          

    else:
        if(reweightNode != ""):
            node = reweightNode
            # Start with file which is already a combination of the 4 NLO nodes 
            f = "{inDir}/GluGluToHHTo2G2Qlnu_node_All_NLO_{year}.root".format(inDir=inDir, year=year)
            #out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{reweightNode}_trees/".format(year=year, reweightNode=reweightNode)
            # out_d = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{reweightNode}_trees/".format(year=year, reweightNode=reweightNode)
            out_d = "/eos/user/c/chuw/ForAbe/HIG-21-014_Reweighting_Semileptonic/{year}/{reweightNode}_trees/".format(year=year, reweightNode=reweightNode)

            if(not os.path.isdir(out_d)):
                print("Creating output directory:",out_d)
                os.system("mkdir {out_d}".format(out_d=out_d))
                # os.system("mkdir -p {out_d}".format(out_d=out_d))
            outName = "{out_d}/GluGluToHHTo2G2Qlnu_node_{reweightNode}_{year}_{syst}.root".format(out_d=out_d, reweightNode=reweightNode, year=year, syst=syst) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards    

        else:
            # Start with files with reweight branches for combining 
            d = "/eos/user/p/pmandrik/HHWWgg_central/January_2021_Production_v2/{year}/Signal/SL_NLO_{year}_hadded/".format(year=year)
            f = "{d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}.root".format(d=d, node=node, year=year)
            out_d = "/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/{year}/Signal/SL_allNLO_Reweighted/{node}/".format(year=year, node=node)
            if(not os.path.isdir(out_d)):
                print("Creating output directory:",out_d)
                os.system("mkdir -p {out_d}".format(out_d=out_d))            
            outName = "{out_d}/GluGluToHHTo2G2Qlnu_node_{node}_{year}_{syst}.root".format(out_d=out_d, node=node, year=year, syst=syst) # save a file per systematic tree so that you can run them all in parallel and just hadd them all afterwards

    if(evenOddSplit):
        outFile_even = ROOT.TFile(outName_even, "RECREATE")
        outFile_odd = ROOT.TFile(outName_odd, "RECREATE")
    else:
        outFile = ROOT.TFile(outName, "RECREATE")
    inFile = ROOT.TFile(f,"READ")
    if(TDirec != ""):
        inDir = inFile.Get(TDirec)  
        treeNames = inDir.GetListOfKeys()
    else:
        treeNames = inFile.GetListOfKeys()

    if(GENnorm):
        Norm = GetNorm(year, node)
    else:
        Norm = 1. 
    print("Norm:",Norm)

    # find tree that this job is meant to process
    # expecting tree name format:
    # nominal tree:    GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0
    # Systematic tree: GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0_<systematic>    

    # Combined file:
    # GluGluToHHTo2G2Qlnu_node_All_NLO_2017_Normalized_13TeV_HHWWggTag_0

    if(Single_Higgs):

        # for even odd stuff 
        # SingleHiggsTreeDict = {
        #     "VHToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "wzh_125_13TeV_HHWWggTag_0",
        #     "ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars_v2" : "tth_125_13TeV_HHWWggTag_0",

        #     "VHToGG_2017_HHWWggTag_0_MoreVars_v2" : "wzh_125_13TeV_HHWWggTag_0",
        #     "ttHJetToGG_2017_HHWWggTag_0_MoreVars_v2" : "tth_125_13TeV_HHWWggTag_0",

        #     "VHToGG_M125_2018_HHWWggTag_0_MoreVars_v2" : "wzh_125_13TeV_HHWWggTag_0",
        #     "ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars_v2" : "tth_125_13TeV_HHWWggTag_0"            
        # }

        # post DNN score categorization 
        SingleHiggsTreeDict = {

            "GluGluHToGG" : "ggh_125_13TeV_HHWWggTag_0",
            "VBFHToGG" : "vbf_125_13TeV_HHWWggTag_0",
            "VHToGG" : "wzh_125_13TeV_HHWWggTag_0",
            "ttHJetToGG" : "tth_125_13TeV_HHWWggTag_0"

        }


        nonSystTreePath = SingleHiggsTreeDict[Single_Higgs_File]

        if(syst == "Nominal"):
            systExt = "v1"
        else:
            systExt = "%s_v1"%(syst)

        fullTreePath = "%s_%s"%(nonSystTreePath, systExt)
        treeToProcess = fullTreePath

    elif(isData):
        fullTreePath = "Data_13TeV_HHWWggTag_0_v1"
        treeToProcess = "Data_13TeV_HHWWggTag_0_v1"

    else:

        if(categorize):
            treeNode = node 
        elif(evenOddSplit):
            treeNode = reweightNode 
        else:
            if(reweightNode != ""):
                treeNode = "All_NLO_{year}_Normalized".format(year=year) 
            else:
                treeNode = node
        
        if(categorize or evenOddSplit):
            if(syst == "Nominal"):
                treeToProcess = "GluGluToHHTo2G2Qlnu_node_{treeNode}_{year}_13TeV_HHWWggTag_0".format(treeNode=treeNode, year=year)
            else: 
                treeToProcess = "GluGluToHHTo2G2Qlnu_node_{treeNode}_{year}_13TeV_HHWWggTag_0_{syst}".format(treeNode=treeNode, year=year, syst=syst)   
        else:
            if(syst == "Nominal"):
                treeToProcess = "GluGluToHHTo2G2Qlnu_node_{treeNode}_13TeV_HHWWggTag_0".format(treeNode=treeNode)
            else:
                treeToProcess = "GluGluToHHTo2G2Qlnu_node_{treeNode}_13TeV_HHWWggTag_0_{syst}".format(treeNode=treeNode, syst=syst)   


    print("treeToProcess:",treeToProcess)
    foundTree = 0 # to avoid the problem of having copies of a tree name in keys 
    for t_i, treeName in enumerate(treeNames): 
        kname = treeName.GetName()
        # check current tree 
        if((kname == treeToProcess) and foundTree == 0):
            print("Found tree to process: {kname}".format(kname=kname))
            foundTree = 1 

            treeInfo = kname.split('_')
            NumTreeKeys = len(treeInfo)

            if((not Single_Higgs) and (not isData)):

                # already combined files have a different number of underscores in the tree name 
                if(categorize or evenOddSplit):
                    if(reweightNode != ""):
                        if(NumTreeKeys == 7):
                            syst = "Nominal"
                        elif(NumTreeKeys == 8):
                            syst = treeInfo[-1]
                        else:
                            raise Exception("Number of keys in tree name is {NumTreeKeys} -- do not know how to handle that.".format(NumTreeKeys=NumTreeKeys))                
                else:
                    if(reweightNode != ""):
                        if(NumTreeKeys == 9):
                            syst = "Nominal"
                        elif(NumTreeKeys == 10):
                            syst = treeInfo[-1]
                        else:
                            raise Exception("Number of keys in tree name is {NumTreeKeys} -- do not know how to handle that.".format(NumTreeKeys=NumTreeKeys))

                    else:
                        if(NumTreeKeys == 6):
                            syst = "Nominal"
                        elif(NumTreeKeys == 7):
                            syst = treeInfo[-1]
                        else:
                            raise Exception("Number of keys in tree name is {NumTreeKeys} -- do not know how to handle that.".format(NumTreeKeys=NumTreeKeys))

            if(TDirec != ""): fullTreePath = "%s/%s"%(TDirec, kname)
            else: fullTreePath = kname
            inTree = inFile.Get(fullTreePath)        
            if(not evenOddSplit):
                outFile.cd()
            if(categorize):
                Categorize(inTree, kname, runLowEvents, reweightNode)
            elif(evenOddSplit):
                EvenOddSplit(inFile, runLowEvents, outFile_even, outFile_odd, fullTreePath, additionalSF, reweightNode, syst, Single_Higgs, year, Single_Higgs_File) # split events into even and odd 
            else:
                if(reweightNode != ""):
                    Reweight(inTree, kname, year, runLowEvents, Norm, reweightNode, addNodeBranch) # reweight already combined sample 
                else: # add variables 
                    addVariables(inTree, kname, year, runLowEvents, Norm, reweightNode, isMC)                
                
        else: continue # do not process this tree 
    if(not evenOddSplit): outFile.Close()        
