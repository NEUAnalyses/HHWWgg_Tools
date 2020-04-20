########################################################################################################################
# Abe Tishelman-Charny
# 20 April 2020
#
# The purpose of this python module is to provide functions and variables for GenPlot.py 
########################################################################################################################

from ROOT import TCanvas, TH1F  

def DrawSave(h_,drawOption,outName_):
    c = TCanvas('c','c',800,600)
    h_.Draw(drawOption)
    c.SaveAs(outName_)

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