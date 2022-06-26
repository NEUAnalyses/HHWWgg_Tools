import os 
nodes = [str(i) for i in range(1,21)]
years = ["2016", "2018"]
for year in years:
    for node in nodes:
        CMD = "python Reweight_NLO.py --reweightNode {node} --year {year} --syst Nominal --TDirec '' --categorize --isData".format(node=node, year=year)
        print("$",CMD)
        os.system(CMD)