# Abe Tishelman-Charny
# 5 December 2019 
# The purpose of this module is to create an MC_Configs.json file to run with . main.sh

outputName = 'MC_Configs.json' # output json file path 

# Begin writing file 
MC_Configs = '[' 

# Object key values
step = "GEN-SIM"
nEvents = 100
jobs_jobsize = 1
masses = [250]
finalStates = ["qqlnugg"]

## Setup for fully leptonic GEN-SIM production 
# step = "GEN-SIM"
# nEvents = 100000
# jobs_jobsize = 200
# masses = [260, 270, 280, 300, 320, 350, 400, 500, 550, 600, 650, 700, 800, 850, 900, 1000]
# finalStates = ["lnulnugg"]

# Create json objects 
for im,mass in enumerate(masses):
  for ifs,finalState in enumerate(finalStates):

		# Indentation of text chosen for visual output
		MC_Configs_Entry = '''
    { 
        "step"      : "{step}",
        "events"    : {events},
        "jobs_jobsize"      : {jobs_jobsize},
        "fragment_directory"  : "ggF_X{mass}_WWgg_{finalState}",
        "pileup"              : "wPU" 
    }'''

		MC_Configs_Entry = MC_Configs_Entry.replace("{mass}",str(mass))
		MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
		MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
		MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
		MC_Configs_Entry = MC_Configs_Entry.replace("{finalState}",str(finalState))
		MC_Configs += MC_Configs_Entry

		if im is not len(masses)-1: MC_Configs += ',' # need comma separation 
		else: continue # no comma at end of last object 

MC_Configs += '\n]\n' # finish json 

with open(outputName, "w") as output:
    output.write(MC_Configs) # write json file 
