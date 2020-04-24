########################################################################################################################
# Abe Tishelman-Charny
# 20 April 2020
#
# The purpose of this python module is to plot variables from GEN-SIM files to verify this step of production. 
#
# Example Usage:
#
# python GenPlot.py --genType NMSSM_300_170 -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/NMSSM_XYHWWggqqlnu_MX300_MY170/10000events_GEN/200422_070152/0000/hadded.root -v pdgId,px,py,pz,pt,eta,phi,M --nEvents 10000
### python GenPlot.py -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_node/1_1000events_GEN-SIM//200420_065712/0000/GluGluToHHTo_WWgg_qqlnu_node_1_1000events_GEN-SIM_1.root -v M,pt,eta,phi
########################################################################################################################

import argparse
import os 
from os import path 
from DataFormats.FWLite import Handle, Runs, Lumis, Events
from ROOT import gROOT, Math, TTree, TFile 
from GenPlotTools import *
from array import array 

parser = argparse.ArgumentParser(description='Madgraph/pythia configuration creator')
parser.add_argument('-i', type=str, default="", help="Input GEN file, format: 'store/.../.root", required=True)
parser.add_argument('-v', type=str, default="", help="Comma separated list of variables to plot", required=True)
parser.add_argument('-sp', type=str, default="", help="Single particles to plot variables of", required=False)
parser.add_argument('--genType', type=str, default="GEN", help="Gen type. Used to create output folder", required=False)
parser.add_argument('--nEvents', type=float, default=-1, help="Max number of events to run on", required=False)

args = parser.parse_args()

DeltaR = Math.VectorUtil.DeltaR 
DeltaPhi = Math.VectorUtil.DeltaPhi 
genType = args.genType
variables = args.v.split(',')
singleParticles = args.sp.split(',')

NMSSM, EFT = 0, 0
if("NMSSM" in genType and "EFT" in genType):
    print("ERROR - genType cannot contain both NMSSM and EFT")
    print("Exiting")
    exit(1)
if("NMSSM" in genType): NMSSM = 1 
elif("EFT" in genType): EFT = 1 

gROOT.SetBatch(True)
genHandle = Handle('vector<reco::GenParticle>')
ol = '/eos/user/a/atishelm/www/HHWWgg_Analysis/GEN/%s'%(genType)
inputFile = args.i 
fnalPath = "root://cmsxrootd.fnal.gov//%s"%(inputFile)
outFilePath = '%s/GEN_%s.root'%(ol,genType)
# outFilePath = 'GEN_%s.root'%(genType) # local 
events = Events(fnalPath) # needs to be file with root prefix
outFile = TFile(outFilePath, 'recreate')
outTree = TTree('GEN','GEN variables')
branches = []
extraBranches = []
particleNames = []
if(NMSSM): 
    particleNames = ['X','Y','H']
    extraVars = ['DR_YH','DPhi_YH','DEta_YH'] #,'DEta_YH']

maxpdgIds = 100

if('pdgId' in variables): # Can make this nonp4vars if you want 
    pdgId = array('d', maxpdgIds*[-99]) #
    outTree.Branch('pdgId',pdgId,'pdgId[50]/D')
    branches.append("pdgId")
    variables.remove('pdgId') # remove because it's not a p4 variable 
for v in variables:
    exec("%s_arr = array('d', 50*[-99])"%(v))
    eval("outTree.Branch('%s', %s_arr, '%s_arr[50]/D')"%(v,v,v))  
    branches.append(v)

for eV in extraVars:
    exec("%s = array('d', [0.])"%(eV))
    eval("outTree.Branch('%s',%s,'%s[1]/D')"%(eV,eV,eV))
    extraBranches.append(eV)

print'Looping events ...'
for iev, event in enumerate(events):
    if(iev%100==0): print'On event:',iev 
    if(iev == int(args.nEvents)): 
        print("Reached max desired events")
        break 
    events.getByLabel('genParticles', genHandle)
    genParticles = genHandle.product()  
    ps = [p for p in genParticles if p.isHardProcess()]

    for ip,particle in enumerate(ps):
        pdgId_val = particle.pdgId() 
        pdgId[ip] = pdgId_val
        if(NMSSM):
            if(pdgId_val == 25): Higgs = particle.p4()
            elif(pdgId_val == 35): IRP = particle.p4() 
        for v in variables: 
            exec("%s_val = particle.p4().%s()"%(v,v))
            exec("%s_arr[%s] = %s_val"%(v,ip,v))

    if(NMSSM):
        H_eta, Y_eta = Higgs.eta(), IRP.eta()  
        DR_YH_val = DeltaR(Higgs,IRP)
        DPhi_YH_val = DeltaPhi(Higgs,IRP)
        DEta_YH_val = float(H_eta - Y_eta)        
        for eV in extraVars:
            exec("%s[0] = %s_val"%(eV,eV))

    outTree.Fill() # fill tree once per event 

# Draw all branches in tree 
for branch in branches:
    if(branch == "pdgId"): 
        outName = "%s/pdgId.png"%(ol)
        cut = "pdgId != -99"
        DrawSaveBranch(outTree,branch,outName,cut)
    else: 
        for pN in particleNames:
            pId = GetPdgId(pN)
            cut = "pdgId == %s"%(pId)
            outName = "%s/%s_%s.png"%(ol,pN,branch)
            DrawSaveBranch(outTree,branch,outName,cut)        

for eB in extraBranches:
    outName = "%s/%s.png"%(ol,eB)
    cut = ""
    DrawSaveBranch(outTree,eB,outName,cut)

outFile.Write()
outFile.Close()
print("nTuple saved to: ",outFilePath)
print("DONE")