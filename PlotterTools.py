from ROOT import *

## Cuts to selection
Cut = ''
## Plots output location
outputLoc = '/eos/user/a/atishelm/www/analysis_plots/'

##Variables to be plotted
#[ name of tree branch, name of pdf file, name of variable, number of bins, min bin, max bin, xaxis title]
Vars = []

# MINIAOD variables
Vars.append(['patPhotons_slimmedPhotons__PAT.obj.m_state.p4Polar_.fCoordinates.fPt', 'Photon_pT', 'patPhotons p_{t}',100,0,100,'patphoton_pt'])
Vars.append(['patJets_slimmedJets__PAT.obj.m_state.p4Polar_.fCoordinates.fPt', 'Jet_pT', 'patJet p_{t}',100,0,100,'patjet_pt'])

# MICROAOD variables 
# Vars.append(['flashggDiPhotonCandidates_flashggDiPhotons__FLASHggMicroAOD.obj.m_state.p4Polar_.fCoordinates.fM', 'DiPhotonMass', 'DiPhotonMass',50,0,250])     
# Vars.append(['flashggDiPhotonCandidates_flashggDiPhotons__FLASHggMicroAOD.obj.m_state.p4Polar_.fCoordinates.fPt', 'DiPhotonpt', 'DiPhotonpt',50,0,250])
# Vars.append(['flashggMets_flashggMets__FLASHggMicroAOD.obj.sumet', 'MET_sumet', 'MET_sumet',100,0,2000])    

# TAG file variables 

#Vars.append(['flashggMets_flashggMets__FLASHggMicroAOD.obj.m_state.p4Polar_.fCoordinates.fPt', 'ptmiss', 'ptmiss',50,0,1000,'p_{T}_{miss}']) 
#Vars.append(['flashggDiPhotonCandidates_flashggPreselectedDiPhotons__FLASHggTag.obj.m_state.p4Polar_.fCoordinates.fM', 'PreSel_Dipho_M', 'PreSel_Dipho_M',90,100,150,'M_{#gamma#gamma}'])

#Vars.append(['flashggJets_flashggUnpackedJets_0_FLASHggTag.obj.m_state.vertex_.fCoordinates.fPt','Jet0_pt','Jet0_pt',50,0,1000])
#Vars.append(['flashggJets_flashggUnpackedJets_1_FLASHggTag.obj.m_state.vertex_.fCoordinates.fPt','Jet0_pt','Jet0_pt',50,0,1000])

#flashggDiPhotonCandidates_flashggDiPhotons__FLASHggMicroAOD.obj.m_state.p4Polar_.fCoordinates.fEta
#flashggDiPhotonCandidates_flashggDiPhotons__FLASHggMicroAOD.obj.m_state.p4Polar_.fCoordinates.fPt

# Maybe add directories here that are searched, where histograms are added together so no need for large hadd 

##Files to be plotted
#[ file name, legend, line color, fill color, normalization]
Files = []
#Files.append(['/afs/cern.ch/work/a/atishelm/private/H4GFlash/WWgg_miniAOD_1000events.root','test note',kBlue,kCyan-9, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/private/CMSSW_7_1_25/src/ggF_X1000_WWgg_enuenugg_20events_MiniAOD.root','e#nue#nugg',kBlue,kCyan-9, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/private/CMSSW_7_1_25/src/ggF_X1000_WWgg_jjenugg_20events_MiniAOD.root','e#nujjgg',kPink,kMagenta, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/private/ggF_X1000_WWgg_enuenugg_woPU_3events_MiniAOD.root','e#nujjgg',kGreen,kGreen-9, 0, 1])
#Files.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/WWgg_jjenugg_signal/190115_225031/0000/ggF_X1000_WWgg_jjenugg_20events_9.root','jje#nugg_combined',kBlue,kCyan-9, 0, 1])
Files.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD/190119_131750/0000/ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root','enuenugg_woPU',kBlue,kCyan-9, 0, 1])

#Files.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190121_082606/0000/ggF_X1000_WWgg_jjenugg_wPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root','jjenugg_wPU',kBlue,kCyan-9, 0, 1])

#Files.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190121_101134/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root','jjenugg_woPU',kBlue,kCyan-9, 0, 1])

# MINIAOD Files

Files.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD/190121_101134/0000/ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root','csenu_woPU_miniaod',kRed,kRed-10, 0, 1])

#Files.append(['/afs/cern.ch/work/a/atishelm/15JanFlashgg/CMSSW_8_0_26_patch1/src/flashgg/myMicroAODoutput_ggF_X1000_WWgg_enuenugg_woPU_10000events_1_DR1_1_DR2_1_MINIAOD_1.root','enuenu_woPU_micro',kBlue,kCyan-9, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/15JanFlashgg/CMSSW_8_0_26_patch1/src/flashgg/myMicroAODOutput_ggF_X1000_WWgg_jjenugg_woPU_1000events_GEN_1_DR1_1_DR2_1_MINIAOD_1.root','jjenu_woPU_micro',kRed,kRed-9, 0, 1])

# Tag Files

#Files.append(['/afs/cern.ch/work/a/atishelm/15JanFlashgg/CMSSW_8_0_26_patch1/src/flashgg/myTagOutputFile.root','csenu_woPU_micro',kRed,kRed-10, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/15JanFlashgg/CMSSW_8_0_26_patch1/src/flashgg/myTagOutputFile2.root','enuenu_woPU_micro',kBlue,kCyan, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/15JanFlashgg/CMSSW_8_0_26_patch1/src/flashgg/myTagOutputFile3.root','munumunu_woPU_micro',kGreen+1,kGreen-10, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/15JanFlashgg/CMSSW_8_0_26_patch1/src/flashgg/myTagOutputFile.root','csenu_woPU_micro',kRed,kWhite, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/15JanFlashgg/CMSSW_8_0_26_patch1/src/flashgg/myTagOutputFile2.root','enuenu_woPU_micro',kBlue,kWhite, 0, 1])
#Files.append(['/afs/cern.ch/work/a/atishelm/15JanFlashgg/CMSSW_8_0_26_patch1/src/flashgg/myTagOutputFile3.root','munumunu_woPU_micro',kGreen+1,kWhite, 0, 1])

#Directories = []
# [ directory path, legend, line color, fill color, normalization ]
#Directories.append(['/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal/MinBias/ggF_X1000_WWgg_enuenugg_woPU_10000events_woPU/190116_231710/0000/','',kBlue,kCyan-9, 0, 1])