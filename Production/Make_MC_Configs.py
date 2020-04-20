########################################################################################################################
# Abe Tishelman-Charny
# 17 April 2020
#
# The purpose of this python module is to create an MC_Configs json file to run with . SubmitMCJobs.sh
#
# Example Usage:
#
# Resonant Points:
# python Make_MC_Configs.py --step GEN-SIM --nEvents 1000 --jobs_jobsize 1 --finalStates qqlnu --Resonant --masses 260,750 --diHiggsDecay WWgg --fragOutDir HHWWgg
#
# EFT benchmarks:
# python Make_MC_Configs.py --step GEN-SIM --nEvents 1000 --jobs_jobsize 1 --EFT --EFT_BMs 1 --finalStates qqlnu --diHiggsDecay WWgg --fragOutDir EFT
#
# NMSSM Points:
# python Make_MC_Configs.py --step GEN-SIM --nEvents 1000 --jobs_jobsize 1 --NMSSM --finalStates qqlnu --masses 500,300 --diHiggsDecay WWgg --fragOutDir HHWWgg_NMSSM
#
########################################################################################################################

import argparse
import os 
from os import path 
from Make_MC_Configs_Tools import * 
parser = argparse.ArgumentParser(description='MC_Configs.json creator')
parser.add_argument('--step', type=str, default="", help="Step to run. Options: GEN, GEN-SIM, DR1, DR2, MINIAOD", required=True)
parser.add_argument('--nEvents', type=int, default=1000, help="Number of events to produce", required=True)
parser.add_argument('--jobs_jobsize', type=int, default=1, help="GEN/GEN-SIM: Number of jobs to spread events over. Other steps: Number of input files per job", required=True)
parser.add_argument('--masses', type=str, default="", help="Comma separated list of masses to run", required=False) # for res case or NMSSM 
parser.add_argument('--finalStates', type=str, default="", help="Comma separated list of final states to run", required=True) 
parser.add_argument("--Resonant", action="store_true", default=False, help="Resonant case", required=False)
parser.add_argument("--EFT", action="store_true", default=False, help="EFT Benchmark models case", required=False)
parser.add_argument('--EFT_BMs', type=str, default="", help="Comma separated list of EFT Benchmarks to run", required=False) # 0 indexed. BM 0, 1, 2, ... gridpack BM is indexed 1
parser.add_argument("--NMSSM", action="store_true", default=False, help="NMSSM models case", required=False)
parser.add_argument('--diHiggsDecay', type=str, default="", help="Di-Higgs decay channel", required=True) # HH decay. Should be whatever you used in HHWWgg_Tools/Fragments. Ex: WWgg
parser.add_argument('--fragOutDir', type=str, default="", help="Directory fragments are in. HHWWgg_Tools/Fragments/Outputs/<fragOutDir>", required=True) # Ex: HHWWgg_NMSSM

# # masses = [260, 270, 280, 300, 320, 350, 400, 500, 550, 600, 650, 700, 800, 850, 900, 1000]

args = parser.parse_args()

# Perform argument checks 
ArgChecks(args)

# Set arguments 
step, nEvents, jobs_jobsize, diHiggsDecay = args.step, args.nEvents, args.jobs_jobsize, args.diHiggsDecay
fragOutDir = args.fragOutDir
masses = args.masses.split(',')
finalStates = args.finalStates.split(',')
EFT_BMs = args.EFT_BMs.split(',')

# exit(1)

# Begin writing file 
outputName = 'MC_Configs.json' # output json file path 
MC_Configs = '[' 

postGENSteps = ["DR1","DR2","MINIAOD"]
postGEN = 0 
if step in postGENSteps: postGEN = 1 

# if CMSSW_9_3_9_patch1 doesn't exist, get it now, so that fragments are setup 
if(not path.exists("CMSSW_9_3_9_patch1")):
	print'CMSSW_9_3_9_patch1 does not exist. Getting now ...'
	os.system('export SCRAM_ARCH=slc6_amd64_gcc630')
	os.system('cmsrel CMSSW_9_3_9_patch1') 
	if(step == "GEN" or step == "GEN-SIM") and (not path.exists('CMSSW_9_3_9_patch1/src/Configuration/GenProduction/python')):
		print'Want to create GEN or GEN-SIM step but do not have fragment folder '
		print'Creating now ...'
		os.system('cd CMSSW_9_3_9_patch1/src') 
		os.system('mkdir -p Configuration/GenProduction/python') 
		os.system('cd ../..') 

else:
	print'All proper CMSSW paths exist. Continuting...'

if(postGEN):

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
					direc += '0000/' # Might need to be careful here. May not always be in 0000
					print'Found direc: ',direc 
					cmd = 'ls -1 '
					cmd += direc
					cmd += ' | wc -l'
					print 'Number of files in direc: ',os.system(cmd) 
					directories.append(direc)

## Create json objects 

# GEN-SIM step 
if step == "GEN-SIM":
	ultimateFragDirec = "CMSSW_9_3_9_patch1/src/Configuration/GenProduction/python"
	
	# If EFT, go through benchmarks and final states 
	if(args.EFT):
		# EFT_BMs = args.EFT_BMs.split(',')		
		for ibm,bm in enumerate(EFT_BMs):
			for finalState in finalStates:
				expectedFragmentEnd = "GluGluToHHTo_%s_%s_node%s.py"%(diHiggsDecay,finalState,bm)
				skip = ManageFragment(expectedFragmentEnd,fragOutDir,ultimateFragDirec)
				if(skip): continue 

				# Indentation of text chosen for visual output
				MC_Configs_Entry = '''
				{ 
						"step"      : "{step}",
						"events"    : {events},
						"jobs_jobsize"      : {jobs_jobsize},
						"fragment_directory"  : "GluGluToHHTo_{diHiggsDecay}_{finalState}_node{bm}",
						"pileup"              : "wPU",
						"localGridpack"                : "0" 
				}'''

				MC_Configs_Entry = MC_Configs_Entry.replace("{bm}",str(bm))
				MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
				MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
				MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
				MC_Configs_Entry = MC_Configs_Entry.replace("{finalState}",str(finalState))
				MC_Configs_Entry = MC_Configs_Entry.replace("{diHiggsDecay}",str(diHiggsDecay))
				
				MC_Configs += MC_Configs_Entry

				if ibm is not len(EFT_BMs)-1: MC_Configs += ',' # need comma separation 
				else: continue # no comma at end of last object 				

	# If resonant or NMSSM, go through masses (pair or non-pairs) and final states 
	elif(args.Resonant):
		for im,mass in enumerate(masses):
			for ifs,finalState in enumerate(finalStates):

				expectedFragmentEnd = "ggF_X%s_HH%s_%s.py"%(mass,diHiggsDecay,finalState)
				skip = ManageFragment(expectedFragmentEnd,fragOutDir,ultimateFragDirec)
				if(skip): continue 		

				# Indentation of text chosen for visual output
				MC_Configs_Entry = '''
				{ 
						"step"      : "{step}",
						"events"    : {events},
						"jobs_jobsize"      : {jobs_jobsize},
						"fragment_directory"  : "ggF_X{mass}_{diHiggsDecay}_{finalState}",
						"pileup"              : "wPU",
						"localGridpack"                : "0"
				}'''

				MC_Configs_Entry = MC_Configs_Entry.replace("{mass}",str(mass))
				MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
				MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
				MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
				MC_Configs_Entry = MC_Configs_Entry.replace("{finalState}",str(finalState))
				MC_Configs_Entry = MC_Configs_Entry.replace("{diHiggsDecay}",str(diHiggsDecay))

				MC_Configs += MC_Configs_Entry

				if im is not len(masses)-1: MC_Configs += ',' # need comma separation 
				else: continue # no comma at end of last object 

	elif(args.NMSSM):
		massPairs = [] 
		massPairs = GetMassPairs(massPairs, masses)
		for imp,massPair in enumerate(massPairs):
			massHS = massPair[0]
			massIS = massPair[1]
			for ifs,finalState in enumerate(finalStates):
				expectedFragmentEnd = "NMSSM_XYH%s%s_MX%s_MY%s.py"%(diHiggsDecay,finalState,massHS,massIS)
				skip = ManageFragment(expectedFragmentEnd,fragOutDir,ultimateFragDirec)
				if(skip): continue 					

				# Indentation of text chosen for visual output
				MC_Configs_Entry = '''
				{ 
						"step"      : "{step}",
						"events"    : {events},
						"jobs_jobsize"      : {jobs_jobsize},
						"fragment_directory"  : "NMSSM_XYH{diHiggsDecay}{finalState}_MX{massHS}_MY{massIS}", 
						"pileup"              : "wPU",
						"localGridpack"                : "1"
				}'''
				MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
				MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
				MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
				MC_Configs_Entry = MC_Configs_Entry.replace("{finalState}",str(finalState))
				MC_Configs_Entry = MC_Configs_Entry.replace("{massHS}",str(massHS)) # mass of heavy scalar 
				MC_Configs_Entry = MC_Configs_Entry.replace("{massIS}",str(massIS)) # mass of intermediate scalar 				
				MC_Configs_Entry = MC_Configs_Entry.replace("{diHiggsDecay}",str(diHiggsDecay)) 

				MC_Configs += MC_Configs_Entry

				if imp is not len(massPairs)-1: MC_Configs += ',' # need comma separation 
				else: continue # no comma at end of last object 

	MC_Configs += '\n]\n' # finish json 

	with open(outputName, "w") as output:
			output.write(MC_Configs) # write json file 



##### need to configure .... 

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

###########################

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