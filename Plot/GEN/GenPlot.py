########################################################################################################################
# Abe Tishelman-Charny
# 20 April 2020
#
# The purpose of this python module is to plot variables from GEN-SIM files to verify this step of production. 
#
# Example Usage:
#
# python GenPlot.py -i store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/test/NMSSM_XYH_WWgg_MX_500_MY_300_output.root -v M,pt
# <command2>
# <command3>
#
########################################################################################################################

import argparse
import os 
from DataFormats.FWLite import Handle, Runs, Lumis, Events
from ROOT import gROOT  
from GenPlotTools import *
parser = argparse.ArgumentParser(description='Madgraph/pythia configuration creator')
parser.add_argument('-i', type=str, default="", help="Input GEN file, format: 'store/.../.root", required=True)
parser.add_argument('-v', type=str, default="", help="Comma separated list of variables to plot", required=True)

# parser.add_argument("-pt", action="store_true", default=False, help="Plot invariant masses of NMSSM particles", required=False)

# parser.add_argument("--Resonant", action="store_true", default=False, help="Create Radion/Graviton model", required=False)

args = parser.parse_args()

print"Plotting HH variables"

variables = args.v.split(',')

gROOT.SetBatch(True)
genHandle = Handle('vector<reco::GenParticle>')
ol = '/eos/user/a/atishelm/www/HHWWgg_Analysis/GEN/'
inputFile = args.i 
fnalPath = "root://cmsxrootd.fnal.gov//%s"%(inputFile)

events = Events(fnalPath) # needs to be file with root prefix
pdgIds = TH1F('pdgIds','pdgIds',100,-50,50)

# histos = []
# histos = MakeVarHistos(variables) # make variable histograms 
# for h in histos:
    # print'h:',h
    # h.SetDirectory(0)

for v in variables:
    Make_X_h = "X_%s_h = TH1F('X_%s_h','X_%s_h',%d,%d,%d)"%(v,v,v,1000,0,1000)
    Make_Y_h = "Y_%s_h = TH1F('Y_%s_h','Y_%s_h',%d,%d,%d)"%(v,v,v,1000,0,1000)
    exec(Make_X_h)
    exec(Make_Y_h)

print'Looping events ...'
for iev, event in enumerate(events):
    if(iev%100==0): print'On event:',iev 
    events.getByLabel('genParticles', genHandle)
    genParticles = genHandle.product()  
    ps = [p for p in genParticles if p.isHardProcess()]
    for particle in ps:
        pdgId = particle.pdgId() 
        for v in variables: exec("%s = particle.p4().%s()"%(v,v))
        pdgIds.Fill(pdgId)
        if(pdgId == 45): 
            for v in variables:
                eval("X_%s_h.Fill(%s)"%(v,v))
        elif(pdgId == 35): 
            for v in variables:
                eval("Y_%s_h.Fill(%s)"%(v,v))

outName = "%s/pdgIds.png"%(ol)
DrawSave(pdgIds,"",outName)

for v in variables:
    X_histogram = eval("X_%s_h"%(v))
    Y_histogram = eval("Y_%s_h"%(v))
    DrawSave(X_histogram,"","%s/%s.png"%(ol,X_histogram.GetTitle()))
    DrawSave(Y_histogram,"","%s/%s.png"%(ol,Y_histogram.GetTitle()))

# SaveVarPlots(variables) # save variables plots 