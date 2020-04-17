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

    ## RECO

    # Electrons
    "leading_elec_pt": ['pt','le',0],
    "leading_elec_eta": ['eta','le',0],
    "subleading_elec_pt": ['pt','sle',0],

    # Muons
    "leading_muon_pt": ['pt','lm',0],
    "subleading_muon_pt": ['pt','slm',0],
    
    # Met

    # Jets
    "mdj_invmass": ['invmass','mjj',0],
    "nmdj_invmass": ['invmass','nmjj',0],

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

    # #---------------------------------------------------------------------------------------------------#

    # ## Booleans

    # # These allow you to plot variables with whichever cut combinations you'd like with plotter 
    # # "Passed_Preselection              := Pass_PS()", # preselection tag 
    # # "Passed_SLW              := SLW_tag()", # semileptonic W tag 
    # "Cut_0                      := Cut_Results[0]", 
    # "Cut_1                      := Cut_Results[1]",
    # "Cut_2                      := Cut_Results[2]",
    # "Cut_3                      := Cut_Results[3]",
    # "Cut_4                      := Cut_Results[4]",
    # "Cut_5                      := Cut_Results[5]",
    # "Cut_6                      := Cut_Results[6]",
    # "Cut_7                      := Cut_Results[7]",

    # #---------------------------------------------------------------------------------------------------#

    # ## GEN Variables 

    # # Electrons 
    # # Set to -99 if there's no value 
    # "gen_leading_elec_pt              := ? gen_leading_elec.pt() != 0 ? gen_leading_elec.pt() : -99 ",
    # "gen_leading_elec_eta              :=? gen_leading_elec.eta() != 0 ? gen_leading_elec.eta() : -99 ",
    # "gen_leading_elec_phi              := ? gen_leading_elec.phi() != 0 ? gen_leading_elec.phi() : -99 ",
    # "gen_subleading_elec_pt              := ? gen_subleading_elec.pt() != 0 ? gen_subleading_elec.pt() : -99 ",
    # "gen_subleading_elec_eta              := ? gen_subleading_elec.eta() != 0 ? gen_subleading_elec.eta() : -99 ",
    # "gen_subleading_elec_phi              := ? gen_subleading_elec.phi() != 0 ? gen_subleading_elec.phi() : -99 ",

    # # Muons 
    # # Set to -99 if there's no value 
    # "gen_leading_muon_pt                  := ? gen_leading_muon.pt() != 0 ? gen_leading_muon.pt() : -99 ",
    # "gen_leading_muon_eta                 := ? gen_leading_muon.eta() != 0 ? gen_leading_muon.eta() : -99 ",
    # "gen_leading_muon_phi                 := ? gen_leading_muon.phi() != 0 ? gen_leading_muon.phi() : -99 ",
    # "gen_subleading_muon_pt               := ? gen_subleading_muon.pt() != 0 ? gen_subleading_muon.pt() : -99 ",
    # "gen_subleading_muon_eta              := ? gen_subleading_muon.eta() != 0 ? gen_subleading_muon.eta() : -99 ",
    # "gen_subleading_muon_phi              := ? gen_subleading_muon.phi() != 0 ? gen_subleading_muon.phi() : -99 ",

    # # Quarks 
    # "mdq_invmass                    := MatchingDiQuark.mass()",
    # "nmdq_invmass                   := NonMatchingDiQuark.mass()",

    # #---------------------------------------------------------------------------------------------------#

    # ## RECO Variables

    # # Photons
    # "n_photons                    := phoVector.size()",

    # # DiPhoton(s)
    # # leading_dpho = diphoton with highest pt 
    # "n_ps_dipho                     := diphoVector.size()",
    # "leading_dpho_mass              := ? leading_dpho.mass() != 0 ? leading_dpho.mass() : -999 ", 
    # "leading_dpho_pt                := leading_dpho.pt()",
    # "leading_dpho_eta               := leading_dpho.eta()",
    # "leading_dpho_phi               := leading_dpho.phi()",

    # # Electrons
    # # If there is no leading electron (electronVector_.size() == 0) or no subleading electron (electronVector_.size() <= 1) plot -99 
    # "leading_elec_pt              := ? leading_elec.pt() != 0 ? leading_elec.pt() : -99 ",  
    # "leading_elec_eta              := ? leading_elec.eta() != 0 ? leading_elec.eta() : -99 ",
    # "leading_elec_phi              := ? leading_elec.phi() != 0 ? leading_elec.phi() : -99 ",
    # "subleading_elec_pt              := ? subleading_elec.pt() != 0 ? subleading_elec.pt() : -99 ",
    # "subleading_elec_eta              := ? subleading_elec.eta() != 0 ? subleading_elec.eta() : -99 ",
    # "subleading_elec_phi              := ? subleading_elec.phi() != 0 ? subleading_elec.phi() : -99 ",

    # # Muons 
    # # If there is no leading muon (muonVector_.size() == 0) or no subleading muon (muonVector_.size() <= 1) plot -99 
    # "leading_muon_pt              := ? leading_muon.pt() != 0 ? leading_muon.pt() : -99 ",
    # "leading_muon_eta              := ? leading_muon.eta() != 0 ? leading_muon.eta() : -99 ",
    # "leading_muon_phi              := ? leading_muon.phi() != 0 ? leading_muon.phi() : -99 ",
    # "subleading_muon_pt              := ? subleading_muon.pt() != 0 ? subleading_muon.pt() : -99 ",
    # "subleading_muon_eta              := ? subleading_muon.eta() != 0 ? subleading_muon.eta() : -99 ",
    # "subleading_muon_phi              := ? subleading_muon.phi() != 0 ? subleading_muon.phi() : -99 ",

    # # Jets 
    # "n_jets                        := JetVector.size()", 
    #     # Using GEN information
    #     "mdj_invmass                    := MatchingDiJet.mass()",  
    #     "nmdj_invmass                   := NonMatchingDiJet.mass()", 

    #     # Not using GEN information 
    #     # JetVector is ordered by pT
    #     "jet0_pt                        := ? JetVector.size() >= 1 ? JetVector[0].pt() : -99 ",
    #     "jet0_eta                        := ? JetVector.size() >= 1 ? JetVector[0].eta() : -99 ",
    #     "jet0_phi                        := ? JetVector.size() >= 1 ? JetVector[0].phi() : -99 ",
    #     "jet1_pt                        := ? JetVector.size() >= 2 ? JetVector[1].pt() : -99 ",
    #     "jet2_pt                        := ? JetVector.size() >= 3 ? JetVector[2].pt() : -99 ",
    #     "jet3_pt                        := ? JetVector.size() >= 4 ? JetVector[3].pt() : -99 ",
    #     "jet4_pt                        := ? JetVector.size() >= 5 ? JetVector[4].pt() : -99 ",
    #     "jet5_pt                        := ? JetVector.size() >= 6  ? JetVector[5].pt() : -99 ",
    #     "jet6_pt                        := ? JetVector.size() >= 7  ? JetVector[6].pt() : -99 ",
    #     "jet7_pt                        := ? JetVector.size() >= 8  ? JetVector[7].pt() : -99 ",
    #     "jet8_pt                        := ? JetVector.size() >= 9  ? JetVector[8].pt() : -99 ",
    #     "jet9_pt                        := ? JetVector.size() >= 10  ? JetVector[9].pt() : -99 ",

    #     "lsl_dij_mass                        := ? lsl_dij.mass() !=0 ? lsl_dij.mass() : -99 ", # dijet made from leading and subleading jets 

    # # MET 
    # "MET                          := MET_fourvec.pt()",


    reco_var = ''
    for key in var_conv:    
        if (var_conv[key][0] == v0_) and (var_conv[key][1] == plab_) and (var_conv[key][2] == G_):
            reco_var = key
            break 

    return reco_var