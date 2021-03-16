#include <sys/types.h>
#include <dirent.h>
 
void Print(string text) 
{
    cout << text << endl; 
}

vector<string> read_directory(string name)
{
    vector<string> v;
    DIR* dirp = opendir(name.c_str());
    struct dirent * dp;
    while ((dp = readdir(dirp)) != NULL) {
        string file = dp->d_name;
        if(file != "." && file != "..")
            {
                // cout << "Found file: " << file << endl;
                v.push_back(file);
            }
    }
    closedir(dirp);
    return v; 
}

string GetMCTreeName(string fileName)
{
    map<string, string> MCTreesMap; 
    MCTreesMap.insert(make_pair("DiPhotonJetsBox_M40_80-Sherpa_Hadded.root","DiPhotonJetsBox_M40_80_Sherpa"));
    MCTreesMap.insert(make_pair("DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8_Hadded.root","DiPhotonJets_MGG_80toInf_13TeV_amcatnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("WW_TuneCP5_13TeV-pythia8_Hadded.root","WW_TuneCP5_13TeV_pythia8"));
    MCTreesMap.insert(make_pair("GluGluHToGG_M-125_13TeV_powheg_pythia8_Hadded.root","GluGluHToGG_M_125_13TeV_powheg_pythia8"));
    MCTreesMap.insert(make_pair("GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8_Hadded.root","GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root","ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8"));
    MCTreesMap.insert(make_pair("DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa_Hadded.root","DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa"));
    MCTreesMap.insert(make_pair("GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root","GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8"));
    MCTreesMap.insert(make_pair("GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root","GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8"));
    MCTreesMap.insert(make_pair("GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root","GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8"));
    MCTreesMap.insert(make_pair("QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root","QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8"));
    MCTreesMap.insert(make_pair("QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8_Hadded.root","QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8"));
    MCTreesMap.insert(make_pair("QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8_Hadded.root","QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8"));
    MCTreesMap.insert(make_pair("VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root","VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8"));
    MCTreesMap.insert(make_pair("TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_Hadded.root","TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8"));
    MCTreesMap.insert(make_pair("DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root","DYJetsToLL_M_50_TuneCP5_13TeV_amcatnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("VBFHToGG_M-125_13TeV_powheg_pythia8_Hadded.root","VBFHToGG_M_125_13TeV_powheg_pythia8"));
    MCTreesMap.insert(make_pair("TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8_Hadded.root","TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Hadded.root","TTGJets_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8"));
    MCTreesMap.insert(make_pair("THQ_ctcvcp_HToGG_M125_13TeV-madgraph-pythia8_TuneCP5_Hadded.root","THQ_ctcvcp_HToGG_M125_13TeV_madgraph_pythia8_TuneCP5"));
    MCTreesMap.insert(make_pair("TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root","TTJets_HT_2500toInf_TuneCP5_13TeV_madgraphMLM_pythia8"));
    MCTreesMap.insert(make_pair("TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root","TTJets_HT_600to800_TuneCP5_13TeV_madgraphMLM_pythia8"));
    MCTreesMap.insert(make_pair("TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root","TTJets_HT_800to1200_TuneCP5_13TeV_madgraphMLM_pythia8"));
    MCTreesMap.insert(make_pair("TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root","TTJets_HT_1200to2500_TuneCP5_13TeV_madgraphMLM_pythia8"));
    MCTreesMap.insert(make_pair("TTToHadronic_TuneCP5_13TeV-powheg-pythia8_Hadded.root","TTToHadronic_TuneCP5_13TeV_powheg_pythia8"));
    MCTreesMap.insert(make_pair("W1JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W1JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W1JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W1JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W1JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W1JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W1JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W1JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W1JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W1JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W1JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W1JetsToLNu_LHEWpT_100_150_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W2JetsToLNu_LHEWpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W2JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root","W3JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8"));
    MCTreesMap.insert(make_pair("W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Hadded.root","W4JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8"));
    MCTreesMap.insert(make_pair("W2JetsToLNu_LHEWpT_0-50_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W2JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W2JetsToLNu_LHEWpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W2JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W2JetsToLNu_LHEWpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W2JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W2JetsToLNu_LHEWpT_100-150_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W2JetsToLNu_LHEWpT_100_150_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("W2JetsToLNu_LHEWpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8_Hadded.root","W2JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8"));
    MCTreesMap.insert(make_pair("WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root","WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8"));
    MCTreesMap.insert(make_pair("WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_Hadded.root","WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8"));
    MCTreesMap.insert(make_pair("ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_Hadded.root","ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8"));
    MCTreesMap.insert(make_pair("WGJJToLNuGJJ_EWK_aQGC-FS-FM_TuneCP5_13TeV-madgraph-pythia8.root","WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8"));
    MCTreesMap.insert(make_pair("ggF_SM_WWgg_qqlnugg_Hadded.root","ggF_SM_WWgg_qqlnugg"));
    MCTreesMap.insert(make_pair("ggF_SM_WWgg_qqlnugg_Hadded_WithTaus.root","GluGluToHHTo_WWgg_qqlnu_nodeSM"));
   
    return MCTreesMap[fileName];
}
