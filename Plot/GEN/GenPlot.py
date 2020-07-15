########################################################################################################################
# Abe Tishelman-Charny
# 20 April 2020
#
# The purpose of this python module is to plot variables from GEN-SIM files to verify this step of production. 
#
# Example Usage:
#
# ##-- Create GEN Ntuples
# python GenPlot.py --CreateNtuple --genType NONRES_qqlnu_2016 -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/Test_for_HHWWgg_SM/qqlnu.root -v pdgId,px,py,pz,pt,eta,phi,M --nEvents 100 --requireHardProcess --outPlots 
# python GenPlot.py --CreateNtuple --genType NMSSM_300_170 -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/NMSSM_XYHWWggqqlnu_MX300_MY170/10000events_GEN/200422_070152/0000/hadded.root -v pdgId,px,py,pz,pt,eta,phi,M --nEvents 10000
# python GenPlot.py --CreateNtuple -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/GluGluToHHTo_WWgg_qqlnu_node/1_1000events_GEN-SIM//200420_065712/0000/GluGluToHHTo_WWgg_qqlnu_node_1_1000events_GEN-SIM_1.root -v M,pt,eta,phi
# python GenPlot.py --CreateNtuple --genType RES -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X260_HHWWgg_qqlnu/1000events_GEN/200520_140918/0000/ggF_X260_HHWWgg_qqlnu_1000events_GEN_1.root --nEvents 1000 -v pdgId,pt --requireHardProcess
#
# python GenPlot.py --CreateNtuple --genType RES_X260_withTb -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X260_HHWWgg_qqlnu/100000events_GEN-SIM/200523_125055/Hadded/ggF_X260_HHWWgg_qqlnu_100000events_GEN-SIM_Hadded.root -v pdgId --nEvents 100000 --outPlots --requireHardProcess
# python GenPlot.py --CreateNtuple --genType RES_X260_withoutTb -i /store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X260_WWgg_qqlnugg/100000events_GEN-SIM/191205_151201/Hadded/ggF_X260_WWgg_qqlnugg_100000events_GEN-SIM_Hadded.root -v pdgId --nEvents 1000 --outPlots --requireHardProcess
#
# ##-- Compare Ntuples
# python GenPlot.py --CompareNtuples --compareFiles /eos/user/a/atishelm/www/HHWWgg_Analysis/GEN/RES_X260_withoutTb/GEN_RES_X260_withoutTb.root,/eos/user/a/atishelm/www/HHWWgg_Analysis/GEN/RES_X260_withTb/GEN_RES_X260_withTb.root -v pdgId,pt,eta,phi -p 5,15
# python GenPlot.py --CompareNtuples --compareFiles /eos/user/a/atishelm/www/HHWWgg_Analysis/GEN/RES_X260_withoutTb/GEN_RES_X260_withoutTb.root,/eos/user/a/atishelm/www/HHWWgg_Analysis/GEN/RES_X260_withTb/GEN_RES_X260_withTb.root -v pt --particles 25 --fileLabels NO_Tb,WITH_Tb
########################################################################################################################

import argparse
import os 
from os import path 
from DataFormats.FWLite import Handle, Runs, Lumis, Events
from ROOT import gROOT, Math, TTree, TFile, TCanvas, TH1F, TTree, TLegend, gStyle 
from GenPlotTools import *
from array import array 

parser = argparse.ArgumentParser(description='GEN and GEN-SIM ntuple production and comparison')

##-- Create GEN Ntuples
parser.add_argument("--CreateNtuple", action="store_true", default=False, help="Create GEN Ntuple", required=False)
parser.add_argument("--outPlots", action="store_true", default=False, help="Output plots to website, or output location", required=False)
parser.add_argument('-i', type=str, default="", help="Input GEN file, format: 'store/.../.root", required=False)
parser.add_argument('-v', type=str, default="pdgId", help="Comma separated list of variables to plot", required=False)
parser.add_argument('-sp', type=str, default="", help="Single particles to plot variables of", required=False)
parser.add_argument('--genType', type=str, default="GEN", help="Gen type. Used to create output folder", required=False)
parser.add_argument('--nEvents', type=float, default=-1, help="Max number of events to run on", required=False)
parser.add_argument("--requireHardProcess", action="store_true", default=False, help="Require looking at hard process particles only", required=False)

##-- Compare Ntuples 
parser.add_argument("--CompareNtuples", action="store_true", default=False, help="Create GEN Ntuple", required=False)
parser.add_argument('--outDirec', type=str, default="defaultOut", help="Output directory for ntuple comparison", required=False)
parser.add_argument('--compareFiles', type=str, default="", help="Comma separated list of root files to compare variables of", required=False)
parser.add_argument('--particles', type=str, default="", help="Comma separated list of particles (pdgIds) to compare variables of", required=False)
parser.add_argument('--fileLabels', type=str, default="", help="Comma separated list of file labels for legend", required=False)

##-- Misc
parser.add_argument("--doTauChecks", action="store_true", default=False, help="Checks for proper Tau production", required=False)

args = parser.parse_args()

if(args.CreateNtuple):

    DeltaR = Math.VectorUtil.DeltaR 
    DeltaPhi = Math.VectorUtil.DeltaPhi 
    invmass = Math.VectorUtil.InvariantMass
    genType = args.genType
    variables = args.v.split(',')
    singleParticles = args.sp.split(',')
    requireHardProcess = args.requireHardProcess 
    NMSSM, EFT, RES, NONRES = 0, 0, 0, 0
    if("NMSSM" in genType and "EFT" in genType):
        print("ERROR - genType cannot contain both NMSSM and EFT")
        print("Exiting")
        exit(1)
    if("NMSSM" in genType): NMSSM = 1 
    elif("EFT" in genType): EFT = 1 
    elif("RES" in genType): RES = 1 
    elif("NONRES" in genType): NONRES = 1 

    gROOT.SetBatch(True)
    # genHandle = Handle('vector<reco::GenParticle>')
    beforeOl = "/eos/user/a/atishelm/www/HHWWgg/GEN/"
    ol = '/eos/user/a/atishelm/www/HHWWgg/GEN/%s'%(genType)
    if(args.i == ""):
        print"ERROR - Need to provide an input file with the -i flag"
        print"Exiting"
        exit(1)
    print"Creating output directory: %s if it doesn't exist"%(ol)
    if(not os.path.exists(ol)):
        print"Creating output directory: %s"%(ol)
        os.system('mkdir %s'%(ol))
        os.system('cp %s/index.php %s'%(beforeOl,ol))        
    inputFile = args.i 
    fnalPath = "root://cmsxrootd.fnal.gov//%s"%(inputFile)
    outFilePath = '%s/GEN_%s.root'%(ol,genType) # website output 
    # outFilePath = 'GEN_%s.root'%(genType) # local output 
    # events = Events(fnalPath) # needs to be file with root prefix
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
        # particleNames = ['Y','H','tau','b']
        extraVars = ['invM_HH']
    if(NONRES):
        particleNames = ['H']
        extraVars = ['invM_HH']
    maxpdgIds = 10000

    iEvent = array('i', 10000*[-99]) #
    outTree.Branch('iEvent',iEvent,'iEvent[10000]/I')
    branches.append("iEvent")

    status = array('d', 10000*[-99]) #
    outTree.Branch('status',status,'status[10000]/D')
    branches.append("status")

    isPromptFinalState = array('d', 10000*[-99]) #
    outTree.Branch('isPromptFinalState',isPromptFinalState,'isPromptFinalState[10000]/D')
    branches.append("isPromptFinalState")
    
    fromHardProcessFinalState = array('d', 10000*[-99]) #
    outTree.Branch('fromHardProcessFinalState',fromHardProcessFinalState,'fromHardProcessFinalState[10000]/D')
    branches.append("fromHardProcessFinalState")

    isHardProcess = array('d', 10000*[-99]) #
    outTree.Branch('isHardProcess',isHardProcess,'isHardProcess[10000]/D')
    branches.append("isHardProcess")

    numberOfDaughters = array('d', 10000*[-99]) #
    outTree.Branch('numberOfDaughters',numberOfDaughters,'numberOfDaughters[10000]/D')
    branches.append("numberOfDaughters")

    daughterOnepdgId = array('d', 10000*[-99]) #
    outTree.Branch('daughterOnepdgId',daughterOnepdgId,'daughterOnepdgId[10000]/D')
    branches.append("daughterOnepdgId")

    if(args.doTauChecks):
        isDirectHardProcessTauDecayProductFinalState = array('d', 10000*[-99]) #
        outTree.Branch('isDirectHardProcessTauDecayProductFinalState',isDirectHardProcessTauDecayProductFinalState,'isDirectHardProcessTauDecayProductFinalState[10000]/D')
        branches.append("isDirectHardProcessTauDecayProductFinalState")

        isDirectPromptTauDecayProductFinalState = array('d', 10000*[-99]) #
        outTree.Branch('isDirectPromptTauDecayProductFinalState',isDirectPromptTauDecayProductFinalState,'isDirectHardProcessTauDecayProductFinalState[10000]/D')
        branches.append("isDirectPromptTauDecayProductFinalState")



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

    # if(not requireHardProcess): events.getByLabel('genParticles', genHandle) # all particles 
    events = Events(fnalPath) # needs to be file with root prefix
    # events.getByLabel('genParticles', genHandle) # all particles 
    genHandle = Handle('vector<reco::GenParticle>')

    if(args.doTauChecks):
        N_taus = 0 
        N_leptonicTauDecays = 0 
        tauDaughters_h = TH1F("tauDaughters_h","tau Daughters, pdgIds",1000,-500,500)

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

        event.getByLabel('genParticles',genHandle)

        # if(requireHardProcess): events.getByLabel('genParticles', genHandle) # all particles 

        genParticles = genHandle.product()  

        if(requireHardProcess): ps = [p for p in genParticles if p.isHardProcess()]
        else: ps = [p for p in genParticles]

        # ps = [p for p in genParticles]
        
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

        if(RES or NONRES): foundFirstHiggs = 0
        for ip,particle in enumerate(ps):
            # print"ip:",ip
            iEvent[ip] = iev     
            status[ip] = particle.status()
            isHardProcess[ip] = particle.isHardProcess()
            numberOfDaughters[ip] = particle.numberOfDaughters()  
            isPromptFinalState[ip] = particle.isPromptFinalState()
            fromHardProcessFinalState[ip] = particle.fromHardProcessFinalState()
            if(args.doTauChecks):
                isDirectHardProcessTauDecayProductFinalState[ip] = particle.isDirectHardProcessTauDecayProductFinalState()
                isDirectPromptTauDecayProductFinalState[ip] = particle.isDirectPromptTauDecayProductFinalState()

            if(args.doTauChecks):

                if(abs(particle.pdgId())) == 15: 
                    tauMother = particle.mother(0).pdgId()
                    daughters = [] 
                    nDaughters = particle.numberOfDaughters()
                    for d in range(nDaughters):
                        daughterID = particle.daughter(d).pdgId()
                        daughters.append(daughterID)     
                    # do not want to look at intermediate taus 
                    if(15 in daughters or -15 in daughters): continue    
                    if(tauMother==431 or tauMother==-431): continue # don't want to look at a tau from a D meson        
                    # if(abs(tauMother)!=24): continue # only want to look at taus from W bosons 
                    if(tauMother==15 or tauMother==-15):
                        tauGrandMother = particle.mother(0).mother(0).pdgId()
                        # if(abs(tauGrandMother)!=24): continue                  
                        if(abs(tauGrandMother)==431): continue                  
                    # if(abs(tauMother)) == 15: continue 
                    print"On tau"
                    print"tau mother:",tauMother
                    print"daughters:",daughters 

                    N_taus += 1 
                    for d in daughters:
                        tauDaughters_h.Fill(d)
                    # leptons = [11,13]
                    if(11 in daughters or -11 in daughters or 13 in daughters or -13 in daughters):
                        N_leptonicTauDecays += 1
                
            # isDirectPromptTauDecayProduct[ip] = particle.isDirectPromptTauDecayProduct
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
            # print"pdgID:",pdgId_val
            if(NMSSM):
                if(pdgId_val == 25): Higgs = particle.p4()
                elif(pdgId_val == 35): IRP = particle.p4() 
            if(RES or NONRES):
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
        if(RES or NONRES):
            invM_HH_val = invmass(H1,H2)
            for eV in extraVars:
                exec("%s[0] = %s_val"%(eV,eV))          

        outTree.Fill() # fill tree once per event 

    if(args.doTauChecks):
        # figuring out taus 
        print"N_taus:",N_taus
        print"N_leptonicTauDecays:",N_leptonicTauDecays

        tauDaughters_h.SaveAs("tauDaughters_h.root")

    # Draw all branches in tree, place in output on website 
    if(args.outPlots):
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

elif(args.CompareNtuples):
    print"comparing Ntuples"
    ol = '/eos/user/a/atishelm/www/HHWWgg_Analysis/GEN/compare'
    gROOT.SetBatch(1) # Do not output upon draw statement 
    if(args.compareFiles == ""):
        print"ERROR - Need to provide input file with the --compareFiles flag"
        print"Exiting"
        exit(1)    
    files = args.compareFiles.split(',')
    fileLabels = args.fileLabels.split(',')
    vars = args.v.split(',')
    particles = args.particles.split(',')
    gStyle.SetOptStat(0)
    for v in vars:
        print"v:",v
        for pdgId in particles:
            histos = [] 
            lineStyles = [2,3]
            lineColors = [3,4]   
            legend = TLegend(0.65,0.7,0.89,0.89)
            # legend.SetTextSize(0.015)
            legend.SetTextSize(0.03)
            legend.SetBorderSize(0)                      
            for ipath,fpath in enumerate(files):
                print"fpath:",fpath
                fileLabel = fileLabels[ipath]
                cut = "abs(pdgId) == %s"%(pdgId)
                if(v == "pdgId"): cut = ""
                lineStyle = lineStyles[ipath]
                lineColor = lineColors[ipath]
                f = TFile(fpath)
                fTree = f.Get("GEN")
                nEntries = fTree.GetEntries()
                print"nEntries:",nEntries
                bins = [100,0,100]
                if(v == "eta" or v == "phi"): bins = [10,-5,5]
                if(v == "pdgId"): bins = [80,-40,40]
                h_tmp = TH1F("h_tmp","h_tmp",bins[0],bins[1],bins[2])
                h_tmp.SetLineColor(lineColor)
                h_tmp.SetFillColorAlpha(lineColor,0.35)
                h_tmp.SetLineStyle(lineStyle)
                fTree.Draw("%s >> h_tmp"%(v),cut)
                nBins=h_tmp.GetNbinsX()
                # print"GetNbinsX:",nBins
                integral = h_tmp.Integral(1,nBins)
                # print"integral",integral
                if(integral != 0): h_tmp.Scale(1/float(integral)) # normalize
                h_copy = h_tmp.Clone("h_copy")
                legend.AddEntry(h_copy,fileLabel,"FL")
                h_copy.SetDirectory(0)
                # h_copy.Scale(1/nEntries) # normalize 
                histos.append(h_copy)
            # legend = TLegend(0.65,0.7,0.89,0.89)
            # legend.SetTextSize(0.015)
            # legend.SetBorderSize(0)        
            c = TCanvas()
            for ih,h in enumerate(histos):
                print"h:",h
                if(ih==0): 
                    h.Draw("hist")
                    h.SetTitle("%s_%s"%(v,pdgId))
                else: h.Draw("hist same")
                # legend.AddEntry(h,fileLabel,"FL")
                
            legend.Draw("same")
            c.SaveAs("%s/%s_%s_compare.png"%(ol,v,pdgId))
            c.SaveAs("%s/%s_%s_compare.pdf"%(ol,v,pdgId))





