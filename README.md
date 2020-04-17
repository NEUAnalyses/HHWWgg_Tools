# HHWWgg Tools

Contacts: 
- Abraham Tishelman-Charny - abraham.tishelman.charny@cern.ch 
- Badder Marzocchi - badder.marzocchi@cern.ch
- Toyoko Orimoto - Toyoko.Orimoto@cern.ch 

Presentations: 
- [11 November 2019 Analysis Update](https://indico.cern.ch/event/847923/contributions/3632148/attachments/1942588/3221820/HH_WWgg_Analysis_Update_11_November_2019_2.pdf)
- [21 October 2019 Analysis Status](https://indico.cern.ch/event/847927/contributions/3606888/attachments/1930081/3196452/HH_WWgg_Analysis_Status_21_October_2019.pdf)

Repositories:
- [HHWWgg Development](https://github.com/atishelmanch/flashgg/tree/HHWWgg_dev)
- [HHWWgg MicroAOD Production](https://github.com/atishelmanch/flashgg/tree/HHWWgg_Crab)

The purpose of this repository is to create private monte carlo samples for the HH->WWgg analysis. Main features:

1) Private MC production with centralled produced gridpacks 
2) Creation of NMSSM gridpacks for HH analyses
3) Creation of pythia fragments interfaced with a MadGraph gridpack 

# Cloning the Repository

After moving to your desired working directory, the cloning should be done with:

Via HTTPS:

    git clone https://github.com/NEUAnalyses/HHWWgg_Tools.git 

or via SSH:

    git clone git@github.com:NEUAnalyses/HHWWgg_Tools.git

# NMSSM Gridpacks

In order to create NMSSM gridpacks for HH analysis interpretations, see the README in the [NMSSM directory](https://github.com/NEUAnalyses/HHWWgg_Tools/tree/master/NMSSM#nmssm)

# Pythia Fragments 

To create pythia fragments interfaced with MadGraph gridpacks, see the README in the [Fragments directory](https://github.com/NEUAnalyses/HHWWgg_Tools/tree/master/Fragments#fragments) 

# Private MC Production

To submit jobs for creation of private MC, see the [Production directory](https://github.com/NEUAnalyses/HHWWgg_Tools/tree/master/Production#private-mc-production) 