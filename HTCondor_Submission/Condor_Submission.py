"""
25 November 2021 
Abraham Tishelman-Charny

The purpose of this module is to submit condor jobs for custom python module processes.

Example commands:
python Condor_Submission.py --outDir /eos/user/a/atishelm/ntuples/Test_Condor

"""

import os, sys
import argparse
import logging
import pwd
import subprocess
import shutil
import time
import glob

#!/usr/bin/python

logging.basicConfig(level=logging.DEBUG)

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

python3 DummyPythonModule.py --InputParameter $2 --condor # command to run in condor directory 

echo "----- directory after running :"
"""

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

transfer_output_remaps = "DummyValue.p={output_dir}/DummyValue_$(ProcId).p"

+JobFlavour           = "{queue}"
universe = vanilla 

queue InputParameter from {jobdir}/inputParams.dat
"""

def main():

    # command line flags 
    parser = argparse.ArgumentParser(description='Condor submission')
    parser.add_argument("--JobFlavour", type=str, default="microcentury", help="Condor submission flavour to determine max run time per job")
    parser.add_argument("--force", action="store_true", help="Recreate files and jobs")
    parser.add_argument("--dryRun", action="store_true", help="To run without submission")
    parser.add_argument("--outDir", type=str, help="Directory to transfer output files to")
    options = parser.parse_args()

    # set command line flag values to variables to be used 
    jobs_dir = "jobs"
    outdir = options.outDir
    JobFlavour = options.JobFlavour
    dryRun = options.dryRun
    force = options.force 

    # see if output directory for job files already exists 
    if os.path.isdir(jobs_dir):
        if not force:
            logging.error(" " + jobs_dir + " already exist !")
            raise Exception(" " + jobs_dir + " already exist !")
        else:
            logging.warning(" " + jobs_dir + " already exists, forcing its deletion!")
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

    with open(os.path.join(jobs_dir, "script.sh"), "w") as scriptfile:
        script = script_TEMPLATE.format(
            outputdir=outdir
        )
        scriptfile.write(script)
        scriptfile.close()

    # include necessary input files which are needed for running your processes 
    with open(os.path.join(jobs_dir, "condor.sub"), "w") as condorfile:
        allFiles = [
            "../DummyPythonModule.py",
            "../python/DummyPythonModule_Tools.py" # copy necessary input modules to condor area 
        ]
        condor = condor_TEMPLATE.format(
            transfer_files = ",".join(allFiles),
            output_dir = outdir,
            jobdir=jobs_dir,
            queue=JobFlavour
        )
        condorfile.write(condor)
        condorfile.close()

    # as long as you are not performing a dry run, submit the jobs 
    if not dryRun:
        htc = subprocess.Popen(
            "condor_submit " + os.path.join(jobs_dir, "condor.sub"),
            shell  = True,
            stdin  = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            close_fds=True
        )
        out, err = htc.communicate()
        exit_status = htc.returncode
        logging.info("condor submission status : {} ---> 0 = should be submitted. Try running 'condor_q'. 1 = some kind of error.".format(exit_status))

if __name__ == "__main__":
    main()
    print("DONE")
