import ROOT
import argparse

if __name__ == '__main__':

   ROOT.gROOT.SetBatch(ROOT.kTRUE)

   year = "2018"

   #  parser =  argparse.ArgumentParser(description='split_Tree')
   #  parser.add_argument('-i', '--input', dest='input', required=True, type=str)
   #  parser.add_argument('-d', '--dir', dest='dir', required=False, type=str) 
   #  args = parser.parse_args()

   if(year == "2016"):
      ##-- 2016 
      inDir = "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production/2016/Single_H_hadded/"
      files = [
         "GluGluHToGG_M125_2016_HHWWggTag_0_MoreVars.root",
         "VBFHToGG_M125_2016_HHWWggTag_0_MoreVars.root",
         "VHToGG_M125_2016_HHWWggTag_0_MoreVars.root",
         "ttHJetToGG_M125_2016_HHWWggTag_0_MoreVars.root"
      ]      

   elif(year == "2017"):
      ##-- 2017 
      inDir = "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production/2017/Single_H/"
      files = [
         "GluGluHToGG_2017_HHWWggTag_0_MoreVars.root", 
         "VBFHToGG_2017_HHWWggTag_0_MoreVars.root", 
         "VHToGG_2017_HHWWggTag_0_MoreVars.root",
         "ttHJetToGG_2017_HHWWggTag_0_MoreVars.root"
      ]      
   elif(year == "2018"):
      ##-- 2018 
      inDir = "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production/2018/Single_H_2018_hadded/"
      files = [
         "GluGluHToGG_M125_2018_HHWWggTag_0_MoreVars.root",
         "VBFHToGG_M125_2018_HHWWggTag_0_MoreVars.root",
         "VHToGG_M125_2018_HHWWggTag_0_MoreVars.root",
         "ttHJetToGG_2018_M125_HHWWggTag_0_MoreVars.root"
      ]

   for f in files:
      output_name = "%s/%s"%(inDir, f)
      print"on File:",output_name

      #  output_name = args.input

      output_nameEven_short = output_name.replace('.root','_even.root')
      output_nameOdd_short = output_name.replace('.root','_odd.root')

      output_nameEven = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/EvenOddNtuples/%s/%s"%(year, output_nameEven_short.split('/')[-1])
      output_nameOdd = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/EvenOddNtuples/%s/%s"%(year, output_nameOdd_short.split('/')[-1])

      outfile_even = ROOT.TFile(output_nameEven, "RECREATE")
      outfile_odd = ROOT.TFile(output_nameOdd, "RECREATE")
      inFile = ROOT.TFile(output_name,"READ")
      # dir = args.dir 
      dir = ""
      print "Running on even events..."
      if dir!="":
         dir1 = inFile.Get("tagsDumper") 
         dir2 = dir1.Get("trees") 
         print dir2.GetName()
         for key in dir2.GetListOfKeys():
            print "Even events:",key.GetName()
            tree = inFile.Get(dir+"/"+key.GetName())
            outfile_even.cd()
            outtree_even = tree.CloneTree(0)
            nentries = tree.GetEntries()
            for i in range(0, nentries):
               tree.GetEntry(i) 
               if i%2 == 0: outtree_even.Fill() 
            outtree_even.Write(key.GetName())
         outfile_even.Close()
         for key in dir2.GetListOfKeys():
            print "Odd events:",key.GetName()
            tree = inFile.Get(dir+"/"+key.GetName())
            outfile_odd.cd()
            outtree_odd = tree.CloneTree(0)
            nentries = tree.GetEntries()
            for i in range(0, nentries):
               tree.GetEntry(i) 
               if i%2 != 0: outtree_odd.Fill() 
            outtree_odd.Write(key.GetName())
         outfile_odd.Close()
      else:
         for key in inFile.GetListOfKeys():
            print "Even events:",key.GetName()
            tree = inFile.Get(key.GetName())
            outfile_even.cd()
            outtree_even = tree.CloneTree(0)
            nentries = tree.GetEntries()
            for i in range(0, nentries):
               tree.GetEntry(i) 
               if i%2 == 0: outtree_even.Fill() 
            outtree_even.Write(key.GetName())
         outfile_even.Close()
         for key in inFile.GetListOfKeys():
            print "Odd events:",key.GetName()
            tree = inFile.Get(key.GetName())
            outfile_odd.cd()
            outtree_odd = tree.CloneTree(0)
            nentries = tree.GetEntries()
            for i in range(0, nentries):
               tree.GetEntry(i) 
               if i%2 != 0: outtree_odd.Fill() 
            outtree_odd.Write(key.GetName())
         outfile_odd.Close()

