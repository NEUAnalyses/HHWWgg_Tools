"""
26 January 2022
Abraham Tishelman-Charny 

The purpose of this python module is to add variables to WWZ CR files in order to have the corrected MET for the HIG-21-014, AN_20_165_v7 SL SM DNN validation.
"""

import ROOT 
import os 
from array import array 
from Reweight_Tools import addVariables

def GetTreeName(treeNames_):
    treeNameToUse_ = "NOTREENAME"
    for treeName_ in treeNames_:
        kname_ = treeName_.GetName()
        # Take semileptonic:
        if("HHWWggTag_0" in kname_):
            treeNameToUse_ = kname_
    return treeNameToUse_ 

if(__name__ == '__main__'):

    DY_CR_Direc = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/WWZ_SignalTopology_Checks/2017/"

    data_files = [
            # ####-- Zee / WWZ phase space samples
            ##-- Data
            '{DY_CR_Direc}/Data/Data_WWZPhaseSpace_2017_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc), ##-- DoubleEG Data (with electron HLT path)
            '{DY_CR_Direc}/SingleElectron_Data_2017_hadded/SingleElectron_Data_2017_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc), ##-- SingleElectron Data (with electron HLT path)
    ]

    MC_files = [

            # ##-- MC
            '{DY_CR_Direc}/Zee_hadded/Zee_2017_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc), ##-- DY + Jets
            '{DY_CR_Direc}/WWZ_2017_hadded/WWZ_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc), ##-- WWZ
            '{DY_CR_Direc}/Zee_hadded/Zee_v14_ext1-v1_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),

            '{DY_CR_Direc}/Flashgg_Backgrounds_Zee_Preselections_2017_hadded/GJet_Pt-20to40_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Flashgg_Backgrounds_Zee_Preselections_2017_hadded/GJet_Pt-20toInf_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Flashgg_Backgrounds_Zee_Preselections_2017_hadded/GJet_Pt-40toInf_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Flashgg_Backgrounds_Zee_Preselections_2017_hadded/DiPhotonJetsBox_M40_80_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Flashgg_Backgrounds_Zee_Preselections_2017_hadded/WW_TuneCP5_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Flashgg_Backgrounds_Zee_Preselections_2017_hadded/TTGJets_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Flashgg_Backgrounds_Zee_Preselections_2017_hadded/TTJets_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Flashgg_Backgrounds_Zee_Preselections_2017_hadded/TTGG_0Jets_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Flashgg_Backgrounds_Zee_Preselections_2017_hadded/DiPhotonJetsBox_MGG-80toInf_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),

            '{DY_CR_Direc}/HHWWgg_Backgrounds_ZeePreselections_2017_hadded/WGGJets_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/HHWWgg_Backgrounds_ZeePreselections_2017_hadded/WGJJToLNu_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/HHWWgg_Backgrounds_ZeePreselections_2017_hadded/WWTo1L1Nu2Q_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/HHWWgg_Backgrounds_ZeePreselections_2017_hadded/ttWJets_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),

            '{DY_CR_Direc}/More_Backgrounds_hadded/ZZ_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/More_Backgrounds_hadded/TTWJetsToLNu_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/More_Backgrounds_hadded/TTZToLLNuNu_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),

            '{DY_CR_Direc}/More_Backgrounds_v2_hadded/WGToLNuG_01J_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/WGToLNuG_hadded/WGToLNuG_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/More_Backgrounds_v3_hadded/ZGToLLG_01J_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Higgs_bkg_2017_125Only_hadded/GluGluHToGG_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Higgs_bkg_2017_125Only_hadded/VBFHToGG_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),
            '{DY_CR_Direc}/Higgs_bkg_2017_125Only_hadded/VHToGG_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),  

            '{DY_CR_Direc}/WJets_pTBinned_hadded/W1JetsToLNu_LHEWpT_0-50_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),   
            '{DY_CR_Direc}/WJets_pTBinned_hadded/W1JetsToLNu_LHEWpT_50-150_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),   
            '{DY_CR_Direc}/WJets_pTBinned_hadded/W1JetsToLNu_LHEWpT_150-250_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),   
            '{DY_CR_Direc}/WJets_pTBinned_hadded/W1JetsToLNu_LHEWpT_250-400_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),   
            '{DY_CR_Direc}/WJets_pTBinned_hadded/W1JetsToLNu_LHEWpT_400-inf_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),  

            '{DY_CR_Direc}/WJets_pTBinned_hadded/W2JetsToLNu_LHEWpT_0-50_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),   
            '{DY_CR_Direc}/WJets_pTBinned_hadded/W2JetsToLNu_LHEWpT_50-150_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),   
            '{DY_CR_Direc}/WJets_pTBinned_hadded/W2JetsToLNu_LHEWpT_150-250_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),   
            '{DY_CR_Direc}/WJets_pTBinned_hadded/W2JetsToLNu_LHEWpT_250-400_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),   
            '{DY_CR_Direc}/WJets_pTBinned_hadded/W2JetsToLNu_LHEWpT_400-inf_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),         

            '{DY_CR_Direc}/WJets_pTBinned_hadded/W3JetsToLNu_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),         
            '{DY_CR_Direc}/WJets_pTBinned_hadded/W4JetsToLNu_hadded_MoreVars.root'.format(DY_CR_Direc=DY_CR_Direc),    
    ]    

    changeTreeName = 0
    runLowEvents = 0 
    year = "2017"
    reweightNode = "" # no reweighting
    Norm = 1. # no normalization 

    for data_file in data_files:
        print("On file:",data_file)
        isMC = 0 

        f = data_file
        inFile = ROOT.TFile(f,"READ")
        treeNames = inFile.GetListOfKeys()
        treeNameToUse = GetTreeName(treeNames)
        print("treeNameToUse:",treeNameToUse)
        inTree = inFile.Get(treeNameToUse)      
        fileEnd = f.split('/')[-1]
        out_d = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/WWZ_SignalTopology_Checks/2017/WWZ_CR_With_AddedVariables/"
        outName = "%s/%s"%(out_d, fileEnd)
        outFile = ROOT.TFile(outName, "RECREATE")
        outFile.cd()
        addVariables(inTree, treeNameToUse, year, runLowEvents, Norm, reweightNode, isMC, changeTreeName)   
        outFile.Close()      

    for MC_file in MC_files:
        print("On file:",MC_file)
        isMC = 1
        f = MC_file
        inFile = ROOT.TFile(f,"READ")
        treeNames = inFile.GetListOfKeys()
        treeNameToUse = GetTreeName(treeNames)
        print("treeNameToUse:",treeNameToUse) 
        inTree = inFile.Get(treeNameToUse)      
        fileEnd = f.split('/')[-1]
        out_d = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/WWZ_SignalTopology_Checks/2017/WWZ_CR_With_AddedVariables/"
        outName = "%s/%s"%(out_d, fileEnd)
        outFile = ROOT.TFile(outName, "RECREATE")
        outFile.cd()
        addVariables(inTree, treeNameToUse, year, runLowEvents, Norm, reweightNode, isMC, changeTreeName)   
        outFile.Close()        