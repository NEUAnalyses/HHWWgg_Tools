
# only update MET variable and recreate output file 
def UpdateMET(inTree, name, year, lowEvents, Norm, reweightNode):
  METCor_pt = array('f', [0])
  METCor_eta = array('f', [0])
  METCor_phi = array('f', [0])
  METCor_E = array('f', [0])
  METCor_px = array('f', [0])
  METCor_py = array('f', [0])
  METCor_pz = array('f', [0])
  Wmt_L = array('f', [0])
  _METCor_pt = outTree.Branch('METCor_pt', METCor_pt, 'METCor_pt/F')   
  _METCor_eta = outTree.Branch('METCor_eta', METCor_eta, 'METCor_eta/F')   
  _METCor_phi = outTree.Branch('METCor_phi', METCor_phi, 'METCor_phi/F')   
  _METCor_E = outTree.Branch('METCor_E', METCor_E, 'METCor_E/F')  
  _METCor_px = outTree.Branch('METCor_px', METCor_px, 'METCor_px/F')   
  _METCor_py = outTree.Branch('METCor_py', METCor_py, 'METCor_py/F')  
  _METCor_pz = outTree.Branch('METCor_pz', METCor_pz, 'METCor_pz/F')  
  _Wmt_L = outTree.Branch('Wmt_L', Wmt_L, 'Wmt_L/F') 

  isMC = 1 
  
  met = correctedMET(inTree.MET_pt, inTree.MET_phi, inTree.nvtx, inTree.run, isMC, year)   
  METCor_pt[0] = met[2]
  METCor_eta[0] = 0.
  METCor_phi[0] = met[3]
  METCor_E[0] = met[2]
  METCor_px[0] = met[0]
  METCor_py[0] = met[1]
  METCor_pz[0] = 0.  

  Minimum_Variables = [
        'dZ',
        'centralObjectWeight',
        'candidate_id',
        'sigmaMoM_decorr',
        'LooseMvaSFCentral',
        'PreselSFCentral',
        'TriggerWeightCentral',
        'electronVetoSFCentral',
        'ElectronIDWeightCentral',
        'ElectronRecoWeightCentral',
        'JetBTagCutWeightCentral',
        'JetBTagReshapeWeightCentral',
        'MuonIDWeightCentral',
        'MuonIsoWeightCentral',
        'prefireWeightCentral',
        'genMhh',
        'weight',
        'puweight',
        'CMS_hgg_mass',
        'goodJets_0_E', 
        'goodLepton_phi', 
        'Subleading_Photon_E',
        'Leading_Photon_pt', 
        'Leading_Photon_MVA', 
        'goodLepton_eta', #5
        'goodJets_1_E', #6
        'Wmass_goodJets12', #7
        'goodLepton_E', #8
        'goodJets_1_eta', #9
        'goodJets_1_phi', #10
        'Subleading_Photon_eta', #11
        'goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probb',
        'goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_probbb',
        'goodJets_1_bDiscriminator_mini_pfDeepFlavourJetTags_problepb', #12
        'goodLepton_pt', #13
        'goodJets_0_pt', #14
        'Node_Number', #15
        'Subleading_Photon_pt', #16
        'Subleading_Photon_phi', #17
        'goodJets_1_pt', #18
        'N_goodJets', #19
        'goodJets_0_phi', #20
        'METCor_pt', #21
        'Leading_Photon_E', #22
        'Leading_Photon_phi', #23
        'Subleading_Photon_MVA', #24
        'goodJets_0_eta', #25
        'Leading_Photon_eta', #26
        'Wmt_L', #27
        'goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probb',
        'goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_probbb',
        'goodJets_0_bDiscriminator_mini_pfDeepFlavourJetTags_problepb' #28
  ]

  inTree.SetBranchStatus("*",0); # disable all branches

  for var in Minimum_Variables: # only want to clone necessary variables to save space. 
    inTree.SetBranchStatus(var, 1)

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