# Abraham Tishelman-Charny
# 15 February 2021
#
# The purpose of this python module is to remove Unconstraned parameters from higgs combine impact jsons in order to plot impacts without unconstrained parameters
#
# Example Usage:
#
# python ManipulateJson.py --Plot
#

import json 
import os
import argparse 

parser = argparse.ArgumentParser()

parser.add_argument("--RemoveUnconstrained",action="store_true")
parser.add_argument("--Plot",action="store_true")

args = parser.parse_args()

direc = "jsonsOnly"
files = ["%s/%s"%(direc,file) for file in os.listdir(direc)]
print files
ol = "/afs/cern.ch/work/a/atishelm/private/AN-20-165/Images/Impacts/"

for file in files:
  fileName = file.split('/')[-1].split('.')[0]
  outFilePath = "JsonsNoUnconstrained/%s_noUnconstrained.json"%(fileName)

  if(args.RemoveUnconstrained):
    ##-- Read Impact Json
    with open(file,"r") as impacts:
      impacts_info = json.load(impacts)
    Nparams = len(impacts_info["params"])
    print"Nparams:",Nparams

    ##-- Locate Unconstrained Params
    params_to_remove = []
    for param_i in range(0,Nparams):
      param_info = impacts_info["params"][param_i]
      if(param_info["type"] == "Unconstrained"):
        params_to_remove.append(param_i)
        print"Removing param:",param_i

    params_to_remove.reverse() ## to avoid trying to delete not accessible element (already removed elements, shortens length of dictionary)

    ##-- Remove Unconstrained Params
    for param_to_remove in params_to_remove:
      print"removing param:",param_to_remove
      #print json.dumps(impacts_info["params"][param_to_remove], indent=4)
      del(impacts_info["params"][param_to_remove])

    ##-- Save updated impacts info as new json 
    with open(outFilePath,"w") as updatedJson:
      json.dump(impacts_info, updatedJson)
  if(args.Plot):
    outFileName = outFilePath.replace(".json","")
    PLOT_COMMAND = "plotImpacts.py -i %s -o Impacts_%s "%(outFilePath, fileName)
    print"PLOT_COMMAND:",PLOT_COMMAND
    os.system(PLOT_COMMAND)
    COPY_COMMAND = "cp Impacts_%s.pdf /eos/user/a/atishelm/www/HHWWgg/January-2021-Production/Results/Impacts/"%(fileName)
    COPY_COMMAND_2 = "cp Impacts_%s.pdf %s/"%(fileName,ol)
    print"COPY_COMMAND:",COPY_COMMAND
    os.system(COPY_COMMAND)
    os.system(COPY_COMMAND_2)
