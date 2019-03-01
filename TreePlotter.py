from PlotterTools import *
from ROOT import * # Importing root twice can lead to problems 
gROOT.SetBatch(1) # Don't display canvas when drawing 

# GEN

#ROOT.PyConfig.IgnoreCommandLineOptions = True
#from DataFormats.FWLite import Handle, Runs, Lumis, Events
#import sys


#gStyle.SetOptStat(1) # Stats Box option  

# For each variable 
for v in Vars:
   hists1 = []
   hists2 = []
   leg = TLegend(0.6, 0.7, 0.89, 0.89)
   #leg.SetBorderSize(0)
   Max = -0.
   
   # For each file, create 1d histogram, add to hists1 
   for fi,f in enumerate(Files):
      #gStyle.SetOptStat(1) # Stats Box

      #print'file number: ',fi
      #print'file: ',f
      
      #ch = TChain('Events')
      #ch = TChain('HHWWggCandidateDumper/trees/_13TeV_All')
      ch = TChain('HHWWggCandidateDumper/trees/_13TeV_SemiLeptonic')
      ch.Add(f[0])
      hname1 = v[1]+'_'+f[1]
      h1 = TH1F(hname1, v[2] + '_' + f[1], v[3], v[4], v[5])
      #ch.Draw(v[0]+'>>'+hname1,TCut(Cut))
      ch.Draw(v[0]+'>>'+hname1,TCut( str(v[0]) + gtz_Cut))
      total1 = h1.Integral()
      h1.SetLineColor(f[2])
      h1.SetFillColor(f[3])
      #h1.SetLineStyle(f[5])
      h1.SetLineWidth(2)
      #h.SetMaximum(h.GetMaximum()+0.9*h.GetMaximum())
      #h1.SetTitle(v[6] + ' ' + f[1])
      h1.GetXaxis().SetTitle(v[6])
      h1.GetXaxis().SetTitleOffset(1.2)
      #h1.GetYaxis().SetTitle()

      h1.GetYaxis().SetTitleOffset(1.5)
      hists1.append([h1,f[1]])

      c1 = TCanvas('c1', 'c1', 800, 600)
      h1.Draw()
      c1.Update()
      c1.SaveAs( outputLoc + v[1] + '_' + f[1] +'.png')
  
   # for fi,f in enumerate(Files):
   #    ch = TChain('Events')
   #    ch.Add(f[0])
   #    hname2 = v[1]+'_'+str(fi)
   #    h2 = TH1F(hname2, v[2], v[3], v[4], v[5])
   #    ch.Draw(v[0]+'>>'+hname2,TCut(Cut))
   #    total2 = h2.Integral()
   #    h2.Scale(float(f[5])/float(total2))
   #    h2.SetLineColor(f[3])
   #    h2.SetLineWidth(2)
   #    hists2.append([h2,f[1]])

   #h2.Draw('same')

   c0 = TCanvas('c0', 'c0', 800, 600)

   # hc =c0.DrawFrame(0.,0.,1.,1.)
   # hc.SetXTitle("Test")
   # c0.Modified()

   

   for fi,hh1 in enumerate(hists1):
      

      #print'file number: ',fi
      #print'file: ',hh1

      leg.AddEntry(hh1[0],hh1[1], 'lf')
      leg.SetTextSize(0.02)
      hh1[0].SetTitle(v[1] + ' Combined ')
      hh1[0].SetFillColor(kWhite)
      #hh[0].SetMaximum(Max*1.5)
      #hh[0].SetMinimum(0.0001)
      if fi == 0:
         #hh1[0].SetTitle(v[1] + ' Combined ')
         #gStyle.SetOptStat(0) # No Stats Box
         hh1[0].Draw('h')
      if fi > 0:
         #gStyle.SetOptStat(0) # No Stats Box
         hh1[0].Draw('h same')

   #gStyle.SetOptStat(0) # No Stats Box
   leg.Draw('same')
   c0.SaveAs( outputLoc + v[1] + '_combined' + '.png')
      

   # for fi2,hh2 in enumerate(hists2):
   #     leg.AddEntry(hh2[0],hh2[1], 'lf')
   #     leg.SetTextSize(0.02)
   #     #hh[0].SetMaximum(Max*1.5)
   #     #hh[0].SetMinimum(0.0001)
   #     if fi == 0:
   #        hh2[0].Draw('h')
   #     if fi > 0:
   #        hh2[0].Draw('h same')

      # c0 = TCanvas('a', 'a', 800, 600)
      # h1.Draw()
      # c0.Update()
      # c0.SaveAs( outputLoc+v[1]+'_file' + str(fi)+'.png')
