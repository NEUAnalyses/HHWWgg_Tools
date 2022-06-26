"""
29 July 2021 
Abraham Tishelman-Charny 

The purpose of this module is to privately produce MC either locally or 
on CRAB.

Example usage:

python Submit.py 
"""

"""
Start with 1k GEN events of:
gluongluon-->Spin-0(250)-->HH-->WWyy-->qqqqyy 

Need:
- cmssw setup script 
- pythia fragment 
- gridpack location 
- cmsDriver command 

Notes:
HIG-RunIISummer19UL17wmLHEGEN-00664 
"""

import os 


# Following prep_id B2G-RunIISummer20UL17MiniAOD-00765

# LHE step 
# B2G-RunIISummer20UL17wmLHEGEN-01293


# # LHEGEN step 
# COMMAND = "./HIG-RunIISummer19UL17wmLHEGEN-00664_setup.sh" # chmod u=rwx HIG-RunIISummer19UL17wmLHEGEN-00664_setup.sh
# print(COMMAND)
# os.system(COMMAND)

# os.chdir("CMSSW_10_6_9/src")
# os.system("pwd")

# Proc_Name = "GluGluToRadionToHHTo2G2WTo2G4Q_M-250_narrow_13TeV_madgraph_pythia8"
# cmsDriver_command = "cmsDriver.py Configuration/GenProduction/python/%s-fragment.py --python_filename %s_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN,LHE --fileout file:%s.root --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN --geometry DB:Extended --era Run2_2017 --no_exec --mc -n 10"%(Proc_Name, Proc_Name, Proc_Name)
# print(cmsDriver_command)
# # os.system("cmsenv")
# # os.system(cmsDriver_command)

# # SIM step from HIG-RunIISummer19UL17SIM-00545
# COMMAND = "./HIG-RunIISummer19UL17SIM-00545_setup.sh" 
# print(COMMAND)
# os.system(COMMAND)

# # cmsDriver_command = 'cmsDriver.py --python_filename HIG-RunIISummer19UL17SIM-00545_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:HIG-RunIISummer19UL17SIM-00545.root --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step SIM --geometry DB:Extended --filein "dbs:/GluGluToBulkGravitonToHHTo2B2G_M-1000_narrow_TuneCP5_13TeV-madgraph-pythia8/RunIISummer19UL17wmLHEGEN-106X_mc2017_realistic_v6-v1/GEN" --era Run2_2017 --runUnscheduled --no_exec --mc -n 10'
# cmsDriver_command = 'cmsDriver.py --python_filename HIG-RunIISummer19UL17SIM-00545_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:HIG-RunIISummer19UL17SIM-00545.root --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step SIM --geometry DB:Extended --filein "dbs:/GluGluToBulkGravitonToHHTo2B2G_M-1000_narrow_TuneCP5_13TeV-madgraph-pythia8/RunIISummer19UL17wmLHEGEN-106X_mc2017_realistic_v6-v1/GEN" --era Run2_2017 --runUnscheduled --no_exec --mc -n 10'
# print(cmsDriver_command)

# cmsDriver.py --python_filename HIG-RunIISummer19UL17SIM-00545_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:HIG-RunIISummer19UL17SIM-00545.root --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step SIM --geometry DB:Extended --filein file:CMSSW_10_6_9/src/GluGluToRadionToHHTo2G2WTo2G4Q_M-250_narrow_13TeV_madgraph_pythia8.root --era Run2_2017 --runUnscheduled --no_exec --mc -n 10

# DIGI premix HIG-RunIISummer19UL17DIGIPremix-00434
# COMMAND = "./HIG-RunIISummer19UL17DIGIPremix-00434_setup.sh" 
# print(COMMAND)
# os.system(COMMAND)

# cmsDriver_command = 'cmsDriver.py  --python_filename HIG-RunIISummer19UL17DIGIPremix-00434_1_cfg.py --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --fileout file:HIG-RunIISummer19UL17DIGIPremix-00434.root --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer19ULPrePremix-UL17_106X_mc2017_realistic_v6-v1/PREMIX" --conditions 106X_mc2017_realistic_v6 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --filein file:HIG-RunIISummer19UL17SIM-00545.root --datamix PreMix --era Run2_2017 --runUnscheduled --no_exec --mc -n 10 > /dev/null' # do not output the many many pileup files names
# print(cmsDriver_command)