###########################################################################################################################
# Abraham Tishelman-Charny
# 15 June 2020
#
# The purpose of this module is to provide variables and definitions for NtupleAnalysisTools.py 
#
###########################################################################################################################

def GetVars(VarBatch):
    finalStateVars_ = [] 
    if(VarBatch == "basic"):
        return ["CMS_hgg_mass"]
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
    elif(VarBatch == "loose"):
        L3vars = [
            "CMS_hgg_mass",
            ##-- Photon variables
            "Leading_Photon_pt","Subleading_Photon_pt",
            "Leading_Photon_MVA","Subleading_Photon_MVA",  
            ##-- Lepton / Jet variables  
            "N_allElectrons","N_allMuons","N_allJets",
            "N_goodElectrons","N_goodMuons","N_goodJets",
            "allElectrons_0_pt","allMuons_0_pt",
            "allJets_0_pt","allJets_1_pt",
            "MET_pt"            
        ]
        return L3vars 
    elif(VarBatch == "all"):
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

        # for removal of prompt-prompt events from QCD and GJet samples 
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

def GetBins(variable_):
    binDict = {
        "Leading_Photon_MVA": [20,-1,1],
        "Subleading_Photon_MVA": [20,-1,1],
        # "CMS_hgg_mass": [80,100,180],
        # "CMS_hgg_mass": [24,100,180],
        "CMS_hgg_mass": [30,100,180],
        "weight":[1000,-2,2],
        "puweight":[1000,-2,2],
    }    
    otherVars = ["Leading_Photon_MVA","Subleading_Photon_MVA","CMS_hgg_mass","weight","puweight"]
    if variable_ in otherVars:
        return binDict[variable_]
    elif "N_" in variable_:
        return [10,0,10]
    else:
        if ("eta" in variable_) or ("phi" in variable_):
            return [16,-4,4]
        elif ("pt" in variable_):
            return [20,0,200]   
        else:
            return [10,0,100]

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
        "N_" : "unitless"
    }

    for varFrag in variableUnitDict:
        varUnit = variableUnitDict[varFrag]
        if varFrag in variableName: variableUnit = varUnit

    xAxisTitle = "%s [%s]"%(variableName,variableUnit)
    return xAxisTitle             