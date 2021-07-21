from python.Datasets import * 

import pandas as pd 
import time 
import pickle 
import os 
from ROOT import Math 
from DataFormats.FWLite import Handle, Events
from array import array 
from math import sqrt 

##-- Get pdgId of first daughter of a particle 
def GetDaughterPdgId(particle_):
    DaughterPdgId = particle_.daughter(0).pdgId()
    return DaughterPdgId

##-- Print particle daughter IDs, for debugging 
def PrintDaughterIDs(daughter0ID_,daughter1ID_,message):
    print"***********"
    print"%s:"%(message)
    print"daughters:"
    print"\t%s"%(daughter0ID_)
    print"\t%s"%(daughter1ID_)
    print"***********" 
    return 0 

##-- If you have a W boson, get particle that has multiple daughters by skipping intermediate boson decays 
def SkipInternalWDecays(W_0):
    nDaughters = W_0.numberOfDaughters()
    if(nDaughters==2): return W_0
    tries = 0
    while(nDaughters!=2):
        W_0 = W_0.daughter(0)
        nDaughters = W_0.numberOfDaughters()
        if(nDaughters==2):
            return W_0
        tries += 1 
        if(tries == 50):
            print"ERROR - Couldn't skip W internal decays after 50 tries"
            print"Exiting"
            exit(1)

##-- 
def SkipPhoRadVtx(particle0_,debug):
    daughter0ID = particle0_.daughter(0).pdgId()
    daughter1ID = particle0_.daughter(1).pdgId()
    ##-- If first daughter is photon, try to get daughters from other particle (W boson)
    if(daughter0ID==22): 
        if(debug): print"found photon daughter 1"
        WBoson_Cand = particle0_.daughter(1)
        WBoson_Cand = SkipInternalWDecays(WBoson_Cand)
        daughter0ID = WBoson_Cand.daughter(0).pdgId()
        daughter1ID = WBoson_Cand.daughter(1).pdgId()   

    ##-- If second daughter is photon, try to get daughters from the other particle (W boson)
    elif(daughter1ID==22):
        if(debug): print"found photon daughter 2"  

        WBoson_Cand = particle0_.daughter(0)
        WBoson_Cand = SkipInternalWDecays(WBoson_Cand)
        daughter0ID = WBoson_Cand.daughter(0).pdgId()
        daughter1ID = WBoson_Cand.daughter(1).pdgId()   

    ##-- If neither daughter is a photon, we've succesfully skipped over the WyW vertices 
    else: WBoson_Cand = particle0_ 
    return WBoson_Cand

##-- Function built to circumvent WyW vertices to get W daughters of qq or lnu 
def SkipPhoRadVtxs(particle0,debug):
    WBoson_Cand = SkipPhoRadVtx(particle0,debug)
    tries = 0 
    while(not ((WBoson_Cand.numberOfDaughters()==2) and (WBoson_Cand.daughter(0).pdgId()!=22) and (WBoson_Cand.daughter(1).pdgId()!=22))):
        WBoson_Cand = SkipPhoRadVtx(WBoson_Cand,debug)
        tries += 1 
        if(tries==50): 
            print"Could not remove photon chains after 50 tries"
            print"Exiting"
            exit(1)
    WBoson_ = WBoson_Cand 
    return WBoson_ 

def CreateDataFrame(args_):
    debug = args_.debug     
    datasets = GetDatasets(args_.DatasetBatch)
    printerval = args_.printerval
    for dsetKey in datasets:
        if(debug):
            print "dsetKey:",dsetKey
            print "dsetVal:",datasets[dsetKey]
        inFolder = datasets[dsetKey]
        maxFiles = args_.maxFiles
        files = [] 
        if(dsetKey == "qqlnuSM_2016"): maxFiles *= 5 # 2016: 500 events per file. 17/18: 2500 each 
        maxFiles = int(maxFiles)
        allFiles = [file for file in os.listdir(inFolder) if (file.endswith(".root") and ("inLHE" not in file))]

        shortInFolder = inFolder.replace("/eos/cms/","")     
        for file_i,file in enumerate(allFiles):
            if file_i == maxFiles: break 
            file = file.replace("/eos/cms/","")  
            fnalPath = "root://cmsxrootd.fnal.gov//%s/%s"%(shortInFolder,file)
            files.append(fnalPath)
            
        if(debug): print"Number of input files:",len(files)
        DeltaR = Math.VectorUtil.DeltaR 
        DeltaPhi = Math.VectorUtil.DeltaPhi 
        invmass = Math.VectorUtil.InvariantMass
        genType = args_.genType
        variables = args_.v.split(',')
        singleParticles = args_.sp.split(',')
        NMSSM, EFT, RES, NONRES = 0, 0, 0, 0
        if("NMSSM" in genType and "EFT" in genType):
            print("ERROR - genType cannot contain both NMSSM and EFT")
            print("Exiting")
            exit(1)
        if("NMSSM" in genType): NMSSM = 1 
        elif("EFT" in genType): EFT = 1 
        # elif("RES" in genType): RES = 1 
        elif("NONRES" in genType): NONRES = 1 

        dfOutDirec = "Dataframes/%s"%(genType)
        if(not os.path.exists(dfOutDirec)):
            print"Creating output directory: %s"%(dfOutDirec)
            os.system('mkdir %s'%(dfOutDirec))

        eventsChain = Events(files)
        genHandle = Handle('vector<reco::GenParticle>')
        
        ##-- Pandas dataframe lists 
        doVBF = 0
        d = {}
        # if(doVBF): # particles = ["Lead_H","Sublead_H","Lead_Pho","Sublead_Pho","Lead_q","Sublead_q","Lead_incVBFq","Sublead_incVBFq","Lead_outVBFq","Sublead_outVBFq","lep","nu"] ##-- qqlnu final state 
        particles = ["Lead_H","Sublead_H","Lead_Pho","Sublead_Pho","Lead_q","Sublead_q","lep","nu"] ##-- qqlnu final state 
        if(RES): particles.append("X")
        variables = ["pt","eta","phi","p","px","py","pz","status"]

        is_ZZgg = 1 

        if(is_ZZgg):
            d["invmass_Zqq"] = []
            d["invmass_Zll"] = []
            d["invmass_Znunu"] = []

        # for p in particles:
        #     for v in variables:
        #         columnName = "%s_%s"%(p,v)
        #         d[columnName] = [] 

        d["pdgIds"] = [] 

        ##-- Initialize Special Variables Lists
        # if(doVBF): # for p in ["H","Pho","q","incVBFq","outVBFq"]:

        """

        for p in ["H","Pho","q"]:
            for v in ["invmass","DeltaR"]:
                exec("d['%s%s_%s'] = []"%(p,p,v))

        """

        # non4VecVars = ["status","pdgId"]

        print'Looping events ...'
        time_i = time.time()

        ##-- For Each Event 
        for iev, event in enumerate(eventsChain):
            # filledqq = 0
            if(iev == 0): 
                time_f = time.time()
                total_time = int(time_f) - int(time_i)
                time_mins = float(total_time)/60.
                print"It took %.5g seconds (%.5g minutes) to begin event loop"%(total_time, time_mins)
            if(iev%int(printerval)==0): print'On event:',iev 
            if(iev < int(args_.firstEvent)): continue 
            if(iev == int(args_.nEvents)): 
                print("Reached max desired events")
                break 
            
            event.getByLabel('genParticles',genHandle)
            genParticles = genHandle.product()  
            if(dsetKey == "qqlnuSM_2016"): ps = [p for p in genParticles] ##-- 2016 sample gen particles accessed differently 
            else: ps = [p for p in genParticles if p.isHardProcess()]
            foundFirstPhoton = 0 
            foundFirstQuark = 0
            foundFirstIncVBFQuark = 0
            foundFirstOutVBFQuark = 0
            foundFirstW = 0 
            if(RES or NONRES): foundFirstHiggs = 0
            # phoCount = 0 

            if(is_ZZgg):
                # foundFirstZ1lep = 0
                # foundFirstZ1nu = 0
                # foundFirstZ1q = 0 

                # foundFirstZ2lep = 0
                # foundFirstZ2nu = 0
                # foundFirstZ2q = 0       

                foundFirstZ = 0           


            ##-- For Each Particle Save the genParticle objects of interest 
            nWs = 0
            pdgIds = []

            for ip,particle in enumerate(ps):
                pdgId_val = particle.pdgId() 

                # if(particle.mother(0).pdgId() == 23):
                    # print("pdgId:",pdgId_val)
                # if(pdgId_val == 22 and particle.mother(0).pdgId() == 25): phoCount += 1 

                ##-- Only save pdgID if Z decay, or H/g
                if( (particle.mother(0).pdgId() == 23) or pdgId_val == 25 or pdgId_val == 22 or pdgId_val == 23):
                    pdgIds.append(pdgId_val)   

                if(pdgId_val == 23):
                    if(not foundFirstZ):
                        foundFirstZ = 1 
                        Z1_d1 = particle.daughter(0)
                        Z1_d2 = particle.daughter(1)
                    else:
                        Z2_d1 = particle.daughter(0)
                        Z2_d2 = particle.daughter(1) 



                
                # ##-- Get Z daughters for invariant mass 
                # if(particle.mother(0).pdgId() == 23):
                #     if(abs(pdgId_val) in [11, 13, 15]):
                #         if(not foundFirstZlep):
                #             Zlep_1 = particle 
                #             foundFirstZlep = 1 
                #         else:
                #             Zlep_2 = particle 
                #     elif(abs(pdgId_val) in [12, 14, 16]):
                #         if(not foundFirstZnu):
                #             Znu_1 = particle 
                #             foundFirstZnu = 1 
                #         else:
                #             Znu_2 = particle 
                #     elif(abs(pdgId_val) >=1 and abs(pdgId_val) <= 5):
                #         if(not foundFirstZq):
                #             Zq_1 = particle 
                #             foundFirstZq = 1 
                #         else:
                #             Zq_2 = particle 







                # ##-- Heavy resonance 
                # if(RES): 
                #     if(pdgId_val == 35 or pdgId_val == 39): # Radion, or graviton 
                #         X = particle 

                # ##-- Higgs 
                # if(pdgId_val==25) and (particle.status() >=21 and particle.status() <= 24) and not foundFirstHiggs:
                #     foundFirstHiggs=1
                #     H1 = particle
                # elif(pdgId_val==25) and (particle.status() >=21 and particle.status() <= 24) and foundFirstHiggs:
                #     H2 = particle 

                # ##-- Photons 
                # if(pdgId_val==22) and (particle.mother(0).pdgId() == 25) and not foundFirstPhoton:
                #     foundFirstPhoton=1
                #     Pho1 = particle
                # elif(pdgId_val==22) and (particle.mother(0).pdgId() == 25) and foundFirstPhoton:
                #     Pho2 = particle

                # ##-- W Bosons
                # if(abs(pdgId_val) == 24) and not foundFirstW:
                #     foundFirstW = 1
                #     W1 = particle 
                # elif(abs(pdgId_val) == 24) and foundFirstW:
                #     W2 = particle 

                # ##-- Quarks
                # if(abs(pdgId_val) >=1 and abs(pdgId_val) <= 5): 
                #     motherID = particle.mother(0).pdgId()
                #     if(abs(motherID) == 24): 
                #         if(not foundFirstQuark):
                #             foundFirstQuark = 1
                #             q1 = particle 
                #         elif(foundFirstQuark):
                #             q2 = particle 
                #     ##-- Incoming quarks recoiling off Vector bosons 
                #     else:

                #         if(doVBF):
                #             # if(debug): 
                #                 # print("Mother ID:",motherID)
                #                 # print"status:",particle.status()
                #             if(particle.status()==21):
                #                 if(not foundFirstIncVBFQuark):
                #                     if(debug): print("Found first inc VBF quark")
                #                     foundFirstIncVBFQuark = 1
                #                     incVBFq1 = particle 
                #                 elif(foundFirstIncVBFQuark):
                #                     if(debug): print("Found second inc VBF quark")
                #                     incVBFq2 = particle     
                #             elif(particle.status()==23):
                #                 if(not foundFirstOutVBFQuark):
                #                     if(debug): print("Found first out VBF quark")
                #                     foundFirstOutVBFQuark = 1
                #                     outVBFq1 = particle 
                #                 elif(foundFirstOutVBFQuark):
                #                     if(debug): print("Found second out VBF quark")
                #                     outVBFq2 = particle      
                #             else: 
                #                 print("quark status is not 21 or 23:")
                #                 print("status:",particle.status())
                #                 print("Mother ID:",motherID)

                # ##-- Lepton 
                # elif(abs(pdgId_val) == 11 or abs(pdgId_val) == 13 or abs(pdgId_val) == 15): lep = particle 

                # ##-- Neutrino 
                # elif(abs(pdgId_val) == 12 or abs(pdgId_val) == 14 or abs(pdgId_val) == 16): nu = particle  





            # if(doVBF): 
                # if(pdgIds.count(21)>0): 
                #     print("pdgId count of 21 > 0")
                #     print("pdgIds:",pdgIds)
                #     print("Skipping event")
                #     continue ## couldn't get VBF quarks in this case 

            """

            if(RES or NONRES):

                # print"Higgs pdgIds:",H1.pdgId(), H2.pdgId()
                # print"Photon pdgIds:",Pho1.pdgId(), Pho2.pdgId()
                # print"Quark pdgIds:",q1.pdgId(), q2.pdgId()
                # print"Lepton pdgId:",lep.pdgId()
                # print"neutrino pdgId:",nu.pdgId()

                ##-- Determine Leading, Subleading particles, save variables 
                # if(doVBF): for p in ["H","Pho","q","incVBFq","outVBFq"]:


                for p in ["H","Pho","q"]:
                    p1 = eval("%s1"%(p)) 
                    p2 = eval("%s2"%(p))                                       
                    if(p1.pt() > p2.pt()):
                        exec("Lead_%s = p1"%(p))
                        exec("Sublead_%s = p2"%(p))
                    elif(p2.pt() > p1.pt()):
                        exec("Lead_%s = p2"%(p))
                        exec("Sublead_%s = p1"%(p))   
                    else:
                        exec("Lead_%s = p1"%(p))
                        exec("Sublead_%s = p2"%(p))  
                    for v in variables:
                        if(v == "status"): continue 
                        if(v == "p"): 
                            lvExp = "sqrt(Lead_%s.p4().px()*Lead_%s.p4().px() + Lead_%s.p4().py()*Lead_%s.p4().py() + Lead_%s.p4().pz()*Lead_%s.p4().pz())"%(p,p,p,p,p,p)
                            slvExp = "sqrt(Sublead_%s.p4().px()*Sublead_%s.p4().px() + Sublead_%s.p4().py()*Sublead_%s.p4().py() + Sublead_%s.p4().pz()*Sublead_%s.p4().pz())"%(p,p,p,p,p,p)
                        else: 
                            lvExp = "Lead_%s.p4().%s()"%(p,v) # leading variable expression                  
                            slvExp = "Sublead_%s.p4().%s()"%(p,v) # subleading variable expression                         
                        exec("Lead_%s_%s = %s"%(p,v,lvExp))
                        exec("d['Lead_%s_%s'].append(Lead_%s_%s)"%(p,v,p,v))      
                        exec("Sublead_%s_%s = %s"%(p,v,slvExp))
                        exec("d['Sublead_%s_%s'].append(Sublead_%s_%s)"%(p,v,p,v)) 
                    exec("Lead_%s_status = Lead_%s.status()"%(p,p))
                    exec("d['Lead_%s_status'].append(Lead_%s_status)"%(p,p))      
                    exec("Sublead_%s_status = Sublead_%s.status()"%(p,p))
                    exec("d['Sublead_%s_status'].append(Sublead_%s_status)"%(p,p))      

                pNames = ["lep","nu"]
                if(RES): pNames.append("X")
                for pName in pNames:
                    p = eval(pName)
                    for v in variables:
                        if(v == "status"): continue 
                        if(v == "p"): vExp = "sqrt(p.p4().px()**2 + p.p4().py()**2 + p.p4().pz()**2)"
                        else: vExp = "p.p4().%s()"%(v) 
                        exec("%s_%s = %s"%(pName,v,vExp))
                        exec("d['%s_%s'].append(%s_%s)"%(pName,v,pName,v))
                    exec("%s_status = p.status()"%(pName))
                    exec("d['%s_status'].append(%s_status)"%(pName,pName))                    

                ##-- Compute and append special variables   
                # if(doVBF): for p in ["H","Pho","q","incVBFq","outVBFq"]:
                for p in ["H","Pho","q"]:
                    for v in ["invmass","DeltaR"]:
                        exec("%s%s_%s = %s(Lead_%s.p4(),Sublead_%s.p4())"%(p,p,v,v,p,p))                                                              
                        exec("d['%s%s_%s'].append(%s%s_%s)"%(p,p,v,p,p,v)) 
            """

            if(is_ZZgg):
                absIDs = [abs(id_i) for id_i in pdgIds]

                ##-- Z1 mass 


                print("absIDs:",absIDs)
                # if( (absIDs.count(11) + absIDs.count(13) + absIDs.count(15)) == 2 ):
                #     m = invmass(Zlep_1.p4(), Zlep_2.p4())
                #     d["invmass_Zll"].append(m)
                #     d["invmass_Znunu"].append(-99)
                #     d["invmass_Zqq"].append(-99)
                # elif( (absIDs.count(12) + absIDs.count(14) + absIDs.count(16)) == 2 ):
                #     m = invmass(Znu_1.p4(), Znu_2.p4())
                #     d["invmass_Zll"].append(-99)
                #     d["invmass_Znunu"].append(m)
                #     d["invmass_Zqq"].append(-99)   
                # elif( (absIDs.count(1) + absIDs.count(2) + absIDs.count(3) + absIDs.count(4) + absIDs.count(5)) == 2 ):
                #     m = invmass(Zq_1.p4(), Zq_2.p4())
                #     d["invmass_Zll"].append(-99)
                #     d["invmass_Znunu"].append(-99)
                #     d["invmass_Zqq"].append(m)                                      

            ##- Save pdgIds to dataframe 
            # if(len(pdgIds) != 10):
                # print("len(pdgIds):",len(pdgIds))
            d['pdgIds'].append(pdgIds)

            if(is_ZZgg):
                print("len(d['pdgIds']:",len(d['pdgIds']))
                print("len(d['invmass_Z1ll']:",len(d['invmass_Z1ll']))
                print("len(d['invmass_Z1nunu']:",len(d['invmass_Z1nunu']))
                print("len(d['invmass_Z1qq']:",len(d['invmass_Z1qq']))
                print("len(d['invmass_Z2ll']:",len(d['invmass_Z2ll']))
                print("len(d['invmass_Z2nunu']:",len(d['invmass_Z2nunu']))
                print("len(d['invmass_Z2qq']:",len(d['invmass_Z2qq']))                

            #if(debug): 
                #if(not filledqq): print"---------------------Did not fill mqq"

        if(debug):
            for p in particles:
                for v in variables:
                    columnName = "%s_%s"%(p,v)
                    print"len(%s):"%(columnName),len(d[columnName])
            # print"len('HH_invm'):",len(d['HH_invm'])
            # print"len('qq_invm'):",len(d['qq_invm'])
        
        df = pd.DataFrame(data=d)
        print df 
        # print df["VBFqVBFq_invmass"]
        dfOutName = args_.dfOutName
        dfOutName = dfOutName.replace("{node}",dsetKey)
        pickle.dump( df, open( "Dataframes/%s/%s.p"%(genType,dfOutName), "wb" ))
        if(args_.condor): 
            print "Copying file from condor to afs"
            outFilePath = "%s/%s.p"%(genType,dfOutName)
            os.system('cp Dataframes/%s /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/Plot/GEN/CondorOutputFiles/'%(outFilePath))

    print("DONE")
