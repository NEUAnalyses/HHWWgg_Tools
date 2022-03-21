# How to run the gen plotter / analyzer

https://github.com/NEUAnalyses/HHWWgg_Tools/blob/17e9f2b08411adc2a7e4baf7ced26cfb2b62e394/Plot/GEN/GenPlot_PD.py

Where you can see an example plotting command I used for a recent Phase II file check first to create a dataframe: 

python GenPlot_PD.py --CreateDataframe --genType NONRES --nEvents 1000  --maxFiles 1 --dfOutName PhaseII_HHWWgg --DatasetBatch PhaseIIHHWWgg-GF-nonres-SM --printerval 100

And then to plot variables from the dataframe: 

python GenPlot_PD.py --PlotDataFrame --dfTypes NONRES --outDirectory NONRES_PhaseII --extraVariables HH_invmass --particles Lead_H,Sublead_H --variables pt --plotSingles

When you create a dataframe from a file with the first step, you need to make sure the directory is defined in the MasterDatasetDict  dictionary: 

https://github.com/NEUAnalyses/HHWWgg_Tools/blob/17e9f2b08411adc2a7e4baf7ced26cfb2b62e394/Plot/GEN/python/Datasets.py#L12

Where for example you can just follow what I did for a Phase II file but use the proper location which I believe needs to be on /cms/store 

https://github.com/NEUAnalyses/HHWWgg_Tools/blob/17e9f2b08411adc2a7e4baf7ced26cfb2b62e394/Plot/GEN/python/Datasets.py#L88-L91

Where you can see the dataset name in the dictionary "PhaseIIHHWWgg-GF-nonres-SM" is defined as the --DatasetBatch flag argument in the create dataframe command

I think by default the dataframe should already save information from the gg and tau tau at least in the pdgId variable. I would suggest running this on your ggTauTau file and look at the output dataframe to see if it contains useful variables. You can see here the code used to obtain gen particle information: 

https://github.com/NEUAnalyses/HHWWgg_Tools/blob/17e9f2b08411adc2a7e4baf7ced26cfb2b62e394/Plot/GEN/python/CreateDataFrame.py#L194-L256
