# The purpose of this file is to create a dictionary of ECAL XTAL ID->DOF1,DOF2
# Where for EB: (DOF1,DOF2) = (ieta, iphi), EE: (DOF1,DOF2) = (ix, iy)

import csv
import pickle 

ID_DOF_Map={} # dictionary 
i = 0
ID = 0
DOF1 = 0
DOF2 = 0
fname = '/afs/cern.ch/work/a/atishelm/private/CMSSW_9_4_9/src/newclone/ecall1algooptimization/PulseShapeWeights/ComputeWeights/data/Full_DOF.txt'
with open(fname,'r') as tsv:
    for line in csv.reader(tsv, delimiter="\t"):
        # Skip first line 
        if (i == 0): 
            i += 1
            continue 
        #print 'line = ',line
        ID = line[0]
        DOF1 = line[5]
        DOF2 = line[6]
        #print 'ID = ',ID
        #print 'DOF1 = ',DOF1
        #print 'DOF2 = ',DOF2
        ID_DOF_Map[ID]=[DOF1,DOF2]
        #for item in line:
            #print 'item = ',item 
        i += 1
        if i == 10: break 
        
print "ID_DOF_Map = ",ID_DOF_Map

# Save dictionary 

ff = open("ID_DOF_Map.pkl","wb")
pickle.dump(ID_DOF_Map,ff)
ff.close()
