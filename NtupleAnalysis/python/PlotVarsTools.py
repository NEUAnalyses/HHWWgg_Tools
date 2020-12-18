####################################################################################
# Abraham Tishelman-Charny                                                         #
# 3 November 2020                                                                  #
#                                                                                  #
# The purpose of this python module is to provide functions for PlotVars.py        #
####################################################################################

import os 
from matplotlib import pyplot as plt 
from root_numpy import tree2array 
import numpy as np

##-- Create Output directory if it doesn't already exist 
def CreateDirec(OutputLoc):
    prevDirec = "%s/../"%(OutputLoc) # Assumes previous directory exists for .php file 
    if(not os.path.exists(OutputLoc)):
        print"[python/PlotVarsTools]: Creating Directory:",OutputLoc
        os.system('mkdir %s'%(OutputLoc))
        indexLoc = "%s/index.php"%(prevDirec)
        print"[python/PlotVarsTools]: Copying %s to %s"%(indexLoc,OutputLoc)
        os.system('cp %s %s'%(indexLoc,OutputLoc))  

##-- Should have preset lists
def GetVarsList(VarsBatch):

    ##-- fgg EFT Reweights 
    benchmarkReweightLabels = [str(i) for i in range(0,12)]
    benchmarkReweightLabels.append("SM")
    benchmarkReweightLabels.append("box")
    benchmarkReweightLabels.append("2017fake")
    weightNames = [] 
    for reweightLabel in benchmarkReweightLabels:
        weightName = "benchmark_reweight_%s"%(reweightLabel)
        weightNames.append(weightName)

    ##-- Mhh vars 
    reweightSets = ['benchmark_reweight_2017fake', 'benchmark_reweight_SM', 'weight_lo_SM', 'weight_nlo_SM']
    mhhVars = ['genMhh']
    for reWeightSet in reweightSets:
        combinedVar = "genMhh*%s"%(reWeightSet)
        mhhVars.append(combinedVar)

    VSEVAweights = ['weight_lo_SM', 'weight_nlo_SM']

    ##-- Scale Factors 
    SF_xmin, SF_xmax = 0.8, 1.2 
    SFs = ["LooseMvaSF", "PreselSF", "TriggerWeight", "prefireWeight", "electronVetoSF", 
           "ElectronIDWeight", "ElectronRecoWeight", "MuonTightIDWeight", "MuonTightRelISOWeight", 
           "JetBTagCutWeight", "JetBTagReshapeWeight"]
    SFnames = ["%sCentral"%(SF) for SF in SFs]
    SFnames.append("weight")
    SFnames.append("centralObjectWeight")
    SFnames.append("puweight")

    centralProduct = ""
    for i,SFname in enumerate(SFnames):
        if(SFname != "weight" and SFname != "centralObjectWeight"): 
            centralProduct += SFname 
            if(i != len(SFnames) - 1): centralProduct += "*"
    print"centralProduct:",centralProduct   
    SFnames.append(centralProduct)

    VarsListDict = {
        "fggWeights": [weightNames,0,2], # variable list, xmin, max
        "VSEVAweights" : [VSEVAweights, 0, 2],
        "mhh" : [mhhVars,0,1000],
        # "ScaleFactors" : [[centralProduct],SF_xmin,SF_xmax]
        "ScaleFactors" : [SFnames,SF_xmin,SF_xmax]
    }

    if VarsBatch in VarsListDict: return VarsListDict[VarsBatch]
    else: return VarsBatch

def GetVarTitle(VarName_):
    SFs = ["LooseMvaSF", "PreselSF", "TriggerWeight", "prefireWeight", "electronVetoSF", 
           "ElectronIDWeight", "ElectronRecoWeight", "MuonTightIDWeight", "MuonTightRelISOWeight", 
           "JetBTagCutWeight", "JetBTagReshapeWeight"]    
    SFnames = ["%sCentral"%(SF) for SF in SFs]
    SFnames.append("weight")
    SFnames.append("centralObjectWeight")
    SFnames.append("puweight")    
    centralProduct = ""
    for i,SFname in enumerate(SFnames):
        if(SFname != "weight" and SFname != "centralObjectWeight"): 
            centralProduct += SFname 
            if(i != len(SFnames) - 1): centralProduct += "*"

    VarTitleDict = {
        centralProduct : "SF-Product"
    }
    return VarTitleDict[VarName_]

def PlotVar(VarName,tree,OutputLoc,xmin,xmax):
    nbins = 100
    bins = np.linspace(xmin,xmax,nbins+1)
    fig, ax = plt.subplots()
    print"Plotting variable:",VarName
    # VarTitle = GetVarTitle(VarName)

    numProducts = len(VarName.split('*'))

    ##-- If variable is a product of branches
    if(numProducts == 2):
        var1, var2 = VarName.split('*')[0], VarName.split('*')[1]
        exec("%s = tree2array(tree, branches='%s')"%(var1,var1))
        exec("%s = tree2array(tree, branches='%s')"%(var2,var2))
        VarArray = np.multiply(eval(var1), eval(var2))
    elif(numProducts > 2):
        VarTitle = GetVarTitle(VarName)
        for var_i in range(numProducts):
            varName = VarName.split('*')[var_i]
            exec("var%s = VarName.split('*')[%s]"%(var_i,var_i))
            exec("%s = tree2array(tree, branches='%s')"%(varName,varName))
            if(var_i == 0): VarArray = eval(varName)
            else: VarArray = np.multiply(VarArray,eval(varName))
            
    else: 
        VarTitle = VarName
        exec("VarArray = tree2array(tree, branches='%s')"%(VarName))

    mean, std = VarArray.mean(), VarArray.std()

    print("mean:",mean)
    plt.hist(VarArray,
            bins = bins,
            label = VarTitle,
            )    

    textstr = r'$\mu=%.5f$' % (mean, )
    props = dict(boxstyle='round', facecolor='aqua', alpha=0.2)
    # plt.text(0.7, 0.85, textstr, transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)
    plt.text(0.2, 0.85, textstr, transform=ax.transAxes, fontsize=14,verticalalignment='top', bbox=props)
    plt.title(VarTitle)
    plt.xlabel("Value")
    plt.ylabel("Entries (A.U.)")
    plt.legend()
    plt.savefig('%s/%s.png'%(OutputLoc,VarTitle))
    plt.savefig('%s/%s.pdf'%(OutputLoc,VarTitle))
    plt.close()

def PlotVarsTogether(Vars,tree,OutputLoc,VarsBatch,xmin,xmax):
    nbins = 100
    bins = np.linspace(xmin,xmax,nbins+1)
    for VarName in Vars:
        ##-- If variable is a product of branches
        if(len(VarName.split('*')) == 2):
            var1, var2 = VarName.split('*')[0], VarName.split('*')[1]
            exec("%s = tree2array(tree, branches='%s')"%(var1,var1))
            exec("%s = tree2array(tree, branches='%s')"%(var2,var2))
            VarArray = np.multiply(eval(var1), eval(var2))
        else: 
            exec("VarArray = tree2array(tree, branches='%s')"%(VarName))

        mean, std = VarArray.mean(), VarArray.std()

        plt.hist(VarArray,
                bins = bins,
                label = VarName,
                )    

    plt.title(VarsBatch)
    plt.xlabel("Value")
    plt.ylabel("Entries (A.U.)")
    plt.legend()
    plotOutNamepng = '%s/AllVars_%s.png'%(OutputLoc,VarsBatch)
    plotOutNamepdf = '%s/AllVars_%s.pdf'%(OutputLoc,VarsBatch)
    print"Saving plot: %s"%(plotOutNamepng)
    print"Saving plot: %s"%(plotOutNamepdf)
    plt.savefig(plotOutNamepng)
    plt.savefig(plotOutNamepdf)    

def PlotSFVariations(SFnames,tree,OutputLoc,xmin,xmax):
    for SFname in SFnames:
        if "Central" in SFname: 
            name = SFname
    print"Plotting:",SFnames
    nbins = 100
    bins = np.linspace(xmin,xmax,nbins+1)
    for SFname in SFnames:
        exec("VarArray = tree2array(tree, branches='%s')"%(SFname))
        mean, std = VarArray.mean(), VarArray.std()
        plt.hist(VarArray,
                bins = bins,
                label = SFname,
                histtype='step'
                ##--turn fill color off 
                )    
    plt.title(name)
    plt.xlabel("Value")
    plt.ylabel("Entries (A.U.)")
    plt.legend()
    plotOutNamepng = '%s/%s_CentralUpDown.png'%(OutputLoc,name)
    plotOutNamepdf = '%s/%s_CentralUpDown.pdf'%(OutputLoc,name)
    print"Saving plot: %s"%(plotOutNamepng)
    print"Saving plot: %s"%(plotOutNamepdf)
    plt.savefig(plotOutNamepng)
    plt.savefig(plotOutNamepdf)   
    plt.close()  

def PlotSFDifferences(SFnames,tree,OutputLoc,xmin,xmax):
    # for SFname in SFnames:
        # if "Central" in SFname: 
            # name = SFname
    print"Plotting Differences Between:",SFnames
    
    Var_central = "" 
    Var_down = ""
    Var_up = ""

    for name in SFnames:
        if "Central" in name: Var_central = name[:]
        if "Up01sigma" in name: Var_up = name[:]
        if "Down01sigma" in name: Var_down = name[:]

    print"Var_central:",Var_central
    print"Var_up:",Var_up
    print"Var_down:",Var_down

    nbins = 100
    bins = np.linspace(xmin,xmax,nbins+1)
    VarArrayCentral = tree2array(tree, branches=Var_central)
    VarArrayUp = tree2array(tree, branches=Var_up)
    VarArrayDown = tree2array(tree, branches=Var_down)

    VarArrayDmC = np.subtract(VarArrayDown,VarArrayCentral)
    VarArrayUmC = np.subtract(VarArrayUp,VarArrayCentral)

    plt.hist(VarArrayDmC,
             bins = bins,
             label = 'Down-Central',
             histtype='step'
             
    )
    plt.hist(VarArrayUmC,
             bins = bins,
             label = 'Up-Central',
             histtype='step'
             
    )    
    # dcTitle = "%s-%s"%(Var_down, Var_central)
    plt.title("%s Differences"%(Var_central))
    plt.xlabel("Value")
    plt.ylabel("Entries (A.U.)")
    plt.legend()
    plotOutNamepng = '%s/%s_Differences.png'%(OutputLoc,Var_central)
    plotOutNamepdf = '%s/%s_Differences.pdf'%(OutputLoc,Var_central)
    print"Saving plot: %s"%(plotOutNamepng)
    print"Saving plot: %s"%(plotOutNamepdf)
    plt.savefig(plotOutNamepng)
    plt.savefig(plotOutNamepdf)   
    plt.close()       

    # plt.hist(VarArrayUmC,
    #          bins = bins,
    #          label = 'Up-Central',
    #          histtype='step'
             
    # )
    # dcTitle = "%s-%s"%(Var_up, Var_central)
    # plt.title(dcTitle)
    # plt.xlabel("Value")
    # plt.ylabel("Entries (A.U.)")
    # plt.legend()
    # plotOutNamepng = '%s/%s_Differences.png'%(OutputLoc,Var_central)
    # plotOutNamepdf = '%s/%s_Differences.pdf'%(OutputLoc,Var_central)
    # print"Saving plot: %s"%(plotOutNamepng)
    # print"Saving plot: %s"%(plotOutNamepdf)
    # plt.savefig(plotOutNamepng)
    # plt.savefig(plotOutNamepdf)   
    # plt.close()           