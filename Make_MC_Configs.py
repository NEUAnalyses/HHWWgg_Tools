# Abe Tishelman-Charny
# 5 December 2019 
# The purpose of this module is to create an MC_Configs.json file to run with . main.sh

import os 
# import subprocess

outputName = 'MC_Configs.json' # output json file path 

# Begin writing file 
MC_Configs = '[' 

# Object key values

## GEN-SIM Setup Example 

# step = "GEN-SIM"
# nEvents = 100
# jobs_jobsize = 1
# masses = [250]
# finalStates = ["qqlnugg"]

## Setup for fully leptonic GEN-SIM production 
step = "GEN-SIM"
nEvents = 1000
jobs_jobsize = 1
masses = [250]
# masses = [260, 270, 280, 300, 320, 350, 400, 500, 550, 600, 650, 700, 800, 850, 900, 1000]
finalStates = ["lnulnugg"]

postGEN = 0 

if(postGEN):

	## DR1, DR2 and MINIAOD setup example
	# step = "MINIAOD" # can also put "DR2" or "MINIAOD" here 
	# prevStep_prefix = "wPU_DR2" # if step == DR1: this = GEN-SIM. if step == DR2 with pileup: this = wPU_DR1 
	# nEvents = 100000 
	# jobs_jobsize = 1 
	# directory_prefix = "/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/" # location of GEN-SIM, DR1 or DR2 output files 
	# pileup = "wPU"
	# masses = ['X260', 'X270', 'X280', 'X300', 'X320', 'X350', 'X400', 'X500', 'X550', 'X600', 'X650', 'X700', 'X800', 'X850', 'X900', 'X1000']
	# finalStates = ["qqlnugg"]

	## Fully leptonic DR1 production example
	## DR1, DR2 and MINIAOD setup example
	# step = "DR1" # can also put "DR2" or "MINIAOD" here 
	# nEvents = 100000 
	# jobs_jobsize = 1 
	# directory_prefix = "/path/to/GEN-SIM/output" # location of GEN-SIM, DR1 or DR2 output files. Should contain directories with names like ggF_X260_WWgg_lnulnugg, ggF_X280_WWgg_lnulnugg, etc. 
	# pileup = "wPU"
	# masses = ['X260', 'X270', 'X280', 'X300', 'X320', 'X350', 'X400', 'X500', 'X550', 'X600', 'X650', 'X700', 'X800', 'X850', 'X900', 'X1000']
	# finalStates = ["lnulnugg"]

	dir_list = os.listdir(directory_prefix) 
	
	# print("Files and directories in '", directory_prefix, "' :")  
	
	# print the list 
	# print(dir_list) 

	# masses = [260, 270, 280, 300, 320, 350, 400, 500, 550, 600, 650, 700, 800, 850, 900, 1000]

	directories = [] 
	i = 0 
	for dir in dir_list:
		dir_mass, dir_fstate = str(dir).split('_')[1], str(dir).split('_')[3]
		# print 'dir = ',dir 	
		# print 'dir_mass = ',dir_mass
		# print 'dir_fstate = ',dir_fstate
		if dir_mass in masses and dir_fstate in finalStates:
			direc = directory_prefix 
			direc += dir 
			for sndDirec in os.listdir(direc):
				# print 'sndDirec = ',sndDireci
				#print'prevStep_prefix = ',prevStep_prefix
				if str(sndDirec) == str(nEvents) + 'events_' + prevStep_prefix: 
					direc += '/'
					direc += (sndDirec)
					# print'direc = ',direc 
					newestDir = sorted(os.listdir(direc))[-1] # take latest crab job output in this direc 
					direc += '/' 
					direc += newestDir
					direc += '/'
					direc += '0000/'
					print'Found direc: ',direc 
					cmd = 'ls -1 '
					cmd += direc
					cmd += ' | wc -l'
					print 'Number of files in direc: ',os.system(cmd) 
					directories.append(direc)

## Create json objects 

# GEN-SIM step 
if step == "GEN-SIM":
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

## if the step is DR1, DR2 or MINIAOD, you need a different config type 
## DR1, DR2, or MINIAOD step 
else:
	for id,directory in enumerate(directories):
			MC_Configs_Entry = '''
			{ 
					"step"      : "{step}",
					"events"    : {events},
					"jobs_jobsize"      : {jobs_jobsize},
					"fragment_directory"  : "{directory}",
					"pileup"              : "wPU" 
			}'''

			MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
			MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
			MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
			MC_Configs_Entry = MC_Configs_Entry.replace("{directory}",str(directory))
			MC_Configs += MC_Configs_Entry

			if id is not len(directories)-1: MC_Configs += ',' # need comma separation 
			else: continue # no comma at end of last object 

	MC_Configs += '\n]\n' # finish json 

	with open(outputName, "w") as output:
			output.write(MC_Configs) # write json file 

print 
print'[Make_MC_Configs] - MC_Configs.json created'
print'[Make_MC_Configs] - Make sure MC_Configs.json looks good before submitting with . main.sh !' 
print 
