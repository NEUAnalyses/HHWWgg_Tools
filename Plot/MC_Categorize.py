def MC_Cat(bkg): 
    # print'bkg = ',bkg
    bkg_cat_ = ''
    #bkg_cat_ = bkg.split('/')[-1].split('_')[1] # background label 
    bkg_cat_ = bkg.split('_')[0] # background label 
# Before '-' to '_' conversion:
#
# DiPhotonJetsBox_M40_80-Sherpa
# DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa
# GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8
# GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8
# GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8
# QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8
# QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8
# QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8
#  "DYToLL"   : [ "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1-74c0514daa3d87bd951f57782e8afcd5/USER" ]
# GluGluHToGG_M-125_13TeV_powheg_pythia8
# VBFHToGG_M-125_13TeV_powheg_pythia8
# VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8
# TTGG_0Jets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8
# TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8
# TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8
# TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
# ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_v2

    # bkg_categories = {
    #     "DiPhoton":['DiPhotonJetsBox_M40_80_Sherpa'],
    #     "DiPhoton":['DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa'],
    #     "GJet":['GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCUETP8M1_13TeV_Pythia8'],
    #     "GJet":['GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCUETP8M1_13TeV_Pythia8'],
    #     "GJet":['GJet_Pt_40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8'],
    #     "QCD":['QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCUETP8M1_13TeV_Pythia8'], 
    #     "QCD":['QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCUETP8M1_13TeV_Pythia8'], 
    #     "QCD":['QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCUETP8M1_13TeV_Pythia8'], 
    #     #"":[''], # reserved for DYToLL
    #     "":['GluGluHToGG_M_125_13TeV_powheg_pythia8'], 
    #     "":['VBFHToGG_M_125_13TeV_powheg_pythia8'], 
    #     "":['VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8'], 
    #     "":['TTGG_0Jets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8'], 
    #     "":['TTGJets_TuneCUETP8M1_13TeV_amcatnloFXFX_madspin_pythia8'], 
    #     "":['TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8'], 
    #     "":['TTJets_TuneCUETP8M1_13TeV_madgraphMLM_pythia8'], 
    #     "":['ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_v2'], 
    # }

    bkg_categories = {
        "0": ['DiPhotonJetsBox'],
        "1": ['GJet'],
        "2": ['QCD'],
        "3": ['DYToLL'],
        "4": ['DYJetsToLL'],
        "5": ['GluGluHToGG'],
        "6": ['VBFHToGG'],
        "7": ['TTGG'],
        "8": ['TTGJets'],
        "9": ['TGJets'],
        "10": ['TTJets'],
        "11": ['ttHJetToGG'],
        }

    bkg_colors = {
        "kRed": ['DiPhotonJetsBox'],
        "kOrange": ['GJet'],
        "kYellow": ['QCD'],
        "kSpring": ['DYToLL'],
        "kBlack": ['DYJetsToLL'],
        "kGreen": ['GluGluHToGG'],
        "kTeal": ['VBFHToGG'],
        "kCyan": ['TTGG'],
        "kAzure": ['TTGJets'],
        "kBlue": ['TGJets'],
        "kViolet": ['TTJets'],
        "kMagenta": ['ttHJetToGG'],
        }

    color = ''
    for key in bkg_colors:    
        if (bkg_colors[key][0] == bkg_cat_):
            color = key
            break 

    if color == '':
        print'I couldn\'t find a predefined color for the background category:',bkg_cat_
        print'Exiting'
        exit(0)

    icat = ''
    for key in bkg_categories:    
        if (bkg_categories[key][0] == bkg_cat_):
            icat = key
            break 

    if icat == '':
        print'I couldn\'t find the background category:',bkg_cat_
        print'Exiting'
        exit(0)

    return icat, color
