from PlotterTools import *
from ROOT import *
gROOT.SetBatch(1)

#gStyle.SetOptStat(0) # Stat box option 
for v in Vars:
   hists1 = []
   hists2 = []
   #leg = TLegend(0.6, 0.7, 0.89, 0.89)
   #leg.SetBorderSize(0)
   Max = -0.
   for fi,f in enumerate(Files):
      #ch = TChain('geninf')
      #ch.Add(f[0])
      #ch = TChain('h4gflash/H4GTree')
      
      ch = TChain('Events')
      ch.Add(f[0])
      #hname1 = v[1]+'_'+str(fi)
      hname1 = v[1]+'_'+f[1]
      #blah = str(fi)
      #hname_resolved = v[1]+'_'+str(fi)
      #hname_fat = v[1]+'_'+str(fi)
      h1 = TH1F(hname1, v[2] + '_' + f[1], v[3], v[4], v[5])

      #h2 = TH1F(blah, v[2], v[3], v[4], v[5])
      #h_resolved = TH1F(hname_resolved, v[2], v[3], v[4], v[5])
      #h_fat = TH1F(hname_fat, v[2], v[3], v[4], v[5])

      ch.Draw(v[0]+'>>'+hname1,TCut(Cut))
      #ch1.Draw(v[0]+'>>'+blah,TCut(Cut_fat))
      #ch2.Draw(v[0]+'>>'+hname_2,TCut(Cut_fat))
      #ch.Draw(v[0]+'>>'+hname_2,TCut(Cut_fat))
      #ch.Draw(v[0]+'>>'+hname_resolved,TCut(Cut_resolved))
      #ch.Draw(v[0]+'>>'+hname_fat,TCut(Cut_fat))
      #h.Sumw2()
      total1 = h1.Integral()
      #total_fat = h2.Integral()
      #h1.Scale(float(f[5])/float(total1))

      h1.SetLineColor(f[2])
      h1.SetFillColor(f[3])
      #h1.SetLineStyle(f[5])
      h1.SetLineWidth(2)
      #print h.GetMaximum()
      #h.SetMaximum(h.GetMaximum()+0.9*h.GetMaximum())
      #h1.GetXaxis().SetTitle()
      #h1.GetYaxis().SetTitle()


      h1.GetYaxis().SetTitleOffset(1.5)

      #h1.Scale(float(f[5])/float(total_resolved))
      #h1.SetLineColor(kRed)
      #h1.SetLineWidth(2)
      #h2.Scale(float(f[5])/float(total_fat))
      #h2.SetLineColor(kBlue)
      # h2.SetLineWidth(2)
      #h2.SetLineColor(kBlue)
      #h_fat.SetLineColor(f[3])
      #h_fat.SetLineWidth(3)
      #h_fat.SetMinimum(0)
      #h_fat.GetYaxis().SetTitleOffset(1.5)
      #h.SetFillColor(f[3])
      #h.SetFillStyle(f[5])
      hists1.append([h1,f[1]])
   #hists.append([h2,f[2]])
      #hists.append([h_fat,f[1]])
    #   if h.GetMaximum() > Max:
    #      Max = h.GetMaximum()
   #h.SetMaximum(Max)
      #print "Max ", Max

      
   # for fi,f in enumerate(Files):
   #    ch = TChain('h4gflash/H4GTree')
   #    ch.Add(f[0])
   #    hname2 = v[1]+'_'+str(fi)
   #    h2 = TH1F(hname2, v[2], v[3], v[4], v[5])
   #    ch.Draw(v[0]+'>>'+hname2,TCut(Cut_resolved))
   #    total2 = h2.Integral()
   #    h2.Scale(float(f[5])/float(total2))
   #    h2.SetLineColor(f[3])
   #    h2.SetLineWidth(2)
   #    hists2.append([h2,f[1]])

   #h2.Draw('same')

   # for fi,hh in enumerate(hists1):
   #    leg.AddEntry(hh1[0],hh1[1], 'lf')
   #    leg.SetTextSize(0.02)
   #    #hh[0].SetMaximum(Max*1.5)
   #    #hh[0].SetMinimum(0.0001)
   #    if fi == 0:
   #       hh1[0].Draw('h')
   #    if fi > 0:
   #       hh1[0].Draw('h same')
   # for fi2,hh2 in enumerate(hists2):
   #     leg.AddEntry(hh2[0],hh2[1], 'lf')
   #     leg.SetTextSize(0.02)
   #     #hh[0].SetMaximum(Max*1.5)
   #     #hh[0].SetMinimum(0.0001)
   #     if fi == 0:
   #        hh2[0].Draw('h')
   #     if fi > 0:
   #        hh2[0].Draw('h same')

   #leg.Draw('same')

   # tlatex = TLatex()
   # tlatex.SetNDC()
   # tlatex.SetTextAngle(0)
   # tlatex.SetTextColor(kBlack)
   # tlatex.SetTextFont(63)
   # tlatex.SetTextAlign(11)
   # tlatex.SetTextSize(25)
   # #tlatex.DrawLatex(0.11,0.91,"Simulation")
   # tlatex.SetTextFont(53)
   # tlatex.DrawLatex(0.18,0.91,"Simulation")
   # tlatex.SetTextFont(43)
   # tlatex.SetTextSize(23)


      c0 = TCanvas('a', 'a', 800, 600)
      h1.Draw()

      c0.Update()

      #c0.SaveAs( outputLoc+v[1]+'.pdf')
      c0.SaveAs( outputLoc+v[1]+'_file' + str(fi)+'.png')
   #c0.SaveAs( outputLoc+v[1]+'.root')

   #c0.SetLogy()
   #c0.SaveAs( outputLoc+v[1]+'_log.pstr(
   #c0.SaveAs( outputLoc+v[1]+'_log.pstr(
   #c0.SaveAs( outputLoc+v[1]+'_log.root')
   #c0.SaveAs('testing.root')

#Lumi = "35.87" + " fb^{-1} (13TeV)"
#tlatex.SetTextAlign(31)
#tlatex.DrawLatex(0.9,0.91,Lumi)
#tlatex.SetTextAlign(11)