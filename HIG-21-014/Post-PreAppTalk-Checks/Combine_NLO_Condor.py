"""
10 November 2021
Abraham Tishelman-Charny 

The purpose of this module is to parallelize the combination of 4 NLO nodes for HIG-21-014 reweighting, running over 4 NLO nodes (cHHH0, cHHH1, cHHH2p45, cHHH5) and 3 years (2016, 2017, 2018) at once. 

Example usage:
python Combine_NLO_Condor.py --nodes cHHH1 --years 2016

"""

#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
import itertools
import argparse
import operator
import os

if __name__ == '__main__':

  parser =  argparse.ArgumentParser()
  parser.add_argument('--nodes',default = "cHHH1", required=False, type=str, help = "Comma separated list of nodes to run")
  parser.add_argument('--years',default = "2017", required=False, type=str, help = "Comma separated list of years to run")
  args = parser.parse_args()

  nodes = args.nodes.split(',')
  years = args.years.split(',')

  scriptName = "condor_job.txt"

  print("nodes:",nodes)
  print("years:",years)

  local = os.getcwd()
  if not os.path.isdir('error'): os.mkdir('error') 
  if not os.path.isdir('output'): os.mkdir('output') 
  if not os.path.isdir('log'): os.mkdir('log') 
   
  # Prepare condor jobs
  condor = '''executable              = run_script.sh
output                  = output/$(ClusterId).$(ProcId).out
error                   = error/$(ClusterId).$(ProcId).err
log                     = log/$(ClusterId).log
transfer_input_files    = run_script.sh
    
+JobFlavour             = "microcentury"
queue arguments from arguments.txt
'''

  with open(scriptName, "w") as cnd_out:
     cnd_out.write(condor)

  script = '''#!/bin/sh -e

LOCAL=$1
NODE=$2
YEAR=$3

echo -e "Combining NLO samples for node ${NODE}, year ${YEAR}..."
python ${LOCAL}/Combine_NLO.py --node ${NODE} --year ${YEAR}

echo -e "DONE";
'''

  arguments = []
  
  for year in years:
    for node in nodes:
      arguments.append("{} {} {}".format(local, node, year))

  # Save arguments to text file to be input for condor jobs 
  with open("arguments.txt", "w") as args:
    args.write("\n".join(arguments))

  with open("run_script.sh", "w") as rs:
    rs.write(script) 

  submitCommand = "condor_submit {scriptName}".format(scriptName=scriptName)
  print("$ {submitCommand}".format(submitCommand=submitCommand))
  os.system(submitCommand)
  print("DONE")