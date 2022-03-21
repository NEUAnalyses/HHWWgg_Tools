"""
25 November 2021
Abraham Tishelman-Charny 

The purpose of this dummy python module is to serve as an example process to be run over HTCondor. 
"""

import argparse 
import pickle 

parser = argparse.ArgumentParser()
parser.add_argument("--InputParameter", type = float, help = "Dummy input parameter to be passed through python command run over HTCondor")
parser.add_argument("--condor", action = "store_true", help = "Run over HTCondor")
args = parser.parse_args()

InputParameter = args.InputParameter 
condor = args.condor 

# change import location based on running over condor or not 
if(condor): 
    from DummyPythonModule_Tools import MultiplyParameter
else:
    from python.DummyPythonModule_Tools import MultiplyParameter # make sure __init__.py file exists in python directory

print("Running DummyPythonModule")
print("Input parameter: ",InputParameter)
newValue = MultiplyParameter(InputParameter)
print("newValue:",newValue)

# just to test transfer of output files, save newValue as a pickle file 
pickle.dump( newValue, open( 'DummyValue.p', "wb" ))  # on condor, this then gets transferred from the condor area to your output location     

print("Done running DummyPythonModule")
