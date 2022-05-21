# The purpose of this module is to provide dictionaries and functions for PlotDataFrame.py 

##-- Get nbins, xmin, xmax, unit based on variable name 
def GetVarParams(var_,args__):
    VarDict = {
        ##-- nbins, xmin, xmax
        "invmass_LeadZ_ll" : [100, 0, 100, "GeV"],        
        "invmass_LeadZ_qq" : [100, 0, 100, "GeV"],        
        "invmass_LeadZ_nunu" : [100, 0, 100, "GeV"],        
        "invmass_SubleadZ_ll" : [100, 0, 100, "GeV"],        
        "invmass_SubleadZ_qq" : [100, 0, 100, "GeV"],        
        "invmass_SubleadZ_nunu" : [100, 0, 100, "GeV"],        
        "qq_invmass" : [30,0,100,"GeV"],
        "qq_DeltaR" : [20,0,5,"radians"],
        # "HH_invmass" : [100,0,1000,"GeV"],
        "HH_invmass" : [50,250,1000,"GeV"],
        # "HH_DeltaR" : [20,0,6,"radians"], # Arb 
        # "HH_DeltaR" : [20,0,0.08,"radians"], # 250 GeV 
        "HH_DeltaR" : [30,0,5.5,"radians"], # 850 GeV 
        "status" : [100,0,100,"unitless"],
        "PhoPho_invmass" : [10,115,135,"GeV"],
        "PhoPho_DeltaR" : [20,0,5,"radians"],
        "incVBFqincVBFq_invmass" : [35,0,7000,"GeV"],
        "outVBFqoutVBFq_invmass" : [30,0,3000,"GeV"],
        "incVBFqincVBFq_DeltaR" : [30,0,15,"radians"],
        "outVBFqoutVBFq_DeltaR" : [40,0,10,"radians"],
        "Lead_incVBFq_pt" : [60,0,1200,"GeV"],
        "Sublead_incVBFq_pt" : [30,0,250,"GeV"],
        "Lead_outVBFq_pt" : [60,0,1200,"GeV"],
        "Sublead_outVBFq_pt" : [30,0,250,"GeV"],
        "pdgIds" : [100,-50,50,"unitless"]
    }

    ps = args__.particles.split(',') 
    vs = args__.variables.split(',')
 
    for p in ps:
        for v in vs:
            varName = "%s_%s"%(p,v)
            # if("pdgIds" in varName): VarDict[varName] = []
            if("Lead_q_pt" in varName): VarDict[varName] = [50,0,500,"GeV"]
            elif("Sublead_q_pt" in varName): VarDict[varName] = [25,0,250,"GeV"]
            # if("q_pt" in varName): VarDict[varName] = [50,0,500,"GeV"]
            elif("nu_pt" in varName): VarDict[varName] = [40,0,400,"GeV"]
            elif("Lead_H_pt" in varName): VarDict[varName] = [30,0,600,"GeV"]
            # elif("Sublead_H_pt" in varName): VarDict[varName] = [30,0,500,"GeV"]
            elif("Sublead_H_pt" in varName): VarDict[varName] = [30,0,600,"GeV"]
            elif("nu_pt" in varName): VarDict[varName] = [20,0,400,"GeV"]
            elif("pz" in v or "px" in v or "py" in v): VarDict[varName] = [100,-2000,2000,"GeV"]
            elif("eta" in v or "phi" in v): VarDict[varName] = [50,-5,5,"radians"]
            elif(varName == "X_p"): VarDict[varName] = [50,0,2000,"GeV"]
            elif("Sublead_outVBFq_pt" in varName): VarDict[varName] = [30,0,250,"GeV"]
            # elif("Lead_incVBFq_pt" in varName or "Sublead_incVBFq_pt" in varName): VarDict[varName] = [60,0,1200,"GeV"]
            # elif("Lead_outVBFq_pt" in varName or "Sublead_outVBFq_pt" in varName): VarDict[varName] = [60,0,600,"GeV"]
            elif("Lead_outVBFq_pt" in varName or "Sublead_outVBFq_pt" in varName): VarDict[varName] = [60,0,1200,"GeV"]
            else: VarDict[varName] = [100,-100,100,""]

    return VarDict[var_]