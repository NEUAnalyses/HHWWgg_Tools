# NtupleAnalysis

The purpose of the python modules in this directory is to analyze flashgg outputs from the dumpers and tagger in HHWWgg_dev. At the moment there are two features: Signal efficiency and Data / MC comparisons. 

**Note**: Can probably speed up plotting by implementing uproot 

## Data / MC: Example Usage and Explanation 

An example command to produce Data / MC comparison plots and yields tables is: 

    python NtupleAnalysis.py --DataMC --dataFolder Data --mcFolder Backgrounds --signalFolder Signal --VarBatch PhotonVars --CutsType Loose --Lumi 41.5 --Tags HHWWggTag_0,HHWWggTag_1,HHWWggTag_2,combined --verbose --noQCD

**Note**: Plots are setup to output on a CERN website. This needs to be set by the user in the python module NtupleAnalysis: [here](https://github.com/NEUAnalyses/HHWWgg_Tools/blob/master/NtupleAnalysis/NtupleAnalysis.py#L76-L77), where ol = output location. Note that you can also set a separate output location to test features (the ol definition when args.testFeatures is true).  

An explanation of each flag in the command: 

- DataMC: This means to run the modules to plot Data / MC ratios and produce yields tables 
- dataFolder: This is the folder to search for data nTuples. This folder will be looked for in the location of the public nTuples: /afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/
- mcFolder: The folder to search for background nTuples. This folder will also be searched for in /afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/
- signalFolder: The folder to search for signal nTuples. Again searched for in /afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/
- VarBatch: The batch of variables to plot. These are defined in [python/VariableTools.py](https://github.com/NEUAnalyses/HHWWgg_Tools/blob/master/NtupleAnalysis/python/VariableTools.py) 