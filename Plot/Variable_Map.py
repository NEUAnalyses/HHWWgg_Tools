def var_map(v0_,plab_,G_):
    #G_ = boolean of GEN. If gen, = 1. if reco, = 0 
    var_conv = {
    # "TagVarString": ['<v[0]>','<plabel>',GEN=1 RECO=0]

    # Cuts
    # "Cut_0": ['Cut_0','le',0],
    # "Cut_0                      := Cut_Results[0]", 
    # "Cut_1                      := Cut_Results[1]",
    # "Cut_2                      := Cut_Results[2]",
    # "Cut_3                      := Cut_Results[3]",
    # "Cut_4                      := Cut_Results[4]",
    # "Cut_5                      := Cut_Results[5]",
    # "Cut_6                      := Cut_Results[6]",
    # "Cut_7                      := Cut_Results[7]",
        # if (n_photons >= 2) Cut_Results[1] = 1.0; # cut 1 
        # if (n_electrons >= 1) Cut_Results[2] = 1.0; # cut 2 
        # if (n_muons >= 1) Cut_Results[3] = 1.0;
        # if (n_jets >= 1) Cut_Results[4] = 1.0;
        # if (one_ps_dp) Cut_Results[5] = 1.0;
        # if (one_slw_tag) Cut_Results[6] = 1.0;
        # if ( (one_ps_dp) and (one_slw_tag) ) Cut_Results[7] = 1.0;
    ## RECO

    # Photons 
    "leading_pho_pt": ['pt','lp',0],
    "leading_pho_eta": ['eta','lp',0],
    "leading_pho_phi": ['phi','lp',0],
    "sub_leading_pho_pt": ['pt','slp',0],
    "sub_leading_pho_eta": ['eta','slp',0],
    "sub_leading_pho_phi": ['phi','slp',0],  
    
    # Electrons
    "leading_elec_pt": ['pt','le',0],
    "leading_elec_eta": ['eta','le',0],
    "leading_elec_phi": ['phi','le',0],
    "subleading_elec_pt": ['pt','sle',0],
    "subleading_elec_eta": ['eta','sle',0],
    "subleading_elec_phi": ['phi','sle',0],

    # Muons
    "leading_muon_pt": ['pt','lm',0],
    "leading_muon_eta": ['eta','lm',0],
    "leading_muon_phi": ['phi','lm',0],
    "subleading_muon_pt": ['pt','slm',0],
    "subleading_muon_eta": ['eta','slm',0],
    "subleading_muon_phi": ['phi','slm',0],
    
    # Met

    # Jets
    "mdj_invmass": ['invmass','mjj',0],
    "nmdj_invmass": ['invmass','nmjj',0],

#############################################

    ## GEN

    # Electrons
    "gen_leading_elec_pt": ['pt','le',1],
    "gen_subleading_elec_pt": ['pt','sle',1],

    # Muons 
    "gen_leading_muon_pt": ['pt','lm',1],
    "gen_subleading_muon_pt": ['pt','slm',1], 

    # Met 

    # Quarks 
    "mdq_invmass": ['invmass','mjj',1],
    "nmdq_invmass": ['invmass','nmjj',1],

    }

    # ## RECO Variables

    # # Photons 
    # "n_photons                           := phoVector.size()",
    # "leading_pho_pt                      := ? leading_pho.pt() != 0 ? leading_pho.pt() : - 99",
    # "leading_pho_eta                     := ? leading_pho.eta() != 0 ? leading_pho.eta() : - 99",
    # "leading_pho_phi                     := ? leading_pho.phi() != 0 ? leading_pho.phi() : - 99",
    # "sub_leading_pho_pt                  := ? sub_leading_pho.pt() != 0 ? sub_leading_pho.pt() : -99 ",
    # "sub_leading_pho_eta                 := ? sub_leading_pho.eta() != 0 ? sub_leading_pho.eta() : -99",
    # "sub_leading_pho_phi                 := ? sub_leading_pho.phi() != 0 ? sub_leading_pho.phi() : -99",
    # # leading photon pt, eta, phi
    # # subleading photon pt, eta, phi 

    # # DiPhoton(s)
    # # leading_dpho = diphoton with highest pt 
    # "n_ps_dipho                          := diphoVector.size()",
    # "leading_dpho_mass                   := ? leading_dpho.mass() != 0 ? leading_dpho.mass() : -99 ", 
    # "leading_dpho_pt                     := ? leading_dpho.pt() != 0 ? leading_dpho.pt() : -99",
    # "leading_dpho_eta                    := ? leading_dpho.eta() != 0 ? leading_dpho.eta() : -99",
    # "leading_dpho_phi                    := ? leading_dpho.phi() != 0 ? leading_dpho.phi() : -99",

    # # Electrons
    # # If there is no leading electron (electronVector_.size() == 0) or no subleading electron (electronVector_.size() <= 1) plot -99 
    # "leading_elec_pt                     := ? leading_elec.pt() != 0 ? leading_elec.pt() : -99 ",  
    # "leading_elec_eta                    := ? leading_elec.eta() != 0 ? leading_elec.eta() : -99 ",
    # "leading_elec_phi                    := ? leading_elec.phi() != 0 ? leading_elec.phi() : -99 ",
    # "subleading_elec_pt                  := ? subleading_elec.pt() != 0 ? subleading_elec.pt() : -99 ",
    # "subleading_elec_eta                 := ? subleading_elec.eta() != 0 ? subleading_elec.eta() : -99 ",
    # "subleading_elec_phi                 := ? subleading_elec.phi() != 0 ? subleading_elec.phi() : -99 ",

    # # Muons 
    # # If there is no leading muon (muonVector_.size() == 0) or no subleading muon (muonVector_.size() <= 1) plot -99 
    # "leading_muon_pt                     := ? leading_muon.pt() != 0 ? leading_muon.pt() : -99 ",
    # "leading_muon_eta                    := ? leading_muon.eta() != 0 ? leading_muon.eta() : -99 ",
    # "leading_muon_phi                    := ? leading_muon.phi() != 0 ? leading_muon.phi() : -99 ",
    # "subleading_muon_pt                  := ? subleading_muon.pt() != 0 ? subleading_muon.pt() : -99 ",
    # "subleading_muon_eta                 := ? subleading_muon.eta() != 0 ? subleading_muon.eta() : -99 ",
    # "subleading_muon_phi                 := ? subleading_muon.phi() != 0 ? subleading_muon.phi() : -99 ",

    # # Jets 
    # "n_jets                              := JetVector.size()", 
    #     # Using GEN information
    #     "mdj_invmass                     := MatchingDiJet.mass()",  
    #     "nmdj_invmass                    := NonMatchingDiJet.mass()", 

    #     # Not using GEN information 
    #     # JetVector is ordered by pT
    #     "jet0_pt                         := ? JetVector.size() >= 1 ? JetVector[0].pt() : -99 ",
    #     "jet0_eta                        := ? JetVector.size() >= 1 ? JetVector[0].eta() : -99 ",
    #     "jet0_phi                        := ? JetVector.size() >= 1 ? JetVector[0].phi() : -99 ",
    #     "jet1_pt                         := ? JetVector.size() >= 2 ? JetVector[1].pt() : -99 ",
    #     "jet1_eta                        := ? JetVector.size() >= 2 ? JetVector[1].eta() : -99 ",
    #     "jet1_phi                        := ? JetVector.size() >= 2 ? JetVector[1].phi() : -99 ",
    #     "jet2_pt                         := ? JetVector.size() >= 3 ? JetVector[2].pt() : -99 ",
    #     "jet2_eta                        := ? JetVector.size() >= 3 ? JetVector[2].eta() : -99 ",
    #     "jet2_phi                        := ? JetVector.size() >= 3 ? JetVector[2].phi() : -99 ",
    #     "jet3_pt                         := ? JetVector.size() >= 4 ? JetVector[3].pt() : -99 ",
    #     "jet3_eta                        := ? JetVector.size() >= 4 ? JetVector[3].eta() : -99 ",
    #     "jet3_phi                        := ? JetVector.size() >= 4 ? JetVector[3].phi() : -99 ",
    #     "jet4_pt                         := ? JetVector.size() >= 5 ? JetVector[4].pt() : -99 ",
    #     "jet4_eta                        := ? JetVector.size() >= 5 ? JetVector[4].eta() : -99 ",
    #     "jet4_phi                        := ? JetVector.size() >= 5 ? JetVector[4].phi() : -99 ",
    #     "jet5_pt                         := ? JetVector.size() >= 6 ? JetVector[5].pt() : -99 ",
    #     "jet5_eta                        := ? JetVector.size() >= 6 ? JetVector[5].eta() : -99 ",
    #     "jet5_phi                        := ? JetVector.size() >= 6 ? JetVector[5].phi() : -99 ",
    #     "jet6_pt                         := ? JetVector.size() >= 7 ? JetVector[6].pt() : -99 ",
    #     "jet6_eta                        := ? JetVector.size() >= 7 ? JetVector[6].eta() : -99 ",
    #     "jet6_phi                        := ? JetVector.size() >= 7 ? JetVector[6].phi() : -99 ",
    #     "jet7_pt                         := ? JetVector.size() >= 8 ? JetVector[7].pt() : -99 ",
    #     "jet7_eta                        := ? JetVector.size() >= 8 ? JetVector[7].eta() : -99 ",
    #     "jet7_phi                        := ? JetVector.size() >= 8 ? JetVector[7].phi() : -99 ",
    #     "jet8_pt                         := ? JetVector.size() >= 9 ? JetVector[8].pt() : -99 ",
    #     "jet8_eta                        := ? JetVector.size() >= 9 ? JetVector[8].eta() : -99 ",
    #     "jet8_phi                        := ? JetVector.size() >= 9 ? JetVector[8].phi() : -99 ",
    #     "jet9_pt                         := ? JetVector.size() >= 10 ? JetVector[9].pt() : -99 ",
    #     "jet9_eta                        := ? JetVector.size() >= 10 ? JetVector[9].eta() : -99 ",
    #     "jet9_phi                        := ? JetVector.size() >= 10 ? JetVector[9].phi() : -99 ",

    #     "lsl_dij_mass                    := ? lsl_dij.mass() !=0 ? lsl_dij.mass() : -99 ", # dijet made from leading and subleading jets 

    # # MET 
    # "MET                                 := MET_fourvec.pt()",


    reco_var = ''
    for key in var_conv:    
        if (var_conv[key][0] == v0_) and (var_conv[key][1] == plab_) and (var_conv[key][2] == G_):
            reco_var = key
            break 

    return reco_var
