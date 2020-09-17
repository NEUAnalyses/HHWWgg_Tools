#include <iostream>
#include <fstream>
#include <TH1F.h>
#include <TTree.h>
#include <TPaveText.h>
#include <TStyle.h>
#include <TCanvas.h>
#include "TLorentzVector.h"
#include <iomanip>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include "TFile.h"
#include "TROOT.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TGraph.h"
#include <algorithm>    // std::min_element, std::max_element

// #include <boost/filesystem.hpp>

#include "CatOptUtils.C"

using namespace std;

//g++ optimize_cats.C -g -o opt `root-config --cflags --glibs` -lMLP -lXMLIO

void optimize_cats(const int NCAT) {
	gROOT->SetBatch("kTrue");

	// Parameters 
	TString outDir = "/eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/DNN/DNN_Categorization/";
	TString what_to_opt = "evalDNN";
	double xmin = 0.0;
	double xmax = 1.0;
	Double_t precision=0.01;
	TString Mgg_window = "*((CMS_hgg_mass>115)&&(CMS_hgg_mass<135))";
	TString Mgg_sideband = "*((CMS_hgg_mass<=115)||(CMS_hgg_mass>=135))";
	TString selection_sig = "33.49*0.00097*0.441*41.5*weight*(CMS_hgg_mass > 100 && CMS_hgg_mass < 180)"; // normalize signal properly with cross section 
	TString selection_bg = "41.5*weight*(CMS_hgg_mass > 100 && CMS_hgg_mass < 180)";
	TString selection_data = "1";
	TString outstr = "";
	double minevents = 10.;
	TString s; TString sel;
	TString outnameborder = s.Format("output_SB_%s_cat%d_mineventborders%.0f_borders",what_to_opt.Data(),NCAT,minevents);
	TString outname = s.Format("output_SB_%s_cat%d_minevents%.0f_%s",what_to_opt.Data(),NCAT,minevents,outstr.Data());

	// Signal Trees
	TChain *file_s =  new TChain("file_s");
	file_s->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Signal/ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root/GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_0");
	file_s->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Signal/ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root/GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_1");
	file_s->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Signal/ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root/GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_2");
	TH1F *hist_S = new TH1F("hist_S","hist_S",int((xmax-xmin)/precision),xmin,xmax);
    s.Form("%s>>hist_S",what_to_opt.Data());
    sel.Form("%s",(selection_sig+Mgg_window).Data());
	file_s->Draw(s,sel,"goff");

	// Background Trees
	TChain *tree_bg =  new TChain("tree_bg");

	string backgroundDirec = "/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Backgrounds";
	// string backgroundDirec = "/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Backgrounds_short";
	vector<string> v;     
	v = read_directory(backgroundDirec);
	cout << "Number of background files: " << v.size() << endl;

	for(int i = 0; i < v.size(); i++){ // for each file 
		for(int c = 0; c < 3; c++){ // for each category 
			string cat = to_string(c);
			string file = v[i];
			string treePath = GetMCTreeName(file);
			string fullPath = backgroundDirec + "/"; 
			fullPath.append(file);
			fullPath.append( "/" + treePath + "_13TeV_HHWWggTag_" + cat);
			
			// cout << "full path: " << fullPath << endl;

			tree_bg->Add(fullPath.c_str());

		}
	}

	// Data Trees 
	TChain *tree_data =  new TChain("tree_data");
	tree_data->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Data/Data.root/Data_13TeV_HHWWggTag_0");
	tree_data->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Data/Data.root/Data_13TeV_HHWWggTag_1");
	tree_data->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Data/Data.root/Data_13TeV_HHWWggTag_2");

	double scale = 1;
	TH1F *hist_B = new TH1F("hist_B","hist_B",int((xmax-xmin)/precision),xmin,xmax); //200 bins  -- background signal region
    s.Form("%s>>hist_B",what_to_opt.Data());
    sel.Form("%s",(selection_bg+Mgg_window).Data());
	tree_bg->Draw(s,sel,"goff");
	// hist_B->Scale(scale/hist_B->Integral());
	cout<<"BG integral under Mgg "<<hist_B->Integral()<<endl;
	TH1F *hist_B_sideband = new TH1F("hist_B_sideband","hist_B_sideband",int((xmax-xmin)/precision),xmin,xmax); //200 bins -- background sideband region
	// TH1F *hist_B_sideband = new TH1F("hist_B_sideband","hist_B_sideband",int(nbins),xmin,xmax); //200 bins -- background sideband region


    s.Form("%s>>hist_B_sideband",what_to_opt.Data());
    sel.Form("%s",(selection_bg+Mgg_sideband).Data());
	tree_bg->Draw(s,sel,"goff");
	hist_B_sideband->Scale(scale);
	cout<<"BG integral sidebands "<<hist_B_sideband->Integral()<<endl;

	TH1F *hist_D_sideband = new TH1F("hist_D_sideband","hist_D_sideband",int((xmax-xmin)/precision),xmin,xmax); //200 bins -- data sideband region
	// TH1F *hist_D_sideband = new TH1F("hist_D_sideband","hist_D_sideband",int(nbins),xmin,xmax); //200 bins -- data sideband region
	// TH1F *hist_D_sideband = new TH1F("hist_D_sideband","hist_D_sideband",30,xmin,xmax); //200 bins

    s.Form("%s>>hist_D_sideband",what_to_opt.Data());
    sel.Form("%s",(selection_data+Mgg_sideband).Data());
	tree_data->Draw(s,sel,"goff");
	cout<<"Data integral sidebands "<<hist_D_sideband->Integral()<<endl;

	double END = hist_B->GetBinCenter(hist_B->FindLastBinAbove(-1.))+hist_B->GetBinWidth(1)/2.; //right end of BDT distibution
	double START = hist_B->GetBinCenter(hist_B->FindFirstBinAbove(-1.))-hist_B->GetBinWidth(1)/2.; //right end of BDT distibution
	cout<<"start = "<<START<<" , end = "<<END<<endl;

	hist_S->SetFillStyle(4050);
	hist_S->SetLineColor(kRed);
	hist_S->SetFillColor(kRed-7);
	hist_S->SetLineWidth(2);
	hist_B->SetFillStyle(4050);
	hist_B->SetLineColor(kBlue+1);
	hist_B->SetFillColor(kBlue-10);
	hist_B->SetLineWidth(2);

	TH1F *hist_B2 = (TH1F*)hist_B->Clone("b_new");
	hist_B2->Rebin(1); //4
	// hist_B2->GetXaxis()->SetRange(0,1);
	TH1F *hist_S2 = (TH1F*)hist_S->Clone("s_new");
	hist_S2->Rebin(1); //4
	// hist_S2->GetXaxis()->SetRange(0,1);
	hist_S2->Scale();

	// CMS info
	float left2 = gStyle->GetPadLeftMargin();
	float right2 = gStyle->GetPadRightMargin();
	float top2 = gStyle->GetPadTopMargin();
	float bottom2 = gStyle->GetPadBottomMargin();
	TPaveText pCMS1(left2,1.-top2,0.4,1.,"NDC");
	pCMS1.SetTextFont(62);
	pCMS1.SetTextSize(top2*0.75);
	pCMS1.SetTextAlign(12);
	pCMS1.SetFillStyle(-1);
	pCMS1.SetBorderSize(0);
	pCMS1.AddText("CMS");
	TPaveText pCMS12(left2+0.1,1.-top2*1.1,0.6,1.,"NDC");
	pCMS12.SetTextFont(52);
	pCMS12.SetTextSize(top2*0.75);
	pCMS12.SetTextAlign(12);
	pCMS12.SetFillStyle(-1);
	pCMS12.SetBorderSize(0);
	pCMS12.AddText("Preliminary");
	TPaveText pCMS2(0.5,1.-top2,1.-right2*0.5,1.,"NDC");
	pCMS2.SetTextFont(42);
	pCMS2.SetTextSize(top2*0.75);
	pCMS2.SetTextAlign(32);
	pCMS2.SetFillStyle(-1);
	pCMS2.SetBorderSize(0);
	pCMS2.AddText("(13 TeV)");
	TPaveText pave22(0.2,0.8,0.4,1.-top2*1.666,"NDC");
	pave22.SetTextAlign(11);
	pave22.SetFillStyle(-1);
	pave22.SetBorderSize(0);
	pave22.SetTextFont(62);
	pave22.SetTextSize(top2*0.5);
	pave22.AddText("HHbbgg");
	TPaveText pave33(0.2,0.75,0.4,0.8,"NDC");
	pave33.SetTextAlign(11);
	pave33.SetFillStyle(-1);
	pave33.SetBorderSize(0);
	pave33.SetTextFont(42);
	pave33.SetTextColor(kBlue);
	pave33.SetTextSize(top2*0.5);
	TLegend *leg = new TLegend(0.72,0.78,0.85,0.9);
	leg->SetFillColor(0);
	leg->SetBorderSize(0);
	leg->SetTextFont(42);
	leg->SetTextSize(0.025);
	leg->AddEntry(hist_S2,"Sig","F");
	leg->AddEntry(hist_B2,"BG","F");

	double bin=0.;
	double s1=0; double b1=0;
	int i=0;
	float max_all=0;
		do	{
			s1=hist_S2->GetBinContent(i+1);
			b1=hist_B2->GetBinContent(i+1);
			bin=(double) hist_S2->GetBinCenter(i+1+1);
			if ((b1)!=0) max_all += pow(s1,2)/(b1);
			i++;
		} while (bin < END);

double max = 0;
double borders[10] = {};   // including START and END
borders[0] = START;
double sig_n[10] = {0,0,0,0,0,0,0,0,0,0};
double bkg_n[10] = {0,0,0,0,0,0,0,0,0,0};
double data_n[10] = {0,0,0,0,0,0,0,0,0,0};
double bkg_sideband_n[10] = {0,0,0,0,0,0,0,0,0,0};
double data_sideband_n[10] = {0,0,0,0,0,0,0,0,0,0};
double max_n[10] = {0,0,0,0,0,0,0,0,0,0};
double max_final[10] = {0,0,0,0,0,0,0,0,0,0};
double max_total = 0;
double start_n[10] = {0,0,0,0,0,0,0,0,0,0};
double bkg_yields[10] = {0,0,0,0,0,0,0,0,0,0};
double bkg_yields_sideband[10] = {0,0,0,0,0,0,0,0,0,0};
double data_yields[10] = {0,0,0,0,0,0,0,0,0,0};
double data_yields_sideband[10] = {0,0,0,0,0,0,0,0,0,0};
double sig_yields[10] = {0,0,0,0,0,0,0,0,0,0};


for (int index=0;index<NCAT;index++)
     start_n[index]=START+(index+1)*precision;
int minevt_cond_n[10] = {};

std::vector<double> categories_scans0;
std::vector<double> categories_scans1;
std::vector<double> categories_scans2;
std::vector<double> categories_scans3;
std::vector<double> significance_scans0;
std::vector<double> significance_scans1;
std::vector<double> significance_scans2;
std::vector<double> significance_scans3;

	do {
		max_n[0]=0;
		sig_n[0] = hist_S->Integral(1,hist_S->FindBin(start_n[0])-1);
		bkg_n[0] = hist_B->Integral(1,hist_B->FindBin(start_n[0])-1);
		bkg_sideband_n[0] = hist_B_sideband->Integral(1,hist_B_sideband->FindBin(start_n[0])-1);
		data_sideband_n[0] = hist_D_sideband->Integral(1,hist_D_sideband->FindBin(start_n[0])-1);
		if (bkg_n[0]!=0) max_n[0]=pow(sig_n[0],2)/bkg_n[0];
		start_n[1]=start_n[0]+precision;

		bkg_sideband_n[1] = hist_B_sideband->Integral(hist_B_sideband->FindBin(start_n[0]),hist_B_sideband->GetNbinsX()+1);
		data_sideband_n[1] = hist_D_sideband->Integral(hist_D_sideband->FindBin(start_n[0]),hist_D_sideband->GetNbinsX()+1);
		// cout << "#1 BIN " << start_n[0] << endl;
		if (bkg_n[1]!=0) max_n[1]=pow(sig_n[1],2)/bkg_n[1];

		if (1>0) {
			categories_scans0.push_back(start_n[0]);
			significance_scans0.push_back(sqrt(max_n[1]));
			// cout << sqrt(max_n[1]) << endl;
		}

		do {
			max_n[1]=0;
			sig_n[1] = hist_S->Integral(hist_S->FindBin(start_n[0]),hist_S->FindBin(start_n[1])-1);
			bkg_n[1] = hist_B->Integral(hist_B->FindBin(start_n[0]),hist_B->FindBin(start_n[1])-1);
			bkg_sideband_n[1] = hist_B_sideband->Integral(hist_B_sideband->FindBin(start_n[0]),hist_B_sideband->FindBin(start_n[1])-1);
			data_sideband_n[1] = hist_D_sideband->Integral(hist_D_sideband->FindBin(start_n[0]),hist_D_sideband->FindBin(start_n[1])-1);
			// cout << "#2 BIN " << start_n[0] << endl;
			if (bkg_n[1]!=0) max_n[1]=pow(sig_n[1],2)/bkg_n[1];

			start_n[2]=start_n[1]+precision;
			do{
				max_n[2]=0;
				if (NCAT<=2) {
					sig_n[2] = 0;
					bkg_n[2] = 1;
					bkg_sideband_n[2] = 1;
					data_n[2] = 1;
					data_sideband_n[2] = 1;
				} else {
					sig_n[2] = hist_S->Integral(hist_S->FindBin(start_n[1]),hist_S->FindBin(start_n[2])-1);
					bkg_n[2] = hist_B->Integral(hist_B->FindBin(start_n[1]),hist_B->FindBin(start_n[2])-1);
					bkg_sideband_n[2] = hist_B_sideband->Integral(hist_B_sideband->FindBin(start_n[1]),hist_B_sideband->FindBin(start_n[2])-1);
					data_sideband_n[2] = hist_D_sideband->Integral(hist_D_sideband->FindBin(start_n[1]),hist_D_sideband->FindBin(start_n[2])-1);
					// cout << "#3 BIN " << start_n[1] << endl;
				}
				if (bkg_n[2]!=0) max_n[2]=pow(sig_n[2],2)/bkg_n[2];

				start_n[3]=start_n[2]+precision;
				do{
					max_n[3]=0;
					if (NCAT<=3) {
						sig_n[3] = 0;
						bkg_n[3] = 1;
						bkg_sideband_n[3] = 1;
						data_sideband_n[3] = 1;
					} else {
						sig_n[3] = hist_S->Integral(hist_S->FindBin(start_n[2]),hist_S->FindBin(start_n[3])-1);
						bkg_n[3] = hist_B->Integral(hist_B->FindBin(start_n[2]),hist_B->FindBin(start_n[3])-1);
						bkg_sideband_n[3] = hist_B_sideband->Integral(hist_B_sideband->FindBin(start_n[2]),hist_B_sideband->FindBin(start_n[3])-1);
						data_sideband_n[3] = hist_D_sideband->Integral(hist_D_sideband->FindBin(start_n[2]),hist_D_sideband->FindBin(start_n[3])-1);
						// cout << "#4 BIN " << start_n[2] << endl;
					}
					if (bkg_n[3]!=0) max_n[3]=pow(sig_n[3],2)/bkg_n[3];

					max_n[4]=0;
               if (NCAT<=4) {
               	sig_n[4] = 0.;
                  bkg_n[4] = 1.;
                  bkg_sideband_n[4] = 1.;
									data_sideband_n[4] = 1.;
               } else {
						sig_n[4] = hist_S->Integral(hist_S->FindBin(start_n[3]),hist_S->GetNbinsX()+1);
						bkg_n[4] = hist_B->Integral(hist_B->FindBin(start_n[3]),hist_B->GetNbinsX()+1);
						bkg_sideband_n[4] = hist_B_sideband->Integral(hist_B_sideband->FindBin(start_n[3]),hist_B_sideband->GetNbinsX()+1);
						data_sideband_n[4] = hist_D_sideband->Integral(hist_D_sideband->FindBin(start_n[3]),hist_D_sideband->GetNbinsX()+1);
						// cout << "#5 BIN " << start_n[3] << endl;
               }
					if (bkg_n[4]!=0) max_n[4]=pow(sig_n[4],2)/bkg_n[4];

					double max_sum = 0;
					int minevt_cond = 0; //condition is false
					for (int index=0;index<NCAT;index++){ //start from 1 for tth  only when optimizing separately
						max_sum+=max_n[index];
						// minevt_cond_n[index] = ( (data_sideband_n[index] >= 4));
						 // minevt_cond_n[index] = (bkg_sideband_n[index]>=minevents );
						minevt_cond_n[index] = (bkg_sideband_n[index]>=minevents && (data_sideband_n[index] >= 6));
					}
					minevt_cond = std::accumulate(minevt_cond_n, minevt_cond_n + NCAT, 0); // minevt_cond_n+1 for tth only when optimizing separately
					if (((max_sum)>=max) && (minevt_cond==(NCAT))) { //NCAT-1 for tth
						max = max_sum;
						for (int index=0;index<NCAT;index++){
							borders[index+1] = start_n[index]; //first and last are START and END
							max_final[index] = max_n[index];
							bkg_yields[index] = bkg_n[index];
							bkg_yields_sideband[index] = bkg_sideband_n[index];
							data_yields_sideband[index] = data_sideband_n[index];
							sig_yields[index] = sig_n[index];
							max_total = max_sum;
						}
					}
					start_n[3]+=precision;
				} while (start_n[3]<=(END-(NCAT-4)*precision));
				start_n[2]+=precision;
			} while (start_n[2]<=(END-(NCAT-3)*precision));
			start_n[1]+=precision;
		} while (start_n[1]<=(END-(NCAT-2)*precision));
		start_n[0]+=precision;
	} while (start_n[0]<=(END-(NCAT-1)*precision));

	borders[NCAT] = END;

	ofstream outborder;
	outborder.open(s.Format("%s%s_fineBinning_combined.txt",outDir.Data(),outnameborder.Data()));
	for (int index=0;index<NCAT+1;index++)
		outborder<<borders[index]<<"\t";
	outborder<<endl;
	outborder.close();

	ofstream out;
	out.open(s.Format("%s%s_fineBinning_combined.txt",outDir.Data(),outname.Data()));
	// out<<"subcategory : "<<subcategory<<endl;
	out<<"S2/B over all bins, sqrt : "<<max_all<<"  , "<<sqrt(max_all)<<endl;
	out<<endl;
	out<<"S**2/B total over the chosen categories : "<<max_total<<"  ,S/sqrt(B) =  "<<sqrt(max_total)<<endl;
	out<<endl;
	out<<"borders of categories : ";
	for (int index=0;index<NCAT+1;index++)
		out<<borders[index]<<"\t";
	out<<endl;
	out<<endl;
	out<<"S**2/B in each category : ";
	for (int index=0;index<NCAT;index++)
		out<<max_final[index]<<"\t";
	out<<endl;
	out<<endl;
	out<<"sqrt(S**2/B) in each category : ";
	for (int index=0;index<NCAT;index++)
		out<<sqrt(max_final[index])<<"\t";
	out<<endl;
	out<<endl;
	out<<"Mgg sidebands bkg yields in categories : ";
	for (int index=0;index<NCAT;index++)
		out<<bkg_yields_sideband[index]<<"\t";
	out<<endl;
	out<<"bkg yields in categories : ";
	for (int index=0;index<NCAT;index++)
		out<<bkg_yields[index]<<"\t";
	out<<endl;
	out<<"sig yields in categories : ";
	for (int index=0;index<NCAT;index++)
		out<<sig_yields[index]<<"\t";
  out<<endl;
	out<<"Mgg sidebands data yields in categories : ";
	for (int index=0;index<NCAT;index++)
		out<<data_yields_sideband[index]<<"\t";
	out<<endl;
	out.close();

  string line;
  ifstream outfile(s.Format("%s%s_fineBinning_combined.txt",outDir.Data(),outname.Data()));
  if (outfile.is_open()){
    while ( getline (outfile,line) )
      cout << line << '\n';
    outfile.close();
  }



	float ymin=hist_S2->GetBinContent(hist_S2->FindFirstBinAbove(0.))*0.1;
	float ymax=hist_B2->GetMaximum()*1e02;

	TLine* lines[10];
	for (int index=0;index<NCAT-1;index++){
		lines[index] = new TLine(borders[index+1],ymin,borders[index+1],hist_B2->GetBinContent(hist_B2->FindBin(borders[index+1]))+5);
		lines[index]->SetLineStyle(9);
		lines[index]->SetLineColor(1);
		lines[index]->SetLineWidth(3);
	}

	TCanvas *c1 = new TCanvas("Fit","",800,800);
	c1->SetLogy();
	c1->cd();
	TH1F *frame2 = new TH1F("frame2","",50,xmin,xmax);


	frame2->GetXaxis()->SetNdivisions(505);
//	frame2->GetYaxis()->SetRangeUser(80,150);
   frame2->SetStats(0);
	frame2->SetYTitle("Events");
	frame2->SetXTitle(s.Format("%s",what_to_opt.Data()));
	frame2->SetMinimum(ymin);
	frame2->SetMaximum(ymax);
	frame2->Draw();

	// hist_B2->GetXaxis()->SetRange(0,1);
	// hist_S2->GetXaxis()->SetRange(0,1);
	hist_B2->Draw("HISTsame");
	hist_S2->Draw("HISTsame");
//	hist_B_cut_tth->Draw("HISTsame")
  TLatex latex;
  latex.SetTextSize(0.025);
  latex.SetTextAlign(13);  //align at top
	// for (int index=0;index<NCAT;index++)
		// latex.DrawLatex(-1,100000,std::to_string(sig_yields[index]).c_str());
  // latex.DrawLatex(-1,100000,"K_{S}");
	// latex.Draw();
//	leg->AddEntry(hist_B_cut_tth,"ttH","L");

	gPad->Update();
	// pCMS1.Draw("same");
	// pCMS2.Draw("same");
	// pCMS12.Draw("same");
	// pave22.Draw("same");
	// pave33.Draw("same");
	leg->Draw("same");
	for (int index=0;index<NCAT-1;index++)
		lines[index]->Draw("same");
	gPad->RedrawAxis();
	c1->Print(s.Format("%s%s_fineBinning_combined.png",outDir.Data(),outname.Data()));
	c1->Print(s.Format("%s%s_fineBinning_combined.pdf",outDir.Data(),outname.Data()));



	double* cat_scan = &categories_scans0[0];
	double* sign_scan = &significance_scans0[0];
	int counter = significance_scans0.size();
	TGraph *gr =new TGraph(counter,cat_scan,sign_scan);

	// cout << sign_scan << endl;
	// cout << "ymin: " << *std::max_element(sign_scan,sign_scan+counter) << endl;
	ymin = *std::max_element(sign_scan,sign_scan+counter) * 0.01;
	ymax = *std::max_element(sign_scan,sign_scan+counter) * 1.1;
	gr->SetMarkerStyle(20);
	int max_pos = std::distance(sign_scan, std::max_element(sign_scan,sign_scan+counter));

	TCanvas *c2 = new TCanvas("B","",800,800);
	c2->cd();
	TH1F *frame3 = new TH1F("frame3","",50,xmin,xmax);
	frame3->GetXaxis()->SetNdivisions(505);
   frame3->SetStats(0);
//	frame3->SetYTitle("S/#sqrt{B_{#gamma#gamma}+B_{ttH}}");
	frame3->SetYTitle("S/#sqrt{B}");
	frame3->GetYaxis()->SetTitleOffset(1.32);
	frame3->SetXTitle(s.Format("%s",what_to_opt.Data()));
	frame3->SetMinimum(ymin);
	frame3->SetMaximum(ymax);
	frame3->Draw();
	gr->Draw("Psame");
	gPad->Update();
	// pCMS1.Draw("same");
	// pCMS2.Draw("same");
	// pCMS12.Draw("same");
	// pave22.Draw("same");
	// pave33.Draw("same");
	gPad->RedrawAxis();
	c2->Print(s.Format("%ssignificance_%s_fineBinning_combined.pdf",outDir.Data(),outname.Data()));
	c2->Print(s.Format("%ssignificance_%s_fineBinning_combined.png",outDir.Data(),outname.Data()));
	cout<<counter<<endl;

}
