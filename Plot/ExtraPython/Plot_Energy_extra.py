# The purpose of this file is to plot ECAL energy vs. DOF1 vs. DOF2 from a MINIAOD
# Because the MINIAOD has ID instead of DOF information, need to use a dictionary to convert ID to DOF1 and 2 

#from ROOT import TH2F, TH1F, TChain, TCut 
#from ROOT import *  
from ROOT import TTree, TFile 
import pickle 

# Open dictionary  
pickle_in = open("ID_DOF_Map.pkl","rb")
ID_DOF_Map = pickle.load(pickle_in)

#print ID_DOF_Map

# Open root file 


file_loc='/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X1250_WWgg_lnulnugg/100000events_wPU_MINIAOD/190403_092057/0000/ggF_X1250_WWgg_lnulnugg_100000events_wPU_MINIAOD_88.root'
f = TFile.Open(file_loc)
total_num_events = f.Events.GetEntries()
print 'total_num_events = ',total_num_events
Etree = f.Get("Events")
Etree.GetEntry(0)
b = Etree.GetBranch("EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_")
# print 'b = ',b.Print()

for event in f.Events:
    print 'hello'

#idval = Etree.EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_()
#IDTree = f.Get("EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_")

#t = f.Get("Events")
#b = t.GetBranch("EcalRecHitsSorted_reducedEgamma_reducedESRecHits_PAT.obj.obj.id_.id_")

# for iev in xrange(t.GetEntries()): 
#     t.GetEntry(iev)
#     value = getattr(t, 'EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_')
#     print 'value = ',value 

# #for event in f.Events: 
# for event in f.Events: 
#     #print event.EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.energy_
#     print 'hello'
#     print event.EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_



#print 'numevents = ', f.Events.GetEntries()

#for event in f.Events.EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.energy_:
#tree = TTree("a","a",f.Get("Events/EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT/obj/obj/id_/energy_"))
#val = f.Events.GetEntries()

#etree = f.Get("Events")




# print 'tree = ',tree

# for i in range(val):
#     print 'hello'
#     print etree.GetEntry(i)
#     print 'thing = ',tree.GetEntry(0) 
# tree.GetEntry(0)
# val = tree.EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT
# val = val2.obj
# print'val = ',tree.Print()
# print tree.GetEntry(0)
# for event in f.Events.EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT:
# for event in tree.GetEntry(): 
#     print 'hello'

# tree = f.Get("Events")
# tree.GetEntry(0)
# val = tree.EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.energy_
# print 'val = ',val 

# i = 0
# for ev in tree.GetEntry():
# for ev in tree:
    # print'i = ',i
    # i += 1

#i = 0
# for event in f.Events: 
    #print 'hello'
    # print"i = ",i
    #i+=1
    #val = event.EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.energy_
    #print 'val = ',val 


# ch = TChain('Events') 
# #var = 'EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_:EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_:EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_'
# #var = 'EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.energy_'
# var = 'EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_'
# ch.Add(file_loc)
# hname1 = 'hname'
# hid = 'hname'
# params = [100,0,100,100,0,100]

# #h1 = TH2F(hname1, hid, params[0], params[1], params[2], params[3], params[4], params[5])
# h1 = TH1F(hname1, hid, params[0], params[1], params[2])
# #h1.SetDirectory(0)
# ch.Draw(var +'>>'+hname1,TCut(''),"COLZ")
# #print 'h1 = ',h1
# print 'h1.GetEntries() = ',h1.GetEntries() # Tells you if the histogram was actually filled 

# values = int(h1.GetEntries())
# For each entry, turn id into DOF1, DOF2 



#for event in h1:
    #print 'event = ',event 

# for i in range(values):
#     print 'entry = ',h1.GetXaxis().GetBinContent(i)

# h1.SaveAs("output.root")