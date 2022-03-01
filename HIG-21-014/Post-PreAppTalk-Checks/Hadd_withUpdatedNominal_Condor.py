"""
7 December 2021 
Abraham Tishelman-Charny 

The purpose of this script is to save time by hadding over 20 nodes in parallel over HTCondor.

Example commands to run:

python Hadd_withUpdatedNominal_Condor.py --nodes 1 --years 2016

python Hadd_withUpdatedNominal_Condor.py --nodes 2 --years 2017
python Hadd_withUpdatedNominal_Condor.py --nodes 12,14,15,16 --years 2016
python Hadd_withUpdatedNominal_Condor.py --nodes 5,6,14 --years 2018
python Hadd_withUpdatedNominal_Condor.py --nodes 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 --years 2016

"""

import os 
import argparse 
from SystematicTreeNames import GetSystLabels

parser =  argparse.ArgumentParser()
parser.add_argument('--nodes',default = "NO_NODES", required=True, type=str, help = "Comma separated list of nodes to run on")
parser.add_argument('--years',default = "NO_YEARS", required=True, type=str, help = "Comma separated list of years of CMS conditions to run")

args = parser.parse_args()

nodes = args.nodes.split(',')
years = args.years.split(',')

if(not os.path.isdir('error')): os.mkdir('error') 
if(not os.path.isdir('output')): os.mkdir('output') 
if(not os.path.isdir('log')): os.mkdir('log') 

scriptName = "condor_job.txt"

condor = ''' executable              = run_script.sh
output                  = output/$(ClusterId).$(ProcId).out
error                   = error/$(ClusterId).$(ProcId).err
log                     = log/$(ClusterId).log
transfer_input_files    = run_script.sh
    
+JobFlavour             = "longlunch"
queue arguments from arguments.txt
'''

with open(scriptName, "w") as cnd_out:
  cnd_out.write(condor)

script = '''#!/bin/sh -e

LOCAL="/afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/HIG-21-014/Post-PreAppTalk-Checks/"
NODE=$1
YEAR=$2
SYSTLABEL=$3
cd ${LOCAL}
python Hadd_withUpdatedNominal.py --node ${NODE} --year ${YEAR} --verbose --syst ${SYSTLABEL}
echo -e "DONE";
'''

arguments = []

for node in nodes:
  for year in years:
    systLabels = GetSystLabels(year)
    print("systematic labels:",systLabels)    
    for systLabel in systLabels:
      # Skip nominal tree for this process
      if(systLabel == "Nominal"): continue 
      arguments.append("{} {} {}".format(node, year, systLabel))

with open("arguments.txt", "w") as args:
  args.write("\n".join(arguments))

with open("run_script.sh", "w") as rs:
  rs.write(script)

submitCommand = "condor_submit {scriptName}".format(scriptName=scriptName)
print("$ {submitCommand}".format(submitCommand=submitCommand))
os.system(submitCommand)
print("DONE")
