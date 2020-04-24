########################################################################################################################
# Abe Tishelman-Charny
# 20 April 2020
#
# The purpose of this python module is to provide functions and variables for GenPlot.py 
########################################################################################################################

from ROOT import TCanvas, TH1F  

def GetPdgId(pName_):
    PdgIdDictionary = {
        "H": 25,
        "Y": 35,
        "X": 45
    }
    return PdgIdDictionary[pName_]

def DrawSaveBranch(tree_,branch_,outName_,cut_):
    c = TCanvas('c','c',800,600)
    tree_.Draw(branch_,cut_)
    c.SaveAs(outName_)

def DrawSave(h_,drawOption,outName_):
    c = TCanvas('c','c',800,600)
    h_.Draw(drawOption)
    c.SaveAs(outName_)

def GetBins(v_):
    varBinDictionary = {
    "M": [1000,0,1000],
    "pt": [100,0,750],
    "eta": [50,-10,10],
    "phi": [50,-10,10],
    "px": [500,0,500],
    "py": [500,0,500],
    "pz": [500,0,500]
    }
    return varBinDictionary[v_]

# def GetDesignParams(v_):
#     varBinDictionary = {
#     "M": [1000,0,1000],
#     "pt": [100,0,750],
#     "eta": [10,-10,10],
#     "phi": [10,-10,10]
#     }
#     return varBinDictionary[v_]

# def MakeVarHistos(variables_):
#     histos = []
#     for v in variables_:
#         Make_X_h = "X_%s_h = TH1F('X_%s_h','X_%s_h',%d,%d,%d)"%(v,v,v,1000,0,1000)
#         Make_Y_h = "Y_%s_h = TH1F('Y_%s_h','Y_%s_h',%d,%d,%d)"%(v,v,v,1000,0,1000)
#         exec(Make_X_h)
#         exec(Make_Y_h)
#         histos.append(eval("X_%s_h"%(v)))
#         histos.append(eval("Y_%s_h"%(v)))
#     return histos 

# def SaveVarPlots(variables_):
    # for v in variables_:
    #     X_histogram = eval("X_%s_h"%(v))
    #     Y_histogram = eval("Y_%s_h"%(v))
    #     DrawSave(X_histogram,"","%s/%s.png"%(ol,X_histogram.GetTitle()))
    #     DrawSave(Y_histogram,"","%s/%s.png"%(ol,Y_histogram.GetTitle()))
    # return 1 

# if(not path.exists("CMSSW_9_3_9_patch1")):
#     print'CMSSW_9_3_9_patch1 does not exist. Getting now ...'
#     os.system('export SCRAM_ARCH=slc6_amd64_gcc630')
#     os.system('cmsrel CMSSW_9_3_9_patch1') 
#     print'Setting cmsenv environment variables ...'
#     os.system('cd CMSSW_9_3_9_patch1/src; cmsenv; cd ../../ ')

# else: 
#     print'Setting cmsenv environment variables ...'
#     os.system('cd CMSSW_9_3_9_patch1/src; cmsenv; cd ../../ ')    