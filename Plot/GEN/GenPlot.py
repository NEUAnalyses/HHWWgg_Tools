########################################################################################################################
# Abe Tishelman-Charny
# 20 April 2020
#
# The purpose of this python module is to plot variables from GEN-SIM files to verify this step of production. 
#
# Example Usage:
#
# python GenPlot.py --genType NMSSM_300_170 -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/NMSSM_XYHWWggqqlnu_MX300_MY170/10000events_GEN/200422_070152/0000/hadded.root -v pdgId,px,py,pz,pt,eta,phi,M --nEvents 10000
# python GenPlot.py -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_node/1_1000events_GEN-SIM//200420_065712/0000/GluGluToHHTo_WWgg_qqlnu_node_1_1000events_GEN-SIM_1.root -v M,pt,eta,phi
# python GenPlot.py --genType RES -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X260_HHWWgg_qqlnu/1000events_GEN/200520_140918/0000/ggF_X260_HHWWgg_qqlnu_1000events_GEN_1.root --nEvents 1000 -v pdgId,pt --requireHardProcess
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
parser.add_argument("--requireHardProcess", action="store_true", default=False, help="Require looking at hard process particles only", required=False)

args = parser.parse_args()

DeltaR = Math.VectorUtil.DeltaR 
DeltaPhi = Math.VectorUtil.DeltaPhi 
invmass = Math.VectorUtil.InvariantMass
genType = args.genType
variables = args.v.split(',')
singleParticles = args.sp.split(',')
requireHardProcess = args.requireHardProcess 
NMSSM, EFT, RES = 0, 0, 0 
if("NMSSM" in genType and "EFT" in genType):
    print("ERROR - genType cannot contain both NMSSM and EFT")
    print("Exiting")
    exit(1)
if("NMSSM" in genType): NMSSM = 1 
elif("EFT" in genType): EFT = 1 
elif("RES" in genType): RES = 1 

gROOT.SetBatch(True)
genHandle = Handle('vector<reco::GenParticle>')
ol = '/eos/user/a/atishelm/www/HHWWgg_Analysis/GEN/%s'%(genType)
inputFile = args.i 
fnalPath = "root://cmsxrootd.fnal.gov//%s"%(inputFile)
outFilePath = '%s/GEN_%s.root'%(ol,genType) # website output 
# outFilePath = 'GEN_%s.root'%(genType) # local output 
events = Events(fnalPath) # needs to be file with root prefix
outFile = TFile(outFilePath, 'recreate')
outTree = TTree('GEN','GEN variables')
branches = []
extraBranches = []
particleNames = []
extraVars = [] 
if(NMSSM): 
    particleNames = ['X','Y','H']
    extraVars = ['DR_YH','DPhi_YH','DEta_YH'] #,'DEta_YH']

if(RES):
    particleNames = ['Y','H','tau','b']
    extraVars = ['invM_HH']
maxpdgIds = 10000

iEvent = array('i', 10000*[-99]) #
outTree.Branch('iEvent',iEvent,'iEvent[10000]/I')
branches.append("iEvent")

status = array('d', 10000*[-99]) #
outTree.Branch('status',status,'status[10000]/D')
branches.append("status")

isHardProcess = array('d', 10000*[-99]) #
outTree.Branch('isHardProcess',isHardProcess,'isHardProcess[10000]/D')
branches.append("isHardProcess")

numberOfDaughters = array('d', 10000*[-99]) #
outTree.Branch('numberOfDaughters',numberOfDaughters,'numberOfDaughters[10000]/D')
branches.append("numberOfDaughters")

daughterOnepdgId = array('d', 10000*[-99]) #
outTree.Branch('daughterOnepdgId',daughterOnepdgId,'daughterOnepdgId[10000]/D')
branches.append("daughterOnepdgId")

# pdgId = array('d', 10000*[-99]) #
# outTree.Branch('pdgId',pdgId,'pdgId[10000]/D')
# branches.append("pdgId")

# outTree, branches = DefineBranch("isHardProcess",outTree,branches)
# outTree, branches = DefineBranch("status",outTree,branches)
# print("output:",output)``
# print("output[0]:",output[0])
# print("output[1]:",output[1])

# exit(1)

# DefineBranch("numberOfDaughters",outTree)

# numberOfDaughter

# status_h = TH1F("status","status",201,0,201)
# HP_status_h = TH1F("HP_status","HP_status",201,0,201)

# if('pdgId' in variables): # Can make this nonp4vars if you want 
#     pdgId = array('d', maxpdgIds*[-99]) #
#     outTree.Branch('pdgId',pdgId,'pdgId[10000]/D')
#     branches.append("pdgId")
#     variables.remove('pdgId') # remove because it's not a p4 variable 
for v in variables:
    exec("%s_arr = array('d', 10000*[-99])"%(v))
    eval("outTree.Branch('%s', %s_arr, '%s_arr[10000]/D')"%(v,v,v))  
    branches.append(v)

if len(extraVars) > 0:
    for eV in extraVars:
        exec("%s = array('d', [0.])"%(eV))
        eval("outTree.Branch('%s',%s,'%s[1]/D')"%(eV,eV,eV))
        extraBranches.append(eV)

print'Looping events ...'
if(not requireHardProcess): events.getByLabel('genParticles', genHandle) # all particles 
for iev, event in enumerate(events):
    # print'-------------------------------------------------------'
    if(iev%100==0): print'On event:',iev 
    if(iev == int(args.nEvents)): 
        print("Reached max desired events")
        break 
    # iEvent[0] = iev     
    # iEvent = array('i', 10000*[iev])   
    # events.getByLabel('genParticles', genHandle) # isHardProcess condition 
    # events.getByLabel('genParticles', genHandle)
    if(requireHardProcess): events.getByLabel('genParticles', genHandle) # all particles 
    genParticles = genHandle.product()  
    if(requireHardProcess): ps = [p for p in genParticles if p.isHardProcess()]
    else: ps = [p for p in genParticles]
    
    # ps = [p for p in genParticles]

    # status[]
    # for ip,p in enumerate(ps):
        # status[ip] = p.status()
        # isHardProcess[ip] = p.isHardProcess()
        # numberOfDaughters[ip] = p.numberOfDaughters()
        # status_h.Fill(p.status())
        # if(p.isHardProcess()):
            # HP_status_h.Fill(p.status())

    # HP_ps = [p for p in genParticles if p.isHardProcess()]
    # for ip,p in enumerate(HP_ps):
    #     HP_status[ip] = p.status()
    #     pdgId_val = p.pdgId() 
    #     pdgId[ip] = pdgId_val

    # Trying to find ISR ...
    # for ip,p in enumerate(ps):
        # if(p.pdgId == 45):
            # print("45")
        # print"---"
        # print"Hard Process pdgId:",p.pdgId()
        # print"number of daughters:",p.numberOfDaughters()
        # # if(p.pdgId == 35):
        # print"mother pdgID: ",p.mother(0).pdgId()
        
        # if(p.pdgId == 45):
        #     print"daughter pdgID: ",p.daughter(0).pdgId()
        # print"---"
        # print"p.daughter(0)",p.daughter(0)
        # if(p.daughter(0) is not None):
        #     print"Mother pdgId:",p.pdgId()
        #     # print p.daughter(0)
        #     if(p.daughter(0).pdgId() is not None):
        #         print "Daughter(0) pdgId:",p.daughter(0).pdgId()
        # print"p.daughter(1)",p.daughter(1)
        # if(p.daughter(1) is not None):
        #     if(p.daughter(1).pdgId() is not None):
        #         print "Daughter(1) pdgId:",p.daughter(1).pdgId()          
            # if(p.daughter(0).pdgId() is not None):
            #     pdgId_ = p.pdgId()
            #     print("---")
            #     print("mother pdgId:",pdgId_)
            #     print("daughter pdgId:",p.daughter(0).pdgId())
            #     print("---")
            # print("mother:",p.daughter(0))
    # check daughter particles of gluons 

    if(RES): foundFirstHiggs = 0
    for ip,particle in enumerate(ps):
        iEvent[ip] = iev     
        status[ip] = particle.status()
        isHardProcess[ip] = particle.isHardProcess()
        numberOfDaughters[ip] = particle.numberOfDaughters()  

        # if(particle.numberOfDaughters() > 0):
        #     # print 'motherParticle:',particle.mother(0).pdgId()
        #     print 'pdgId:',particle.pdgId()
        #     nDaughters = int(particle.numberOfDaughters())
        #     print 'nDaughters:',nDaughters
        #     if (nDaughters == 1): print'daughterPdgId:',particle.daughter(0).pdgId()
        #     if (nDaughters == 2):
        #         print'Daughter 1:',particle.daughter(0).pdgId()
        #         print'Daughter 2:',particle.daughter(1).pdgId()

            # print("pdgId:",particle.pdgId())
            # print("particle.numberOfDaughters == ",particle.numberOfDaughters())
            # print("particle.daughter(0).pdgId() == ",particle.daughter(0).pdgId())

            # daughterOnepdgId[ip] = particle.daughter(0).pdgId()    

        pdgId_val = particle.pdgId() 
        # pdgId[ip] = pdgId_val

        if(NMSSM):
            if(pdgId_val == 25): Higgs = particle.p4()
            elif(pdgId_val == 35): IRP = particle.p4() 
        if(RES):
            if(pdgId_val == 25): 
                if(foundFirstHiggs == 0): 
                    foundFirstHiggs = 1 
                    H1 = particle.p4()
                elif(foundFirstHiggs == 1):
                    H2 = particle.p4()

        for v in variables: 
            if(v == "pdgId"): # this variable is member of particle, not particle.p4()
                exec("%s_val = particle.%s()"%(v,v))
                exec("%s_arr[%s] = %s_val"%(v,ip,v))  
            else:
                exec("%s_val = particle.p4().%s()"%(v,v))
                exec("%s_arr[%s] = %s_val"%(v,ip,v))

    if(NMSSM):
        H_eta, Y_eta = Higgs.eta(), IRP.eta()  
        DR_YH_val = DeltaR(Higgs,IRP)
        DPhi_YH_val = DeltaPhi(Higgs,IRP)
        DEta_YH_val = float(H_eta - Y_eta)   
        for eV in extraVars:
            exec("%s[0] = %s_val"%(eV,eV))
    if(RES):
        invM_HH_val = invmass(H1,H2)
        for eV in extraVars:
            exec("%s[0] = %s_val"%(eV,eV))

    outTree.Fill() # fill tree once per event 

# Draw all branches in tree, place in output on website 
dontDrawBranches = ["iEvent","status","isHardProcess","numberOfDaughters","daughterOnepdgId"]
for branch in branches:
    if branch in dontDrawBranches: continue 
    if(branch == "pdgId"): 
        outName = "%s/pdgId.png"%(ol)
        cut = "pdgId != -99"
        DrawSaveBranch(outTree,branch,outName,cut)
    else: 
        for pN in particleNames:
            pId = GetPdgId(pN)
            cut = "abs(pdgId) == %s"%(pId)
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
