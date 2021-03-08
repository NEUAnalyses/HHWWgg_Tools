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

Note that when running, background trees are defined in a map in the GetMCTreeName function in the CatOptUtils macro. You should make sure your background files have their tree names mapped here in order to be accessible by the optimize_cats.C macro. Also note the slashes included in the command. These are required for proper formatting. 

If the optimize_cats command works properly, you should find output files of the DNN score for signal and background, as well as S / sqrt(B) vs DNN score bin, with vertical lines to visualize the difference categories. Of importance for the next step is the output "Borders_..._.txt", containing one line with the borders of the categories. Which for example may look like this: 

    0	0.7	1.00001	

In this case, there are two categories: 0-0.7 and 0.7-1.00001. The 1.00001 is used in order to include entries with a value of 1. 

You should also see a txt file whose name ends with "CatSignificances". This contains the S / sqrt(B) values for each category. These are not used by any subsequent steps, but are useful to know as they are a rough approximation of the result from the asymptotic limit method calculation by combine. 

## Tree Categorization

Now that you have optimized category boundaries, the next step is to separate your trees by category in order to eventually combine as separate categories in signal fitting, background fitting, and combine results. This is done with the python module CategorizeTrees.py 

An example command to run this with the previous step's output is the following:

    python CategorizeTrees.py --iD /eos/user/b/bmarzocc/HHWWgg/HHWWgg_DataSignalMCnTuples/PromptPromptApplied-TagsMerged/HHWWyyDNN_binary_testnewfiles_allBkgs/Signal/  --opt signal --year 2017  --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFiles/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools/Borders_withSidebandScale_TestNewFiles.txt

Where each flag is defined as follows:

- iD: Input directory. When running over signal, this should contain a signal file (need to extend to multiple)
- opt: Option. "signal" or "Data". 
- year: 2016, 2017 or 2018 
- oD: Output directory. Location to put categorized trees.
- nCat: Text file with category borders created from optimize_cats.C macro.

Important: Make sure the common_cut selection is the same as your optimize_cats selection, which should also be the same as your training selections to keep everything consistently optimized for a certain phase space. 

If this works properly, you should have an output file "signal_CategorizedTrees.root" containing a tree for each category, where the purist to least pure category goes from 0 --> N. 

A similar command is run for data:

    python CategorizeTrees.py --iD /eos/user/b/bmarzocc/HHWWgg/HHWWgg_DataSignalMCnTuples/PromptPromptApplied-TagsMerged/HHWWyyDNN_binary_testnewfiles_allBkgs/Data/  --opt Data --year 2017  --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFiles/ --nCat /eos/user/a/atishelm/www/HHWWgg/DNN_Tools/Borders_withSidebandScale_TestNewFiles.txt

The only differences here are the location being changed to the directory containing the data file, and the opt option being changed to Data. If this works, you should find a Data_CategorizedTrees.root output file with one tree per category. 

## Workspace Categorization

Now that you have trees with events separated by category, you will need a RooWorkspace in order for your files to be compatible with flashggfinalfit. This is done using the python module MakeCategorizedWorkspaces.py. 

**Important:** When creating workspaces, you must do so in the same cms environment that will be used to open the workspaces in flashggfinalfit, otherwise you will run into errors. You can do this by running the following commands **before** running the MakeCategorizedWorkspaces module:

    cd <flashggFinalFitArea>
    cmsenv
    cd /<HHWWgg_Tools_Area>/DNN_Tools/

This way when you run the workspace creation module, you will be doing so in the cms environment that will be used when you run flashggfinalfit. 

An example command run this step after setting up the proper cms environment:

    python MakeCategorizedWorkspaces.py --iD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFiles/Signal/ --i signal  --opt signal --t PerYear  --year 2017  --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFiles/

Where each flag is defined as follows:

- iD: Input directory. This should contain the output from the Categorize Trees step.
- i: Name for output file. 
- opt: signal or data.
- t: Type of splitting. PerYear to create separate models per year, or Run2 to combine three years into single model. 
- year: 2016, 2017 or 2018 
- oD: Output directory. Where to place the categorized workspaces. 

Note: You may see a large  "Memory map" printout due to something looking like "Error in `python': free(): invalid pointer: 0x000000000a616c4c", and "Backtrace" outputs. The cause of this is unknown, but it appears this does not corrupt the output files, so for now can be safely ignored. 

If this works properly, the output directory should contain a root file with the TDirectoryFile tagsDumper, containing a RooWorkspace cms_hgg_13TeV. You can print the contents of the RooWorkspace with cms_hgg_13TeV->Print() (after tagsDumper->cd()). You should see a RooDataset for each tag. These will be used to create signal models with flashggfinalfit. 

A similar command is run to run over data: 

    python MakeCategorizedWorkspaces.py --iD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFiles/Data/ --i data  --opt data --t PerYear  --year 2017  --oD /eos/user/a/atishelm/ntuples/HHWWgg_DNN_Categorization/TestNewFiles/

The difference between this and the signal command are that the input directory is changed to the data output location from the categorize trees step, and the i and opt flags are changed to data. If this works properly, you should have a data root file output in the output location. 