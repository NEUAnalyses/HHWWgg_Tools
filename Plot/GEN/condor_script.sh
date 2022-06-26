#!/bin/sh -e 

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

python GenPlot_PD.py --CreateDataframe --genType VBFRES-100kEvents --nEvents 100000  --maxFiles 40 --dfOutName VBFToBulkGravitonToHH_WWgg_qqlnu_{node}_df --DatasetBatch VBF-Resonant --printerval 10000 --condor 
# python GenPlot_PD.py --CreateDataframe --genType VBFRES-CondorTest --nEvents 1000  --maxFiles 1 --dfOutName VBFToBulkGravitonToHH_WWgg_qqlnu_{node}_df --DatasetBatch VBF-Resonant --printerval 100 --condor 