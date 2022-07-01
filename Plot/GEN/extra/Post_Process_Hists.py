from os import listdir
import ROOT
ROOT.gROOT.SetBatch(1)
def sort_second(val):
    return val[1]
histo_direc = '/eos/user/a/atishelm/www/analysis_plots/GEN/plot/' # directory with histograms you want 
file_paths = [fp for fp in listdir(histo_direc) if '.root' in fp]  # Save paths of non-LHE files
full_file_paths = []
for p in file_paths:
    ffp = '/eos/user/a/atishelm/www/analysis_plots/GEN/plot/'
    ffp += p
    full_file_paths.append(ffp)
path_mass = []
for pa in full_file_paths:
    mass = pa.split('/')[-1].split('_')[0]
    mass = mass[1:]
    mass = float(mass)
    path_mass.append([pa,mass])
path_mass.sort(key = sort_second)
ordered_paths = []
for pm in path_mass:
    ordered_paths.append(pm[0])
xmin, ymin, xmax, ymax = 0.65,0.65,0.85,0.85
legend = ROOT.TLegend(xmin,ymin,xmax,ymax)
c1 = ROOT.TCanvas()
for ip,path in enumerate(ordered_paths):
    f = ROOT.TFile(path,"READ")
    h = f.Get('h1')
    h.SetDirectory(0)
    norm = 1 # Normalize integral to one for GEN comparisons. Just want to compare shapes 
    scale = float(norm)/float(h.Integral())
    h.Scale(scale)
    print'h = ',h
    if ip == 0:
        legend.AddEntry(h)
        h.SetMaximum(1.5)
        h.SetStats(0)
        h.SetTitle('SL m_{HH}')
        # h.SetTitle('H_{#gamma#gamma} p_{T}')
        h.GetXaxis().SetTitle('H_{#gamma#gamma} p_{T}')
        # h.GetXaxis().SetTitle('m_{HH}')
        h.GetYaxis().SetTitle('A.U.')
        h.Draw('hist')
    else:
        # if ip == 1:
        #     h.SetLineColor(ROOT.kGreen)
        h.Draw('histsame')
        legend.AddEntry(h)
    
legend.Draw('same')
c1.SaveAs(histo_direc + 'combined_plot.pdf')