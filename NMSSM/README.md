# NMSSM

The purpose of this directory is to produce HHWWgg NMSSM signal samples. 

## Cloning cms-sw/genproductions

You'll now need to clone the cms genproductions repository in order to produce gridpacks. You can do that with the following commands. Depending on the year you would like to produce samples corresponding to, you need to clone different branches of the repository, as the GEN group has chosen different PDF's for different years. 

### For 2016:

Via HTTPS:

    cd HHWWgg_Tools/NMSSM
    git clone -b mg242legacy https://github.com/cms-sw/genproductions.git

or via SSH:

    cd HHWWgg_Tools/NMSSM
    git clone -b mg242legacy git@github.com:cms-sw/genproductions.git


### For 2017/18:

Via HTTPS:

    cd HHWWgg_Tools/NMSSM
    git clone -b mg260legacy https://github.com/cms-sw/genproductions.git

or via SSH:

    cd HHWWgg_Tools/NMSSM
    git clone -b mg260legacy git@github.com:cms-sw/genproductions.git

**N.B.**: I've found that cloning via SSH leads to no requirement to enter my git username and password everytime I push to the remote repository, but I'm not sure how I set that up ...

## Creating Gridpacks

### Updating the Directory Name

You will find in this repository the folder "NMSSM_XYH_WWgg" containing the Template folder and generate_grid.py pythod module. The first thing you should do is change the name of this folder to match your signal process name. This should be changed to your di-Higgs final state. All that needs to be changed is "WWgg" as this is the di-Higgs final state of the HH->WWgg analysis. For example, for the bbbb final state, you would change this name to: 

    cd HHWWgg_Tools/NMSSM
    mv NMSSM_XYH_WWgg NMSSM_XYH_bbbb

more generally for your final state:

    HHWWgg_Tools/NMSSM
    mv NMSSM_XYH_WWgg NMSSM_XYH_<diHiggsFinalState>

**N.B.**: Try to create a <diHiggsFinalState> name without special characters, underscores or spaces as this could potentially cause problems later when accessing this directory. 

### Updating the MadGraph Proc Card 

In your newly named NMSSM_XYH_<diHiggsFinalState> directory, you will find the folder "Template". This contains the files necessary to create a MadGraph gridpack. For an NMSSM di-Higgs interpretation, the process created by the MadGraph gridpack is:

h03 -> h02 h01 with the convention:

h03 , pdgID 45 —> heaviest scalar
h02 , pdgID 35 —> intermediate scalar
h01 , pdgID 25 —> the Higgs boson (125 GeV)

You can see this process in Template/proc_card.dat

    generate g g > h03 , (h03 > h02 h01) 

this tells MadGraph to produce h03, a heavy scalar, via gluon gluon fusion. It's then told to decay it into h03 and h01, corresponding to an intermediate scalar and the 125 GeV higgs boson. While it is possible to further decay the h02 and h01 in MadGraph, in these instructions the procedure is to produce gg -> h03 -> h02 h01 in MadGraph and then have Pythia decay the h02 h01 into your di-Higgs final state. 

In the final line of Template/proc_card.dat, you will see the output name:

    NMSSM_XYH_WWgg_MX_TEMPLATEMH03_MY_TEMPLATEMH02

this should be changed to your di-Higgs final state in the same was as done when renaming the directory. For example, for the bbbb final state, you would change this name to: 

    NMSSM_XYH_bbbb_MX_TEMPLATEMH03_MY_TEMPLATEMH02

more generally for your final state:

    NMSSM_XYH_<diHiggsFinalState>_MX_TEMPLATEMH03_MY_TEMPLATEMH02

### Updating generate_grid.py Production Folder 

Next, you will find the python module "generate_grid.py". This is used to produce the necessary MadGraph cards to create gridpacks for each pair of (h03,h02) masses. For each mass point created, a folder will be created following the template stored in the python variable prod_proto. This should be changed to match your signal process in the same way you changed the output folder in proc_card.dat. 

So change:

    prod_proto = "NMSSM_XYH_WWgg_MX_{0}_MY_{1}" 

to:

    prod_proto = "NMSSM_XYH_<diHiggsFinalState>_MX_{0}_MY_{1}"

using the same <diHiggsFinalState> name as in proc_card.dat. For an inital test, you can leave the default mass points at the bottom of the python module:

    ## mX, mY
    points = [
        (500, 300),
        (700, 400),
    ]

this will create the folders necessary to create MadGraph gridpacks for two pairs of mass points. 

### Copy Template to genproductions

When running the gridpack generation executable, the folder with the MadGraph dat files will be searched for and needs to be located in genproductions. It's therefore recommended you copy your Template folder to genproductions like so:

    cd HHWWgg_Tools/NMSSM
    cp -r NMSSM_XYH_<diHiggsFinalState> genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/

### Produce MadGraph .dat Cards

After setting the mass points in generate_grid.py do the desired pairs, you can create folders for each with:

    cd genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/NMSSM_XYH_<diHiggsFinalState>
    python generate_grid.py 

If this worked properly, you should have two folders added:

    genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/NMSSM_XYH_<diHiggsFinalState>/NMSSM_XYH_WWgg_MX_700_MY_400
    genproductions/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/NMSSM_XYH_<diHiggsFinalState>/NMSSM_XYH_WWgg_MX_500_MY_300

Each containing four .dat files to be used by MadGraph. Looking at the MX_500_MY_300 directory for example, in NMSSM_XYH_<diHiggsFinalState>_MX_500_MY_300_customizecards.dat you should see the masses of the heavy and intermediate scalars set:

    set param_card mass 45 500
    set param_card mass 35 300

And at the bottom of the _proc_card.dat you should see the proper output name:

    output NMSSM_XYH_<diHiggsFinalState>_MX_500_MY_300 -nojpeg

### Producing a Single Gridpack

**N.B.**: I've found that when using the mg260legacy branch of genproductions in order to run with the 2017 chosen PDF, one must run the gridpack_generation script from an lxplus machine with architecture slc6_amd64_gcc630, so you may need to ssh with:

    ssh <lxplusUsername>@lxplus6.cern.ch

Following the instructions listed here: [Gridpack_Twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/QuickGuideMadGraph5aMCatNLO#Quick_tutorial_on_how_to_produce), we can now produce a gridpack for a given mass point:

    cd genproductions/bin/MadGraph5_aMCatNLO/
    ./gridpack_generation.sh <name of process card without _proc_card.dat> <folder containing cards relative to current location>

For the MX_500_MY_300 case:

    cd genproductions/bin/MadGraph5_aMCatNLO/
    ./gridpack_generation.sh NMSSM_XYH_WWgg_MX_500_MY_300 cards/production/2017/13TeV/NMSSM_XYH_<diHiggsFinalState>/NMSSM_XYH_<diHiggsFinalState>_MX_500_MY_300

This may take some time, but if you see output similar to this: 

    Running gridpack generation step ALL
    Starting job on Thu Jan 30 16:51:47 CET 2020
    Running on Linux lxplus ... 
    ...

then it should be running properly. The printout statements should eventually get to:

    preparing final gridpack

and then:

    Creating tarball

and finally:

    Gridpack created successfully at <gridpack tarball location>
    End of job

## Creating Pythia Fragments

Now that you have a gridpack, you have the step simulating the physics process gg -> h03 -> h02 h01. You can now create a Pythia configuration file that will decay the h02 h01 particles into your desired final state. This can be done in HHWWgg_Tools/Fragments, following the instructions for [NMSSM](https://github.com/NEUAnalyses/HHWWgg_Tools/tree/master/Fragments#nmssm)


## Submitting Jobs to CRAB for Production  

With your pythia fragments in hand, you can create cmssw and crab configuration files that will simulate events of your process to be further analyzed. This is done in HHWWgg_Tools/Production, following [these](https://github.com/NEUAnalyses/HHWWgg_Tools/tree/master/Production#private-mc-production) instructions, where the input madgraph/pythia configuration(s) for the GEN-SIM or GEN step should be the configuration(s) created in the steps above. 

# Local Testing 

    cmsDriver.py NMSSM_XYH_WWgg_qqlnu_MX_500_MY_300 --fileout file:NMSSM_XYH_WWgg_MX_500_MY_300_output.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename NMSSM_cmsswConfig.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(123456%100)" -n 10

    Begin processing the 8th record. Run 1, Event 8, LumiSection 1 at 20-Apr-2020 10:47:30.906 CEST
    PYTHIA Error in ResonanceDecays::next: no open decay channel for id = 35
    PYTHIA Abort from Pythia::next: reached end of Les Houches Events File  
    Begin processing the 9th record. Run 1, Event 9, LumiSection 1 at 20-Apr-2020 10:47:30.931 CEST    

    From MadAnalysis, 25 and 35 higgs have save pT spectrums...

    Running into problems decaying 35 in Pythia, so may have to set 25 and 35 decays in MadGraph
    Or maybe just set 35 decay...