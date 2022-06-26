"""
7 December 2021 
Abraham Tishelman-Charny 

The purpose of this script is to save time by hadding over 20 nodes in parallel over HTCondor.
"""

import os 

if(not os.path.isdir('error')): os.mkdir('error') 
if(not os.path.isdir('output')): os.mkdir('output') 
if(not os.path.isdir('log')): os.mkdir('log') 

scriptName = "condor_job.txt"

condor = ''' executable              = run_script.sh
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

NODE=$1
LOCAL="/eos/user/c/chuw/ForAbe/HIG-21-014_Reweighting_Semileptonic/2018/"
cd ${LOCAL}
#python hadd.py --nodes ${NODE} --year 2017 
python hadd.py --nodes ${NODE} 
echo -e "DONE";
'''

arguments = []
nodes = [11,12,13,14,15,16,17,18,19,20]
for node in nodes:
  arguments.append("{}".format(node))

with open("arguments.txt", "w") as args:
  args.write("\n".join(arguments))

with open("run_script.sh", "w") as rs:
  rs.write(script)

submitCommand = "condor_submit {scriptName}".format(scriptName=scriptName)
print("$ {submitCommand}".format(submitCommand=submitCommand))
os.system(submitCommand)
print("DONE")
