"""
1 March 2022
Abraham Tishelman-Charny (thanks to Jonathon Langford)

The purpose of this module is to plot signal models from RooWorkspaces for different nuisance parameter values in order to try and understand expected nuisance impacts (HIG-21-014).

"""

# imports 
import ROOT

def PlotModel(w_, Model_, Nuisance_):
    ol = "/eos/user/a/atishelm/www/HIG-21-014/AN_20_165_v7/Investigate_Impacts/"
    ROOT.gROOT.SetBatch(True) # do not output plot image upon drawing 
    ROOT.gStyle.SetOptStat(0)  # do not plot histogram statistics in canvas 

    modelLabelDict = {
        "shapeBkg_ggh_2016_hgg_HHWWggTag_SLDNN_0" : "ggH_2016_SLDNN_0",
        "shapeBkg_ggh_2017_hgg_HHWWggTag_SLDNN_0" : "ggH_2017_SLDNN_0",
        "shapeBkg_ggh_2018_hgg_HHWWggTag_SLDNN_0" : "ggH_2018_SLDNN_0",
        "shapeBkg_vbf_2016_hgg_HHWWggTag_SLDNN_0" : "vbf_2016_SLDNN_0",
        "shapeBkg_vbf_2017_hgg_HHWWggTag_SLDNN_0" : "vbf_2017_SLDNN_0",
        "shapeBkg_vbf_2018_hgg_HHWWggTag_SLDNN_0" : "vbf_2018_SLDNN_0",
        "shapeBkg_ggh_2016_hgg_HHWWggTag_SLDNN_1" : "ggH_2016_SLDNN_1",
        "shapeBkg_ggh_2017_hgg_HHWWggTag_SLDNN_1" : "ggH_2017_SLDNN_1",
        "shapeBkg_ggh_2018_hgg_HHWWggTag_SLDNN_1" : "ggH_2018_SLDNN_1",
        "shapeBkg_vbf_2016_hgg_HHWWggTag_SLDNN_1" : "vbf_2016_SLDNN_1",
        "shapeBkg_vbf_2017_hgg_HHWWggTag_SLDNN_1" : "vbf_2017_SLDNN_1",
        "shapeBkg_vbf_2018_hgg_HHWWggTag_SLDNN_1" : "vbf_2018_SLDNN_1",        

        "shapeSig_GluGluToHHTo2G2Qlnu_2016_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_0" : "GluGluToHHTo2G2Qlnu_2016_SLDNN_0",
        "shapeSig_GluGluToHHTo2G2Qlnu_2016_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_1" : "GluGluToHHTo2G2Qlnu_2016_SLDNN_1",

        "shapeSig_GluGluToHHTo2G2Qlnu_2017_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_0" : "GluGluToHHTo2G2Qlnu_2016_SLDNN_0",
        "shapeSig_GluGluToHHTo2G2Qlnu_2017_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_1" : "GluGluToHHTo2G2Qlnu_2016_SLDNN_1",

        "shapeSig_GluGluToHHTo2G2Qlnu_2018_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_0" : "GluGluToHHTo2G2Qlnu_2016_SLDNN_0",
        "shapeSig_GluGluToHHTo2G2Qlnu_2018_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_1" : "GluGluToHHTo2G2Qlnu_2016_SLDNN_1",                
        
    }

    modelLabel = modelLabelDict[Model_]

    # plotting parameters 
    # nbins, xmin, xmax = 320, 100, 180 # full fit range 
    nbins, xmin, xmax = 80, 115, 135
    xvar = w.var("CMS_hgg_mass")

    # plot di-photon mass for three cases on same canvas: NP = 0 (pre-fit value), -1 sigma, +1 sigma 
    c = ROOT.TCanvas()

    # NP = 0 -- prefit value 
    NP = w.var(Nuisance_)
    NP.setVal(0)
    h_zero = w.pdf(Model_).createHistogram("h_zero",xvar,ROOT.RooFit.Binning(nbins, xmin, xmax))
    h_zero.SetLineColor(1)
    h_zero.Draw()

    # NP = -1 sigma value 
    NP = w.var(Nuisance_)
    NP.setVal(-1)
    h_minone = w.pdf(Model_).createHistogram("h_minone",xvar,ROOT.RooFit.Binning(nbins, xmin, xmax))
    h_minone.SetLineColor(2)
    h_minone.Draw("same")

    # NP = +1 sigma value 
    NP = w.var(Nuisance_)
    NP.setVal(1)
    h_plusone = w.pdf(Model_).createHistogram("h_plusone",xvar,ROOT.RooFit.Binning(nbins, xmin, xmax))
    h_plusone.SetLineColor(3)
    h_plusone.Draw("same")

    l = ROOT.TLegend()
    l.SetHeader("Nuisance parameter values", "C")
    l.AddEntry(h_minone, "-1 sigma")
    l.AddEntry(h_zero, "pre-fit value")
    l.AddEntry(h_plusone, "+1 sigma")
    l.Draw("same")

    #c.BuildLegend()
    c.SaveAs("%s/%s_%s.png"%(ol, modelLabel, Nuisance_))

    # delete objects to avoid possible memory leaks 
    del c 
    del h_zero 
    del h_minone 
    del h_plusone

if(__name__ == '__main__'):

    f = ROOT.TFile("SL.root","r") # open file (output from text2workspace)
    w = f.Get("w") # get RooWorkspace of all datacard objects 

    # some useful printing commands:
    # w.allPdfs()
    # w.allPdfs().Print()

    # models to inspect. E.g. single higgs GF 2017, ... 
    Models = [
        # Single Higgs
        "shapeBkg_ggh_2016_hgg_HHWWggTag_SLDNN_0",
        "shapeBkg_ggh_2017_hgg_HHWWggTag_SLDNN_0",
        # "shapeBkg_ggh_2018_hgg_HHWWggTag_SLDNN_0",
        "shapeBkg_vbf_2016_hgg_HHWWggTag_SLDNN_0",
        "shapeBkg_vbf_2017_hgg_HHWWggTag_SLDNN_0",
        # "shapeBkg_vbf_2018_hgg_HHWWggTag_SLDNN_0", 
        "shapeBkg_ggh_2016_hgg_HHWWggTag_SLDNN_1",
        "shapeBkg_ggh_2017_hgg_HHWWggTag_SLDNN_1",
        # "shapeBkg_ggh_2018_hgg_HHWWggTag_SLDNN_1",
        "shapeBkg_vbf_2016_hgg_HHWWggTag_SLDNN_1",
        "shapeBkg_vbf_2017_hgg_HHWWggTag_SLDNN_1",
        # "shapeBkg_vbf_2018_hgg_HHWWggTag_SLDNN_1",              

        # HH    
        "shapeSig_GluGluToHHTo2G2Qlnu_2016_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_0",
        "shapeSig_GluGluToHHTo2G2Qlnu_2017_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_0",
        "shapeSig_GluGluToHHTo2G2Qlnu_2018_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_0",
        "shapeSig_GluGluToHHTo2G2Qlnu_2016_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_1",
        "shapeSig_GluGluToHHTo2G2Qlnu_2017_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_1",
        "shapeSig_GluGluToHHTo2G2Qlnu_2018_hwwhgg_node_cHHH1_HHWWggTag_SLDNN_1",        
    ]

    Nuisances = [
        # correlated across years 
        # "CMS_hgg_nuisance_ShowerShapeHighR9EE_13TeVscaleCorr",
        # "CMS_hgg_nuisance_ShowerShapeLowR9EB_13TeVscaleCorr",
        # "CMS_hgg_nuisance_MaterialForward_13TeVscaleCorr",
        # "CMS_hgg_nuisance_ShowerShapeLowR9EE_13TeVscaleCorr",
        # "CMS_hgg_nuisance_LowR9EBPhi_13TeVsmear_2016", # example of non-onesided impact 
        "CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear_2016", # example of onesided impact 
        # "CMS_hgg_nuisance_HighR9EEPhi_13TeVsmear_2016" # somewhat onesided
        "CMS_hgg_nuisance_LowR9EB_13TeVscale_2017", # not as one sided 

        # # 2016 
        # "CMS_hgg_nuisance_HighR9EB_13TeVscale_2016",
        # "CMS_hgg_nuisance_LowR9EEPhi_13TeVsmear_2016",
        # "CMS_hgg_nuisance_LowR9EE_13TeVscale_2016",
        # "CMS_hgg_nuisance_LowR9EBRho_13TeVsmear_2016",
        # "CMS_hgg_nuisance_LowR9EERho_13TeVsmear_2016",
        # "CMS_hgg_nuisance_HighR9EERho_13TeVsmear_2016",
        # "CMS_hgg_nuisance_HighR9EBRho_13TeVsmear_2016",
        # "CMS_hgg_nuisance_LowR9EB_13TeVscale_2016",
        # "CMS_hgg_nuisance_HighR9EE_13TeVscale_2016",
    ]

    for Model in Models:
        print("Model:",Model)
        for Nuisance in Nuisances:
            print("Nuisance:",Nuisance)
            # don't look for year based nuisance in a model which doesn't have it 
            if( ("2016" in Nuisance) and ("2016" not in Model)):
                print("skipping")
                continue 
            if( ("2017" in Nuisance) and ("2017" not in Model)):
                print("skipping")
                continue 
            if( ("2018" in Nuisance) and ("2018" not in Model)):
                print("skipping")
                continue                        
            PlotModel(w, Model, Nuisance)

    # useful printing commands:
    #w.pdf("hggpdfsmrel_ggh_single_Higgs_2017_HHWWggTag_SLDNN_0_13TeV")
    #w.allPdfs().selectByName("*hggpdfsmrel_ggh_single_Higgs_2017_HHWWggTag_SLDNN_0_13TeV*")
    #w.allPdfs().selectByName("*hggpdfsmrel_ggh_single_Higgs_2017_HHWWggTag_SLDNN_0_13TeV*").Print()
    #w.allPdfs().selectByName("*ggh_single_Higgs_2017_HHWWggTag_SLDNN_0_13TeV*").Print()
    #w.pdf("gaus_g0_ggh_single_Higgs_2017_HHWWggTag_SLDNN_0_13TeV").Print("v")
    #w.pdf("shapeBkg_ggh_2017_hgg_HHWWggTag_SLDNN_0")
    #w.pdf("shapeBkg_ggh_2017_hgg_HHWWggTag_SLDNN_0").Print()

    # NP.Print()
    # NP.setVal(1)
    # h_NP1 = w.pdf("shapeBkg_ggh_2017_hgg_HHWWggTag_SLDNN_0").createHistogram("h_NP1",xvar,ROOT.RooFit.Binning(320, 100, 180))
    # h_NP1.SetLineColor(2)
    # h_NP1.Draw()
    # h.Draw("same")
