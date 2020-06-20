from ROOT import *
from array import array
import argparse
# parser =  argparse.ArgumentParser(description='Create Classification BDT weights')
# parser.add_argument('--mcFolder', type=str, default="", help="Input folder with hadded MC ntuples", required=False)
# parser.add_argument('--Tags', type=str, default="", help="Comma separated list of tags to run. Ex: HHWWggTag_0,HHWWggTag_1,HHWWggTag_2 or HHWWggTag_2 or HHWWggTag_2,combined", required=False)

# parser.add_argument('-m', '--mass', dest='mass', required=True, type=str)
# parser.add_argument('-iD', '--iD', dest='inDir', required=True, type=str)
# parser.add_argument('-F', '--file', dest='File', required=True, type=str)
# parser.add_argument('-W', '--weight', dest='Weight', required=True, type=str)
# parser.add_argument('-T', '--tree', dest='Tree', required=True, type=str)
# parser.add_argument('-O', '--output', dest='Out', required=True, type=str)

opt = parser.parse_args()
reader = TMVA.Reader()

# nTupleDirec = "/eos/user/a/atishelm/ntuples/HHWWgg"

# ctscs = array('f', [0])
# cta1 = array('f', [0])
# cta2 = array('f', [0])
# a1ptohm = array('f',[0])
# a2ptohm = array('f',[0])
# p1ptoa1m = array('f', [0])
# p1ptoa2m = array('f', [0])

MET_pt = array('f',[0])
Leading_Photon_MVA = array('f',[0])
Leading_Photon_pt = array('f',[0])
Subleading_Photon_MVA = array('f',[0])
Subleading_Photon_pt = array('f',[0])

# reader.AddVariable('CTStarCS',ctscs)
# reader.AddVariable('CT_a1Pho1',cta1)
# reader.AddVariable('CT_a2Pho1',cta2)
# reader.AddVariable('a1_Pt/tp_mass',a1ptohm)
# reader.AddVariable('a2_Pt/tp_mass',a2ptohm)
# reader.AddVariable('a1_Pho1PtOvera1Mass',p1ptoa1m)
# reader.AddVariable('a2_Pho1PtOvera2Mass',p1ptoa2m)

# reader.AddVariable('pho1_MVA',p1mva)
# reader.AddVariable('pho2_MVA',p2mva)
# reader.AddVariable('pho3_MVA',p3mva)
# reader.AddVariable('pho4_MVA',p4mva)

reader.AddVariable('MET_pt',MET_pt)
reader.AddVariable('Leading_Photon_MVA',Leading_Photon_MVA)
reader.AddVariable('Leading_Photon_pt',Leading_Photon_pt)
reader.AddVariable('Subleading_Photon_pt',Subleading_Photon_pt)

#reader.AddVariable('pho1_pt',p1pt)
#reader.AddVariable('pho2_pt',p2pt)
#reader.AddVariable('pho3_pt',p3pt)
#reader.AddVariable('pho4_pt',p4pt)
#reader.AddVariable('pho1_eta',p1eta)
#reader.AddVariable('pho2_eta',p2eta)
#reader.AddVariable('pho3_eta',p3eta)
#reader.AddVariable('pho4_eta',p4eta)
#reader.AddVariable('tp_pt',tppt)
#reader.AddVariable('tp_eta',tpeta)

# reader.BookMVA("BDT",opt.Weight)
reader.BookMVA("BDT","dataset/weights/TMVAClassification_BDT.weights.xml")

# FilesToRedo = opt.File.split(',')
Files = ['/eos/user/a/atishelm/ntuples/HHWWgg/HHWWgg_Backgrounds_Hadded/DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_Hadded.root']
for f in Files:
#   print f
  infilename = f 
  infile = TFile(infilename)
  print "file name:", infile
  tree = 'tagsDumper/trees/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_HHWWggTag_0'
#   tree = 

#   if ('signal' in f):
#       tree = 'SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8'
#   elif ('DiPho80toInf' in f):
#       print "HERE "
#       tree = 'DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa'
#   elif ('DiPho40to80' in f):
#       tree = 'DiPhotonJetsBox_M40_80_Sherpa'
#   else: tree = 'Data'

  intree = infile.Get(tree)
  # intree = infile.Get(str(opt.Tree)+"_13TeV_4photons")
  print "tree name: ", intree
#   outfile = TFile(opt.Out, "RECREATE")
  outfile = TFile("ApplyCatBDT_Output.root", "RECREATE")
  # outfile = TFile(opt.Out+f.split("/")[len(f.split("/"))-1], "RECREATE")
  outtree = intree.CloneTree(0)
  bdt = array('f', [0])
  _bdt = outtree.Branch('bdt', bdt, 'bdt/F')
  # cat_MVA_value = array('f', [0])
  # _cat_MVA_value = outtree.Branch('cat_MVA_value', cat_MVA_value, 'cat_MVA_value/F')

  nentries = intree.GetEntries()

  for i in range(0, nentries):
     if i%1000 == 0: print i
     if i==10000: break 
     intree.GetEntry(i)
     # ctscs[0] = intree.CTStarCS
     # cta1[0] = intree.CT_a1Pho1
     # cta2[0] = intree.CT_a2Pho1
     # a1ptohm[0] = intree.a1_Pt/intree.tp_mass
     # a2ptohm[0] = intree.a2_Pt/intree.tp_mass
     # p1ptoa1m[0] = intree.a1_Pho1PtOvera1Mass
     # p1ptoa2m[0] = intree.a2_Pho1PtOvera2Mass
    # reader.AddVariable('MET_pt',MET_pt)
    # reader.AddVariable('Leading_Photon_MVA',Leading_Photon_MVA)
    # reader.AddVariable('Leading_Photon_pt',Leading_Photon_pt)
    # reader.AddVariable('Subleading_Photon_pt',Subleading_Photon_pt)     
     MET_pt[0] = float(intree.MET_pt)
     Leading_Photon_MVA[0] = float(intree.Leading_Photon_MVA)
     Leading_Photon_pt[0] = float(intree.Leading_Photon_pt)
     Subleading_Photon_pt[0] = float(intree.Subleading_Photon_pt)
     #p1pt[0] = float(intree.pho1_pt)
     #p2pt[0] = float(intree.pho2_pt)
     #p3pt[0] = float(intree.pho3_pt)
     #p4pt[0] = float(intree.pho4_pt)
     #p1eta[0] = float(intree.pho1_eta)
     #p2eta[0] = float(intree.pho2_eta)
     #p3eta[0] = float(intree.pho3_eta)
     #p4eta[0] = float(intree.pho4_eta)
     #tppt[0] = float(intree.tp_pt)
     #tpeta[0] = float(intree.tp_eta)

     #a1ptom[0] = intree.a1_Pt/intree.a1_mass
     # a2ptom[0] = intree.a2_Pt/intree.a2_mass
     #a1a2dr[0] = intree.a1_a2_DR
     #p2ptoa1m[0] = intree.a1_Pho2PtOvera1Mass

     # mvas[0] = intree.pairMVAscore
     # rho[0] = intree.rho
     # p2ptoa2m[0] = intree.a2_Pho2PtOvera2Mass
     # a1m[0] = intree.a1_mass
     # a2m[0] = intree.a2_mass
     bdt[0] = reader.EvaluateMVA("BDT")
     # cat_MVA_value[0] = reader.EvaluateMVA("BDT")
     # if (cat_MVA_value[0] == -1):
         # print "-1 value"
     # print cat_MVA_value[0]

     outtree.Fill()

  outfile.cd()
  outtree.Write()
  outfile.Close()