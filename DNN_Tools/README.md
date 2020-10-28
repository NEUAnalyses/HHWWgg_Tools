# HH-->WWgg DNN Tools 

The purpose of the modules and functions in this directory is to process DNN outputs. The main features are categorization of events by DNN score to optimize S / sqrt(B), the creation of trees by category, and the creation of RooWorkspaces by category in order to produce signal and background models with flashggfinalfit.

## Categorization

After creating signal, backgrounds, and data trees with a DNN score branch, which can be done using the [DNN_Evaluation Repository](https://github.com/bmarzocc/DNN_Evaluation), you can find category boundaries using optimize_cats.C in order to create successive S / sqrt(B) purity categories.

The macro optimize_cats.C can be run with a command with the corresponding variables:

    root -l optimize_cats.C\(\<NCATS>\,\<scaleBkgSideband>\,\<verbose>\,\<xcutoff>\,\<bin_width_>\,\<ext>\,\<nTupleLocation>\)

Where each variable is defined as the following:

- NCATS: The number of categories to make. For the current macro this cannot exceed 4. 
- scaleBkgSideband: Scale the background in both the signal and sideband regions by the ratio of the integral of the data in the sidebands to the background integral in the sidebands. 
- verbose: Print extra messages.
- xcutoff: Minimum x value in DNN score to use in categorization. Useful if there is a very low score bin with different signal and background scores than the other bins which may throw off the categorization.
- bin_width_: Width of DNN score bin. Can alter categorization. 
- ext: File extension for outputs.
- nTupleLocation: Location of Signal, Background and Data ntuples containing DNN score branch. Macro will look for files in the nTupleLocation subdirectories: Signal, Data, Bkgs, so make sure these subdirectories exist. Also note that file names and tree names expected by optimize_cats.C may need to be changed. 

Make sure to also care for signal normalization with properly WWgg final state branching ratio. For example, 0.441 is used for the semi-leptonic final state. Also take care to use the proper luminosity for scaling.  

An example command to run this is:

    root -l optimize_cats.C\(\2\,\1\,\1\,\0.0\,\0.1\,\"\TestNewFiles\"\,\"/eos/user/b/bmarzocc/HHWWgg/HHWWgg_DataSignalMCnTuples/PromptPromptApplied-TagsMerged/HHWWyyDNN_binary_testnewfiles_allBkgs/\"\)

Note that when running, background trees are defined in a map in the GetMCTreeName function in the CatOptUtils macro. You should make sure your background files have their tree names mapped here in order to be accessible by the optimize_cats.C macro. 

If the optimize_cats command works properly, you should find output files of the DNN score for signal and background, as well as S / sqrt(B) vs DNN score bin, with vertical lines to visualize the difference categories. Of importance for the next step is the output "Borders_..._.txt", containing one line with the borders of the categories. Which for example may look like this: 

    0	0.7	1.00001	

In this case, there are two categories: 0-0.7 and 0.7-1.00001. The 1.00001 is used in order to include entries with a value of 1. 

You should also see a txt file whose name ends with "CatSignificances". This contains the S / sqrt(B) values for each category. These are not used by any subsequent steps, but are useful to know as they are a rough approximation of the result from the asymptotic limit method calculation by combine. 

## Categorize Trees

Now that you have optimized category boundaries, the next step is to separate your trees by category in order to eventually combine as separate categories in signal fitting, background fitting, and combine results. This is done with the python module CategorizeTrees.py 

An example command to run this with the previous step's output is the following:

    python reduceTrees.py --iD /eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN_addWjets/ForResults_Signal_Combined/ --opt signal --year 2017  --oD /eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN_addWjets/Signal_ForResults_Skimmed/ --nCat /eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/DNN/DNN_Categorization/Borders_noSidebandScale_3cats.txt

Where each flag is defined as follows:

- iD: Input directory. 