# Private MC Production

**N.B.**: I've found that testing locally only works if you run from an lxplus 6 machine:

    ssh <lxplusUser>@lxplus6.cern.ch

## Quick Start

Example usage for the main module Make_MC_Configs.py:

Resonant Points:

    python Make_MC_Configs.py --step GEN-SIM --nEvents 1000 --jobs_jobsize 1 --finalStates qqlnu --Resonant --masses 260,750

EFT benchmarks:

    python Make_MC_Configs.py --step GEN-SIM --nEvents 1000 --jobs_jobsize 1 --EFT --EFT_BMs 1 --finalStates qqlnu

NMSSM Points:

    python Make_MC_Configs.py --step GEN-SIM --nEvents 1000 --jobs_jobsize 1 --NMSSM --finalStates qqlnu --masses 500,300

Then, as long as fragments are in proper location in CMSSW, run:

    . SubmitMCJobs.sh 

## Walkthrough 

### Getting an Example Madgraph / Pythia Config File

Based on how the repository is currently set up, the madgraph / pythia coniguration file you use must be compatible with CMSSW_9_3_9_patch1. To begin, you should clone CMSSW_9_3_9_patch1, and then you should place your madgraph / pythia configuration file in CMSSW_9_3_9_patch1/src/Configuration/GenProduction/python/. An example configuration file can be found here:

[ggF_X250_WWgg_qqlnugg.py.txt](https://twiki.cern.ch/twiki/pub/Sandbox/AbrahamTishelmanCharny/ggF_X250_WWgg_qqlnugg.py.txt)

(just change the extension from .py.txt to .py before use). Note the madgraph gridpack included in the preamble. This will create a 250 GeV Radion in MadGraph, and pythia will decay it into two SM Higgs Bosons, where one Higgs decays into two photons and the other Higgs decays into two W bosons. One of the W bosons will then decay into two quarks (which can be u, d, s or c) which will hadronize, and the other W boson will decay into a lepton and neutrino (of the electron or muon flavor).

This can be done with the steps from an lxplus7 machine: 

    export SCRAM_ARCH=slc6_amd64_gcc630 
    cmsrel CMSSW_9_3_9_patch1
    cd CMSSW_9_3_9_patch1/src
    cmsenv
    wget https://twiki.cern.ch/twiki/pub/Sandbox/AbrahamTishelmanCharny/ggF_X250_WWgg_qqlnugg.py.txt
    mkdir Configuration
    mkdir Configuration/GenProduction
    mkdir Configuration/GenProduction/python
    mv ggF_X250_WWgg_qqlnugg.py.txt Configuration/GenProduction/python/ggF_X250_WWgg_qqlnugg.py

### Create MC_Configs JSON

#### Example with GEN-SIM ggF_X250_WWgg_qqlnugg

The first step in this repository's workflow is the creation of an MC_Configs JSON file specifying which MC steps to run and which files to run them on. You can create one for your newly acquired fragment with:

    python Make_MC_Configs.py --step GEN-SIM --nEvents 1000 --jobs_jobsize 1 --finalStates qqlnu --Resonant --masses 250

this will create an output file called MC_Configs.json. By default, MC_Configs.json will have one object [[1]](https://developers.squarespace.com/what-is-json) in it consisting of five keys, each consisting of one string or value. It should look like this:

    [
        { 
            "step"      : "GEN-SIM",
            "events"    : 100,
            "jobs_jobsize"      : 1,
            "fragment_directory"  : "ggF_X250_WWgg_qqlnugg",
            "pileup"              : "wPU" 
        }
    ]

This corresponds to a production of 100 events of the process: gluon gluon fusion -> 250 GeV Radion -> HH -> WWgg -> qqlnugg, the semileptonic radion decay. This will be split into 1 job containing 100 events (possibly minus a few for decays with quarks in the final state, I don't fully understand this but I think it has something to do with jet / quark matching). For the GEN-SIM step, the pileup key isn't read, but a default string of wPU is stored there to keep the object sizes consistent between MC steps. 

When running jobs for the GEN or GEN-SIM step, the scripts will look for the configuration file: 

    CMSSW_9_3_9_patch1/src/Configuration/GenProduction/python/<fragment_directory>

in this case: 

    CMSSW_9_3_9_patch1/src/Configuration/GenProduction/python/ggF_X250_WWgg_qqlnugg.py 

so when specifying the fragment for a GEN or GEN-SIM config, you must make sure the fragment is available at this relative path. 

#### Other Possibilities

The list of possible "step" values that can be set in MC_Configs.json objects are:

- GEN
- GEN-SIM
- DR1
- DR2
- MINIAOD

In order to go from madgraph/pythia fragment to MINIAOD, you need to first run GEN-SIM, then DR1 on the GEN-SIM output files, then DR2 on the DR1 output files, and MINIAOD on the DR2 output files. 

The current convention used for producing an HHWWgg signal sample is running: 
- GEN-SIM with 100000 events over 200 jobs
- DR1 with 100000 events, pileup = "wPU", with a jobsize of 1 
- DR2 with 100000 events, pileup = "wPU", with a jobsize of 1 
- MINIAOD with 100000 events, pileup = "wPU", with a jobsize of 1 # Note that publish must be set to on when running this step 

### Submit CRAB Jobs 

After creating MC_Configs.json, you can submit crab jobs to run the desired configs. This is simply done with:

    . SubmitMCJobs.sh 

This script will look for the local file MC_Configs.json and submit crab jobs for each object in the json file. 

Note that when running this, the output directory of the CRAB jobs is currently hardcoded. You may wish to change this to your desired output location. This is specified for GEN and GEN-SIM jobs in with the variable outLFNDirBase in Submit_Crab_GEN.sh and in Submit_Crab_postGEN.sh for the other steps. 

You will also need to change the value of the variable localWorkingArea in Submit_Crab_GEN.sh and Submit_Crab_postGEN.sh. This should be set to the working directory containing the HHWWgg_Tools repository. 

It's also useful to manually set your VOMS proxy incase the script doesn't catch that you don't have one set. This can be done with the command:

    voms-proxy-init --voms cms --valid 168:00

as long as you have the certificate setup properly.

The CMS driver commands used to create the cmssw configs are located in MC_Producer_939.sh. 

### Example: Fully Leptonic Production

#### GEN-SIM

After cloning the repository and CMSSW_9_3_9_patch1 with the above instructions, you can put the fully leptonic madgraph/pythia configs into the proper location with the commands:

    cd HHWWgg_Tools
    cp Fragments/Outputs/FullyLeptonic/*.py CMSSW_9_3_9_patch1/src/Configuration/GenProduction/python

If done properly, this should place all of the configs in their proper spot.

The next step is to run Make_MC_Configs.py with the following flags:

    python Make_MC_Configs.py --step GEN-SIM --nEvents 100000 --jobs_jobsize 200 --finalStates lnulnugg --Resonant --masses 260, 270, 280, 300, 320, 350, 400, 500, 550, 600, 650, 700, 800, 850, 900, 1000

Then before running the scripts, make sure to change outLFNDirBase in Submit_Crab_GEN.sh and Submit_Crab_postGEN.sh, and localWorkingArea in Submit_Crab_GEN.sh and Submit_Crab_postGEN.sh to the desired values. outLFNDirBase should be set to the desired output location, and localWorkingArea should be set to the working directory containing the HHWWgg_Tools repository. After setting these and setting up your grid proxy, you can run with:

    . SubmitMCJobs.sh 

If everything works properly, this will submit 200 CRAB jobs for each mass point. 

#### DR1 

To run the DR1 step on the output from GEN-SIM, you need to input the files that were output from the GEN-SIM step. To do this, you can 

    python Make_MC_Configs.py --step GEN-SIM --nEvents 100000 --jobs_jobsize 200 --finalStates lnulnugg --Resonant --masses 260, 270, 280, 300, 320, 350, 400, 500, 550, 600, 650, 700, 800, 850, 900, 1000

    step = "DR1"
    prevStep_prefix = "GEN-SIM"
    nEvents = 100000 
    jobs_jobsize = 1 
    directory_prefix = "/path/to/GEN-SIM/output/" # location of GEN-SIM, DR1 or DR2 output files. Should contain directories with names like ggF_X260_WWgg_lnulnugg, ggF_X280_WWgg_lnulnugg, etc. 
    pileup = "wPU"
    masses = ['X260', 'X270', 'X280', 'X300', 'X320', 'X350', 'X400', 'X500', 'X550', 'X600', 'X650', 'X700', 'X800', 'X850', 'X900', 'X1000']
    finalStates = ["lnulnugg"]

After running the command python Make_MC_Configs.py, you should check the output file MC_Configs.json to make sure the entries look something like this:

    { 
            "step"      : "DR1",
            "events"    : 100000,
            "jobs_jobsize"      : 1,
            "fragment_directory"  : "/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X270_WWgg_qqlnugg/100000events_GEN-SIM/191205_151224/0000/",
            "pileup"              : "wPU" 
    }

In this example entry, the DR1 step will be run on 100000 events using output GEN-SIM files in the directory /eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/ggF_X270_WWgg_qqlnugg/100000events_GEN-SIM/191205_151224/0000/. This directory contains 400 files: 200 GEN-SIM output files containing 500 events each, and 200 LHE files. The DR1 step will take the GEN-SIM output files as intput. Because jobsize is set to 1, there will be a job submitted for each GEN-SIM output file, meaning 200 total DR1 jobs will be submitted. Because pileup is set to "wPU" as opposed to "woPU", pileup files will be searched for in order to add to the digis from the GEN-SIM output. **note** searching for pileup files takes a LONG time because there are many of them and they are all printed. There may be a way to speed this up, but for the moment you should expect it to take quite some time for each MC Config job set to be submitted. It's recommended that this is run on a screen so it doesn't get interrupted. 

If everything works properly, this should submit 200 jobs for each mass point, and should produce 200 output files for each. 

#### DR2

To run the DR2 step you need to change the directory_prefix variable to the directory containing the output directories for the mass points of the DR1 step, and then simply need to change the "step" variable to "DR2", and the prevStep_prefix variable to "wPU_DR1" if pileup was set to "wPU" in the DR1 step.

#### MINIAOD 

The MINIAOD step is the same as the DR2 step, except changing the directory_prefix variable once again, this time to the output from the DR2 step, changing the "step" variable to "MINIAOD" and the prevStep_prefix variable to "wPU_DR2" if pileup was used in the DR2 step. 
