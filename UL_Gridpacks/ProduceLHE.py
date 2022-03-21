# 12 October 2021 
# Abraham Tishelman-Charny 
#
# The purpose of this script is to produce LHE files from MC generator gridpacks. 

##-- Imports 
import os 
import time 
import argparse 

##-- Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--Prod", type=str, default = "ggF", help = "Production mode. ggF or VBF")
parser.add_argument("--Spin", type = str, default = "0", help = "Spin of resonant particle. 0 (Radion) or 2 (Bulk Graviton)")
parser.add_argument("--masses", type=str, default = "250", help = "Comma separated string of Resonant mass points to produce")
parser.add_argument("--localDir", type=str, default = "NO_Local_Dir", help = "Comma separated string of Resonant mass points to produce")
args = parser.parse_args()

os.chdir(args.localDir)

##-- Gridpack Params
gridpack_Type = '%s_Spin-%s'%(args.Prod, args.Spin)
masses = args.masses.split(',')
direc = '/afs/cern.ch/work/a/atishelm/public/UltraLegacy_HH_Gridpacks/%s/'%(gridpack_Type)
gridpacks = ["%s/%s"%(direc, file) for file in os.listdir(direc) if file.endswith('tar.xz')]
print("gridpacks:",gridpacks)
nGridpacks = len(gridpacks)

##-- LHE Production Parameters
nEvents = 10000
RandomSeed = int(time.time())
numberOfCPUs = 10

##-- Produce an LHE file for each gridpack 
for i, gridpack in enumerate(gridpacks):

    gridpackName = gridpack.split('/')[-1].split('.')[0]
    
    print("gridpack Name:",gridpackName)
    print("gridpack Path:",gridpack)

    for mass in masses:
        massString = "M%s_"%(mass)
        if(massString in gridpackName):
            temp_dir = "tmp_{Prod}_Spin-{Spin}_M{mass}".format(Prod=args.Prod, Spin=args.Spin, mass=mass)
            print("temp_dir:",temp_dir)
            os.mkdir(temp_dir)
            os.chdir(temp_dir)

            ##-- Unpack Gridpack Tarball
            UNPACK_TARBALL_COMMAND = "tar -xaf %s"%(gridpack)
            print("UNPACK_TARBALL_COMMAND:",UNPACK_TARBALL_COMMAND)
            os.system(UNPACK_TARBALL_COMMAND)
            
            ##-- Produce LHE file 
            RUN_GRID_COMMAND = "./runcmsgrid.sh %s %s %s"%(nEvents, RandomSeed, numberOfCPUs)
            print("RUN_GRID_COMMAND:",RUN_GRID_COMMAND)
            os.system(RUN_GRID_COMMAND)
            
            ##-- Move LHE file to output directory 
            # MOVE_FILE_COMMAND = "mv cmsgrid_final.lhe %s/LHE_Files/%s/%s.lhe"%(args.localDir, gridpack_Type, gridpackName)
            MOVE_FILE_COMMAND = "mv cmsgrid_final.lhe /eos/user/a/atishelm/SWAN_projects/CMS-GEN/LHE_Files/%s/%s.lhe"%(gridpack_Type, gridpackName)

            print("MOVE_FILE_COMMAND:",MOVE_FILE_COMMAND)
            os.system(MOVE_FILE_COMMAND)

            os.chdir("..")
            print("Removing temporary directory {temp_dir}...".format(temp_dir=temp_dir))
            os.system("rm -rf {temp_dir}".format(temp_dir=temp_dir))
    
print("DONE")
