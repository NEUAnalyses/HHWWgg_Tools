###########################################################################################################################
# Abraham Tishelman-Charny
# 13 May 2020
#
# The purpose of this module is to provide plotting related variables and definitions for NtupleAnalysis.py 
#
###########################################################################################################################
from ROOT import TCanvas 

def GetColors():
    colorsTemp_ = [kRed, kOrange, kCyan, kBlue, kBlack, kGreen]
    colors_ = []
    for ic in colorsTemp_:
        colors_.append(ic)
        colors_.append(ic+2)
        colors_.append(ic-2)
        colors_.append(ic+4)
        colors_.append(ic-4)
    return colors_

def SetGraphStyle(gr_,num_,clr_,msty_):
    gr_.SetLineStyle(num_)
    gr_.SetMarkerStyle(msty_)
    gr_.SetLineColor(clr_)
    gr_.SetMarkerColor(clr_)
    gr_.SetMarkerSize(1.5)
    return 0 

def PlotEffCurves(sig_eff_vals_,ttH_eff_vals_,ol_):
    n = 100
    x, y = array( 'd' ), array( 'd' )
    for ientry,entry in enumerate(sig_eff_vals_):
        x_val, y_val = float(ttH_eff_vals_[ientry]), float(sig_eff_vals_[ientry])
        x.append(x_val)
        y.append(y_val)
        # effVseff_h.SetBinContent(ientry+1,)
        # print'x_val = ',x_val
        # print'y_val = ',y_val
        # effVseff_h.Fill(x_val,y_val)
        # effVseff_h.Fill(x_val,y_val)
        # effVseff_h.SetBinContent()
    # effVseff_h.SetMarkerStyle(8)
    effVseff_h = TGraph(n,x,y)
    effVseff_h.SetLineColor( 2 )
    effVseff_h.SetLineWidth( 4 )
    effVseff_h.SetMarkerColor( 4 )
    effVseff_h.SetMarkerStyle( 21 )
    effVseff_h.SetTitle( 'b veto efficiency' )
    effVseff_h.GetXaxis().SetTitle( 'ttH efficiency' )
    effVseff_h.GetYaxis().SetTitle( 'signal efficiency' )
    outputName = ol_ + 'sigEffvsttHeff.png'
    Draw_Histogram(effVseff_h,'ACP',outputName)
    # TLine *line = new TLine(-3,ymax,3,ymax);
    # effVseff_h.GetXaxis().SetTitle('ttH efficiency')
    # effVseff_h.GetYaxis().SetTitle('signal efficiency')
    # outputName = ol_ + 'sigEffvsttHeff.png'
    # Draw_Histogram(effVseff_h,'COLZ1',outputName)

def PlotEff(h_,ofn_):
    # plot efficiency vs cut
    cuts = [] 
    efficiencies = []
    nBins = h_.GetNbinsX()
    total_entries = h_.Integral()
    # for ix,x_ in enumerate(h_):
    eff_bins = 100 
    eff_min = 0.
    for eb in range(1,eff_bins+1): 
        # if ix == 0: continue # skip underflow bin 
        # elif ix == nBins + 1: break # skip overflow bin  
        thisCut = eff_min + 0.01*float(eb-1) # 0.01 because this is the bin interval
        cuts.append(thisCut)
        entries_in_range = h_.Integral(1,eb+1)
        efficiency = float(entries_in_range) / float(total_entries)
        efficiencies.append(efficiency)
        print'efficiency = ',efficiency
    eff_h = TH1F('eff_h','eff_h',100,0.,1)
    eff_h_2 = h_.Clone()
    eff_h_2.SetDirectory(0)

    for i,val in enumerate(efficiencies):
        x_val, y_val = float(cuts[i]), float(efficiencies[i])
        eff_h.SetBinContent(i+1,y_val) # USE THIS INSTEAD OF FILL 
    eff_h.SetMarkerStyle(8)
    Draw_Histogram(eff_h,'p',ofn_)
    return efficiencies

def Draw_Histogram(h_,opt_,fn_,log_):
    c_tmp = TCanvas('c_tmp','c_tmp',1300,800)
    h_.Draw("apl")
    if(log_): gPad.SetLogy()
    h_.Draw(opt_)

    # c_tmp.BuildLegend(0.75,0.62,0.95,0.84)
    # c_tmp.BuildLegend(0.75,0.42,0.95,0.65)
    c_tmp.BuildLegend(0.75,0.57,0.95,0.8)

    # c_tmp.BuildLegend(0.83, 0.83, 0.99, 0.99)
    # c_tmp.BuildLegend(0.5, 0.3, 0.8, 0.8)
    # c_tmp.BuildLegend(0.6, 0.1, 0.9, 0.6)
    c_tmp.SaveAs(fn_)
    return 

def DrawNonResHistogram(h_,opt_,fn_,log_,N_,plotLabels_):
    c_tmp = TCanvas('c_tmp','c_tmp',1300,800)
    if(log_): gPad.SetLogy()
    # set bin labels 
    # frame = c_tmp.DrawFrame(1.4,0.001, 4.1, 10)
    # frame.SetDirectory(0)
    # frame.GetXaxis().SetLimits(-0.5,N_-0.5)
    # frame.GetXaxis().CenterLabels(True)
    # for i in range(N_):
        # frame.GetXaxis().SetBinLabel(int(1000.*(2*i+1)/(2*N_)),plotLabels_[i])
    # if(N_ > 3): frame.GetXaxis().SetLabelSize(0.07)
    # else: frame.GetXaxis().SetLabelSize(0.12)
    # frame.LabelsOption("h","X")    
    # frame.Draw('axis')
    # print"frame:",frame
    h_.Draw(opt_)
    gPad.Update()
    mg_hist = h_.GetHistogram()
    # mg_hist.Rebin(N_)
    # print"nbins:",mg_hist.GetNbinsX()
    N_xbins = mg_hist.GetNbinsX()
    # N_rebin = int(N_xbins) / 4
    N_rebin = int(N_xbins) / 100
    # N_rebin = 25
    mg_hist.Rebin(N_rebin)
    # mg_hist.SetBarOffset(100)
    # want 4 total
    # rebin means divide total by this. 4 = NXbins / Rebin -> Rebin = NXbins / 4 
    h_.Draw(opt_)
    # h_.GetXaxis().CenterLabels(True)
    # h_.SetBarOffset(-0.5)
    
    if(N_ > 3): h_.GetXaxis().SetLabelSize(0.05)
    else: h_.GetXaxis().SetLabelSize(0.12)

    for i in range(N_):
        h_.GetXaxis().LabelsOption("h")
        # h_.GetXaxis().LabelsOption("d")
        # bin = h_.GetXaxis().FindBin(i+1)
        bin = h_.GetXaxis().FindBin(i)
        #39 62 85 
        # print"bin:",bin
        # h_.GetXaxis().SetBinLabel(bin,plotLabels_[i])
        h_.GetXaxis().SetBinLabel(bin,plotLabels_[i])
    # print"frame:",frame 
    # frame.Draw('axissame')
    # frame.Draw("sameaxis")
        # c_tmp.BuildLegend()
        # c_tmp.BuildLegend(0.65,0.52,0.95,0.82)

    # c_tmp.BuildLegend(0.75,0.62,0.95,0.84)
    # c_tmp.BuildLegend(0.75,0.42,0.95,0.65)
    c_tmp.BuildLegend(0.75,0.57,0.95,0.8)

    # c_tmp.BuildLegend(0.83, 0.83, 0.99, 0.99)
    # c_tmp.BuildLegend(0.5, 0.3, 0.8, 0.8)
    # c_tmp.BuildLegend(0.6, 0.1, 0.9, 0.6)
    c_tmp.SaveAs(fn_)
    # h_.SetName('h')
    # h_.SaveAs("h.root")    

def SetBinLabels(gr_,Npoints_,plotLabels_):
    # nBins = gr_.GetNbinsX()
    nBins = Npoints_
    for i in range(Npoints_):
        gr_.GetXaxis().SetBinLabel(int(nBins*(2*i+1)/(2*Npoints_)),plotLabels_[i])
        if(Npoints_ > 3): gr_.GetXaxis().SetLabelSize(0.07)
        else: gr_.GetXaxis().SetLabelSize(0.12)

def SimpleDrawHisto(h_,option_,outName_,v_):
    c = TCanvas()
    h_.Draw(option_)
    c.SaveAs(outName_)

def SetStyle():
    gStyle.SetPadTickX(1)
    gStyle.SetPadTickY(1)
    gStyle.SetPadGridX(1)
    gStyle.SetPadGridY(1)