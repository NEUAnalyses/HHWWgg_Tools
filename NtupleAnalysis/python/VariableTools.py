###########################################################################################################################
# Abraham Tishelman-Charny
# 15 June 2020
#
# The purpose of this module is to define variable related objects
###########################################################################################################################

import numpy as np 

##-- Get variables to plot based on user input variable batch name 
def GetVars(VarBatch):

    ##-- Definitions of some special variables, created from existing branch values 
    mjj = "sqrt(2*goodJets_0_pt*goodJets_1_pt*(cosh(goodJets_0_eta-goodJets_1_eta)-cos(goodJets_0_phi-goodJets_1_phi)))"
    e_mT = "sqrt(2*goodElectrons_0_pt*MET_pt*(1-cos(goodElectrons_0_phi-MET_phi)))"
    mu_mT = "sqrt(2*goodMuons_0_pt*MET_pt*(1-cos(goodMuons_0_phi-MET_phi)))"
    dr_gg = "sqrt( fabs(Leading_Photon_eta - Subleading_Photon_eta)**2 + fabs( Leading_Photon_phi - Subleading_Photon_phi )**2  )"
    dr_jj = "sqrt( fabs(allJets_0_eta - allJets_1_eta)**2 + fabs( allJets_0_phi - allJets_1_phi )**2  )"
    pT_gg = "Leading_Photon_pt + Subleading_Photon_pt"

    ##-- Variable batch definitions

    # Just diphoton mass 
    # make dictionary 
    if(VarBatch == "mass"):
        return ["CMS_hgg_mass"]
    elif(VarBatch == "DNN"):
        return ["evalDNN"]        

    elif(VarBatch == "Ngood"):
        return ["N_goodElectrons","N_goodMuons","N_goodLeptons","N_goodJets"]

    elif(VarBatch == "LeadPhopt"):
        return ["Leading_Photon_pt"]

    elif(VarBatch == "diphopt"):
        return [pT_gg]

    # Some potentially useful MVA variables  
    elif(VarBatch == "MVA"):
        L2vars =  [
            "CMS_hgg_mass","Leading_Photon_pt","Subleading_Photon_pt",
            "Leading_Photon_MVA","Subleading_Photon_MVA",   
            "N_allElectrons","N_allMuons","N_allJets",
            "N_goodElectrons","N_goodMuons","N_goodJets",
            "goodElectrons_0_pt","goodMuons_0_pt",
            "goodJets_0_pt","goodJets_1_pt",
            "MET_pt"
            ] 
        return L2vars

    # More possible MVA variables 
    elif(VarBatch == "MVA2"):
        L2vars =  [
            "Leading_Photon_eta", "Leading_Photon_phi",
            "Subleading_Photon_eta", "Subleading_Photon_phi",
            "goodElectrons_0_eta", "goodElectrons_0_phi", "goodElectrons_0_E",
            "goodMuons_0_eta", "goodMuons_0_phi", "goodMuons_0_E",
            "goodJets_0_eta", "goodJets_0_phi", "goodJets_0_E",
            "goodJets_1_eta", "goodJets_1_phi", "goodJets_1_E",
            "MET_phi"
            ] 
        return L2vars 

    # MET variables 
    elif(VarBatch == "MET"):
        METvars = [
            "MET_pt","MET_phi"
        ]
        return METvars

    # Photon variables 
    elif(VarBatch == "Photon"):
        PhotonVars = [
            "Leading_Photon_pt","Leading_Photon_eta","Leading_Photon_E","Leading_Photon_MVA",
            "Subleading_Photon_pt","Subleading_Photon_eta","Subleading_Photon_E","Subleading_Photon_MVA"
        ]
        return PhotonVars 

    # Photon variables 
    elif(VarBatch == "LeadingPhoton"):
        PhotonVars = [
            "Leading_Photon_pt","Leading_Photon_eta","Leading_Photon_E","Leading_Photon_MVA"
        ]
        return PhotonVars         

    elif(VarBatch =="bScores"):
        bScores = []
        scores = ['bDiscriminator_mini_pfDeepFlavourJetTags_probb','bDiscriminator_mini_pfDeepFlavourJetTags_probbb','bDiscriminator_mini_pfDeepFlavourJetTags_problepb']
        # scoresum = "(goodJets_0_%s + goodJets_0_%s + goodJets_0_%s)"%(scores[0],scores[1],scores[2])
        # bScores.append(scoresum)
        for score in scores:
            bScores.append("goodJets_0_%s"%(score))
        return bScores 

    # Variables that should be combined with Loose cuts. Plots kinematics of leading lepton (which changes event by event)
    elif(VarBatch == "Loose"):
        LooseVars = []        
        LooseVarsNames = []
        kinVars = ["pt","eta","E"]
        maxObjects = 5
        lepton_pt_cut = 10 
        for kinVar in kinVars:
            LooseGoodLepton_var = ""
            for i in range(0,maxObjects):
                elec, muon = "allElectrons_%s"%(i), "allMuons_%s"%(i)
                elecCut = "( (%s_pt >= %s) && (%s_passLooseId==1 && (fabs(%s_eta)<1.4442 || ((fabs(%s_eta)>1.566 && fabs(%s_eta)<2.5) ) ) ) )"%(elec,lepton_pt_cut,elec,elec,elec,elec)
                muonCut = "((%s_pt >= %s && %s_isTightMuon==1 && fabs(%s_eta)<=2.4))"%(muon,lepton_pt_cut,muon,muon)
                varMatrixElement = "((%s_%s*%s) + (%s_%s*%s))"%(elec,kinVar,elecCut,muon,kinVar,muonCut)
                LooseGoodLepton_var += varMatrixElement
                if(i != maxObjects-1): LooseGoodLepton_var += " + "
            LooseVars.append(LooseGoodLepton_var)
            LooseVarsNames.append("Loose-Good_Lepton_%s"%(kinVar))
        return LooseVars,LooseVarsNames 

    # All known tree variables. This is a LOT 
    elif(VarBatch == "all"):
        finalStateVars_ = []
        ##-- Add lepton, jet variables 
        # p4_variables = ["E","pt","px","py","pz","eta","phi"]
        p4_variables = ["E","pt","eta","phi"]
        checkN = 3
        objectVectors = [] 
        objs = ["Electrons","Muons","Jets"]
        vecTypes = ["all","good"]
        for t in vecTypes:
            for o in objs:
                objVec = "%s%s"%(t,o)
                objectVectors.append(objVec)    
        for objV in objectVectors:
            vtitle = "N_%s"%(objV) 
            entry = "%s"%(vtitle)
            finalStateVars_.append(entry)
            for v in p4_variables:
                for i in range(checkN):
                    vtitle = "%s_%s_%s"%(objV,i,v)
                    entry = "%s"%(vtitle)
                    finalStateVars_.append(entry)
            if("Electrons" in objV):
                eVars = ["passLooseId","passMediumId","passTightId","passMVALooseId","passMVAMediumId","passMVATightId"]
                for eV in eVars:
                    for i in range(checkN):
                        vtitle = "%s_%s_%s"%(objV,i,eV)
                        entry = "%s"%(vtitle)
                        finalStateVars_.append(entry)
            if("Muons" in objV):
                mVars = ["pfIsolationR04().sumChargedHadronPt","pfIsolationR04().sumNeutralHadronEt","pfIsolationR04().sumPhotonEt",
                            "pfIsolationR04().sumPUPt"]
                mVarTitles = ["sumChargedHadronPt","sumNeutralHadronEt","sumPhotonEt","sumPUPt"]
                for imV,mV in enumerate(mVars):
                    mVarTitle = mVarTitles[imV]
                    for i in range(checkN):
                        vtitle = "%s_%s_%s"%(objV,i,mVarTitle)
                        entry = "%s"%(vtitle)
                        finalStateVars_.append(entry)  

            if("Jets" in objV):
                bscores = ["bDiscriminator('mini_pfDeepFlavourJetTags:probb')","bDiscriminator('pfDeepCSVJetTags:probb')",
                            "bDiscriminator('mini_pfDeepFlavourJetTags:probbb')","bDiscriminator('pfDeepCSVJetTags:probbb')"]
                
                btitles = ["bDiscriminator_mini_pfDeepFlavourJetTags_probb","bDiscriminator_pfDeepCSVJetTags_probb",
                            "bDiscriminator_mini_pfDeepFlavourJetTags_probbb","bDiscriminator_pfDeepCSVJetTags_probbb"
                            ]
                for ib,bscore in enumerate(bscores):
                    btitle = btitles[ib]
                    for i in range(checkN):
                        vtitle = "%s_%s_%s"%(objV,i,btitle)
                        entry = "%s"%(vtitle)
                        finalStateVars_.append(entry)                                                                      

        # finalStateVars_.append("Leading_Photon_genMatchType")
        # finalStateVars_.append("Subleading_Photon_genMatchType")

        ##-- Add photon variables 
        objects = ["Leading_Photon","Subleading_Photon","MET"]
        finalStateVars_.append("Leading_Photon_MVA")
        finalStateVars_.append("Subleading_Photon_MVA")
        for obj in objects:
            for var in p4_variables:
                vtitle = "%s_%s"%(obj,var)
                finalStateVars_.append(vtitle)    
    
        return finalStateVars_ 

    # Just dR between two leading jets 
    elif(VarBatch == "special"):
        return [dr_jj]

##-- Get bins for a variable 
def GetBins(variable_,DNNbinWidth_):
# def GetBins(variable_,DNNbinWidth_ = 0.1):

    # evalDNNmin, evalDNNmax = 0, 1.00001
    # evalDNNmin, evalDNNmax = 0.9, 1.00001
    # evalDNNmin, evalDNNmax = 0, 1.00001
    evalDNNmin, evalDNNmax = 0, 1
    nDNNbins = int(float((evalDNNmax - evalDNNmin)) / float(DNNbinWidth_))

    if(DNNbinWidth_ != 0.1):
        print"nDNNbins: ",nDNNbins
    # Specify bins for specific variables 
    binDict = {
        "Leading_Photon_MVA": [20,-1,1],
        "Subleading_Photon_MVA": [20,-1,1],
        "CMS_hgg_mass": [30,100,180],
        "weight":[1000,-10,10],
        "puweight":[1000,-2,2],
        "mjj" : [100,0,300],
        "e_mT" : [100,0,300],
        "mu_mT" : [100,0,300],
        "dr_gg" : [60,0,3],
        "dr_jj" : [60,0,3],
        "pT_gg" : [40,0,400],
        # "evalDNN" : [20,0,1.00001] # To include value == 1 
        # "evalDNN" : [10,0,1.00001] # To include value == 1 
        # "evalDNN" : [25,0,1.00001] # To include value == 1 
        # "evalDNN" : [100,0,1.00001] # To include value == 1 
        "evalDNN" : [nDNNbins,evalDNNmin,evalDNNmax] # To include value == 1 
        # "evalDNN" : [10,0,1] # To include value == 1 
    }    
    specialVars = ["Leading_Photon_MVA","Subleading_Photon_MVA","CMS_hgg_mass","weight","puweight","mjj","e_mT","mu_mT","dr_gg","dr_jj","pT_gg","evalDNN"]

    scores = ['bDiscriminator_mini_pfDeepFlavourJetTags_probb','bDiscriminator_mini_pfDeepFlavourJetTags_probbb','bDiscriminator_mini_pfDeepFlavourJetTags_problepb']
    scoresum = "(goodJets_0_%s + goodJets_0_%s + goodJets_0_%s)"%(scores[0],scores[1],scores[2])
    if variable_ == scoresum: return [50,0,1]
    if variable_ in specialVars:
        return binDict[variable_]

    # If variable is a number of objects
    elif "N_" in variable_:
        return [10,0,10]

    # Specified binning if variable has phi, eta or pt in name 
    else:
        if("phi" in variable_): return [17,-3.14,3.5325]
        # elif("eta" in variable_): return [16,-4,4]
        elif("eta" in variable_): return [10,-2.5,2.5]
        elif ("pt" in variable_): return [20,0,200]   
        elif("bDiscriminator" in variable_): return [20,0,1]
        else: return [30,0,300] # if variable name meets none of the above conditions, default to this binning 

##-- Get x axis title for ratio plot depending on the variable 
def GetXaxisTitle(variable_):
    xAxisTitle = "" 
    variableName = variable_ 
    variableUnit = ""

    variableUnitDict = {
        "CMS_hgg_mass": "GeV",
        "E" : "GeV",
        "pt" : "GeV",
        "eta" : "rad",
        "phi" : "rad",
        "MVA": "unitless",
        "weight":"unitless",
        "N_" : "unitless",
        "mjj": "GeV",
        "e_mT" : "GeV",
        "mu_mT" : "GeV",
        "dr_gg" : "rad",
        "dr_jj" : "rad",
        "pT_gg" : "GeV",
        "DeepJetScore" : "unitless",
        "evalDNN" : "unitless"
    }

    for varFrag in variableUnitDict:
        varUnit = variableUnitDict[varFrag]
        if varFrag in variableName: variableUnit = varUnit

    xAxisTitle = "%s [%s]"%(variableName,variableUnit)
    return xAxisTitle           

##-- Get the name of variable. Useful for variables that have long strings in draw statement. This returns a shortened value to be used for plot title and output file name 
def GetVarTitle(varName):
    varTitle = ""
    scores = ['bDiscriminator_mini_pfDeepFlavourJetTags_probb','bDiscriminator_mini_pfDeepFlavourJetTags_probbb','bDiscriminator_mini_pfDeepFlavourJetTags_problepb']
    scoresum = "(goodJets_0_%s + goodJets_0_%s + goodJets_0_%s)"%(scores[0],scores[1],scores[2])    
    mjj = "sqrt(2*goodJets_0_pt*goodJets_1_pt*(cosh(goodJets_0_eta-goodJets_1_eta)-cos(goodJets_0_phi-goodJets_1_phi)))"
    e_mT = "sqrt(2*goodElectrons_0_pt*MET_pt*(1-cos(goodElectrons_0_phi-MET_phi)))"
    mu_mT = "sqrt(2*goodMuons_0_pt*MET_pt*(1-cos(goodMuons_0_phi-MET_phi)))"    
    dr_gg = "sqrt( fabs(Leading_Photon_eta - Subleading_Photon_eta)**2 + fabs( Leading_Photon_phi - Subleading_Photon_phi )**2  )"
    dr_jj = "sqrt( fabs(allJets_0_eta - allJets_1_eta)**2 + fabs( allJets_0_phi - allJets_1_phi )**2  )"
    pT_gg = "Leading_Photon_pt + Subleading_Photon_pt"
    if(varName == mjj): varTitle = "mjj"
    elif(varName == e_mT): varTitle = "e_mT"
    elif(varName == mu_mT): varTitle = "mu_mT"
    elif(varName == dr_gg): varTitle = "dr_gg"
    elif(varName == dr_jj): varTitle = "dr_jj"
    elif(varName == pT_gg): varTitle = "pT_gg"
    elif(varName == scoresum): varTitle = "DeepJetScore"
    else: varTitle = varName 
    return varTitle 

##-- Compute chi squared for a data / mc plot 
def GetChiSquared(DataHist_,stackSum_):
    # the two histos should have the same binning 
    Nbins = DataHist_.GetNbinsX()
    assert(Nbins == stackSum_.GetNbinsX())
    chi2_total = 0
    for bin_i in range(1,Nbins): # skip underflow bin 
        data_y, MC_sum_y = DataHist_.GetBinContent(bin_i), stackSum_.GetBinContent(bin_i)
        chi2_num = pow(abs(float(data_y)-float(MC_sum_y)),2)
        # avoid a denominator of 0 
        if(data_y == 0.0 and MC_sum_y == 0.0): continue 
        elif(data_y == 0.0 and MC_sum_y != 0.0): chi2_den = MC_sum_y 
        else: chi2_den = data_y  
        # print"data_y:",data_y
        # print"MC_sum_y:",MC_sum_y
        chi2 = chi2_num / chi2_den 
        chi2_total += chi2 
    chi2_total /= Nbins 
    return chi2_total 
