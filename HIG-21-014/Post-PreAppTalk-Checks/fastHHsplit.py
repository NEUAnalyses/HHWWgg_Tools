import os 
nodes = [str(i) for i in range(1,21)]
for node in nodes:
    c = "python3 Reweight_NLO.py --reweightNode {node} --syst Nominal --TDirec '' --evenOddSplit --additionalSF --fromTree".format(node=node)
    print("$",c)
    os.system(c)