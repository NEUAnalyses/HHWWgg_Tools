# HH->WWgg DNN Tools 

The purpose of the modules and functions in this directory is to process DNN outputs. The main features are categorization of events by DNN score to optimize S / sqrt(B), the creation of trees by category, and the creation of RooWorkspaces by category in order to produce signal and background models with flashggfinalfit.

## Categorization

After creating signal and data trees with DNN scores, which can be done using the [DNN_Evaluation Repository](https://github.com/bmarzocc/DNN_Evaluation), you can find category boundaries using optimize_cats.C in order to create successive S / sqrt(B) purity categories.

root -l optimize_cats.C\(\2\,\1\,\1\,\0.0\,\0.1\,\"\TestNewFiles\"\,\"/eos/user/b/bmarzocc/HHWWgg/HHWWgg_DataSignalMCnTuples/PromptPromptApplied-TagsMerged/HHWWyyDNN_binary_testnewfiles_allBkgs/\"\)
