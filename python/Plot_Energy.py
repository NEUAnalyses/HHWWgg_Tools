# The purpose of this file is to plot ECAL energy vs. DOF1 vs. DOF2 from a MINIAOD
# Because the MINIAOD has ID instead of DOF information, need to use a dictionary to convert ID to DOF1 and 2 

import pickle 

# Open dictionary  
pickle_in = open("ID_DOF_Map.pkl","rb")
ID_DOF_Map = pickle.load(pickle_in)

# print ID_DOF_Map

# Open root file 

