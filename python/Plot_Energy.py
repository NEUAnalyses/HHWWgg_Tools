# The purpose of this file is to plot ECAL energy vs. DOF1 vs. DOF2 from a MINIAOD
# Because the MINIAOD has ID instead of DOF information, need to use a dictionary to convert ID to DOF1 and 2 

from ROOT import TH2F, TH1F, TChain, TCut  
import pickle 

# Open dictionary  
pickle_in = open("ID_DOF_Map.pkl","rb")
ID_DOF_Map = pickle.load(pickle_in)

#print ID_DOF_Map

# Open root file 

file_loc='/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X1250_WWgg_lnulnugg/100000events_wPU_MINIAOD/190403_092057/0000/ggF_X1250_WWgg_lnulnugg_100000events_wPU_MINIAOD_88.root'
ch = TChain('Events') 
#var = 'EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_:EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_:EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_'
#var = 'EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.energy_'
var = 'EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_PAT.obj.obj.id_.id_'
ch.Add(file_loc)
hname1 = 'hname'
hid = 'hname'
params = [100,0,100,100,0,100]

#h1 = TH2F(hname1, hid, params[0], params[1], params[2], params[3], params[4], params[5])
h1 = TH1F(hname1, hid, params[0], params[1], params[2])
#h1.SetDirectory(0)
ch.Draw(var +'>>'+hname1,TCut(''),"COLZ")
#print 'h1 = ',h1
print 'h1.GetEntries() = ',h1.GetEntries() # Tells you if the histogram was actually filled 

values = int(h1.GetEntries())
# For each entry, turn id into DOF1, DOF2 

for event in h1:
    print 'event = ',event 

# for i in range(values):
    # print 'entry = ',h1.GetBinContent(i)

h1.SaveAs("output.root")