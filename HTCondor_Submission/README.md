# HTCondor Subimssion

This directory contains example files for running python modules over condor. The main advatange of this is the parallelization of computational tasks. 

## Example usage 

After moving to your desired working directory, the cloning should be done with:

Via HTTPS:

    git clone https://github.com/NEUAnalyses/HHWWgg_Tools.git 

or via SSH:

    git clone git@github.com:NEUAnalyses/HHWWgg_Tools.git

then:

```
  cd HHWWgg_Tools/HTCondor_Submission
  python Condor_Submission.py --outDir <outputDirectory> 
```

If the jobs were successfully submitted, you can check their status with `condor_q`. If you would like to kill all of your condor jobs, for example if you know there is a mistake, you can do so with `condor_rm <lxplusUsername>`. 

You can also monitor your jobs with a [Monidor](https://github.com/atishelmanch/Monidor). 
