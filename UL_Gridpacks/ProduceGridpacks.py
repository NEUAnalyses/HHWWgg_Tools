################################################################################################
# Abraham Tishelman-Charny                                                                     #
# 2 March 2021                                                                                 #
#                                                                                              #
# The purpose of this module is to produce gridpacks with the CMS genproductions repository.   #
################################################################################################

##-- Note that if you try to produce a gridpack with an existing directory in genproductions/bin/MadGraph5_aMCatNLO/, it won't work 

##-- Example Usage:
#
##-- Produce Cards
# python ProduceGridpacks.py --Prod VBF --Spin 0 --masses 250,260,270,280,300,320,350,400,450,500,550,600,650,700,750,800,850,900,1000,1250,1500,1750,2000,2500,3000 --dryRun ##-- Run dryrun first to produce cards 
#
##-- Produce Gridpacks
# python ProduceGridpacks.py --Prod VBF --Spin 0 --masses 250,260,270,280,300,320,350,400,450,500,550,600,650,700,750,800,850,900,1000,1250,1500,1750,2000,2500,3000 ##-- Then run without dryrun to produce gridpacks 

##-- Imports 
import os 
import argparse 

##-- Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--Prod", type=str, default = "ggF", help = "Production mode. ggF or VBF")
parser.add_argument("--Spin", type = str, default = "0", help = "Spin of resonant particle. 0 (Radion) or 2 (Bulk Graviton)")
parser.add_argument("--masses", type=str, default = "250", help = "Comma separated string of Resonant mass points to produce")
parser.add_argument("--dryRun", action="store_true", default = False, help = "Dry run. Do not produce gridpack.")
args = parser.parse_args()

##-- Parameters 
initialDirec = os.getcwd()
productionDirectory = "genproductions/bin/MadGraph5_aMCatNLO/" ##-- the directory containing the gridpack generation executable 
fullProductionDirectory = "%s/%s"%(initialDirec, productionDirectory)
masses_l = args.masses.split(',')
print"initialDirec:",initialDirec
print"Masses:",args.masses
print"fullProductionDirectory:",fullProductionDirectory
direcDict = {
    "ggF" : "genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/exo_diboson/",
    "VBF" : "genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/VBFToXToHH/"
}
direc = direcDict[args.Prod]
print"cd %s"%(direc)
os.chdir(direc)

##-- Gluon Gluon Fusion 
if(args.Prod == "ggF"):
    
    if(args.Spin == "0"):
      sample = "Spin-0/cards_templates/Radion_hh_hdecay_narrow_Mmass"
      finishedSample = "Spin-0/Radion_hh_narrow/Radion_hh_narrow"
      prefix = "Radion_hh_narrow"      

    elif(args.Spin == "2"):
      sample = "Spin-2/cards_templates/BulkGraviton_hh_hdecay_narrow_Mmass"
      finishedSample = "Spin-2/BulkGraviton_hh_narrow/BulkGraviton_hh_GF_HH_narrow"
      prefix = "BulkGraviton_hh_GF_HH_narrow"        

    CREATE_CARDS_COMMAND = "python createCards_BSM_HH_2017.py -g -f %s --masses %s"%(sample, args.masses)
    print"CREATE_CARDS_COMMAND:",CREATE_CARDS_COMMAND
    os.system(CREATE_CARDS_COMMAND)
    os.chdir(fullProductionDirectory)

    for mass in masses_l:
        print"mass:",mass
        print"Output cards to: %s/%s_M%s"%(direc, finishedSample, mass)
        os.chdir(initialDirec)
        if(args.dryRun):
            print"DRY RUN: Not generating gridpack"

        else:
            print"Generating gridpack..."
            os.chdir(fullProductionDirectory)
            GENERATE_COMMAND = "./gridpack_generation.sh %s_M%s cards/production/2017/13TeV/exo_diboson/%s_M%s"%(prefix, mass, finishedSample, mass)
            os.system(GENERATE_COMMAND)            

    print"cd %s"%(initialDirec)
    os.chdir(initialDirec)

##-- Vector Boson Fusion 
elif(args.Prod == "VBF"):
    if(args.Spin == "0"):
      sample = "VBFToRadionToHH_M" 

    elif(args.Spin == "2"):
      sample = "VBFToBulkGravitonToHH_M"  

    postfix = ["_run_card.dat", "_customizecards.dat", "_proc_card.dat",  "_extramodels.dat"]

    for mass in masses_l:
      os.system("mkdir -p %s%s"%(sample, mass))
      for i in range(0,4):
        REPLACE_COMMAND = 'sed "s/<MASS>/%s/g" %s/%s%s > %s%s/%s%s%s'%(mass, sample, sample, postfix[i], sample, mass, sample, mass, postfix[i])
        # print"REPLACE COMMAND: ",REPLACE_COMMAND
        print"Producing %s mass %s %s file..."%(sample, mass, postfix[i])
        os.system(REPLACE_COMMAND)
      print"Output cards to: %s/%s%s"%(direc, sample, mass)

      if(args.dryRun):
        print"DRY RUN: Not generating gridpack"
      else:
        print"Generating gridpack..."
        os.chdir(fullProductionDirectory)
        GENERATE_COMMAND = "./gridpack_generation.sh %s%s cards/production/2017/13TeV/VBFToXToHH/%s%s"%(sample, mass, sample, mass)
        os.system(GENERATE_COMMAND)            
        