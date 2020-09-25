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

#include "CatOptUtils.C"

using namespace std;

void optimize_cats(const int NCATS, bool scaleBkgSideband, bool verbose, double xcutoff, double bin_width_) {
	
	// Misc 
	gROOT->SetBatch("kTrue");

	// Parameters 
	TString scaleOpt;
	if(scaleBkgSideband) scaleOpt = "withSidebandScale";
	else scaleOpt = "noSidebandScale";	
	TString outDir = "/eos/user/a/atishelm/www/HHWWgg/NtupleAnalysis/DNN/DNN_Categorization/";
	TString what_to_opt = "evalDNN";
	double minevents = 1.;
	// double xmin = 0.0;
	double xmin = xcutoff;
	double xmax = 1.00001; // to include values that == 1  
	// Double_t bin_width=0.01; // course binning 
	// Double_t bin_width=0.0025;
	Double_t bin_width = bin_width_;
	TString xmin_str = to_string(xcutoff);
	TString binWidth_str = to_string(bin_width_);
	TString extraSelection = "*(1)";
	// TString extraSelection = "*(N_goodMuons == 1)";
	// TString extraSelection = "*(N_goodMuons == 1)";
	TString Mgg_window = "*((CMS_hgg_mass>115)&&(CMS_hgg_mass<135))";
	TString Mgg_sideband = "*((CMS_hgg_mass<=115)||(CMS_hgg_mass>=135))";
	TString selection_sig = "33.49*0.00097*0.441*41.5*weight*(CMS_hgg_mass > 100 && CMS_hgg_mass < 180)" + extraSelection; // normalize signal properly with cross section 
	TString selection_bg = "41.5*weight*(CMS_hgg_mass > 100 && CMS_hgg_mass < 180)" + extraSelection;
	TString selection_data = "(1)" + extraSelection;
	TString s; TString sel;
	TString outname = s.Format("Categorization_%s_%dcats",what_to_opt.Data(),NCATS);

	// Combine Signal Trees
	cout << "nBins: " << int((xmax-xmin)/bin_width) << endl;
	cout << "xmin: " << xmin << endl;
	cout << "xmax: " << xmax << endl;

	TChain *file_s =  new TChain("file_s");
	file_s->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Signal/ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root/GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_0");
	file_s->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Signal/ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root/GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_1");
	file_s->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Signal/ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root/GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_2");
	file_s->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Signal/ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root/GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_3");
	file_s->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Signal/ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root/GluGluToHHTo_WWgg_qqlnu_nodeSM_13TeV_HHWWggTag_4");
	TH1F *hist_S = new TH1F("hist_S","hist_S",int((xmax-xmin)/bin_width),xmin,xmax);
    s.Form("%s>>hist_S",what_to_opt.Data());
    sel.Form("%s",(selection_sig+Mgg_window).Data());
	file_s->Draw(s,sel,"goff");

	// Combine Background Trees
	TChain *tree_bg =  new TChain("tree_bg");
	string backgroundDirec = "/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Backgrounds_promptpromptselapplied";
	vector<string> v;     
	v = read_directory(backgroundDirec); // Get vector of background files 
	cout << " " << endl; 
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

	// Combine Data Trees 
	TChain *tree_data =  new TChain("tree_data");
	tree_data->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Data/Data.root/Data_13TeV_HHWWggTag_0");
	tree_data->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Data/Data.root/Data_13TeV_HHWWggTag_1");
	tree_data->Add("/eos/user/a/atishelm/ntuples/HHWWgg_DataMC/DNN/Data/Data.root/Data_13TeV_HHWWggTag_2");

	// Get Data over Background in sidebands scale factor 
	TH1F* hist_background_sideband = new TH1F("hist_background_sideband","hist_background_sideband",100,-1,1);
	TH1F* hist_data_sideband = new TH1F("hist_data_sideband","hist_data_sideband",100,-1,1);

	s.Form("evalDNN >> hist_background_sideband");
	sel.Form("%s",(selection_bg+Mgg_sideband).Data());
	tree_bg->Draw(s,sel,"goff");

	s.Form("evalDNN >> hist_data_sideband");
	sel.Form("%s",(selection_data+Mgg_sideband).Data());
	tree_data->Draw(s,sel,"goff");

	if(verbose){
		cout << " " << endl;
		cout << "Background sideband Integral: " << hist_background_sideband->Integral() << endl;
		cout << "Data sideband Integral: " << hist_data_sideband->Integral() << endl;
	}

	double scale = 1;

	if(scaleBkgSideband)
		scale = hist_data_sideband->Integral() / hist_background_sideband->Integral();

	// Create Background Hists
	TH1F *hist_B = new TH1F("hist_B","hist_B",int((xmax-xmin)/bin_width),xmin,xmax); //200 bins  -- background signal region
    s.Form("%s>>hist_B",what_to_opt.Data());
    sel.Form("%s",(selection_bg+Mgg_window).Data());
	tree_bg->Draw(s,sel,"goff");
	hist_B->Scale(scale);
	// hist_B->Scale(scale/hist_B->Integral());
	if(verbose){
		cout << " " << endl;
		cout << "BG integral under Mgg "<< hist_B->Integral() << endl;
	} 
	TH1F *hist_B_sideband = new TH1F("hist_B_sideband","hist_B_sideband",int((xmax-xmin)/bin_width),xmin,xmax); // background sideband region

    s.Form("%s>>hist_B_sideband",what_to_opt.Data());
    sel.Form("%s",(selection_bg+Mgg_sideband).Data());
	tree_bg->Draw(s,sel,"goff");
	hist_B_sideband->Scale(scale);
	if(verbose){
		cout << " " << endl;
		cout << "Sidebands SF: " << scale << endl;
		cout << "BG integral sidebands AFTER scaling " << hist_B_sideband->Integral() << endl;
	}

	// Create Data hist
	TH1F *hist_D_sideband = new TH1F("hist_D_sideband","hist_D_sideband",int((xmax-xmin)/bin_width),xmin,xmax); //200 bins -- data sideband region

    s.Form("%s>>hist_D_sideband",what_to_opt.Data());
    sel.Form("%s",(selection_data+Mgg_sideband).Data());
	tree_data->Draw(s,sel,"goff");
	if(verbose){
		cout << " " << endl;
		cout << "Data integral sidebands " << hist_D_sideband->Integral() << endl;
	} 

	// Get Start and Ends of Optimization Range 
	double END = hist_B->GetBinCenter(hist_B->FindLastBinAbove(-1.)) + hist_B->GetBinWidth(1)/2.; // Left end of BDT distibution
	double START = hist_B->GetBinCenter(hist_B->FindFirstBinAbove(-1.)) - hist_B->GetBinWidth(1)/2.; // Right end of BDT distibution
	if(verbose){
		cout << " " << endl;
		cout << "start = " << START << " , end = " << END << endl;
	}

	hist_S->SetFillStyle(4050);
	hist_S->SetLineColor(kRed);
	hist_S->SetFillColor(kRed-7);
	hist_S->SetLineWidth(2);
	hist_B->SetFillStyle(4050);
	hist_B->SetLineColor(kBlue+1);
	hist_B->SetFillColor(kBlue-10);
	hist_B->SetLineWidth(2);

	// Make Copies of Background and Signal Histograms 
	TH1F *hist_B2 = (TH1F*)hist_B->Clone("b_new");
	TH1F *hist_S2 = (TH1F*)hist_S->Clone("s_new");

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
	TLegend *leg = new TLegend(0.72,0.755,0.85,0.875);
	leg->SetFillColor(0);
	leg->SetBorderSize(0);
	leg->SetTextFont(42);
	leg->SetTextSize(0.025);
	leg->AddEntry(hist_S2,"Sig","F");
	leg->AddEntry(hist_B2,"BG","F");

	double bin=0.;
	double s1=0; double b1=0;
	int i=0;
	float TOTAL_S2OB = 0;

	for(int i = 0; i < (int) hist_S2->GetEntries(); i++){
		s1 = hist_S2->GetBinContent(i+1); // +1 to skip underflow bin 
		b1 = hist_B2->GetBinContent(i+1);
		if(b1 != 0) TOTAL_S2OB += pow(s1,2) / (b1);
	}

	// Do these indices with a max of 10 corresond to a max of 10 categories?
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

	for (int index = 0; index < NCATS; index++){
		start_n[index]=START+(index+1)*bin_width; // what is start_n? Initial CAT Minimum maybe
		cout << "start_n[" << index << "] = " << start_n[index] << endl;
	}
	int minevt_cond_n[10] = {};

	std::vector<double> categories_scans;
	std::vector<double> significance_scans;

	// Categorization 
	do {
		max_n[0] = 0; // I think S^2 / B for one or all categories
		sig_n[0] = hist_S->Integral(1,hist_S->FindBin(start_n[0])-1); // Optimize cats based on integral of Signifiance?
		bkg_n[0] = hist_B->Integral(1,hist_B->FindBin(start_n[0])-1);

		// Sidebands 
		bkg_sideband_n[0] = hist_B_sideband->Integral(1,hist_B_sideband->FindBin(start_n[0])-1);
		data_sideband_n[0] = hist_D_sideband->Integral(1,hist_D_sideband->FindBin(start_n[0])-1);

		if (bkg_n[0]!=0) max_n[0]=pow(sig_n[0],2)/bkg_n[0];
		start_n[1]=start_n[0]+bin_width; // initial min for second category?

		bkg_sideband_n[1] = hist_B_sideband->Integral(hist_B_sideband->FindBin(start_n[0]),hist_B_sideband->GetNbinsX()+1);
		data_sideband_n[1] = hist_D_sideband->Integral(hist_D_sideband->FindBin(start_n[0]),hist_D_sideband->GetNbinsX()+1);

		// cout << "#1 BIN " << start_n[0] << endl;

		if (bkg_n[1]!=0) max_n[1]=pow(sig_n[1],2)/bkg_n[1];

		categories_scans.push_back(start_n[0]);
		significance_scans.push_back(sqrt(max_n[1]));

		do {
			max_n[1]=0;
			sig_n[1] = hist_S->Integral(hist_S->FindBin(start_n[0]),hist_S->FindBin(start_n[1])-1);
			bkg_n[1] = hist_B->Integral(hist_B->FindBin(start_n[0]),hist_B->FindBin(start_n[1])-1);
			bkg_sideband_n[1] = hist_B_sideband->Integral(hist_B_sideband->FindBin(start_n[0]),hist_B_sideband->FindBin(start_n[1])-1);
			data_sideband_n[1] = hist_D_sideband->Integral(hist_D_sideband->FindBin(start_n[0]),hist_D_sideband->FindBin(start_n[1])-1);

			// cout << "#2 BIN " << start_n[0] << endl;

			if (bkg_n[1]!=0) max_n[1]=pow(sig_n[1],2)/bkg_n[1];

			start_n[2]=start_n[1]+bin_width;
			do{
				max_n[2]=0;
				if (NCATS<=2) {
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

				start_n[3]=start_n[2]+bin_width;
				do{
					max_n[3]=0;
					if (NCATS<=3) {
						sig_n[3] = 0;
						bkg_n[3] = 1;
						bkg_sideband_n[3] = 1;
						data_sideband_n[3] = 1;
					} 
					
					else {
						sig_n[3] = hist_S->Integral(hist_S->FindBin(start_n[2]),hist_S->FindBin(start_n[3])-1);
						bkg_n[3] = hist_B->Integral(hist_B->FindBin(start_n[2]),hist_B->FindBin(start_n[3])-1);
						bkg_sideband_n[3] = hist_B_sideband->Integral(hist_B_sideband->FindBin(start_n[2]),hist_B_sideband->FindBin(start_n[3])-1);
						data_sideband_n[3] = hist_D_sideband->Integral(hist_D_sideband->FindBin(start_n[2]),hist_D_sideband->FindBin(start_n[3])-1);

						// cout << "#4 BIN " << start_n[2] << endl;

					}
					if (bkg_n[3]!=0) max_n[3]=pow(sig_n[3],2)/bkg_n[3];

					max_n[4]=0;

					if (NCATS<=4) 
					{
						sig_n[4] = 0.;
						bkg_n[4] = 1.;
						bkg_sideband_n[4] = 1.;
						data_sideband_n[4] = 1.;
					} 
					
					else 
					{
						sig_n[4] = hist_S->Integral(hist_S->FindBin(start_n[3]),hist_S->GetNbinsX()+1); // FindBin returns the bin number corresponding to the x value
						bkg_n[4] = hist_B->Integral(hist_B->FindBin(start_n[3]),hist_B->GetNbinsX()+1); // 

						// Sidebands 
						bkg_sideband_n[4] = hist_B_sideband->Integral(hist_B_sideband->FindBin(start_n[3]),hist_B_sideband->GetNbinsX()+1);
						data_sideband_n[4] = hist_D_sideband->Integral(hist_D_sideband->FindBin(start_n[3]),hist_D_sideband->GetNbinsX()+1);

						// cout << "#5 BIN " << start_n[3] << endl;

					}
						
					if (bkg_n[4]!=0) max_n[4]=pow(sig_n[4],2)/bkg_n[4];

					double max_sum = 0;
					int minevt_cond = 0; //condition is false
					for (int index=0;index<NCATS;index++){ //start from 1 for tth only when optimizing separately
						max_sum+=max_n[index];
						// minevt_cond_n[index] = ( (data_sideband_n[index] >= 4));
						//  minevt_cond_n[index] = (bkg_sideband_n[index]>=minevents );
						minevt_cond_n[index] = (bkg_sideband_n[index]>=minevents && (data_sideband_n[index] >= 6));
					}
					minevt_cond = std::accumulate(minevt_cond_n, minevt_cond_n + NCATS, 0); // minevt_cond_n+1 for tth only when optimizing separately
					if (((max_sum)>=max) && (minevt_cond==(NCATS))) { //NCATS-1 for tth
						max = max_sum;
						for (int index=0;index<NCATS;index++){
							borders[index+1] = start_n[index]; // first and last are START and END
							max_final[index] = max_n[index];
							bkg_yields[index] = bkg_n[index];
							bkg_yields_sideband[index] = bkg_sideband_n[index];
							data_yields_sideband[index] = data_sideband_n[index];
							sig_yields[index] = sig_n[index];
							max_total = max_sum;
						}
					}
					start_n[3]+=bin_width;
				} while (start_n[3]<=(END-(NCATS-4)*bin_width)); // probably max at num cats - NCATS because you can't determine the significance integral for the 1st category so high that cats can't be added at bins starting above it 
				start_n[2]+=bin_width;
			} while (start_n[2]<=(END-(NCATS-3)*bin_width));
			start_n[1]+=bin_width;
		} while (start_n[1]<=(END-(NCATS-2)*bin_width));
		start_n[0]+=bin_width;
	} while (start_n[0]<=(END-(NCATS-1)*bin_width)); 

	borders[NCATS] = END;

	// // Save Border Values to Text File
	// ofstream outborder;
	// outborder.open(s.Format("%s%s_%s.txt",outDir.Data(),outnameborder.Data(),scaleOpt.Data()));
	// for (int index=0;index<NCATS+1;index++)
	// 	outborder<<borders[index] << "\t";
	// outborder<<endl;
	// outborder.close();

	// Write Output Text File 
	ofstream out;
	out.open(s.Format("%s%s_%s_xmin-%s_binWidth-%s.txt",outDir.Data(),outname.Data(),scaleOpt.Data(),xmin_str.Data(),binWidth_str.Data()));
	out << "(S**2)tot/Btot over all bins: " << TOTAL_S2OB << endl;
	out << endl;
	out << "sqrt((S**2)tot/Btot) over all bins: " << sqrt(TOTAL_S2OB) << endl;
	out << endl;	
	out << "S**2/B total over the chosen categories : " << max_total << "  , S/sqrt(B) =  " << sqrt(max_total) << endl;
	out << endl;
	out << "borders of categories : ";
	for (int index=0;index<NCATS+1;index++)
		out << borders[index] << "\t";
	out << endl;
	out << endl;
	out << "S**2/B in each category : ";
	for (int index=0;index<NCATS;index++)
		out << max_final[index] << "\t";
	out << endl;
	out << endl;
	out << "sqrt(S**2/B) in each category : ";
	for (int index=0;index<NCATS;index++)
		out << sqrt(max_final[index]) << "\t";
	out << endl;
	out << endl;
	out << "Mgg sidebands bkg yields in categories : ";
	for (int index=0;index<NCATS;index++)
		out << bkg_yields_sideband[index] << "\t";
	out << endl;
	out << "bkg yields in categories : ";
	for (int index=0;index<NCATS;index++)
		out << bkg_yields[index] << "\t";
	out << endl;
	out << "sig yields in categories : ";
	for (int index=0;index<NCATS;index++)
		out << sig_yields[index] << "\t";
	out << endl;
	out << "Mgg sidebands data yields in categories : ";
	for (int index=0;index<NCATS;index++)
		out << data_yields_sideband[index] << "\t";
	out << endl;
	out.close();

	string line;
	ifstream outfile(s.Format("%s%s_fineBinning_combined.txt",outDir.Data(),outname.Data()));
	if (outfile.is_open()){
		while ( getline (outfile,line) )
		cout << line << '\n';
		outfile.close();
	}

	// float ymin=hist_S2->GetBinContent(hist_S2->FindFirstBinAbove(0.))*0.1;
	float ymin = 0.0001;
	float ymax=hist_B2->GetMaximum()*1e02;

	TLine* lines[10];
	for (int index=0;index<NCATS-1;index++){
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
	frame2->GetYaxis()->SetRangeUser(80,150);
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
	// hist_B_cut_tth->Draw("HISTsame")
	TLatex latex;
	latex.SetTextSize(0.025);
	latex.SetTextAlign(13);  //align at top
	// for (int index=0;index<NCATS;index++)
		// latex.DrawLatex(-1,100000,std::to_string(sig_yields[index]).c_str());
    // latex.DrawLatex(-1,100000,"K_{S}");
	// latex.Draw();
	// leg->AddEntry(hist_B_cut_tth,"ttH","L");

	gPad->Update();
	// pCMS1.Draw("same");
	// pCMS2.Draw("same");
	// pCMS12.Draw("same");
	// pave22.Draw("same");
	// pave33.Draw("same");
	leg->Draw("same");
	for (int index=0;index<NCATS-1;index++)
		lines[index]->Draw("same");
	gPad->RedrawAxis();
	c1->Print(s.Format("%s/%s_%s_xMin-%s_binWidth-%s.png",outDir.Data(),scaleOpt.Data(),outname.Data(),xmin_str.Data(),binWidth_str.Data()));
	c1->Print(s.Format("%s/%s_%s_xMin-%s_binIwdth-%s.pdf",outDir.Data(),scaleOpt.Data(),outname.Data(),xmin_str.Data(),binWidth_str.Data()));

	double* cat_scan = &categories_scans[0];
	double* sign_scan = &significance_scans[0];
	int counter = significance_scans.size();

	// TGraph *gr = new TGraph(counter,cat_scan,sign_scan); // significance plot 

	// cout << sign_scan << endl;
	// cout << "ymin: " << *std::max_element(sign_scan,sign_scan+counter) << endl;
	// old end of ymin: * 0.01 
	ymin = *std::max_element(sign_scan,sign_scan+counter) * 0.01;
	ymax = *std::max_element(sign_scan,sign_scan+counter) * 1.1;
	// gr->SetMarkerStyle(20);
	int max_pos = std::distance(sign_scan, std::max_element(sign_scan,sign_scan+counter));

	TCanvas *c2 = new TCanvas("B","",800,800);
	c2->cd();
	TH1F *frame3 = new TH1F("frame3","",50,xmin,xmax);
	frame3->GetXaxis()->SetNdivisions(505);
	frame3->SetStats(0);
	frame3->SetYTitle("S/#sqrt{B}");
	frame3->GetYaxis()->SetTitleOffset(1.32);
	frame3->SetXTitle(s.Format("%s",what_to_opt.Data()));
	frame3->SetMinimum(ymin);
	frame3->SetMaximum(ymax);
	frame3->Draw();
	// gr->Draw("Psame");
	gPad->Update();
	// pCMS1.Draw("same");
	// pCMS2.Draw("same");
	// pCMS12.Draw("same");
	// pave22.Draw("same");
	// pave33.Draw("same");
	gPad->RedrawAxis();

	// Make Significance Plots
	cout << "Signal integral: " << hist_S2->Integral() << endl;;
	cout << "Background integral: " << hist_B2->Integral() << endl;;

	gStyle->SetOptStat(0000);
	int bin_i = 0;
	double sig, bkg = 0.; 
	double sigOverSqrtb = 0;
	double maxsigOverSqrtb = -99;
	TH1F * Significance_h = new TH1F("Significance_h","S/#sqrt{B} vs. DNN Score " + scaleOpt,int((xmax-xmin)/bin_width),xmin,xmax);
	for(int i = 0; i < (int) hist_S2->GetNbinsX(); i++){
		bin_i = i + 1; // +1 to skip underflow bin
		sig = hist_S2->GetBinContent(bin_i);  
		bkg = hist_B2->GetBinContent(bin_i);
		if(bkg != 0){
			sigOverSqrtb = sig / sqrt(bkg);	
			Significance_h->SetBinContent(bin_i, sigOverSqrtb); 
			if(sigOverSqrtb > maxsigOverSqrtb) maxsigOverSqrtb = sigOverSqrtb;
			cout << "evalDNN bin x min: " << Significance_h->GetBinLowEdge(bin_i) << endl;
			cout << "S : " << sig << endl;
			cout << "B : " << bkg << endl;
			cout << "significance: " << sigOverSqrtb << endl;
		}
	}

	// TH1F * Shaded_Area = new TH1F("Shaded_Area","S/#sqrt{B} vs. DNN Score " + scaleOpt,1,xmin,xcutoff);
	// Shaded_Area->SetFillColorAlpha(kRed,0.5);

	// Get Total Significance for each category
	ofstream catSigOut;
	catSigOut.open(s.Format("%s%s_%s_xmin-%s_binWidth-%s_CatSignificances.txt",outDir.Data(),outname.Data(),scaleOpt.Data(),xmin_str.Data(),binWidth_str.Data()));
	double cat_min, cat_max = 0.; 	
	double Cat_significance = 0.;
	int min_bin, max_bin = 0;
	double S_total, B_total = 0; 
	for(int i = 0; i < NCATS; i++){
		if(i == 0){
			cat_min = xcutoff;
			cat_max = borders[i+1];
		}
		else{
			cat_min = borders[i];
			cat_max = borders[i+1];
		}

		cout << "Cat min: " << cat_min << endl;
		cout << "Cat max: " << cat_max << endl;

		// sig = hist_S2->GetBinContent(bin_i);  
		// bkg = hist_B2->GetBinContent(bin_i);

		min_bin = hist_S2->FindBin(cat_min);
		max_bin = hist_S2->FindBin(cat_max);
		// if(i == NCATS-1) max_bin = Significance_h->FindBin(cat_max);
		// else max_bin = Significance_h->FindBin(cat_max)-1;

		// cout << "min_bin: " << min_bin << endl;
		// cout << "max_bin: " << max_bin << endl;

		cout << "min_bin low edge: " << hist_S2->GetBinLowEdge(min_bin) << endl;
		cout << "max_bin low edge: " << hist_S2->GetBinLowEdge(max_bin) << endl;		

		// cout << "min bin: " << Significance_h->GetBinLowEdge(min_bin) << endl;
		// cout << "max bin: " << Significance_h->GetBinLowEdge(max_bin) << endl;

		// Cat_significance = Significance_h->Integral(min_bin,max_bin); // significance for all signal region events in this category
		S_total = hist_S2->Integral(min_bin, max_bin);
		B_total = hist_B2->Integral(min_bin, max_bin);

		cout << "S: " << S_total << endl; 
		cout << "B: " << B_total << endl; 

		Cat_significance = S_total / sqrt(B_total); 
		cout << "Significance in the signal region events: " << Cat_significance << endl;
		catSigOut << "Cat: [" << cat_min << ", " << cat_max << "]: " << Cat_significance << "\n";
	}

	catSigOut.close();

	TCanvas * sig_c = new TCanvas("sig_c","sig_c",800,600);
	sig_c->cd();
	Significance_h->SetMarkerStyle(kFullCircle);
	Significance_h->GetXaxis()->SetTitle(what_to_opt);
	Significance_h->GetYaxis()->SetTitle("S/#sqrt{B}");
	Significance_h->Draw("P");

	TLine* CatLines[10];
	double canvas_ymin, canvas_ymax = 0.;
	sig_c->Update(); // https://root-forum.cern.ch/t/drawing-tline-over-a-histogram/10279/3
	canvas_ymin = sig_c->GetUymin();
	canvas_ymax = sig_c->GetUymax();
	// double cat_min, cat_max = 0.; 	
	for (int i = 0; i < NCATS-1; i++){
		CatLines[i] = new TLine(borders[i+1],canvas_ymin,borders[i+1],canvas_ymax);
		CatLines[i]->SetLineStyle(9);
		CatLines[i]->SetLineColor(1);
		CatLines[i]->SetLineWidth(3);
		CatLines[i]->Draw("same");
	}

	// Shaded_Area->Fill(0.00001,canvas_ymax);
	// Shaded_Area->Draw("hist same");

	sig_c->SaveAs(outDir + "Significance_" + scaleOpt + "_xmin-" + xmin_str + "_binWidth-" + binWidth_str + ".png");

	TCanvas * sig_c_log = new TCanvas("sig_c_log","sig_c_log",800,600);
	sig_c_log->cd();
	Significance_h->Draw("P");
	sig_c_log->SetLogy();
	gPad->Update();
	TLine* CatLinesLog[10];
	canvas_ymin = sig_c->GetUymin();
	canvas_ymax = sig_c->GetUymax();	
	for (int i = 0; i < NCATS-1; i++){
		Double_t lm = gPad->GetLeftMargin();
		Double_t rm = 1.-gPad->GetRightMargin();
		Double_t tm = 1.-gPad->GetTopMargin();
		Double_t bm = gPad->GetBottomMargin();
		Double_t xndc = (rm-lm)*((borders[i+1]-gPad->GetUxmin())/(gPad->GetUxmax()-gPad->GetUxmin()))+lm;
		CatLinesLog[i] = new TLine(borders[i+1],bm,borders[i+1],tm);
		CatLinesLog[i]->SetLineStyle(9);
		CatLinesLog[i]->SetLineColor(1);
		CatLinesLog[i]->SetLineWidth(3);
		CatLinesLog[i]->DrawLineNDC(xndc,bm,xndc,tm);
	}	

	// Shaded_Area->SetBinContent(1,100);
	// Shaded_Area->Draw("hist same");
	sig_c_log->SaveAs(outDir + "Significance_" + scaleOpt + "_xmin-" + xmin_str + "_binWidth-" + binWidth_str + "_log.png");
}
