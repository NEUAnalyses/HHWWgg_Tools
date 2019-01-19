from ROOT import *

# Need to be in cmsenv to use these 
# It seems these may be necessary for veiwing jet info in SIM objects 

# gROOT.ProcessLine( 'gSystem->Load( "libFWCoreFWLite.so" );' )
# #gROOT.ProcessLine( 'FWLiteEnabler::enable();' )
# gROOT.ProcessLine( 'AutoLibraryLoader::enable();' )
# gROOT.ProcessLine( 'gSystem->Load( "libDataFormatsFWLite.so" );' )
# gROOT.ProcessLine( 'gSystem->Load( "libDataFormatsPatCandidates.so" );' )

## Cuts to selection
Cut = ''
## Plots output location
outputLoc = '/eos/user/a/atishelm/www/analysis_plots/'

##Variables to be plotted
#[ name of tree branch, name of pdf file, name of variable, number of bins, min bin, max bin]
#Vars = []
Vars = []
Vars.append(['patPhotons_slimmedPhotons__PAT.obj.m_state.p4Polar_.fCoordinates.fPt', 'Photon_pT', 'patPhotons p_{t}',100,0,100])
Vars.append(['patJets_slimmedJets__PAT.obj.m_state.p4Polar_.fCoordinates.fPt', 'Jet_pT', 'patJet p_{t}',100,0,100])
#Vars.append(['@recoGenJets_kt4GenJets__SIM.obj.size()', 'Jet_pT', 'patJet p_{t}',100,0,100])
#Vars.append(['recoGenJets_ak4GenJets__SIM.obj.pt', 'Jet_pT', 'patJet p_{t}',100,0,100])
#Vars.append(['recoGenMETs_genMetTrue__SIM.obj.pt_', 'MET_pT', 'MET p_{t}',200,0,700])




# Maybe add directories here that are searched, where histograms are added together so no need for large hadd 



# Gen=[]

# Gen.append([ 'v_gen_mindr','v_gen_mindr',';gen_mindr;Normalized Yields',100,0,2])

# H4GFiles = []

# H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig0p1.root','m(A) = 0.1GeV',1,0,1])
# H4GFiles.append(['/eos/user/t/twamorka/sig_sep14/sig1.root','m(A) = 1 GeV', kRed, 0, 1])

# Genfiles = []

# Genfiles.append(['../AnalyzerPy/Mar26_2018/gen1.root','m(a) = 1 GeV', kGreen-2, 0, 1])
# Genfiles.append(['../AnalyzerPy/Mar26_2018/gen0p1.root','m(a) = 0.1 GeV', kBlue-9, 0, 1])

##Files to be plotted
#[ file name, legend, line color, fill color, normalization]
Files = []
#Files.append(['/afs/cern.ch/work/a/atishelm/private/H4GFlash/WWgg_miniAOD_1000events.root','test note',kBlue,kCyan-9, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/private/CMSSW_7_1_25/src/ggF_X1000_WWgg_enuenugg_20events_MiniAOD.root','e#nue#nugg',kBlue,kCyan-9, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/private/CMSSW_7_1_25/src/ggF_X1000_WWgg_jjenugg_20events_MiniAOD.root','e#nujjgg',kPink,kMagenta, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/private/ggF_X1000_WWgg_enuenugg_woPU_3events_MiniAOD.root','e#nujjgg',kGreen,kGreen-9, 0, 1])
#Files.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/WWgg_jjenugg_signal/190115_225031/0000/ggF_X1000_WWgg_jjenugg_20events_9.root','jje#nugg_combined',kBlue,kCyan-9, 0, 1])
Files.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root','enuenugg_woPU',kBlue,kCyan-9, 0, 1])

