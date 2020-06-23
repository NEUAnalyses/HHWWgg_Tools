###########################################################################################################################
# Abraham Tishelman-Charny
# 13 May 2020
#
# The purpose of this module is to provide cut related variables and definitions for NtupleAnalysis.py 
#
###########################################################################################################################

def GetCuts(CutsType):
    cuts, cutNames = [], []
    if(CutsType == "PS"):
        cuts = ["1"]
        cutNames = ["PreSelections"]
    elif(CutsType == "Loose"):
        ##-- Electrons, Muons, Jets: Keep all analysis selections except dR, pT

        ## Selections that need to be kept:
        # Electrons:
        # passLooseId == 1
        # 1.4442,1.566,2.5
        # Muons: 
        #
        # Jets:
        # abs(eta) <= 2.4
        
        # electronCuts = "(1)"
        # muonCuts = "(1)"
        # jetCuts = "(1)"

        electronCuts = "((allElectrons_0_passLooseId==1)*(   fabs(allElectrons_0_eta)<1.4442 || ((fabs(allElectrons_0_eta)>1.566 && fabs(allElectrons_0_eta)<2.5))   ) )"
        # electronCuts = "(   fabs(allElectrons_0_eta)<1.4442 || ((fabs(allElectrons_0_eta)>1.566 && fabs(allElectrons_0_eta)<2.5))   )  "
        # electronCuts = "((allElectrons_0_passLooseId==1))"
        # electronCuts = "((allElectrons_0_passLooseId==1))"
        muonCuts = "((fabs(allMuons_0_eta) <= 2.4))"
        orLepCuts = "(%s || %s)"%(electronCuts,muonCuts)    
        
        jetCuts = "((fabs(allJets_0_eta) <= 2.4)*(fabs(allJets_1_eta) <= 2.4))"
        # cuts = ["(N_allElectrons == 1 || N_allMuons == 1)*(N_allJets >= 2)*(Leading_Photon_MVA>-0.1)*(Subleading_Photon_MVA>-0.1)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["(N_allElectrons >= 1 || N_allMuons >= 1)*(N_allJets >= 2)*(Leading_Photon_MVA>-0.5)*(Subleading_Photon_MVA>-0.5)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["(N_allElectrons >= 1 || N_allMuons >= 1)*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["( (N_allElectrons >= 1 && N_allElectrons <= 2) || (N_allMuons >= 1 && N_allMuons <= 2) )*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["( N_allElectrons >= 1 || N_allMuons >= 1 )*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["( N_allElectrons == 1 )*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,electronCuts)]
        # cuts = ["( N_allElectrons == 1 )*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,electronCuts)]
        # cuts = ["( N_allElectrons == 1 )*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,electronCuts)]
        # cuts = ["( N_allElectrons == 1 || N_allMuons == 1 )*(N_allJets >= 2)*(passPhotonSels==1)*%s"%(jetCuts)]
        cuts = ["((N_allElectrons == 1 && N_allMuons == 0 ) || (N_allElectrons == 0 && N_allMuons == 1 ))*(N_allJets >= 2)*(passPhotonSels==1)*%s*%s"%(jetCuts,orLepCuts)]
        # cuts = ["((N_allElectrons == 1 && N_allMuons == 0 ) || (N_allElectrons == 0 && N_allMuons == 1 ))*(N_allJets >= 2)*(passPhotonSels==1)*%s"%(jetCuts)]
        cutNames = ["Loose"]
    elif(CutsType == "Medium"):
        cuts = ["(N_allElectrons + N_allMuons == 1)*(N_goodJets >= 2)*(passPhotonSels==1)"]
        cutNames = ["Medium"]
    elif(CutsType == "all"):
        cuts = ["1", "passPhotonSels == 1", "passbVeto == 1", "ExOneLep == 1", "goodJets == 1"] # preselections, photon sels, bVeto, exactly 1 lepton, at least 2 good jets
        cutNames = ["PreSelections","PhotonSelections","bVeto","OneLep","TwoGoodJets"]
    elif(CutsType == "final"):
        cuts = ["(passPhotonSels==1)*(passbVeto==1)*(ExOneLep==1)*(goodJets==1)"]
        cutNames = ["final"]
    return [cuts,cutNames]