import os 
from SystematicTreeNames import GetSystLabels
# nodes = [str(i) for i in range(1,21)]
nodes = ["1"] # should be irrelevant for SM categorization 
# years = ["2016", "2017", "2018"]
years = ["2018"]
procs = ["VHToGG", "ttHJetToGG"]
# procs = ["GluGluHToGG"]
# nodes = ["1"]
# years = ["2016"]
for year in years:
    systLabels = GetSystLabels(year)
    nSyst = len(systLabels)    
    print("nSyst:",nSyst)
    for node in nodes:
        for proc in procs:
            for systLabel in systLabels:
                CMD = "python Reweight_NLO.py --reweightNode {node} --year {year} --syst {systLabel} --TDirec '' --categorize --Single_Higgs --Single_Higgs_File {proc} --inDir 'NoinDir'".format(node=node, year=year, proc=proc, systLabel=systLabel)
                print("$",CMD)
                os.system(CMD)