# NtupleAnalysis

The purpose of the python modules in this directory is to analyze flashgg outputs from the dumpers and tagger in HHWWgg_dev. At the moment there are two features: Signal efficiency and Data / MC comparisons. 

**Note**: Can probably speed up plotting by implementing uproot 

## Data / MC: Example Usage and Explanation 

**Note**: Plots are setup to output onto a CERN website. The website path needs to be set by the user in the python module NtupleAnalysis: [here](https://github.com/NEUAnalyses/HHWWgg_Tools/blob/master/NtupleAnalysis/NtupleAnalysis.py#L36-L37), where ol = output location. Note that you can also set a separate output location to test features (the ol definition when args.testFeatures is true).  

An example command to produce Data / MC comparison plots and yields tables is: 

    python NtupleAnalysis.py --DataMC --dataFolder Data --mcFolder Backgrounds --signalFolder Signal --VarBatch mass --CutsType Loose --Lumi 41.5 --Tags HHWWggTag_0,HHWWggTag_1,HHWWggTag_2,combined --noQCD --verbose 

An explanation of each flag in the command: 

- DataMC: Produce Data / MC ratios and yields tables 
- dataFolder: The folder to search for data nTuples. This folder will be looked for in the location of the public nTuples: /afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/, as defined [here](https://github.com/NEUAnalyses/HHWWgg_Tools/blob/master/NtupleAnalysis/NtupleAnalysis.py#L38)
- mcFolder: The folder to search for background nTuples. This folder will also be searched for in /afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/
- signalFolder: The folder to search for signal nTuples. Again searched for in /afs/cern.ch/work/a/atishelm/public/ForJosh/2017_DataMC_ntuples_moreVars/
- VarBatch: The batch of variables to plot. These are defined in [VariableTools](https://github.com/NEUAnalyses/HHWWgg_Tools/blob/master/NtupleAnalysis/python/VariableTools.py#L20-L158). Note that "mass" is the most basic variable batch, as it only includes the diphoton mass. Current VarBatch options include:
    - mass: Only diphoton mass
    - MVA: Variables potentially useful for MVA study
    - MVA2: More potentially useful MVA study variables 
    - MET: MET Variables. MET pT and MET phi 
    - Photon: pt, eta, E and MVA score of leading and subleading photons 
    - Loose: pt, eta, E of the leading lepton. Meant to be used in conjunction with Loose cuts 
    - all: All tree variables. Warning: This is a LOT of variables and may take forever to run! 
    - special: dR between leading and subleading jets  

- CutsType: The cuts to apply, defined in [CutsTools](https://github.com/NEUAnalyses/HHWWgg_Tools/blob/master/NtupleAnalysis/python/CutsTools.py#L11-L72). In this example Loose is used. The requires exactly one lepton passing loose selections, and at least two jets passing loose selections. Cut options include:
    - Loose: Described above
    - PreSelections: No additional ntuple cuts because preselection already applied
    - final: Apply final analysis selections (may be missing one or two like Tight2017 Jet ID)
    - final-noPhoSels: Apply b Veto, exactly one good lepton, at least two good jets selections (Tight2017 Jet ID may be missing)
    - final-noPhoMVA: Apply b Veto, exactly one good lepton, at least two good jets selections (Tight2017 Jet ID may be missing), and photon pT/mgg selections
    - bVeto-OneLep: Apply b Veto, exactly one good lepton selections 
- Lumi: The luminosity value to scale MC and Signal by in fb-1. Currently required because in flashgg output ntuples are scaled to luminosity 1 fb-1. The example here uses 41.5 for 2017 luminosity.
- Tags: The HHWWgg tags to run on:
    - HHWWggTag_0: Semileptonic electron channel requiring exactly one good lepton and at least two good jets 
    - HHWWggTag_1: Semileptonic muon channel requiring exactly one good lepton and at least two good jets 
    - HHWWggTag_2: Any events that do not fall into categories 0 and 1 
    - combined: Combine all events in ntuples
-- noQCD: Do not add QCD to plots and yields tables for HHWWggTag_0 and HHWWggTag_1. This was added because with some cut options, there are very few QCD events with high weights that are not meaningful
--verbose: Add various print statements while running to provide extra information

**Note**: The first time you run things may run slowly, but I've found when running a second time things speed up. I'm not sure why. It may have to do with the loading of certain modules only being done the first time. I am not sure if things run faster if the ntuples are stored in your CERN box instead of the public space in /afs/cern.ch/work. Might be worth copying the files to your cern box and trying.

If everything works properly, after the running the above command you should find scaled and non-scaled yields tables in your output location. There sould also be a directory created inside your output location titled Loose for loose selections, which should contain four plots: The Data / MC ratio with signal for each tag: 0, 1, 2, combined.

## More Example Commands

A few example commands that can be attempted if you want to test things and get an idea of your options.

Final analysis selections, blinded signal region (no events can fall in HHWWggTag_2):

    python NtupleAnalysis.py --DataMC --dataFolder Data --mcFolder Backgrounds --signalFolder Signal --VarBatch mass --CutsType final --Lumi 41.5 --Tags HHWWggTag_0,HHWWggTag_1,combined --noQCD --verbose 

Plot leading lepton kinematics with loose selections:

    python NtupleAnalysis.py --DataMC --dataFolder Data --mcFolder Backgrounds --signalFolder Signal --VarBatch Loose --CutsType Loose --Lumi 41.5 --Tags HHWWggTag_0,HHWWggTag_1,HHWWggTag_2,combined --noQCD --verbose 

Plot MET variables with loose selections:

    python NtupleAnalysis.py --DataMC --dataFolder Data --mcFolder Backgrounds --signalFolder Signal --VarBatch MET --CutsType Loose --Lumi 41.5 --Tags HHWWggTag_0,HHWWggTag_1,HHWWggTag_2,combined --noQCD --verbose 

Photon variables with loose selections:

    python NtupleAnalysis.py --DataMC --dataFolder Data --mcFolder Backgrounds --signalFolder Signal --VarBatch Photon --CutsType Loose --Lumi 41.5 --Tags HHWWggTag_0,HHWWggTag_1,HHWWggTag_2,combined --noQCD --verbose 
