# https://research.cs.wisc.edu/htcondor/manual/v7.6/2_5Submitting_Job.html

import os 

#for job_i in range(1,5):
# for job_i in [1]:
for job_i in [1,2]:
    job_i_str = str(job_i)

    condorJobFile = '''executable              = condorScript_{job_i}.sh
    output                  = condorOutput/out_{job_i}.out
    error                   = condorError/err_{job_i}.err
    log                     = condorLog/log_{job_i}.log
    transfer_input_files    = python/Datasets.py, python/CreateDataFrame.py, python/PlotDataFrame.py, GenPlot_PD.py 

    +JobFlavour             = "longlunch"
    #requirements = (OpSysAndVer=?= "CentOS7")

    Queue 
    '''

    condorScript = '''#!/bin/sh -e 

    cp -r /afs/cern.ch/work/a/atishelm/private/HHWWgg_Tools/GenAnalysis/CMSSW_10_6_8 .
    cd CMSSW_10_6_8/src
    eval `scramv1 runtime -sh` ##-- cmsenv 
    cd ../../

    mkdir python
    mv Datasets.py python 
    mv CreateDataFrame.py python 
    mv PlotDataFrame.py python 
    touch python/__init__.py 
    mkdir Dataframes

    # python GenPlot_PD.py --CreateDataframe --genType VBFRES-100kEvents --nEvents 100000  --maxFiles 40 --dfOutName VBFToBulkGravitonToHH_WWgg_qqlnu_{node}_df --DatasetBatch VBF-Resonant{job_i} --printerval 10000 --condor 
    python GenPlot_PD.py --CreateDataframe --genType VBFRES-2-6-5-100kEvents --nEvents 100000  --maxFiles 40 --dfOutName VBFToBulkGravitonToHH_WWgg_qqlnu_{node}_df --DatasetBatch VBF-Resonant-2-6-5_{job_i} --printerval 10000 --condor 

    '''

    condorJobFile = condorJobFile.replace("{job_i}",job_i_str)
    condorScript = condorScript.replace("{job_i}",job_i_str)

    with open("condorJobFile_%s.txt"%(job_i_str), "w") as jobFile:
        jobFile.write(condorJobFile)
    
    with open("condorScript_%s.sh"%(job_i_str), "w") as cScript:
        cScript.write(condorScript)

    os.system("condor_submit condorJobFile_%s.txt"%(job_i_str))
