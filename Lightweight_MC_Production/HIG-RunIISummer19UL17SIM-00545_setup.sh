#!/bin/bash

export SCRAM_ARCH=slc7_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_6_2/src ] ; then
  echo release CMSSW_10_6_2 already exists
else
  scram p CMSSW CMSSW_10_6_2
fi
cd CMSSW_10_6_2/src
eval `scram runtime -sh`

scram b
cd ../..

# EVENTS=645

# cmsDriver command
#cmsDriver.py --python_filename HIG-RunIISummer19UL17SIM-00545_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:HIG-RunIISummer19UL17SIM-00545.root --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step SIM --geometry DB:Extended --filein "dbs:/GluGluToBulkGravitonToHHTo2B2G_M-1000_narrow_TuneCP5_13TeV-madgraph-pythia8/RunIISummer19UL17wmLHEGEN-106X_mc2017_realistic_v6-v1/GEN" --era Run2_2017 --runUnscheduled --no_exec --mc -n 10




# # Run generated config
# REPORT_NAME=HIG-RunIISummer19UL17SIM-00545_report.xml
# # Run the cmsRun
# cmsRun -e -j $REPORT_NAME HIG-RunIISummer19UL17SIM-00545_1_cfg.py || exit $? ;

# # Parse values from HIG-RunIISummer19UL17SIM-00545_report.xml report
# processedEvents=$(grep -Po "(?<=<Metric Name=\"NumberEvents\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
# producedEvents=$(grep -Po "(?<=<TotalEvents>)(\d*)(?=</TotalEvents>)" $REPORT_NAME | tail -n 1)
# threads=$(grep -Po "(?<=<Metric Name=\"NumberOfThreads\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
# peakValueRss=$(grep -Po "(?<=<Metric Name=\"PeakValueRss\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
# peakValueVsize=$(grep -Po "(?<=<Metric Name=\"PeakValueVsize\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
# totalSize=$(grep -Po "(?<=<Metric Name=\"Timing-tstoragefile-write-totalMegabytes\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
# totalSizeAlt=$(grep -Po "(?<=<Metric Name=\"Timing-file-write-totalMegabytes\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
# totalJobTime=$(grep -Po "(?<=<Metric Name=\"TotalJobTime\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
# totalJobCPU=$(grep -Po "(?<=<Metric Name=\"TotalJobCPU\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
# eventThroughput=$(grep -Po "(?<=<Metric Name=\"EventThroughput\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
# avgEventTime=$(grep -Po "(?<=<Metric Name=\"AvgEventTime\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
# if [ -z "$threads" ]; then
#   echo "Could not find NumberOfThreads in report, defaulting to 1"
#   threads=1
# fi
# if [ -z "$eventThroughput" ]; then
#   eventThroughput=$(bc -l <<< "scale=4; 1 / ($avgEventTime / $threads)")
# fi
# if [ -z "$totalSize" ]; then
#   totalSize=$totalSizeAlt
# fi
# if [ -z "$processedEvents" ]; then
#   processedEvents=$EVENTS
# fi
# echo "Validation report of HIG-RunIISummer19UL17SIM-00545 sequence 1/1"
# echo "Processed events: $processedEvents"
# echo "Produced events: $producedEvents"
# echo "Threads: $threads"
# echo "Peak value RSS: $peakValueRss MB"
# echo "Peak value Vsize: $peakValueVsize MB"
# echo "Total size: $totalSize MB"
# echo "Total job time: $totalJobTime s"
# echo "Total CPU time: $totalJobCPU s"
# echo "Event throughput: $eventThroughput"
# echo "CPU efficiency: "$(bc -l <<< "scale=2; ($totalJobCPU * 100) / ($threads * $totalJobTime)")" %"
# echo "Size per event: "$(bc -l <<< "scale=4; ($totalSize * 1024 / $producedEvents)")" kB"
# echo "Time per event: "$(bc -l <<< "scale=4; (1 / $eventThroughput)")" s"
# echo "Filter efficiency percent: "$(bc -l <<< "scale=8; ($producedEvents * 100) / $processedEvents")" %"
# echo "Filter efficiency fraction: "$(bc -l <<< "scale=10; ($producedEvents) / $processedEvents")
