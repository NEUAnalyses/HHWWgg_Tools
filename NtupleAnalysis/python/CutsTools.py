###########################################################################################################################
# Abraham Tishelman-Charny
# 13 May 2020
#
# The purpose of this module is to provide cut related variables and definitions for NtupleAnalysis.py 
#
###########################################################################################################################

def GetCuts(CutsType):
    cuts, cutNames = [], []
    if(CutsType == 1):
        cuts = ["1"]
        cutNames = ["PreSelections"]
    elif(CutsType == 2):
        cuts = ["(N_allElectrons + N_allMuons == 1)*(N_allJets >= 2)*(Leading_Photon_MVA>-0.5)*(Subleading_Photon_MVA>-0.5)"]
        cutNames = ["Loose"]
    elif(CutsType == 3):
        cuts = ["1", "passPhotonSels == 1", "passbVeto == 1", "ExOneLep == 1", "goodJets == 1"] # preselections, photon sels, bVeto, exactly 1 lepton, at least 2 good jets
        cutNames = ["PreSelections","PhotonSelections","bVeto","OneLep","TwoGoodJets"]
    return [cuts,cutNames]