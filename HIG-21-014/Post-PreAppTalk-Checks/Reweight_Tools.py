"""
9 November 2021 
Badder Marzocchi, Abraham Tishelman-Charny 

The purpose of this module is to perform various actions on ntuples, including adding variables and reweighting, for HIG-21-014.
"""

import ROOT 
from array import array 
from METCorrections import correctedMET
import math
import pickle 

def SetBranchStatuses(inTree, status, reweightNode):
  if(reweightNode != ""):
    orders = ["LO", "NLO"]
    nodeNames = ["cttHH0", "cttHH3", "cttHH0p35", "3D1", "3D2", "3D3", "SM", "cHHH0", "cHHH2", "cHHH5", "8a"]
    for val in [str(v) for v in range(1, 13)]: # 12 EFT benchmark nodes 
      nodeNames.append(val)
    for val in ["%sb"%(str(v)) for v in range(1, 8)]: # additional benchmarks 
      nodeNames.append(val)      
    
    for order in orders:
      for nodeName in nodeNames:
        weightBranch = "weight_{order}_{nodeName}".format(order=order, nodeName=nodeName)
        inTree.SetBranchStatus(weightBranch, status)

  inTree.SetBranchStatus('weight',status) # disable weight branch when cloning so that a new normed weight branch can be created with the same name 
  # allow access of weight branch so that values from input tree can be used 

def computeMt(part1_px, part1_py, part1_mass, part2_px, part2_py, part2_mass):
  Mt = -99.
  m1 = part1_mass
  m2 = part2_mass
  Et1 = math.sqrt(m1*m1 + part1_px*part1_px + part1_py*part1_py);
  Et2 = math.sqrt(m2*m2 + part2_px*part2_px + part2_py*part2_py);
  pt2 = part1_px*part2_px + part1_py*part2_py;
  Mt = math.sqrt(m1*m1 + m2*m2 + 2*(Et1*Et2 - pt2));
  return Mt;

def selectJets(jet0, jet0_pt, jet1, jet1_pt, jet2, jet2_pt, jet3, jet3_pt, jet4, jet4_pt):

  m01 = 999.
  m02 = 999.
  m03 = 999. 
  m04 = 999.  
  m12 = 999.
  m13 = 999.
  m14 = 999.
  m23 = 999.
  m24 = 999.
  m34 = 999.

  if jet0_pt>=0. and jet1_pt>=0.: m01 = abs((jet0+jet1).M()-80.379)
  if jet0_pt>=0. and jet2_pt>=0.: m02 = abs((jet0+jet2).M()-80.379) 
  if jet0_pt>=0. and jet3_pt>=0.: m03 = abs((jet0+jet3).M()-80.379)
  if jet0_pt>=0. and jet4_pt>=0.: m04 = abs((jet0+jet4).M()-80.379)
  if jet1_pt>=0. and jet2_pt>=0.: m12 = abs((jet1+jet2).M()-80.379)
  if jet1_pt>=0. and jet3_pt>=0.: m13 = abs((jet1+jet3).M()-80.379) 
  if jet1_pt>=0. and jet4_pt>=0.: m14 = abs((jet1+jet4).M()-80.379) 
  if jet2_pt>=0. and jet3_pt>=0.: m23 = abs((jet2+jet3).M()-80.379) 
  if jet2_pt>=0. and jet4_pt>=0.: m24 = abs((jet2+jet4).M()-80.379) 
  if jet3_pt>=0. and jet4_pt>=0.: m24 = abs((jet3+jet4).M()-80.379) 

  diff = [m01, m02, m03, m04, m12, m13, m14, m23, m24, m34]   
  index = diff.index(min(diff))
  
  if diff[index]==999.: return [-1,-1]
  elif index == 0: return [0,1]
  elif index == 1: return [0,2]
  elif index == 2: return [0,3]
  elif index == 3: return [0,4]
  elif index == 4: return [1,2]
  elif index == 5: return [1,3]
  elif index == 6: return [1,4]
  elif index == 7: return [2,3]
  elif index == 8: return [2,4]
  elif index == 9: return [3,4]

# split file into even and odd events 
def EvenOddSplit(inFile, year, lowEvents, outFile_even, outFile_odd, fullTreePath, additionalSF, reweightNode, syst):
  print("on File:",inFile)
  SFfile_dir = "/afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/HIG-21-014/Post-PreAppTalk-Checks/"
  if(additionalSF):
    SF_Dictionary = pickle.load( open( "{SFfile_dir}/EvenOddScaleFactors_2017_Nodes_1to20.p".format(SFfile_dir=SFfile_dir), "rb" ) ) # open pickle file with scale factors to apply per: node x syst x (even/odd)

  # Split into even and odd 

  print("Even events:",fullTreePath)
  tree = inFile.Get(fullTreePath)
  tree.SetBranchStatus("pdfWeights",0)
  tree.SetBranchStatus("scaleWeights",0)

  if(additionalSF):
    tree.SetBranchStatus("weight", 0) # remove weight branch from cloning so that updated weight branch can be added 
  outFile_even.cd()
  outtree_even = tree.CloneTree(0)

  if(additionalSF):
    tree.SetBranchStatus("weight", 1) # allow access of weight branch so that value from input tree can be used
    weight = array('f', [0])
    weight[0] = -99.
    _weight = outtree_even.Branch('weight', weight, 'weight/F')       

  if(lowEvents): nentries = 10
  else: nentries = tree.GetEntries()
  for i in range(0, nentries):
      tree.GetEntry(i) 
      if i%10000==0: print("Entry:",i)
      if (i%2 == 0): 
        if(additionalSF):
          SF_key = "{reweightNode}_{syst}_{div}".format(reweightNode=reweightNode, syst=syst, div="even")
          SF = SF_Dictionary[SF_key]
          Updated_weight = float(tree.weight) * float(SF) 
          weight[0] = Updated_weight              

        outtree_even.Fill() 
      
  outtree_even.Write(fullTreePath)
  outFile_even.Close()

  # odd events 
  print("Odd events:",fullTreePath)
  tree = inFile.Get(fullTreePath)
  tree.SetBranchStatus("pdfWeights",0)
  tree.SetBranchStatus("scaleWeights",0)  

  if(additionalSF):
    tree.SetBranchStatus("weight", 0) # remove weight branch from cloning so that updated weight branch can be added 

  outFile_odd.cd()
  outtree_odd = tree.CloneTree(0)

  if(additionalSF):
    tree.SetBranchStatus("weight", 1) # allow access of weight branch so that value from input tree can be used
    weight = array('f', [0])
    weight[0] = -99.
    _weight = outtree_odd.Branch('weight', weight, 'weight/F')   

  if(lowEvents): nentries = 10
  else: nentries = tree.GetEntries()
  for i in range(0, nentries):
      if i%10000==0: print("Entry:",i)
      tree.GetEntry(i) 
      if (i%2 != 0): 
        if(additionalSF):
          SF_key = "{reweightNode}_{syst}_{div}".format(reweightNode=reweightNode, syst=syst, div="odd")
          SF = SF_Dictionary[SF_key]
          Updated_weight = float(tree.weight) * float(SF) 
          weight[0] = Updated_weight         
        outtree_odd.Fill() 
  outtree_odd.Write(fullTreePath)
    
  outFile_odd.Close()  

def Categorize(inTree, name, year, lowEvents, Norm, reweightNode):

  boundaries = [0.1, 0.64, 0.82, 0.935714285714, 1.] # SM DNN 
  catLabels = ["3", "2", "1", "0"]

  for b_i, boundary in enumerate(boundaries):

    if(b_i == (len(boundaries) - 1)): continue 
    catLabel = catLabels[b_i]
    b_min, b_max = boundary, boundaries[b_i+1]
    print("min:",b_min)
    print("max:",b_max)

    outTree = inTree.CloneTree(0) # might be able to also just copytree and add selection as argument 

    # name tree based on category number 
    outTreeName = name 
    outTreeName = outTreeName.replace("HHWWggTag_0", "HHWWggTag_SL_{catLabel}".format(catLabel=catLabel))

    print("outTreeName:",outTreeName)

    outTree.SetName(outTreeName) 
    outTree.SetTitle(outTreeName)     

    nentries = inTree.GetEntries()

    if(lowEvents): 
        print("Running on low number of events")
        nentries = 1000

    for i in range(0, nentries):
      inTree.GetEntry(i)
      if i%10000==0: print("Entry:",i)

      # if final category, include upper bound
      if(b_i == (len(boundaries) - 1)):
        DNNscore = inTree.evalDNN_HH
        if((DNNscore >= b_min) and (DNNscore <= b_max) ):
          outTree.Fill()
        else:
          continue 
      else:
        DNNscore = inTree.evalDNN_HH
        if((DNNscore >= b_min) and (DNNscore < b_max) ):
          outTree.Fill()
        else:
          continue         

      # only save an event in the output tree if its DNN score is in this category 


    outTree.Write()  

def Reweight(inTree, name, year, lowEvents, Norm, reweightNode, addNodeBranch):
  
  SetBranchStatuses(inTree, 0, reweightNode) # don't clone all weight branches to output file to make it clear no reweighting needs to be done anymore 
  outTree = inTree.CloneTree(0)
  SetBranchStatuses(inTree, 1, reweightNode) # allow access of weight branches so that values from input tree can be used 

  # define combined NLO name (need common tree names to hadd afterwards)
  outTreeName = name # Format: GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0_<systematic> 

  # replace node string 
  outTreeName = outTreeName.replace("node_cHHH0_13TeV","node_All_NLO_{year}_Normalized_13TeV".format(year=year))
  outTreeName = outTreeName.replace("node_cHHH1_13TeV","node_All_NLO_{year}_Normalized_13TeV".format(year=year))
  outTreeName = outTreeName.replace("node_cHHH2p45_13TeV","node_All_NLO_{year}_Normalized_13TeV".format(year=year))
  outTreeName = outTreeName.replace("node_cHHH5_13TeV","node_All_NLO_{year}_Normalized_13TeV".format(year=year))

  # If reweighting to a node, put node name in tree 
  if(reweightNode != ""):
    outTreeName = outTreeName.replace("node_All_NLO_{year}_Normalized_13TeV".format(year=year),"node_{reweightNode}_{year}_13TeV".format(reweightNode=reweightNode, year=year))

  print("outTreeName:",outTreeName)

  outTree.SetName(outTreeName) # Common "ALL NLO" tree name since nodes will be hadded 
  outTree.SetTitle(outTreeName)     

  nentries = inTree.GetEntries()

  if(lowEvents): 
      print("Running on low number of events")
      nentries = 10

  weight = array('f', [0])
  weight[0] = -99.
  _weight = outTree.Branch('weight', weight, 'weight/F')   

  if(addNodeBranch):
    Node_Number = array('f', [0])
    Node_Number[0] = -99
    _Node_Number = outTree.Branch('Node_Number', Node_Number, 'Node_Number/F')

  for i in range(0, nentries):
    inTree.GetEntry(i)
   
    if i%10000==0: print("Entry:",i)

    # Update weight branch based on normalization factor for file, or node you want to reweight to 
    Updated_weight = float(inTree.weight) * float(Norm)
    if(reweightNode != ""):
      nodeBranchDict = {
          "cHHH0" : "weight_NLO_cHHH0",
          "cHHH1" : "weight_NLO_SM",
          "cHHH2p45" : "weight_NLO_cHHH2", # typo in reweight branch names. "weight_NLO_cHHH2" corresponds to cHHH2p45 
          "cHHH5" : "weight_NLO_cHHH5",
          "cttHH3" : "weight_NLO_cttHH3",
          "cttHH0p35" : "weight_NLO_cttHH0p35",
          "3D3" : "weight_NLO_3D3",
          "1"  : "weight_NLO_1",
          "2"  : "weight_NLO_2",
          "3"  : "weight_NLO_3",
          "4"  : "weight_NLO_4",
          "5"  : "weight_NLO_5",
          "6"  : "weight_NLO_6",
          "7"  : "weight_NLO_7",
          "8"  : "weight_NLO_8",
          "9"  : "weight_NLO_9",
          "10"  : "weight_NLO_10",
          "11"  : "weight_NLO_11",
          "12"  : "weight_NLO_12",   
          "13" : "weight_NLO_8a",
          "14" : "weight_NLO_1b",
          "15" : "weight_NLO_2b",
          "16" : "weight_NLO_3b",
          "17" : "weight_NLO_4b",
          "18" : "weight_NLO_5b",
          "19" : "weight_NLO_6b",
          "20" : "weight_NLO_7b",                 
      }      

      # arbitrarily name the 20 nodes 1-20 for parametric DNN training. 
      nodeNumberDict = {
        "1" : "1",
        "2" : "2",
        "3" : "3",
        "4" : "4",
        "5" : "5",
        "6" : "6",
        "7" : "7",
        "8" : "8",
        "9" : "9",
        "10" : "10",
        "11" : "11",
        "12" : "12",
        "13" : "13",
        "14" : "14",
        "15" : "15",
        "16" : "16",
        "17" : "17",
        "18" : "18",
        "19" : "19",
        "20" : "20",
      } 

      reweightNodeBranch = nodeBranchDict[reweightNode]

      exec("node_weight = float(inTree.{reweightNodeBranch})".format(reweightNodeBranch=reweightNodeBranch))
      Updated_weight = Updated_weight * node_weight 

      if(addNodeBranch):
        nodeVal = float(nodeNumberDict[reweightNode])
        Node_Number[0] = nodeVal

    weight[0] = Updated_weight
    
    outTree.Fill() 
  outTree.Write()

def addVariables(inTree, name, year, lowEvents, Norm, reweightNode):

  # inTree.SetBranchStatus('kinWeight',0)
  # inTree.SetBranchStatus('weight_NLO_node',0)
  #inTree.SetBranchStatus('weight_NLO_SM',0)

#   inTree.SetBranchStatus('METCor_pt',0)
#   inTree.SetBranchStatus('METCor_eta',0)
#   inTree.SetBranchStatus('METCor_phi',0)
#   inTree.SetBranchStatus('METCor_E',0)
#   inTree.SetBranchStatus('METCor_px',0)
#   inTree.SetBranchStatus('METCor_py',0) 
#   inTree.SetBranchStatus('METCor_pz',0)
#   inTree.SetBranchStatus('goodLepton_pt',0)
#   inTree.SetBranchStatus('goodLepton_eta',0)
#   inTree.SetBranchStatus('goodLepton_phi',0)
#   inTree.SetBranchStatus('goodLepton_E',0)
#   inTree.SetBranchStatus('goodLepton_px',0)
#   inTree.SetBranchStatus('goodLepton_py',0) 
#   inTree.SetBranchStatus('goodLepton_pz',0)
#   inTree.SetBranchStatus('WJet1_pt',0)
#   inTree.SetBranchStatus('WJet1_eta',0)
#   inTree.SetBranchStatus('WJet1_phi',0)
#   inTree.SetBranchStatus('WJet1_E',0)
#   inTree.SetBranchStatus('WJet2_pt',0)
#   inTree.SetBranchStatus('WJet2_eta',0)
#   inTree.SetBranchStatus('WJet2_phi',0)
#   inTree.SetBranchStatus('WJet2_E',0)
#   inTree.SetBranchStatus('Wmt_L',0)
#   inTree.SetBranchStatus('Wmt_H',0)
#   inTree.SetBranchStatus('Wmt_goodJets12',0)
#   inTree.SetBranchStatus('Wmass_H',0)
#   inTree.SetBranchStatus('Wmass_goodJets12',0)
  
  # kinWeight = array('f', [0])
  # weight_NLO_node = array('f', [0])
  #weight_NLO_SM = array('f', [0])
  METCor_pt = array('f', [0])
  METCor_eta = array('f', [0])
  METCor_phi = array('f', [0])
  METCor_E = array('f', [0])
  METCor_px = array('f', [0])
  METCor_py = array('f', [0])
  METCor_pz = array('f', [0])
  goodLepton_pt = array('f', [0])
  goodLepton_eta = array('f', [0])
  goodLepton_phi = array('f', [0])
  goodLepton_E = array('f', [0])
  goodLepton_px = array('f', [0])
  goodLepton_py = array('f', [0])
  goodLepton_pz = array('f', [0])
  WJet1_pt = array('f', [0])
  WJet1_eta = array('f', [0])
  WJet1_phi = array('f', [0])
  WJet1_E = array('f', [0])
  WJet2_pt = array('f', [0])
  WJet2_eta = array('f', [0])
  WJet2_phi = array('f', [0])
  WJet2_E = array('f', [0])
  Wmt_L = array('f', [0])
  Wmt_H = array('f', [0])
  Wmt_goodJets12 = array('f', [0])
  Wmass_H = array('f', [0])
  Wmass_goodJets12 = array('f', [0])

  # kinWeight[0] = 1.
  # weight_NLO_node[0] = 1. 
  #weight_NLO_SM[0] = 1.
  goodLepton_pt[0] = -99.
  goodLepton_eta[0] = -99.
  goodLepton_phi[0] = -99.
  goodLepton_E[0] = -99.
  goodLepton_px[0] = -99.
  goodLepton_py[0] = -99.
  goodLepton_pz[0] = -99.
  WJet1_pt[0] = -99.
  WJet1_eta[0] = -99.
  WJet1_phi[0] = -99.
  WJet1_E[0] = -99.
  WJet2_pt[0] = -99.
  WJet2_eta[0] = -99.
  WJet2_phi[0] = -99.
  WJet2_E[0] = -99.
  Wmt_L[0] = -99.
  Wmt_H[0] = -99.
  Wmt_goodJets12[0] = -99.
  Wmass_H[0] = -99.
  Wmass_goodJets12[0] = -99.
  
  inTree.SetBranchStatus('weight',0) # disable weight branch when cloning so that a new normed weight branch can be created with the same name 

  # don't clone all weight branches to output file to make it clear no reweighting needs to be done anymore 
  if(reweightNode != ""):
    orders = ["LO", "NLO"]
    nodeNames = ["cttHH0", "cttHH3", "cttHH0p35", "3D1", "3D2", "3D3", "SM", "cHHH0", "cHHH2", "cHHH5", "8a"]
    for val in [str(v) for v in range(1, 13)]: # 12 EFT benchmark nodes 
      nodeNames.append(val)
    for val in ["%sb"%(str(v)) for v in range(1, 8)]: # additional benchmarks 
      nodeNames.append(val)      
    
    for order in orders:
      for nodeName in nodeNames:
        weightBranch = "weight_{order}_{nodeName}".format(order=order, nodeName=nodeName)
        inTree.SetBranchStatus(weightBranch, 0)


  outTree = inTree.CloneTree(0)
  inTree.SetBranchStatus('weight',1) # allow access of weight branch so that values from input tree can be used 

  # allow access of weight branches so that values from input tree can be used 
  if(reweightNode != ""):
    orders = ["LO", "NLO"]
    nodeNames = ["cttHH0", "cttHH3", "cttHH0p35", "3D1", "3D2", "3D3", "SM", "cHHH0", "cHHH2", "cHHH5", "8a"]
    for val in [str(v) for v in range(1, 13)]: # 12 EFT benchmark nodes 
      nodeNames.append(val)
    for val in ["%sb"%(str(v)) for v in range(1, 8)]: # additional benchmarks 
      nodeNames.append(val)      
    
    for order in orders:
      for nodeName in nodeNames:
        weightBranch = "weight_{order}_{nodeName}".format(order=order, nodeName=nodeName)
        inTree.SetBranchStatus(weightBranch, 1)  

  # define combined NLO name (need common tree names to hadd afterwards)
  outTreeName = name # Format: GluGluToHHTo2G2Qlnu_node_cHHH1_13TeV_HHWWggTag_0_<systematic> 

  # replace node string 
  outTreeName = outTreeName.replace("node_cHHH0_13TeV","node_All_NLO_{year}_Normalized_13TeV".format(year=year))
  outTreeName = outTreeName.replace("node_cHHH1_13TeV","node_All_NLO_{year}_Normalized_13TeV".format(year=year))
  outTreeName = outTreeName.replace("node_cHHH2p45_13TeV","node_All_NLO_{year}_Normalized_13TeV".format(year=year))
  outTreeName = outTreeName.replace("node_cHHH5_13TeV","node_All_NLO_{year}_Normalized_13TeV".format(year=year))

  # If reweighting to a node, put node name in tree 
  if(reweightNode != ""):
    outTreeName = outTreeName.replace("node_All_NLO_{year}_Normalized_13TeV".format(year=year),"node_{reweightNode}_{year}_13TeV".format(reweightNode=reweightNode, year=year))

  # print("originalName:",originalName)
  print("outTreeName:",outTreeName)

  outTree.SetName(outTreeName) # Common "ALL NLO" tree name since nodes will be hadded 
  outTree.SetTitle(outTreeName)     

  # _kinWeight = outTree.Branch('kinWeight', kinWeight, 'kinWeight/F')  
  # _weight_NLO_node = outTree.Branch('weight_NLO_node', weight_NLO_node, 'weight_NLO_node/F')   
  #_weight_NLO_SM = outTree.Branch('weight_NLO_SM', weight_NLO_SM, 'weight_NLO_SM/F')  
  _METCor_pt = outTree.Branch('METCor_pt', METCor_pt, 'METCor_pt/F')   
  _METCor_eta = outTree.Branch('METCor_eta', METCor_eta, 'METCor_eta/F')   
  _METCor_phi = outTree.Branch('METCor_phi', METCor_phi, 'METCor_phi/F')   
  _METCor_E = outTree.Branch('METCor_E', METCor_E, 'METCor_E/F')  
  _METCor_px = outTree.Branch('METCor_px', METCor_px, 'METCor_px/F')   
  _METCor_py = outTree.Branch('METCor_py', METCor_py, 'METCor_py/F')  
  _METCor_pz = outTree.Branch('METCor_pz', METCor_pz, 'METCor_pz/F')  
  _goodLepton_pt = outTree.Branch('goodLepton_pt', goodLepton_pt, 'goodLepton_pt/F')   
  _goodLepton_eta = outTree.Branch('goodLepton_eta', goodLepton_eta, 'goodLepton_eta/F')   
  _goodLepton_phi = outTree.Branch('goodLepton_phi', goodLepton_phi, 'goodLepton_phi/F')   
  _goodLepton_E = outTree.Branch('goodLepton_E', goodLepton_E, 'goodLepton_E/F')  
  _goodLepton_px = outTree.Branch('goodLepton_px', goodLepton_px, 'goodLepton_px/F')   
  _goodLepton_py = outTree.Branch('goodLepton_py', goodLepton_py, 'goodLepton_py/F')  
  _goodLepton_pz = outTree.Branch('goodLepton_pz', goodLepton_pz, 'goodLepton_pz/F')  
  _WJet1_pt = outTree.Branch('WJet1_pt', WJet1_pt, 'WJet1_pt/F')   
  _WJet1_eta = outTree.Branch('WJet1_eta', WJet1_eta, 'WJet1_eta/F')   
  _WJet1_phi = outTree.Branch('WJet1_phi', WJet1_phi, 'WJet1_phi/F')   
  _WJet1_E = outTree.Branch('WJet1_E', WJet1_E, 'WJet1_E/F')  
  _WJet2_pt = outTree.Branch('WJet2_pt', WJet2_pt, 'WJet2_pt/F')   
  _WJet2_eta = outTree.Branch('WJet2_eta', WJet2_eta, 'WJet2_eta/F')   
  _WJet2_phi = outTree.Branch('WJet2_phi', WJet2_phi, 'WJet2_phi/F')   
  _WJet2_E = outTree.Branch('WJet2_E', WJet2_E, 'WJet2_E/F')   
  _Wmt_L = outTree.Branch('Wmt_L', Wmt_L, 'Wmt_L/F')    
  _Wmt_H = outTree.Branch('Wmt_H', Wmt_H, 'Wmt_H/F')   
  _Wmt_goodJets12 = outTree.Branch('Wmt_goodJets12', Wmt_goodJets12, 'Wmt_goodJets12/F')     
  _Wmass_H = outTree.Branch('Wmass_H', Wmass_H, 'Wmass_H/F')    
  _Wmass_goodJets12 = outTree.Branch('Wmass_goodJets12', Wmass_goodJets12, 'Wmass_goodJets12/F')  


  nentries = inTree.GetEntries()

  if(lowEvents): 
      print("Running on low number of events")
      nentries = 10

  weight = array('f', [0])
  weight[0] = -99.
  _weight = outTree.Branch('weight', weight, 'weight/F')   

  #print nentries
  for i in range(0, nentries):
    inTree.GetEntry(i)
   
    if i%10000==0: print("Entry:",i)
    #if i>10000: continue 
   
    # eftWeight_val = 1.
    # if eftWeight=="weight_NLO_1": eftWeight_val = inTree.weight_NLO_1
    # elif eftWeight=="weight_NLO_2": eftWeight_val = inTree.weight_NLO_2
    # elif eftWeight=="weight_NLO_3": eftWeight_val = inTree.weight_NLO_3
    # elif eftWeight=="weight_NLO_4": eftWeight_val = inTree.weight_NLO_4
    # elif eftWeight=="weight_NLO_5": eftWeight_val = inTree.weight_NLO_5
    # elif eftWeight=="weight_NLO_6": eftWeight_val = inTree.weight_NLO_6
    # elif eftWeight=="weight_NLO_7": eftWeight_val = inTree.weight_NLO_7
    # elif eftWeight=="weight_NLO_8": eftWeight_val = inTree.weight_NLO_8
    # elif eftWeight=="weight_NLO_9": eftWeight_val = inTree.weight_NLO_9
    # elif eftWeight=="weight_NLO_10": eftWeight_val = inTree.weight_NLO_10
    # elif eftWeight=="weight_NLO_11": eftWeight_val = inTree.weight_NLO_11
    # elif eftWeight=="weight_NLO_12": eftWeight_val = inTree.weight_NLO_12
    # elif eftWeight=="weight_NLO_SM": eftWeight_val = inTree.weight_NLO_SM

    # kinWeight[0] = 1.
    # weight_NLO_node[0] = eftWeight_val
    #weight_NLO_SM[0] = 1.
    
    met = correctedMET(inTree.MET_pt, inTree.MET_phi, inTree.nvtx, inTree.run, False, 2017)   
    METCor_pt[0] = met[2]
    METCor_eta[0] = 0.
    METCor_phi[0] = met[3]
    METCor_E[0] = met[2]
    METCor_px[0] = met[0]
    METCor_py[0] = met[1]
    METCor_pz[0] = 0.
    
    Wmt_L[0] = -99.

    if inTree.goodMuons_0_pt>inTree.goodElectrons_0_pt and inTree.goodMuons_0_pt>=0.: 
      goodLepton_pt[0] = inTree.goodMuons_0_pt
      goodLepton_eta[0] = inTree.goodMuons_0_eta
      goodLepton_phi[0] = inTree.goodMuons_0_phi
      goodLepton_E[0] = inTree.goodMuons_0_E
      goodLepton_px[0] = inTree.goodMuons_0_px
      goodLepton_py[0] = inTree.goodMuons_0_py
      goodLepton_pz[0] = inTree.goodMuons_0_pz
    elif inTree.goodElectrons_0_pt>inTree.goodMuons_0_pt and inTree.goodElectrons_0_pt>=0.: 
      goodLepton_pt[0] = inTree.goodElectrons_0_pt
      goodLepton_eta[0] = inTree.goodElectrons_0_eta
      goodLepton_phi[0] = inTree.goodElectrons_0_phi
      goodLepton_E[0] = inTree.goodElectrons_0_E 
      goodLepton_px[0] = inTree.goodElectrons_0_px 
      goodLepton_py[0] = inTree.goodElectrons_0_py 
      goodLepton_pz[0] = inTree.goodElectrons_0_pz 
    else:
      goodLepton_pt[0] = -99.
      goodLepton_eta[0] = -99.
      goodLepton_phi[0] = -99.
      goodLepton_E[0] = -99.
      goodLepton_px[0] = -99.
      goodLepton_py[0] = -99.
      goodLepton_pz[0] = -99.

    vec = ROOT.TLorentzVector()
    if goodLepton_pt[0]>0.:
      vec.SetPtEtaPhiE(goodLepton_pt[0], goodLepton_eta[0], goodLepton_phi[0], goodLepton_E[0])
      Wmt_L[0] = computeMt(goodLepton_px[0], goodLepton_py[0], vec.M(), METCor_px[0], METCor_py[0], 0.)
     
    jet0 = ROOT.TLorentzVector()
    jet1 = ROOT.TLorentzVector()
    jet2 = ROOT.TLorentzVector()
    jet3 = ROOT.TLorentzVector() 
    jet4 = ROOT.TLorentzVector() 
    jet0.SetPtEtaPhiE(inTree.goodJets_0_pt, inTree.goodJets_0_eta, inTree.goodJets_0_phi, inTree.goodJets_0_E)
    jet1.SetPtEtaPhiE(inTree.goodJets_1_pt, inTree.goodJets_1_eta, inTree.goodJets_1_phi, inTree.goodJets_1_E)
    jet2.SetPtEtaPhiE(inTree.goodJets_2_pt, inTree.goodJets_2_eta, inTree.goodJets_2_phi, inTree.goodJets_2_E)
    jet3.SetPtEtaPhiE(inTree.goodJets_3_pt, inTree.goodJets_3_eta, inTree.goodJets_3_phi, inTree.goodJets_3_E)
    jet4.SetPtEtaPhiE(inTree.goodJets_4_pt, inTree.goodJets_4_eta, inTree.goodJets_4_phi, inTree.goodJets_4_E)

    if inTree.goodJets_0_pt<0. or inTree.goodJets_1_pt<0.:
      Wmt_goodJets12[0] = -99.
      Wmass_goodJets12[0] = -99.
    else: 
      Wmt_goodJets12[0] = computeMt(jet0.Px(), jet0.Py(), jet0.M(), jet1.Px(), jet1.Py(), jet1.M())
      Wmass_goodJets12[0] = (jet0+jet1).M() 
      if (jet0+jet1).M()<-99.: 
        print("Wmass_goodJets12[0]:",(jet0+jet1).M())  
        print("jet0:",inTree.goodJets_0_pt, inTree.goodJets_0_eta, inTree.goodJets_0_phi, inTree.goodJets_0_E)
        print("jet1:",inTree.goodJets_1_pt, inTree.goodJets_1_eta, inTree.goodJets_1_phi, inTree.goodJets_1_E)    
          
    WJets_indices = selectJets(jet0, inTree.goodJets_0_pt, jet1, inTree.goodJets_1_pt, jet2, inTree.goodJets_3_pt, jet3, inTree.goodJets_3_pt, jet4, inTree.goodJets_4_pt)
    if WJets_indices[0]==-1 or WJets_indices[1]==-1: 
      WJet1_pt[0] = -99.
      WJet1_eta[0] = -99.
      WJet1_phi[0] = -99.
      WJet1_E[0] = -99.
      WJet2_pt[0] = -99.
      WJet2_eta[0] = -99.
      WJet2_phi[0] = -99.
      WJet2_E[0] = -99.
      Wmt_H[0] = -99
      Wmass_H[0] = -99. 
    elif WJets_indices[0]==0 and WJets_indices[1]==1: 
      WJet1_pt[0] = jet0.Pt()
      WJet1_eta[0] = jet0.Eta()
      WJet1_phi[0] = jet0.Phi()
      WJet1_E[0] = jet0.Energy()
      WJet2_pt[0] = jet1.Pt()
      WJet2_eta[0] = jet1.Eta()
      WJet2_phi[0] = jet1.Phi()
      WJet2_E[0] = jet1.Energy()
      Wmt_H[0] = computeMt(jet0.Px(), jet0.Py(), jet0.M(), jet1.Px(), jet1.Py(), jet1.M())
      Wmass_H[0] = (jet0+jet1).M() 
    elif WJets_indices[0]==0 and WJets_indices[1]==2: 
      WJet1_pt[0] = jet0.Pt()
      WJet1_eta[0] = jet0.Eta()
      WJet1_phi[0] = jet0.Phi()
      WJet1_E[0] = jet0.Energy()
      WJet2_pt[0] = jet2.Pt()
      WJet2_eta[0] = jet2.Eta()
      WJet2_phi[0] = jet2.Phi()
      WJet2_E[0] = jet2.Energy()
      Wmt_H[0] = computeMt(jet0.Px(), jet0.Py(), jet0.M(), jet2.Px(), jet2.Py(), jet2.M())
      Wmass_H[0] = (jet0+jet2).M() 
    elif WJets_indices[0]==0 and WJets_indices[1]==3: 
      WJet1_pt[0] = jet0.Pt()
      WJet1_eta[0] = jet0.Eta()
      WJet1_phi[0] = jet0.Phi()
      WJet1_E[0] = jet0.Energy()
      WJet2_pt[0] = jet3.Pt()
      WJet2_eta[0] = jet3.Eta()
      WJet2_phi[0] = jet3.Phi()
      WJet2_E[0] = jet3.Energy()
      Wmt_H[0] = computeMt(jet0.Px(), jet0.Py(), jet0.M(), jet3.Px(), jet3.Py(), jet3.M())
      Wmass_H[0] = (jet0+jet3).M()
    elif WJets_indices[0]==0 and WJets_indices[1]==4: 
      WJet1_pt[0] = jet0.Pt()
      WJet1_eta[0] = jet0.Eta()
      WJet1_phi[0] = jet0.Phi()
      WJet1_E[0] = jet0.Energy()
      WJet2_pt[0] = jet4.Pt()
      WJet2_eta[0] = jet4.Eta()
      WJet2_phi[0] = jet4.Phi()
      WJet2_E[0] = jet4.Energy()
      Wmt_H[0] = computeMt(jet0.Px(), jet0.Py(), jet0.M(), jet4.Px(), jet4.Py(), jet4.M())
      Wmass_H[0] = (jet0+jet4).M()
    elif WJets_indices[0]==1 and WJets_indices[1]==2: 
      WJet1_pt[0] = jet1.Pt()
      WJet1_eta[0] = jet1.Eta()
      WJet1_phi[0] = jet1.Phi()
      WJet1_E[0] = jet1.Energy()
      WJet2_pt[0] = jet2.Pt()
      WJet2_eta[0] = jet2.Eta()
      WJet2_phi[0] = jet2.Phi()
      WJet2_E[0] = jet2.Energy()
      Wmt_H[0] = computeMt(jet1.Px(), jet1.Py(), jet1.M(), jet2.Px(), jet2.Py(), jet2.M())
      Wmass_H[0] = (jet1+jet2).M()   
    elif WJets_indices[0]==1 and WJets_indices[1]==3: 
      WJet1_pt[0] = jet1.Pt()
      WJet1_eta[0] = jet1.Eta()
      WJet1_phi[0] = jet1.Phi()
      WJet1_E[0] = jet1.Energy()
      WJet2_pt[0] = jet3.Pt()
      WJet2_eta[0] = jet3.Eta()
      WJet2_phi[0] = jet3.Phi()
      WJet2_E[0] = jet3.Energy()
      Wmt_H[0] = computeMt(jet1.Px(), jet1.Py(), jet1.M(), jet3.Px(), jet3.Py(), jet3.M())
      Wmass_H[0] = (jet1+jet3).M()   
    elif WJets_indices[0]==1 and WJets_indices[1]==4: 
      WJet1_pt[0] = jet1.Pt()
      WJet1_eta[0] = jet1.Eta()
      WJet1_phi[0] = jet1.Phi()
      WJet1_E[0] = jet1.Energy()
      WJet2_pt[0] = jet4.Pt()
      WJet2_eta[0] = jet4.Eta()
      WJet2_phi[0] = jet4.Phi()
      WJet2_E[0] = jet4.Energy()
      Wmt_H[0] = computeMt(jet1.Px(), jet1.Py(), jet1.M(), jet4.Px(), jet4.Py(), jet4.M())
      Wmass_H[0] = (jet1+jet4).M()   
    elif WJets_indices[0]==2 and WJets_indices[1]==3: 
      WJet1_pt[0] = jet2.Pt()
      WJet1_eta[0] = jet2.Eta()
      WJet1_phi[0] = jet2.Phi()
      WJet1_E[0] = jet2.Energy()
      WJet2_pt[0] = jet3.Pt()
      WJet2_eta[0] = jet3.Eta()
      WJet2_phi[0] = jet3.Phi()
      WJet2_E[0] = jet3.Energy()
      Wmt_H[0] = computeMt(jet2.Px(), jet2.Py(), jet2.M(), jet3.Px(), jet3.Py(), jet3.M())
      Wmass_H[0] = (jet2+jet3).M()   
    elif WJets_indices[0]==2 and WJets_indices[1]==4: 
      WJet1_pt[0] = jet2.Pt()
      WJet1_eta[0] = jet2.Eta()
      WJet1_phi[0] = jet2.Phi()
      WJet1_E[0] = jet2.Energy()
      WJet2_pt[0] = jet4.Pt()
      WJet2_eta[0] = jet4.Eta()
      WJet2_phi[0] = jet4.Phi()
      WJet2_E[0] = jet4.Energy()
      Wmt_H[0] = computeMt(jet2.Px(), jet2.Py(), jet2.M(), jet4.Px(), jet4.Py(), jet4.M())
      Wmass_H[0] = (jet2+jet4).M()   
    elif WJets_indices[0]==3 and WJets_indices[1]==4: 
      WJet1_pt[0] = jet3.Pt()
      WJet1_eta[0] = jet3.Eta()
      WJet1_phi[0] = jet3.Phi()
      WJet1_E[0] = jet3.Energy()
      WJet2_pt[0] = jet4.Pt()
      WJet2_eta[0] = jet4.Eta()
      WJet2_phi[0] = jet4.Phi()
      WJet2_E[0] = jet4.Energy()
      Wmt_H[0] = computeMt(jet3.Px(), jet3.Py(), jet3.M(), jet4.Px(), jet4.Py(), jet4.M())
      Wmass_H[0] = (jet3+jet4).M()   

    # Update weight branch based on normalization factor for file, or node you want to reweight to 
    Updated_weight = float(inTree.weight) * float(Norm)
    if(reweightNode != ""):
      nodeBranchDict = {
          "cHHH0" : "weight_NLO_cHHH0",
          "cHHH1" : "weight_NLO_SM",
          "cHHH2p45" : "weight_NLO_cHHH2", # typo in reweight branch names. "weight_NLO_cHHH2" corresponds to cHHH2p45 
          "cHHH5" : "weight_NLO_cHHH5",
          "cttHH3" : "weight_NLO_cttHH3",
          "cttHH0p35" : "weight_NLO_cttHH0p35",
          "3D3" : "weight_NLO_3D3",
          "8a" : "weight_NLO_8a",
          "1b" : "weight_NLO_1b",
          "2b" : "weight_NLO_2b",
          "3b" : "weight_NLO_3b",
          "4b" : "weight_NLO_4b",
          "5b" : "weight_NLO_5b",
          "6b" : "weight_NLO_6b",
          "7b" : "weight_NLO_7b",
      }      

      reweightNodeBranch = nodeBranchDict[reweightNode]

      exec("node_weight = float(inTree.{reweightNodeBranch})".format(reweightNodeBranch=reweightNodeBranch))
      Updated_weight = Updated_weight * node_weight 
    weight[0] = Updated_weight

    outTree.Fill() 
  outTree.Write()