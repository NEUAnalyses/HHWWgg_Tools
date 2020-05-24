########################################################################################################################
# Abe Tishelman-Charny
# 17 April 2020
#
# The purpose of this python module is to create an MC_Configs json file to run with . SubmitMCJobs.sh
#
# Example Usage:
#
# ##-- Resonant Points:
# python Make_MC_Configs.py --step GEN --nEvents 1000 --jobs_jobsize 1 --finalStates qqlnu --Resonant --masses 260,600,1000 --diHiggsDecay WWgg --fragOutDir TestTauRes
# python Make_MC_Configs.py --step GEN-SIM --nEvents 1000 --jobs_jobsize 1 --finalStates qqlnu --Resonant --masses 260,750 --diHiggsDecay HHWWgg --fragOutDir HHWWgg
# python Make_MC_Configs.py --step GEN-SIM --nEvents 100000 --jobs_jobsize 40 --finalStates qqlnu --Resonant --masses 260,600,1000 --diHiggsDecay WWgg --fragOutDir TestTauRes
# python Make_MC_Configs.py --step DR1 --nEvents 100000 --jobs_jobsize 1 --finalStates qqlnu --Resonant --masses 260,600,1000 --diHiggsDecay WWgg --prevOutDir /eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/
#
# ##-- EFT benchmarks:
# GEN-SIM: python Make_MC_Configs.py --step GEN-SIM --nEvents 1000 --jobs_jobsize 1 --EFT --EFT_BMs 1 --finalStates qqlnu --diHiggsDecay WWgg --fragOutDir EFT
# DR1: python Make_MC_Configs.py --step DR1 --nEvents 100000 --jobs_jobsize 1 --EFT --EFT_BMs 2,9 --finalStates qqlnu --diHiggsDecay WWgg --prevOutDir /eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/
#
# ##-- NMSSM Points:
# python Make_MC_Configs.py --step GEN-SIM --nEvents 1000 --jobs_jobsize 1 --NMSSM --finalStates qqlnu --masses 500,300 --diHiggsDecay WWgg --fragOutDir HHWWgg_NMSSM
# postGEN: python Make_MC_Configs.py --step DR2 --nEvents 100000 --jobs_jobsize 1 --NMSSM --finalStates qqlnu --masses 2000,1800 --diHiggsDecay WWgg --prevOutDir /eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/
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
parser.add_argument('--fragOutDir', type=str, default="", help="Directory fragments are in. HHWWgg_Tools/Fragments/Outputs/<fragOutDir>", required=False) # Ex: HHWWgg_NMSSM
parser.add_argument('--prevOutDir', type=str, default="", help="Comma separated list of directories that previous step output files are in", required=False) # Ex: /eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/
parser.add_argument('--PU', type=str, default="wPU", help="Pileup. Options: wPU, woPU", required=False) 

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
prevOutDir = args.prevOutDir
PU = args.PU 

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
	## Function: Get Prev Step Directories	
	prevStep = GetPrevStep(step) 
	dir_list = os.listdir(prevOutDir) 
	prevStepDirectories = [] 

	if(args.NMSSM): 
		# if dir.split('_')[0] != "NMSSM": continue 
		# assuming directory form: "NMSSM_XYH<diHiggsDecay><finalState>_MX<mass1>_MY<mass2>"
		# for example "NMSSM_XYHWWggqqlnu_MX300_MY170"
		# find directory for each mass pair 
		massPairs = [] 
		massPairs = GetMassPairs(massPairs, masses)		
		for massPair in massPairs:
			mass_X, mass_Y = massPair[0], massPair[1] 	
			for finalState in finalStates:
				for dir in dir_list:
					if dir.split('_')[0] != "NMSSM": continue
					desiredName = "NMSSM_XYH%s%s_MX%s_MY%s"%(diHiggsDecay,finalState,mass_X,mass_Y)
					if(dir != desiredName): continue 
					else:
						for sndDirec in os.listdir("%s%s/"%(prevOutDir,dir)):
							if(prevStep == "GEN-SIM"):
								if(sndDirec != "%sevents_%s"%(nEvents,prevStep)): continue 
							else:
								if(sndDirec != "%sevents_%s_%s"%(nEvents,PU,prevStep)): continue
							
							newestDir = sorted(os.listdir("%s/%s/%s"%(prevOutDir,dir,sndDirec)))[-1]
							print(newestDir)
							print("Found full previous step directory:")
							fullDirec = "%s%s/%s/%s/0000/"%(prevOutDir,dir,sndDirec,newestDir) # assuming crab folder 0000....may not also be correct
							print fullDirec
							cmd = "ls -1 %s | wc -l"%(fullDirec)
							print'Number of file in previous step directory:'
							os.system(cmd)
							prevStepDirectories.append(fullDirec)
	elif(args.EFT): 
		# assuming directory form: "GluGluToHHTo_<diHiggsDecay>_<finalState>_node<nodeNumber>"
		# for example "GluGluToHHTo_WWgg_qqlnu_node2"
		for node in EFT_BMs:
			for finalState in finalStates:
				for dir in dir_list:
					if dir.split('_')[0] != "GluGluToHHTo": continue
					desiredName = "GluGluToHHTo_%s_%s_node%s"%(diHiggsDecay,finalState,node)
					if(dir != desiredName): continue 
					else:
						for sndDirec in os.listdir("%s%s/"%(prevOutDir,dir)):
							if(prevStep == "GEN-SIM"):
								if(sndDirec != "%sevents_%s"%(nEvents,prevStep)): continue 
							else:
								if(sndDirec != "%sevents_%s_%s"%(nEvents,PU,prevStep)): continue							
							newestDir = sorted(os.listdir("%s/%s/%s"%(prevOutDir,dir,sndDirec)))[-1]
							print(newestDir)
							print("Found full previous step directory:")
							fullDirec = "%s%s/%s/%s/0000/"%(prevOutDir,dir,sndDirec,newestDir) # assuming crab folder 0000....may not also be correct
							print fullDirec
							cmd = "ls -1 %s | wc -l"%(fullDirec)
							print'Number of file in previous step directory:'
							os.system(cmd)
							prevStepDirectories.append(fullDirec)

	elif(args.Resonant): 
		# assuming directory form: "ggF_X<ResMass>_HH<diHiggsDecay>_<finalState>"
		# for example "ggF_X260_HHWWgg_qqlnu"
		for mass in masses:
			for finalState in finalStates:
				for dir in dir_list:
					if dir.split('_')[0] != "ggF": continue
					desiredName = "ggF_X%s_HH%s_%s"%(mass,diHiggsDecay,finalState)
					if(dir != desiredName): continue 
					else:
						for sndDirec in os.listdir("%s%s/"%(prevOutDir,dir)):
							if(prevStep == "GEN-SIM"):
								if(sndDirec != "%sevents_%s"%(nEvents,prevStep)): continue 
							else:
								if(sndDirec != "%sevents_%s_%s"%(nEvents,PU,prevStep)): continue							
							newestDir = sorted(os.listdir("%s/%s/%s"%(prevOutDir,dir,sndDirec)))[-1]
							print(newestDir)
							print("Found full previous step directory:")
							fullDirec = "%s%s/%s/%s/0000/"%(prevOutDir,dir,sndDirec,newestDir) # assuming crab folder 0000....may not also be correct
							print fullDirec
							cmd = "ls -1 %s | wc -l"%(fullDirec)
							print'Number of file in previous step directory:'
							os.system(cmd)
							prevStepDirectories.append(fullDirec)							

## Create json objects 

# GEN or GEN-SIM step  
if step == "GEN-SIM" or step == "GEN":
	ultimateFragDirec = "CMSSW_9_3_9_patch1/src/Configuration/GenProduction/python"
	
	# If EFT, go through benchmarks and final states 
	if(args.EFT):
		# EFT_BMs = args.EFT_BMs.split(',')		
		for ibm,bm in enumerate(EFT_BMs):
			for finalState in finalStates:
				expectedFragmentEnd = "GluGluToHHTo_%s_%s_node%s.py"%(diHiggsDecay,finalState,bm)
				skip = ManageFragment(expectedFragmentEnd,fragOutDir,ultimateFragDirec,args.NMSSM)
				if(skip): continue 

				# Indentation of text chosen for visual output
				MC_Configs_Entry = '''
				{ 
						"step"      : "{step}",
						"events"    : {events},
						"jobs_jobsize"      : {jobs_jobsize},
						"fragment_directory"  : "GluGluToHHTo_{diHiggsDecay}_{finalState}_node{bm}",
						"pileup"              : "{PU}",
						"localGridpack"                : "0" 
				}'''

				MC_Configs_Entry = MC_Configs_Entry.replace("{bm}",str(bm))
				MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
				MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
				MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
				MC_Configs_Entry = MC_Configs_Entry.replace("{finalState}",str(finalState))
				MC_Configs_Entry = MC_Configs_Entry.replace("{diHiggsDecay}",str(diHiggsDecay))
				MC_Configs_Entry = MC_Configs_Entry.replace("{PU}",str(args.PU))
				
				MC_Configs += MC_Configs_Entry

				if ibm is not len(EFT_BMs)-1: MC_Configs += ',' # need comma separation 
				else: continue # no comma at end of last object 				

	# If resonant or NMSSM, go through masses (pair or non-pairs) and final states 
	elif(args.Resonant):
		for im,mass in enumerate(masses):
			for ifs,finalState in enumerate(finalStates):

				expectedFragmentEnd = "ggF_X%s_HH%s_%s.py"%(mass,diHiggsDecay,finalState)
				skip = ManageFragment(expectedFragmentEnd,fragOutDir,ultimateFragDirec,args.NMSSM)
				if(skip): continue 		

				# Indentation of text chosen for visual output
				MC_Configs_Entry = '''
				{ 
						"step"      : "{step}",
						"events"    : {events},
						"jobs_jobsize"      : {jobs_jobsize},
						"fragment_directory"  : "ggF_X{mass}_HH{diHiggsDecay}_{finalState}",
						"pileup"              : "{PU}",
						"localGridpack"                : "0"
				}'''

				MC_Configs_Entry = MC_Configs_Entry.replace("{mass}",str(mass))
				MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
				MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
				MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
				MC_Configs_Entry = MC_Configs_Entry.replace("{finalState}",str(finalState))
				MC_Configs_Entry = MC_Configs_Entry.replace("{diHiggsDecay}",str(diHiggsDecay))
				MC_Configs_Entry = MC_Configs_Entry.replace("{PU}",str(args.PU))


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
				skip = ManageFragment(expectedFragmentEnd,fragOutDir,ultimateFragDirec,args.NMSSM)
				if(skip): continue 					

				# Indentation of text chosen for visual output
				MC_Configs_Entry = '''
				{ 
						"step"      : "{step}",
						"events"    : {events},
						"jobs_jobsize"      : {jobs_jobsize},
						"fragment_directory"  : "NMSSM_XYH{diHiggsDecay}{finalState}_MX{massHS}_MY{massIS}", 
						"pileup"              : "{PU}",
						"localGridpack"                : "1"
				}'''
				MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
				MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
				MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
				MC_Configs_Entry = MC_Configs_Entry.replace("{finalState}",str(finalState))
				MC_Configs_Entry = MC_Configs_Entry.replace("{massHS}",str(massHS)) # mass of heavy scalar 
				MC_Configs_Entry = MC_Configs_Entry.replace("{massIS}",str(massIS)) # mass of intermediate scalar 				
				MC_Configs_Entry = MC_Configs_Entry.replace("{diHiggsDecay}",str(diHiggsDecay)) 
				MC_Configs_Entry = MC_Configs_Entry.replace("{PU}",str(args.PU))

				MC_Configs += MC_Configs_Entry

				if imp is not len(massPairs)-1: MC_Configs += ',' # need comma separation 
				else: continue # no comma at end of last object 

	MC_Configs += '\n]\n' # finish json 

	with open(outputName, "w") as output:
			output.write(MC_Configs) # write json file 


## if the step is DR1, DR2 or MINIAOD, you need a different config type 
## DR1, DR2, or MINIAOD step 
else:

	if(args.NMSSM):
		# for id,prevDirec in enumerate(prevStepDirectories):
		# prevStepDirectories
		massPairs = [] 
		massPairs = GetMassPairs(massPairs, masses)
		for imp,massPair in enumerate(massPairs):
			for ifs,finalState in enumerate(finalStates):  
				prevDirec = prevStepDirectories[imp+ifs] # assuming prestepdirectories appended for masspair, for final state and found one for each 
				# Indentation of text chosen for visual output
				MC_Configs_Entry = '''
				{ 
						"step"      : "{step}",
						"events"    : {events},
						"jobs_jobsize"      : {jobs_jobsize},
						"fragment_directory"  : "{prevDirec}", 
						"pileup"              : "{PU}",
						"localGridpack"                : "0" 
				}'''
				MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
				MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
				MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
				MC_Configs_Entry = MC_Configs_Entry.replace("{prevDirec}",str(prevDirec))
				MC_Configs_Entry = MC_Configs_Entry.replace("{PU}",str(args.PU))

				MC_Configs += MC_Configs_Entry

				if imp is not len(massPairs)-1: MC_Configs += ',' # need comma separation 
				else: continue # no comma at end of last object 

	# If EFT, go through benchmarks and final states 
	elif(args.EFT):
		# EFT_BMs = args.EFT_BMs.split(',')		
		for ibm,bm in enumerate(EFT_BMs):
			for ifs,finalState in enumerate(finalStates):
				prevDirec = prevStepDirectories[ibm+ifs] # assuming prestepdirectories appended for benchmark, for final state and found one for each

				# Indentation of text chosen for visual output
				MC_Configs_Entry = '''
				{ 
						"step"      : "{step}",
						"events"    : {events},
						"jobs_jobsize"      : {jobs_jobsize},
						"fragment_directory"  : "{prevDirec}", 
						"pileup"              : "{PU}",
						"localGridpack"                : "0" 
				}'''

				MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
				MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
				MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
				MC_Configs_Entry = MC_Configs_Entry.replace("{prevDirec}",str(prevDirec))
				MC_Configs_Entry = MC_Configs_Entry.replace("{PU}",str(args.PU))
				
				MC_Configs += MC_Configs_Entry

				if ibm is not len(EFT_BMs)-1: MC_Configs += ',' # need comma separation 
				else: continue # no comma at end of last object 	

	elif(args.Resonant):
		for im,mass in enumerate(masses):
			for ifs,finalState in enumerate(finalStates):

				# expectedFragmentEnd = "ggF_X%s_HH%s_%s.py"%(mass,diHiggsDecay,finalState)
				# skip = ManageFragment(expectedFragmentEnd,fragOutDir,ultimateFragDirec,args.NMSSM)
				# if(skip): continue 		

				prevDirec = prevStepDirectories[im+ifs] # assuming prestepdirectories appended for mass, for final state and found one for each 

				# Indentation of text chosen for visual output
				MC_Configs_Entry = '''
				{ 
						"step"      : "{step}",
						"events"    : {events},
						"jobs_jobsize"      : {jobs_jobsize},
						"fragment_directory"  : "{prevDirec}",
						"pileup"              : "{PU}",
						"localGridpack"                : "0"
				}'''

				# MC_Configs_Entry = MC_Configs_Entry.replace("{mass}",str(mass))
				MC_Configs_Entry = MC_Configs_Entry.replace("{step}",str(step))
				MC_Configs_Entry = MC_Configs_Entry.replace("{events}",str(nEvents))
				MC_Configs_Entry = MC_Configs_Entry.replace("{jobs_jobsize}",str(jobs_jobsize))
				MC_Configs_Entry = MC_Configs_Entry.replace("{prevDirec}",str(prevDirec))
				MC_Configs_Entry = MC_Configs_Entry.replace("{PU}",str(args.PU))


				MC_Configs += MC_Configs_Entry

				if im is not len(masses)-1: MC_Configs += ',' # need comma separation 
				else: continue # no comma at end of last object 

	MC_Configs += '\n]\n' # finish json 

	with open(outputName, "w") as output:
			output.write(MC_Configs) # write json file 

print 
print'[Make_MC_Configs] - MC_Configs.json created'
print'[Make_MC_Configs] - Make sure MC_Configs.json looks good before submitting with . SubmitMCJobs.sh !' 
print 
