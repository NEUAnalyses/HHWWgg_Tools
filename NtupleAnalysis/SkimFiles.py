##################################################################################################################################################################################################
# Abraham Tishelman-Charny                                                                                                                                                                       #
# 15 October 2020                                                                                                                                                                                #
#                                                                                                                                                                                                #
# The purpose of this module is to apply selections to trees and merge them into a new file.                                                                                                     #
#                                                                                                                                                                                                #
# Special thanks to these links for info on adding tree selections in pyROOT:                                                                                                                    #
# https://indico.cern.ch/event/704163/contributions/2936719/attachments/1693833/2726445/Tutorial-Pypdf                                                                                           #
# https://root-forum.cern.ch/t/copytree-with-a-selection/12908                                                                                                                                   #
# TFile* file = TFile::Open("TEST.root");                                                                                                                                                        #
# TTree* originalTree = (TTree*)file->Get("reducedTree");                                                                                                                                        #
# TFile* ouput = TFile::Open("TESTskim.root","RECREATE");                                                                                                                                        #
# TTree* selectedTree = originalTree->CopyTree("ptLept1>50.")                                                                                                                                    #
#                                                                                                                                                                                                #
# Example Usage:                                                                                                                                                                                 #
# with prompt-prompt removal and merging of trees:                                                                                                                                               #
# ##-- NOTE: when doing prompt-prompt removal, inDir should ONLY contain GJet and QCD samples (up to 6 total)                                                                                    #
# python SkimFiles.py --inDir /eos/user/<letter>/<userName>/<projectDirectory>/skimFilesInput --outDir /eos/user/<letter>/<userName>/<projectDirectory>/skimFilesInput --doppRemoval             #
#                                                                                                                                                                                                # 
# without prompt-prompt removal, just merging of trees:                                                                                                                                          #
# python SkimFiles.py --inDir /eos/user/<letter>/<userName>/<projectDirectory>/skimFilesInput --outDir /eos/user/<letter>/<userName>/<projectDirectory>/skimFilesInput --Signal                  #
##################################################################################################################################################################################################

##-- Imports 
import argparse
import os 
from ROOT import * 
from python.MCTools import GetMCTreeName

##-- Get user args 
parser = argparse.ArgumentParser()
parser.add_argument('--inDir', type=str, default="", help="Comma separated list of ntuple folders", required=False)
parser.add_argument('--outDir', type=str, default="", help="Comma separated list of ntuple folders", required=False)
parser.add_argument('--fileType', type=str, default="", help="File type: Data, Signal, or Bkg", required=True)
parser.add_argument("--doppRemoval", action="store_true", default=False, help="Remove prompt-prompt events", required=False)
parser.add_argument("--oneFile", action="store_true", default=False, help="Only run on one file (helpful for quicker testing)", required=False)
# parser.add_argument("--mergeTags", action="store_true", default=False, help="Merge multiple trees into one tree", required=False) # not implemented yet. merges by default 
args = parser.parse_args()

##-- Set variables to user args 
argNames = ['inDir','outDir','doppRemoval','oneFile','fileType']
for argName in argNames:
  exec("%s = args.%s"%(argName,argName))
  exec("print '%s :', %s"%(argName,argName))

##-- Temporary: Define tags list 
tags = []
if(fileType == "Signal"): tags = [0,1,2,3,4]
else: tags = [0,1,2]

##-- Define tree selection
selection = ""
if(doppRemoval): selection = "(!((Leading_Photon_genMatchType == 1) && (Subleading_Photon_genMatchType == 1)))" # selection: remove events where both photons are prompt
print"Selection:",selection 

##-- Perform actions on files in input directory
for inFileName in os.listdir(inDir): 
  if(not inFileName.endswith(".root")): continue ##-- files ending in .root only. Avoid directories and other files 
  inFilePath = "%s/%s"%(inDir,inFileName)
  print "file name:",inFileName
  print "file path:",inFilePath

  ##-- Open file, get name, instantiate TChain for merging 
  inFile = TFile.Open(inFilePath,"READ")
  if(fileType!="Data"): MCTreeName = GetMCTreeName(inFileName)
  else: MCTreeName = "Data"
  allTags_skimmedTrees = TChain(MCTreeName,MCTreeName)

  ##-- For each tree in input file 
  for tag_i in tags: ##-- "Tag" naming is specific to HHWWgg flashgg tagger 
    print"On Tag ",tag_i
    tagOutFileName = "Tag_%s_skimmed_%s"%(tag_i,inFileName.split('/')[-1])
    tagOutFilePath = "%s/%s"%(outDir,tagOutFileName)
    tagOutFile = TFile.Open(tagOutFilePath,"RECREATE")
    tagOutFile.mkdir("tagsDumper")
    tagOutFile.mkdir("tagsDumper/trees")
    tagOutFile.cd("tagsDumper/trees")
    if(fileType == "Data"): treeName = "tagsDumper/trees/Data_13TeV_HHWWggTag_%s"%(str(tag_i))
    elif(fileType == "Signal"): treeName = "tagsDumper/trees/GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_%s"%(str(tag_i))
    else: treeName = "tagsDumper/trees/%s_13TeV_HHWWggTag_%s"%(MCTreeName,str(tag_i))
    
    originalTree = inFile.Get(treeName)
    selectedTree = originalTree.CopyTree(selection)
    selectedTree.Write()
    tagOutFile.Close()
    allTags_skimmedTrees.Add("%s/%s"%(tagOutFilePath,treeName))

  outFileName = "skimmed_%s"%(inFileName.split('/')[-1])
  outFilePath = "%s/%s"%(outDir,outFileName)
  outFile = TFile.Open(outFilePath,"RECREATE")
  # allTags_skimmedTrees.SetName(MCTreeName)
  # allTags_skimmedTrees.SetTitle(MCTreeName)    
  allTags_skimmedTrees.Merge(outFilePath)
  # allTags_skimmedTrees.SetName(MCTreeName)
  # allTags_skimmedTrees.SetTitle(MCTreeName)  
  outFile.Close()

  ############ ##-- merging into a new TDirectory had problems initially 
  ##-- To put the tree in a certain TDirectory #FIXME
  # outFileName = "skimmed_%s"%(inFileName.split('/')[-1])
  # outFilePath = "%s/%s"%(outDir,outFileName)  
  # outFile = TFile.Open(outFilePath,"RECREATE")
  # outFile.mkdir("tagsDumper")
  # outFile.mkdir("tagsDumper/trees")  
  # outFile.cd("tagsDumper/trees")

  # combinedTree = tmpOutFile_again.Get(MCTreeName)
  # print"nEntries:",combinedTree.GetEntries()
  # combinedTree.SetName(MCTreeName)
  # combinedTree.SetTitle(MCTreeName)  
  # combinedTree.Write()
  # combinedTree.SetName(MCTreeName)
  # combinedTree.SetTitle(MCTreeName)
  # tmpOutFile_again.Close()
  # tmpOutFile_again.Close()
  ############

  inFile.Close()

  ##-- Delete temporary tag files (one for each tree)
  for tag_i in tags: ##-- "Tag" naming is specific to HHWWgg flashgg tagger 
    tagOutFileName = "Tag_%s_skimmed_%s"%(tag_i,inFileName.split('/')[-1])
    tagOutFilePath = "%s/%s"%(outDir,tagOutFileName)    
    os.system("rm %s"%(tagOutFilePath))

  if(oneFile): break 
