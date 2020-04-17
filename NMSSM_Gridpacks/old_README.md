# HHWWgg NMSSM

The purpose of this directory is to produce HHWWgg NMSSM samples. 

## Cloning the Repository

After moving to your desired working directory, the cloning should be done with:

Via HTTPS:

    git clone -b HHWWgg_NMSSM https://github.com/NEUAnalyses/HH_WWgg.git 

or via SSH:

    git clone -b HHWWgg_NMSSM git@github.com:NEUAnalyses/HH_WWgg.git

then enter the working area:

    cd HH_WWgg/HHWWgg_NMSSM

you'll now need to clone the cms genproductions repository in order to produce gridpacks. You can do that with the following commands. Depending on the year you would like to produce samples corresponding to, you need to clone different branches of the repository, as the GEN group has chosen different PDF's for different years. 

### For 2016:

Via HTTPS:
    git clone -b mg242legacy https://github.com/cms-sw/genproductions.git

or via SSH:

    git clone -b mg242legacy git@github.com:cms-sw/genproductions.git


### For 2017/18:

Via HTTPS:
    git clone -b mg260legacy https://github.com/cms-sw/genproductions.git

or via SSH:

    git clone -b mg260legacy git@github.com:cms-sw/genproductions.git

