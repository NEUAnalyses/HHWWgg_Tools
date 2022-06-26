# Make voms proxy
#voms-proxy-init --voms cms --out $(pwd)/voms_proxy.txt --hours 4
#export X509_USER_PROXY=$(pwd)/voms_proxy.txt

export SCRAM_ARCH=slc7_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_6_9/src ] ; then
  echo release CMSSW_10_6_9 already exists
else
  scram p CMSSW CMSSW_10_6_9
fi
cd CMSSW_10_6_9/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-RunIISummer19UL17wmLHEGEN-00664 --retry 3 --create-dirs -o Configuration/GenProduction/python/HIG-RunIISummer19UL17wmLHEGEN-00664-fragment.py
[ -s Configuration/GenProduction/python/HIG-RunIISummer19UL17wmLHEGEN-00664-fragment.py ] || exit $?;
scram b
cd ../..

# cmsDriver command
#cmsDriver.py Configuration/GenProduction/python/HIG-RunIISummer19UL17wmLHEGEN-00664-fragment.py --python_filename HIG-RunIISummer19UL17wmLHEGEN-00664_1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN,LHE --fileout file:HIG-RunIISummer19UL17wmLHEGEN-00664.root --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN --geometry DB:Extended --era Run2_2017 --no_exec --mc -n 10
