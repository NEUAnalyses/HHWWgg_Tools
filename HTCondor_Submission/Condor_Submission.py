"""
25 November 2021 
Abraham Tishelman-Charny

The purpose of this module is to submit condor jobs for custom python module processes.

Example commands:
python Condor_Submission.py --outDir /eos/user/a/atishelm/ntuples/Test_Condor

"""

# python imports 
import os, sys
import argparse
import logging
import pwd
import subprocess
import shutil
import time

#!/usr/bin/python

logging.basicConfig(level=logging.DEBUG)

# create a template for the bash script to be run on condor nodes 
script_TEMPLATE = """#!/bin/bash

echo
echo $_CONDOR_SCRATCH_DIR
cd   $_CONDOR_SCRATCH_DIR
echo
echo "... starting job at" `date "+%Y-%m-%d %H:%M:%S"`
echo "+ PYTHON_PATH = $PYTHON_PATH"
echo "+ PWD         = $PWD"

# command to run in condor directory 
# $1: jobId 
# $2: first argument from inParams

# command to run in condor directory 
python3 DummyPythonModule.py --InputParameter $2 --condor 

"""

# create a template for a condor submission file 
condor_TEMPLATE = """
request_disk          = 2048
request_memory = 8000
executable            = {jobdir}/script.sh
arguments             = $(ProcId) $(InputParameter) 
transfer_input_files = {transfer_files}

output                = $(ClusterId).$(ProcId).out
error                 = $(ClusterId).$(ProcId).err
log                   = $(ClusterId).$(ProcId).log
initialdir            = {jobdir}

# take pickle file output from process and transfer it from the condor scratch directory to a desired output directory 
transfer_output_remaps = "DummyValue.p={output_dir}/DummyValue_$(ProcId).p" 

# job flavour from command line argument. see: https://twiki.cern.ch/twiki/bin/view/ABPComputing/LxbatchHTCondor#Queue_Flavours
+JobFlavour           = "{queue}" 

# HTCondor universe type 
universe = vanilla 

# input file to obtain per job parameters from. For ETT studies, this .dat file could contain for example a lambda signal, lambda spike value per line (per job)
queue InputParameter from {jobdir}/inputParams.dat 
"""

def main():

    # command line flags 
    parser = argparse.ArgumentParser(description='Condor submission') # create argument parser 
    parser.add_argument("--JobFlavour", type=str, default="microcentury", help="Condor submission flavour to determine max run time per job") # see: https://twiki.cern.ch/twiki/bin/view/ABPComputing/LxbatchHTCondor#Queue_Flavours
    parser.add_argument("--force", action="store_true", help="Recreate files and jobs") # if local jobs directory exists, overwrite it 
    parser.add_argument("--dryRun", action="store_true", help="To run without submission") # run without submitting condor jobs 
    parser.add_argument("--outDir", type=str, help="Directory to transfer output files to") # directory for output files from process being run 
    options = parser.parse_args()

    # set command line flag values to variables to be used 
    jobs_dir = "jobs" # directory to contain condor job information: Log, output, error files. 
    outdir = options.outDir # directory for output files from process being run over condor. For ETT, could be "History" pickle files which contain training information. 
    JobFlavour = options.JobFlavour # see: https://twiki.cern.ch/twiki/bin/view/ABPComputing/LxbatchHTCondor#Queue_Flavours
    dryRun = options.dryRun # run without submitting condor jobs 
    force = options.force # if local jobs directory exists, overwrite it 

    # see if output directory for job files already exists 
    if os.path.isdir(jobs_dir):
        if not force:
            logging.error(" " + jobs_dir + " already exist !")
            raise Exception(" " + jobs_dir + " already exist !") # if directory already exists and you don't want to force it, raise an exception 
        else:
            logging.warning(" " + jobs_dir + " already exists, forcing its deletion!") # if directory already exists and you do want to forice it, delete the existing condor job information files 
            shutil.rmtree(jobs_dir)
            os.mkdir(jobs_dir)

    # if it doesn't, create it 
    else:
        os.mkdir(jobs_dir)

    # produce input parameters .dat file. Each line will correspond to its own HTCondor job 
    # for ETT: For each line can pass a lambda_signa, lambda_spike pair to run a training for 
    with open(os.path.join(jobs_dir, "inputParams.dat"), 'w') as inParams:
        inParams.write("1"+"\n")
        inParams.write("2"+"\n")
        inParams.write("3"+"\n")
        inParams.close()
    
    # make output directory if it doesn't already exist 
    os.system("mkdir -p {}".format(outdir))

    # create script which will be run on a condor node 
    with open(os.path.join(jobs_dir, "script.sh"), "w") as scriptfile: # create new .sh file 
        script = script_TEMPLATE.format(
            outputdir=outdir
        )
        scriptfile.write(script)
        scriptfile.close()

    # include necessary input files which are needed for running your processes 
    with open(os.path.join(jobs_dir, "condor.sub"), "w") as condorfile:
        allFiles = [
            "../DummyPythonModule.py", # python module to run 
            "../python/DummyPythonModule_Tools.py" # copy necessary input modules to condor area. E.g., this one is imported by DummyPythonModule.py, so must be transferred to the condor scratch directory in order to run the main python module 
        ]

        # create condor submission file based on template 
        condor = condor_TEMPLATE.format(
            transfer_files = ",".join(allFiles), # files from above which are necessary to be in the condor area for running 
            output_dir = outdir,
            jobdir=jobs_dir,
            queue=JobFlavour 
        )
        condorfile.write(condor)
        condorfile.close()

    # as long as you are not performing a dry run, submit the jobs 
    if not dryRun:
        htc = subprocess.Popen(
            "condor_submit " + os.path.join(jobs_dir, "condor.sub"), # command to submit condor job 
            shell  = True,
            stdin  = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            close_fds=True
        )
        out, err = htc.communicate() # run condor submit command (this will submit the jobs. One per line on the inputParams.dat file)
        exit_status = htc.returncode
        logging.info("condor submission status : {} ---> 0 = should be submitted. Try running 'condor_q'. 1 = some kind of error.".format(exit_status))

if __name__ == "__main__":
    main()
    print("DONE")
