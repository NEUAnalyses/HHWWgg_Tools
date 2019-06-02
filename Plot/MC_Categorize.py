def MC_Cat(bkg):

    bkg_colors = {
        "kBlue": ['DiPhotonJetsBox'],
        "kGreen": ['GJet'],
        }

    color = ''
    for key in bkg_colors:    
        if (bkg_colors[key][0] == bkg):
            color = key
            break 

    return color

# DiPhotonJetsBox, GJet, QCD, DYToLL, GluGluHToGG, VBFHToGG, TTGG, TTGJets, TGJets, TTJets, ttHJetToGG  