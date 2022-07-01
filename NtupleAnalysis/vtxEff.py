from ROOT import *
import math
from MyCMSStyle import *
gStyle.SetOptStat(0)

files = []
##name,marker color, marker style, legend
# files.append(['/eos/cms/store/user/torimoto/physics/4gamma/H4Gamma_2016Analysis/Signal_LowMassPreselOnly/signal_hgg','GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_13TeV','hgg'])
# files.append(['/eos/cms/store/user/torimoto/physics/4gamma/H4Gamma_2016Analysis/Signal_LowMassPreselOnly/signal_m_60','SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV','h4g'])
#files.append(['/afs/cern.ch/work/t/twamorka/ThesisAnalysis/CMSSW_10_5_0/src/flashgg/Signal_Jul15_ver5/signal_60/signal_m_60','SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV','h4g'])
files.append(['/eos/user/t/twamorka/Nov11_wScalesandSmearings/Signal/signal_m_60','SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV','h4g'])

Cut = []
Cut.append(['abs(dZ_hggVtx)','BS_factor_HggVtx'])
Cut.append(['abs(dZ_zeroVtx)','BS_factor_0Vtx'])
Cut.append(['abs(dZ_bdtVtx)','BS_factor_BDTVtx'])


Marker = []
# Marker.append([kGreen+2,20,'Hgg Signal wrt Hgg vtx'])
# Marker.append([kGreen+2,24,'Hgg Signal wrt 0th vtx'])
Marker.append([kBlack,20,'H4G Signal wrt Hgg vtx'])
Marker.append([kBlack,24,'H4G Signal wrt 0th vtx'])
Marker.append([kBlack,21,'H4G Signal wrt H4G vtx'])





graphs  = TMultiGraph()
leg = TLegend(0.586005, 0.543091, 0.876075, 0.732541)
leg.SetBorderSize(0)
leg.SetTextSize(0.035)
leg.SetFillColor(kWhite)
leg.SetFillStyle(0)
c0 = TCanvas("c", "c", 1)
SetPadStyle(c0)
# c0.SetGridy()
hists = []
for fi, f in enumerate(files):
    ch = TChain()
    # ch.Add(f[0]+str('.root/h4gCandidateDumper/trees/')+f[1]+str('_2photons'))
    # ch.Add(f[0]+str('.root/h4gCandidateDumper/trees/')+f[1]+str('_3photons'))
    ch.Add(f[0]+str('.root/h4gCandidateDumper/trees/')+f[1]+str('_4photons'))

    print ch.GetEntries()
    for ci, c in enumerate(Cut):
        hist = f[1]+"_"+c[0]
        print hist
        h = TH1F('h', '', 100, 0., 20.)
        ch.Draw(c[0]+ '>> h','puweight*'+str(c[1]))
        print "variable being plotted ", c[0]
        print "weight being applied ", c[1]
        print h.Integral()
        hists.append(h)

n_bins = hists[0].GetNbinsX()

for hi, h in enumerate(hists):
    gr = TGraphErrors()
    gr.SetMarkerColor()
    gr.SetMarkerStyle()
    gr.SetMarkerSize(1)
    for bin in range(1,n_bins+1):
        # print " bin=" , bin , " , dZ (cm)=" , 20./100.*bin , " -> eff= ", h.Integral(1,bin)/h.Integral() , " - " , h.Integral(1,bin-1) , " - " , h.Integral(1,bin) , " - " , h.Integral(), " - ", h.GetBinContent(bin)
        eff=h.Integral(1,bin)/h.Integral()
        gr.SetPoint(bin-1,20./100.*bin,eff)
        gr.SetPointError(bin-1,0.,math.sqrt(eff*(1-eff)/h.Integral()))
        gr.SetMarkerColorAlpha(Marker[hi][0],0.8)
        gr.SetMarkerStyle(Marker[hi][1])
    # print "***********************************************************************************"
    graphs.Add(gr)

    leg.AddEntry(gr,Marker[hi][2],"lp")

graphs.SetTitle(";dZ;Efficiency")
# graphs.GetYaxis().SetTitleOffset(1.1);
graphs.SetMinimum(0.6)
graphs.SetMaximum(1.01)


c0.Update()
line = TLine(1.,0.6,1.,1.);
line.SetLineColor(kRed+2);
line.SetLineStyle(8);
line.SetLineWidth(2);

graphs.Draw("AP same")
leg.Draw("same")
line.Draw("same")
c0.SaveAs("test_Nov13.pdf")
# c0.SaveAs("/afs/cern.ch/user/t/twamorka/www/H4Gamma/VertexEfficiencyStudy/H4G_60_Hgg_LowMassPresel_withWeight_4photonCategoryOnly.pdf")
# c0.SaveAs("/afs/cern.ch/user/t/twamorka/www/H4Gamma/VertexEfficiencyStudy/H4G_60_Hgg_LowMassPresel_withWeight_4photonCategoryOnly.png")
