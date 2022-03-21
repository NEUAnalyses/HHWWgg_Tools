# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           train-DNN.py
#  Author: Joshuha Thomas-Wilsker
#  Institute of High Energy Physics
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Code to train deep neural network
# for HH->WWyy analysis.
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import pickle
#import shap
from array import array
import time
import pandas
import pandas as pd
import optparse, json, argparse, math
import ROOT
from ROOT import TTree
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler
#from sklearn.utils import class_weight
from sklearn.metrics import log_loss
from sklearn.metrics import roc_curve
import os
from os import environ
os.environ['KERAS_BACKEND'] = 'tensorflow'
import keras
from keras import backend as K
from keras.utils import np_utils
from keras.utils import plot_model
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.optimizers import Adam
from keras.optimizers import Adamax
from keras.optimizers import Nadam
from keras.optimizers import Adadelta
from keras.optimizers import Adagrad
from keras.layers import Dropout
from keras.layers import BatchNormalization
from keras.models import load_model
from keras import regularizers
from keras.wrappers.scikit_learn import KerasClassifier
from keras.callbacks import EarlyStopping
from plotting.plotter import plotter
from numpy.testing import assert_allclose
from keras.callbacks import ModelCheckpoint
from root_numpy import root2array, tree2array

seed = 7
np.random.seed(7)
rng = np.random.RandomState(31337)

def load_data_from_EOS(self, directory, mask='', prepend='root://eosuser.cern.ch'):
    eos_dir = '/eos/user/%s ' % (directory)
    eos_cmd = 'eos ' + prepend + ' ls ' + eos_dir
    print(eos_cmd)
    #out = commands.getoutput(eos_cmd)
    return

def load_data(inputPath,variables,criteria):
    # Load dataset to .csv format file
    my_cols_list=variables
    data = pd.DataFrame(columns=my_cols_list)
    keys=['HH','bckg']
    data = pd.DataFrame(columns=my_cols_list)
    for key in keys :
        print('key: ', key)
        if 'HH' in key:
            sampleNames=key
            subdir_name = '/eos/cms/store/group/phys_higgs/cmshgg/atishelm/flashgg/HIG-21-014/January_2021_Production/2017/Signal/SL_allNLO_Reweighted'
            fileNames = [
            '1_even/GluGluToHHTo2G2Qlnu_node_1_2017_even',
            '2_even/GluGluToHHTo2G2Qlnu_node_2_2017_even',
            '3_even/GluGluToHHTo2G2Qlnu_node_3_2017_even',
            '4_even/GluGluToHHTo2G2Qlnu_node_4_2017_even',
            '5_even/GluGluToHHTo2G2Qlnu_node_5_2017_even',
            '6_even/GluGluToHHTo2G2Qlnu_node_6_2017_even',
            '7_even/GluGluToHHTo2G2Qlnu_node_7_2017_even',
            '8_even/GluGluToHHTo2G2Qlnu_node_8_2017_even',
            '9_even/GluGluToHHTo2G2Qlnu_node_9_2017_even',
            '10_even/GluGluToHHTo2G2Qlnu_node_10_2017_even',
            '11_even/GluGluToHHTo2G2Qlnu_node_11_2017_even',
            '12_even/GluGluToHHTo2G2Qlnu_node_12_2017_even',
            '13_even/GluGluToHHTo2G2Qlnu_node_13_2017_even',
            '14_even/GluGluToHHTo2G2Qlnu_node_14_2017_even',
            '15_even/GluGluToHHTo2G2Qlnu_node_15_2017_even',
            '16_even/GluGluToHHTo2G2Qlnu_node_16_2017_even',
            '17_even/GluGluToHHTo2G2Qlnu_node_17_2017_even',
            '18_even/GluGluToHHTo2G2Qlnu_node_18_2017_even',
            '19_even/GluGluToHHTo2G2Qlnu_node_19_2017_even',
            '20_even/GluGluToHHTo2G2Qlnu_node_20_2017_even'
            ]
            target=1
        else:
            sampleNames = key
            subdir_name = '/eos/user/b/bmarzocc/HHWWgg/January_2021_Production/2017/Backgrounds'
            fileNames = [
            #'DiPhotonJetsBox_M40_80_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'DiPhotonJetsBox_MGG-80toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'GJet_Pt-20to40_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
            #'GJet_Pt-20toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'GJet_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'QCD_Pt-30to40_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'QCD_Pt-30toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
   	    #'QCD_Pt-40toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'DYJetsToLL_M-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'TTGG_0Jets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'TTGJets_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
   	    #'TTJets_HT-600to800_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'TTJets_HT-800to1200_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'TTJets_HT-1200to2500_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'TTJets_HT-2500toInf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'ttWJets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'TTJets_TuneCP5_extra_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'W1JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'W1JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'W1JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'W1JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'W1JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'W2JetsToLNu_LHEWpT_0-50_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',	
	    #'W2JetsToLNu_LHEWpT_50-150_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'W2JetsToLNu_LHEWpT_150-250_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'W2JetsToLNu_LHEWpT_250-400_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'W2JetsToLNu_LHEWpT_400-inf_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'W3JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'W4JetsToLNu_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'WGGJets_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    'WGJJToLNu_EWK_QCD_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'WWTo1L1Nu2Q_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
	    #'WW_TuneCP5_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
            #'GluGluHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
            #'VBFHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar',
            #'VHToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar', 
            #'ttHJetToGG_2017_HHWWggTag_0_MoreVars_kinWeight_noHgg_v2_NodeVar' 
            ]
            target=0

        for filen in fileNames:
            if 'GluGluToHHTo2G2Qlnu_node_1_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_1_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_2_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_2_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_3_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_3_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_4_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_4_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH'   
            elif 'GluGluToHHTo2G2Qlnu_node_5_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_5_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH'              
            elif 'GluGluToHHTo2G2Qlnu_node_6_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_6_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_7_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_7_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_8_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_8_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH'             
            elif 'GluGluToHHTo2G2Qlnu_node_9_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_9_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_10_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_10_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_11_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_11_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH'  
            elif 'GluGluToHHTo2G2Qlnu_node_12_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_12_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_13_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_13_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_14_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_14_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH'  
            elif 'GluGluToHHTo2G2Qlnu_node_15_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_15_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_16_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_16_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_17_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_17_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH'  
            elif 'GluGluToHHTo2G2Qlnu_node_18_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_18_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_19_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_19_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_20_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_20_2017_13TeV_HHWWggTag_0']
                process_ID = 'HH' 
            elif 'GluGluToHHTo2G2Qlnu_node_SM_2017' in filen:
                treename=['GluGluToHHTo2G2Qlnu_node_SM_13TeV_HHWWggTag_0_v1']
                process_ID = 'HH'     
            elif 'GluGluHToGG' in filen:
                treename=['ggh_125_13TeV_HHWWggTag_0_v1']
                process_ID = 'Hgg'
            elif 'VBFHToGG' in filen:
                treename=['vbf_125_13TeV_HHWWggTag_0_v1']
                process_ID = 'Hgg'
            elif 'VHToGG' in filen:
                treename=['wzh_125_13TeV_HHWWggTag_0_v1']
                process_ID = 'Hgg'  
            elif 'ttHJetToGG' in filen:
                treename=['tth_125_13TeV_HHWWggTag_0_v1']
                process_ID = 'Hgg'
            elif 'DiPhotonJetsBox_M40_80' in filen:
                treename=['DiPhotonJetsBox_M40_80_Sherpa_13TeV_HHWWggTag_0',
                ]
                process_ID = 'DiPhoton'
            elif 'DiPhotonJetsBox_MGG-80toInf' in filen:
                treename=['DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_HHWWggTag_0',
                ]
                process_ID = 'DiPhoton'
            elif 'GJet_Pt-20to40' in filen:
                treename=['GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'GJet'
            elif 'GJet_Pt-20toInf' in filen:
                treename=['GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'GJet'
            elif 'GJet_Pt-40toInf' in filen:
                treename=['GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'GJet'
            elif 'QCD_Pt-30to40' in filen:
                treename=['QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'QCD'
            elif 'QCD_Pt-30toInf' in filen:
                treename=['QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCP5_13TeV_Pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'QCD'
            elif 'QCD_Pt-40toInf' in filen:
                treename=['QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'DY'
            elif 'DYJetsToLL_M-50' in filen:
                treename=['DYJetsToLL_M_50_TuneCP5_13TeV_amcatnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'TTGsJets'
            elif 'TTGG_0Jets' in filen:
                treename=['TTGG_0Jets_TuneCP5_13TeV_amcatnlo_madspin_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'TTGsJets'
            elif 'TTGJets_TuneCP5' in filen:
                treename=['TTGJets_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'TTGsJets'
            elif 'TTJets_HT-600to800' in filen:
                treename=['TTJets_HT_600to800_TuneCP5_13TeV_madgraphMLM_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'TTGsJets'
            elif 'TTJets_HT-800to1200' in filen:
                treename=['TTJets_HT_800to1200_TuneCP5_13TeV_madgraphMLM_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'TTGsJets'
            elif 'TTJets_HT-1200to2500' in filen:
                treename=['TTJets_HT_1200to2500_TuneCP5_13TeV_madgraphMLM_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'TTGsJets'
            elif 'TTJets_HT-2500toInf' in filen:
                treename=['TTJets_HT_2500toInf_TuneCP5_13TeV_madgraphMLM_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'TTGsJets'
            elif 'ttWJets' in filen:
                treename=['ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'TTGsJets'
            elif 'TTJets_TuneCP5_extra' in filen:
                treename=['TTJets_TuneCP5_13TeV_amcatnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W1JetsToLNu_LHEWpT_0-50' in filen:
                treename=['W1JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W1JetsToLNu_LHEWpT_50-150' in filen:
                treename=['W1JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W1JetsToLNu_LHEWpT_150-250' in filen:
                treename=['W1JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W1JetsToLNu_LHEWpT_250-400' in filen:
                treename=['W1JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W1JetsToLNu_LHEWpT_400-inf' in filen:
                treename=['W1JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W2JetsToLNu_LHEWpT_0-50' in filen:
                treename=['W2JetsToLNu_LHEWpT_0_50_TuneCP5_13TeV_amcnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W2JetsToLNu_LHEWpT_50-150' in filen:
                treename=['W2JetsToLNu_LHEWpT_50_150_TuneCP5_13TeV_amcnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W2JetsToLNu_LHEWpT_150-250' in filen:
                treename=['W2JetsToLNu_LHEWpT_150_250_TuneCP5_13TeV_amcnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W2JetsToLNu_LHEWpT_250-400' in filen:
                treename=['W2JetsToLNu_LHEWpT_250_400_TuneCP5_13TeV_amcnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W2JetsToLNu_LHEWpT_400-inf' in filen:
                treename=['W2JetsToLNu_LHEWpT_400_inf_TuneCP5_13TeV_amcnloFXFX_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W3JetsToLNu' in filen:
                treename=['W3JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'W4JetsToLNu' in filen:
                treename=['W4JetsToLNu_TuneCP5_13TeV_madgraphMLM_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'WGGJets' in filen:
                treename=['WGGJets_TuneCP5_13TeV_madgraphMLM_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'WGJJToLNuGJJ_EWK' in filen:
                treename=['WGJJToLNuGJJ_EWK_aQGC_FS_FM_TuneCP5_13TeV_madgraph_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets'
            elif 'WGJJToLNu_EWK_QCD' in filen:
                treename=['WGJJToLNu_EWK_QCD_TuneCP5_13TeV_madgraph_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WGsJets' 
            elif 'WWTo1L1Nu2Q' in filen:
                treename=['WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WW'
            elif 'WW_TuneCP5' in filen:
                treename=['WW_TuneCP5_13TeV_pythia8_13TeV_HHWWggTag_0',
                ]
                process_ID = 'WW'

            fileName = os.path.join(subdir_name,filen)
            #filename_fullpath = inputPath+"/"+fileName+".root"
            filename_fullpath = fileName+".root" 
            print("Input file: ", filename_fullpath)
            tfile = ROOT.TFile(filename_fullpath)
            for tname in treename:
                ch_0 = tfile.Get(tname)
                if ch_0 is not None :
                    criteria_tmp = criteria 
                    #if target == 0: criteria_tmp = criteria + " && ( fabs(weight * kinWeight) < 10. )"
                    # Create dataframe for ttree
                    chunk_arr = tree2array(tree=ch_0, branches=my_cols_list[:-5], selection=criteria_tmp)
                    #print "chunk_arr:",chunk_arr
                    #chunk_arr = tree2array(tree=ch_0, branches=my_cols_list[:-5], selection=criteria, start=0, stop=500)
                    # This dataframe will be a chunk of the final total dataframe used in training
                    chunk_df = pd.DataFrame(chunk_arr, columns=my_cols_list)
                    # Add values for the process defined columns.
                    # (i.e. the values that do not change for a given process).
                    chunk_df['key']=key
                    chunk_df['target']=target
                    chunk_df['weight']=chunk_df['weight']
                    #chunk_df['kinWeight']=chunk_df['kinWeight']
                    #chunk_df['weight_NLO_node']=chunk_df['weight_NLO_node']
                    chunk_df['process_ID']=process_ID
                    chunk_df['classweight']=1.0
                    chunk_df['unweighted'] = 1.0
                    #print "chunk_df:",chunk_df['weight'],chunk_df["weight_NLO_node"]
                    # Append this chunk to the 'total' dataframe
                    data = data.append(chunk_df, ignore_index=True)
                else:
                    print("TTree == None")
                ch_0.Delete()
            tfile.Close()
        if len(data) == 0 : continue

    return data

def load_trained_model(model_path):
    print('<load_trained_model> weights_path: ', model_path)
    model = load_model(model_path, compile=False)
    return model

def baseline_model(num_variables,learn_rate=0.001):
    model = Sequential()
    model.add(Dense(64,input_dim=num_variables,kernel_initializer='glorot_normal',activation='relu'))
    #model.add(Dense(64,activation='relu'))
    model.add(Dense(32,activation='relu'))
    model.add(Dense(16,activation='relu'))
    model.add(Dense(8,activation='relu'))
    model.add(Dense(4,activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    #model.compile(loss='binary_crossentropy',optimizer=Nadam(lr=learn_rate),metrics=['acc'])
    optimizer=Nadam(lr=learn_rate)
    model.compile(loss='binary_crossentropy',optimizer=optimizer,metrics=['acc'])
    return model

def gscv_model(learn_rate=0.001):
    model = Sequential()
    model.add(Dense(32,input_dim=29,kernel_initializer='glorot_normal',activation='relu'))
    model.add(Dense(16,activation='relu'))
    model.add(Dense(8,activation='relu'))
    model.add(Dense(4,activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    #model.compile(loss='binary_crossentropy',optimizer=Nadam(lr=learn_rate),metrics=['acc'])
    optimizer=Nadam(lr=learn_rate)
    model.compile(loss='binary_crossentropy',optimizer=optimizer,metrics=['acc'])
    return model

def new_model(num_variables,learn_rate=0.001):
    model = Sequential()
    model.add(Dense(64, input_dim=num_variables,kernel_regularizer=regularizers.l2(0.01)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dense(32,kernel_regularizer=regularizers.l2(0.01)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dense(16,kernel_regularizer=regularizers.l2(0.01)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dense(8,kernel_regularizer=regularizers.l2(0.01)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dense(4,kernel_regularizer=regularizers.l2(0.01)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dense(1, activation="sigmoid")) 
    optimizer=Nadam(lr=learn_rate)
    model.compile(loss='binary_crossentropy',optimizer=optimizer,metrics=['acc'])
    return model

def check_dir(dir):
    if not os.path.exists(dir):
        print('mkdir: ', dir)
        os.makedirs(dir)

def main():
    print('Using Keras version: ', keras.__version__)

    usage = 'usage: %prog [options]'
    parser = argparse.ArgumentParser(usage)
    parser.add_argument('-t', '--train_model', dest='train_model', help='Option to train model or simply make diagnostic plots (0=False, 1=True)', default=1, type=int)
    parser.add_argument('-s', '--suff', dest='suffix', help='Option to choose suffix for training', default='', type=str)
    parser.add_argument('-p', '--para', dest='hyp_param_scan', help='Option to run hyper-parameter scan', default=0, type=int)
    parser.add_argument('-i', '--inputs_file_path', dest='inputs_file_path', help='Path to directory containing directories \'Bkgs\' and \'Signal\' which contain background and signal ntuples respectively.', default='', type=str)
    args = parser.parse_args()
    do_model_fit = args.train_model
    suffix = args.suffix

    # Create instance of the input files directory
    #inputs_file_path = 'HHWWgg_DataSignalMCnTuples/2017/'
    inputs_file_path = ''

    hyp_param_scan=args.hyp_param_scan
    # Set model hyper-parameters
    weights='BalanceYields'# 'BalanceYields' or 'BalanceNonWeighted'
    optimizer = 'Nadam'
    validation_split=0.25
    # hyper-parameter scan results
    if weights == 'BalanceNonWeighted':
        learn_rate = 0.0005
        epochs = 200
        batch_size=200
    if weights == 'BalanceYields':
        learn_rate = 0.0001
        epochs = 600
        batch_size=500
        #epochs = 10
        #batch_size=200

    # Create instance of output directory where all results are saved.
    output_directory = 'HHWWyyDNN_binary_%s_%s/' % (suffix,weights)
    check_dir(output_directory)
    hyperparam_file = os.path.join(output_directory,'additional_model_hyper_params.txt')
    additional_hyperparams = open(hyperparam_file,'w')
    additional_hyperparams.write("optimizer: "+optimizer+"\n")
    additional_hyperparams.write("learn_rate: "+str(learn_rate)+"\n")
    additional_hyperparams.write("epochs: "+str(epochs)+"\n")
    additional_hyperparams.write("validation_split: "+str(validation_split)+"\n")
    additional_hyperparams.write("weights: "+weights+"\n")
    # Create plots subdirectory
    plots_dir = os.path.join(output_directory,'plots/')
    input_var_jsonFile = open('input_variables.json','r')
    #selection_criteria = '( 1.>0. )'
    selection_criteria = '( ( fabs(weight) < 10 ) )'

    # Load Variables from .json
    variable_list = json.load(input_var_jsonFile,encoding="utf-8").items()

    # Create list of headers for dataset .csv
    column_headers = []
    for key,var in variable_list:
        column_headers.append(key)
    column_headers.append('weight')
    #column_headers.append('kinWeight')
    #column_headers.append('weight_NLO_node')
    column_headers.append('unweighted')
    column_headers.append('target')
    column_headers.append('key')
    column_headers.append('classweight')
    column_headers.append('process_ID')

    # Load ttree into .csv including all variables listed in column_headers
    print('<train-DNN> Input file path: ', inputs_file_path)
    outputdataframe_name = '%s/output_dataframe.csv' %(output_directory)
    if os.path.isfile(outputdataframe_name):
        data = pandas.read_csv(outputdataframe_name)
        print('<train-DNN> Loading data .csv from: %s . . . . ' % (outputdataframe_name))
    else:
        print('<train-DNN> Creating new data .csv @: %s . . . . ' % (inputs_file_path))
        data = load_data(inputs_file_path,column_headers,selection_criteria)
        # Change sentinal value to speed up training.
        data = data.mask(data<-25., -9.)
        data = data.mask(data==np.inf, -9.)
        data = data.mask(data==-np.inf, -9.)
        data = data.mask(data==np.nan, -9.)
        data_inf = data.isin([np.inf, -np.inf]) 
        data_nan = data.isin([np.nan]) 
        count_inf = np.isinf(data_inf).values.sum() 
        count_nan = np.isinf(data_nan).values.sum() 
        if count_inf>0: print "WARNING ---> It contained " + str(count_inf) + " infinite values"  
        if count_nan>0: print "WARNING ---> It contained " + str(count_nan) + " NaN values"   
        data.to_csv(outputdataframe_name, index=False)
        data = pandas.read_csv(outputdataframe_name)

    print('<main> data columns: ', (data.columns.values.tolist()))
    n = len(data)
    nHH = len(data.iloc[data.target.values == 1])
    nbckg = len(data.iloc[data.target.values == 0])
    print("Total (train+validation) length of HH = %i, bckg = %i" % (nHH, nbckg))

    # Make instance of plotter tool
    Plotter = plotter()
    # Create statistically independant training/testing data
    traindataset, valdataset = train_test_split(data, test_size=0.25)
    valdataset.to_csv((output_directory+'valid_dataset.csv'), index=False)

    print('<train-DNN> Training dataset shape: ', traindataset.shape)
    print('<train-DNN> Validation dataset shape: ', valdataset.shape)


    # Event weights
    weights_for_HH = traindataset.loc[traindataset['process_ID']=='HH', 'weight']
    #weights_for_HH_NLO = traindataset.loc[traindataset['process_ID']=='HH', 'weight_NLO_node']
    weights_for_Hgg = traindataset.loc[traindataset['process_ID']=='Hgg', 'weight']
    weights_for_DiPhoton = traindataset.loc[traindataset['process_ID']=='DiPhoton', 'weight']
    weights_for_GJet = traindataset.loc[traindataset['process_ID']=='GJet', 'weight']
    weights_for_QCD = traindataset.loc[traindataset['process_ID']=='QCD', 'weight']
    weights_for_DY = traindataset.loc[traindataset['process_ID']=='DY', 'weight']
    weights_for_TTGsJets = traindataset.loc[traindataset['process_ID']=='TTGsJets', 'weight']
    weights_for_WGsJets = traindataset.loc[traindataset['process_ID']=='WGsJets', 'weight']
    weights_for_WW = traindataset.loc[traindataset['process_ID']=='WW', 'weight']
   
    HHsum_weighted= sum(weights_for_HH)
    Hggsum_weighted= sum(weights_for_Hgg)
    DiPhotonsum_weighted= sum(weights_for_DiPhoton) 
    GJetsum_weighted= sum(weights_for_GJet)
    QCDsum_weighted= sum(weights_for_QCD) 
    DYsum_weighted= sum(weights_for_DY)
    TTGsJetssum_weighted= sum(weights_for_TTGsJets)
    WGsJetssum_weighted= sum(weights_for_WGsJets)
    WWsum_weighted= sum(weights_for_WW) 
    bckgsum_weighted = Hggsum_weighted + DiPhotonsum_weighted + GJetsum_weighted + QCDsum_weighted + DYsum_weighted + TTGsJetssum_weighted + WGsJetssum_weighted + WWsum_weighted
 
    nevents_for_HH = traindataset.loc[traindataset['process_ID']=='HH', 'unweighted']
    nevents_for_Hgg = traindataset.loc[traindataset['process_ID']=='Hgg', 'unweighted']
    nevents_for_DiPhoton = traindataset.loc[traindataset['process_ID']=='DiPhoton', 'unweighted']
    nevents_for_GJet = traindataset.loc[traindataset['process_ID']=='GJet', 'unweighted']
    nevents_for_QCD = traindataset.loc[traindataset['process_ID']=='QCD', 'unweighted']
    nevents_for_DY = traindataset.loc[traindataset['process_ID']=='DY', 'unweighted']
    nevents_for_TTGsJets = traindataset.loc[traindataset['process_ID']=='TTGsJets', 'unweighted']
    nevents_for_WGsJets = traindataset.loc[traindataset['process_ID']=='WGsJets', 'unweighted']
    nevents_for_WW = traindataset.loc[traindataset['process_ID']=='WW', 'unweighted']
    
    HHsum_unweighted= sum(nevents_for_HH)
    Hggsum_unweighted= sum(nevents_for_Hgg)
    DiPhotonsum_unweighted= sum(nevents_for_DiPhoton)
    GJetsum_unweighted= sum(nevents_for_GJet)
    QCDsum_unweighted= sum(nevents_for_QCD)
    DYsum_unweighted= sum(nevents_for_DY) 
    TTGsJetssum_unweighted= sum(nevents_for_TTGsJets)
    WGsJetssum_unweighted= sum(nevents_for_WGsJets)
    WWsum_unweighted= sum(nevents_for_WW)
    bckgsum_unweighted = Hggsum_unweighted + DiPhotonsum_unweighted + GJetsum_unweighted + QCDsum_unweighted + DYsum_unweighted + TTGsJetssum_unweighted + WGsJetssum_unweighted + WWsum_unweighted
    
    #HHsum_weighted= HHsum_weighted*2.
    HHsum_unweighted= HHsum_unweighted*2.

    if weights=='BalanceYields':
        print('HHsum_weighted= ' , HHsum_weighted)
        print('Hggsum_weighted= ' , Hggsum_weighted)
        print('DiPhotonsum_weighted= ', DiPhotonsum_weighted)
        print('GJetsum_weighted= ', GJetsum_weighted)
        print('QCDsum_weighted= ', QCDsum_weighted)
        print('DYsum_weighted= ', DYsum_weighted)
        print('TTGsJetssum_weighted= ', TTGsJetssum_weighted)
        print('WGsJetssum_weighted= ', WGsJetssum_weighted)
        print('WWsum_weighted= ', WWsum_weighted)
        print('bckgsum_weighted= ', bckgsum_weighted)
        traindataset.loc[traindataset['process_ID']=='HH', ['classweight']] = HHsum_unweighted/HHsum_weighted
        traindataset.loc[traindataset['process_ID']=='Hgg', ['classweight']] = (HHsum_unweighted/bckgsum_weighted) 
        traindataset.loc[traindataset['process_ID']=='DiPhoton', ['classweight']] = (HHsum_unweighted/bckgsum_weighted) 
        traindataset.loc[traindataset['process_ID']=='GJet', ['classweight']] = (HHsum_unweighted/bckgsum_weighted)
        traindataset.loc[traindataset['process_ID']=='QCD', ['classweight']] = (HHsum_unweighted/bckgsum_weighted)
        traindataset.loc[traindataset['process_ID']=='DY', ['classweight']] = (HHsum_unweighted/bckgsum_weighted)
        traindataset.loc[traindataset['process_ID']=='TTGsJets', ['classweight']] = (HHsum_unweighted/bckgsum_weighted)
        traindataset.loc[traindataset['process_ID']=='WGsJets', ['classweight']] = (HHsum_unweighted/bckgsum_weighted)
        traindataset.loc[traindataset['process_ID']=='WW', ['classweight']] = (HHsum_unweighted/bckgsum_weighted)
        
    if weights=='BalanceNonWeighted':
        print('HHsum_unweighted= ' , HHsum_unweighted)
        print('Hggsum_unweighted= ' , Hggsum_unweighted)
        print('DiPhotonsum_unweighted= ', DiPhotonsum_unweighted)
        print('GJetsum_unweighted= ', GJetsum_unweighted)
        print('QCDsum_unweighted= ', QCDsum_unweighted)
        print('DYsum_unweighted= ', DYsum_unweighted)
        print('TTGsJetssum_unweighted= ', TTGsJetssum_unweighted)
        print('WGsJetssum_unweighted= ', WGsJetssum_unweighted)
        print('WWsum_unweighted= ', WWsum_unweighted)
        print('bckgsum_unweighted= ', bckgsum_unweighted)
        traindataset.loc[traindataset['process_ID']=='HH', ['classweight']] = 1.
        traindataset.loc[traindataset['process_ID']=='Hgg', ['classweight']] = (HHsum_unweighted/bckgsum_unweighted)  
        traindataset.loc[traindataset['process_ID']=='DiPhoton', ['classweight']] = (HHsum_unweighted/bckgsum_unweighted) 
        traindataset.loc[traindataset['process_ID']=='GJet', ['classweight']] = (HHsum_unweighted/bckgsum_unweighted) 
        traindataset.loc[traindataset['process_ID']=='QCD', ['classweight']] = (HHsum_unweighted/bckgsum_unweighted) 
        traindataset.loc[traindataset['process_ID']=='DY', ['classweight']] = (HHsum_unweighted/bckgsum_unweighted) 
        traindataset.loc[traindataset['process_ID']=='TTGsJets', ['classweight']] = (HHsum_unweighted/bckgsum_unweighted) 
        traindataset.loc[traindataset['process_ID']=='WGsJets', ['classweight']] = (HHsum_unweighted/bckgsum_unweighted) 
        traindataset.loc[traindataset['process_ID']=='WW', ['classweight']] = (HHsum_unweighted/bckgsum_unweighted) 
        

    # Remove column headers that aren't input variables
    training_columns = column_headers[:-6]
    print('<train-DNN> Training features: ', training_columns)

    column_order_txt = '%s/column_order.txt' %(output_directory)
    column_order_file = open(column_order_txt, "wb")
    for tc_i in training_columns:
        line = tc_i+"\n"
        pickle.dump(str(line), column_order_file)

    num_variables = len(training_columns)

    # Extract training and testing data
    X_train = traindataset[training_columns].values
    X_test = valdataset[training_columns].values

    # Extract labels data
    Y_train = traindataset['target'].values
    Y_test = valdataset['target'].values

    # Create dataframe containing input features only (for correlation matrix)
    train_df = data.iloc[:traindataset.shape[0]]

    # Event weights if wanted
    #train_weights = traindataset['weight'].values*traindataset['weight_NLO_node'].values
    #test_weights = valdataset['weight'].values*valdataset['weight_NLO_node'].values
    #train_weights = abs(traindataset['weight'].values)*abs(traindataset['weight_NLO_node'].values)
    #test_weights = abs(valdataset['weight'].values)*abs(valdataset['weight_NLO_node'].values)
    #train_weights = abs(traindataset['weight'].values)*abs(traindataset['kinWeight'].values)*abs(traindataset['weight_NLO_node'].values)
    #test_weights = abs(valdataset['weight'].values)*abs(valdataset['kinWeight'].values)*abs(valdataset['weight_NLO_node'].values)
    train_weights = abs(traindataset['weight'].values)
    test_weights = abs(valdataset['weight'].values)
   
    # Weights applied during training.
    if weights=='BalanceYields':
        #trainingweights = traindataset.loc[:,'classweight']*traindataset.loc[:,'weight']*traindataset.loc[:,'weight_NLO_node']
        #trainingweights = traindataset.loc[:,'classweight'].abs()*traindataset.loc[:,'weight'].abs()*traindataset.loc[:,'weight_NLO_node'].abs()
        #trainingweights = traindataset.loc[:,'classweight'].abs() * traindataset.loc[:,'weight'].abs() * traindataset.loc[:,'kinWeight'].abs() * traindataset.loc[:,'weight_NLO_node'].abs()  
        trainingweights = traindataset.loc[:,'classweight'].abs() * traindataset.loc[:,'weight'].abs()  
    if weights=='BalanceNonWeighted':
        trainingweights = traindataset.loc[:,'classweight']
    trainingweights = np.array(trainingweights)

    ## Input Variable Correlation plot
    correlation_plot_file_name = 'correlation_plot'
    Plotter.correlation_matrix(train_df)
    Plotter.save_plots(dir=plots_dir, filename=correlation_plot_file_name+'.png')
    Plotter.save_plots(dir=plots_dir, filename=correlation_plot_file_name+'.pdf')

    # Fit label encoder to Y_train
    newencoder = LabelEncoder()
    newencoder.fit(Y_train)
    # Transform to encoded array
    encoded_Y = newencoder.transform(Y_train)
    encoded_Y_test = newencoder.transform(Y_test)

    if do_model_fit == 1:
        print('<train-BinaryDNN> Training new model . . . . ')
        histories = []
        labels = []

        if hyp_param_scan == 1:
            print('Begin at local time: ', time.localtime())
            hyp_param_scan_name = 'hyp_param_scan_results.txt'
            hyp_param_scan_results = open(hyp_param_scan_name,'a')
            time_str = str(time.localtime())+'\n'
            hyp_param_scan_results.write(time_str)
            hyp_param_scan_results.write(weights)
            learn_rates=[0.00001, 0.0001]
            epochs = [150,200]
            batch_size = [400,500]
            param_grid = dict(learn_rate=learn_rates,epochs=epochs,batch_size=batch_size)
            model = KerasClassifier(build_fn=gscv_model,verbose=0)
            grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)
            grid_result = grid.fit(X_train,Y_train,shuffle=True,sample_weight=trainingweights)
            print("Best score: %f , best params: %s" % (grid_result.best_score_,grid_result.best_params_))
            hyp_param_scan_results.write("Best score: %f , best params: %s\n" %(grid_result.best_score_,grid_result.best_params_))
            means = grid_result.cv_results_['mean_test_score']
            stds = grid_result.cv_results_['std_test_score']
            params = grid_result.cv_results_['params']
            for mean, stdev, param in zip(means, stds, params):
                print("Mean (stdev) test score: %f (%f) with parameters: %r" % (mean,stdev,param))
                hyp_param_scan_results.write("Mean (stdev) test score: %f (%f) with parameters: %r\n" % (mean,stdev,param))
            exit()
        else:
            # Define model for analysis
            early_stopping_monitor = EarlyStopping(patience=100, monitor='val_loss', min_delta=0.0001, verbose=1)
            #model = baseline_model(num_variables, learn_rate=learn_rate)
            model = new_model(num_variables, learn_rate=learn_rate)

            # Fit the model
            # Batch size = examples before updating weights (larger = faster training)
            # Epoch = One pass over data (useful for periodic logging and evaluation)
            #class_weights = np.array(class_weight.compute_class_weight('balanced',np.unique(Y_train),Y_train))
            history = model.fit(X_train,Y_train,validation_split=validation_split,epochs=epochs,batch_size=batch_size,verbose=1,shuffle=True,sample_weight=trainingweights,callbacks=[early_stopping_monitor])
            histories.append(history)
            labels.append(optimizer)
            # Make plot of loss function evolution
            #Plotter.plot_training_progress_acc(histories, labels)
            #acc_progress_filename = 'DNN_acc_wrt_epoch'
            #Plotter.save_plots(dir=plots_dir, filename=acc_progress_filename+'.png')
            #Plotter.save_plots(dir=plots_dir, filename=acc_progress_filename+'.pdf') 

            Plotter.history_plot(history, label='loss')
            Plotter.save_plots(dir=plots_dir, filename='history_loss.png')
            Plotter.save_plots(dir=plots_dir, filename='history_loss.pdf')   

            Plotter.history_plot(history, label='acc')
            Plotter.save_plots(dir=plots_dir, filename='history_accuracy.png')
            Plotter.save_plots(dir=plots_dir, filename='history_accuracy.pdf')   
    else:
        model_name = os.path.join(output_directory,'model.h5')
        model = load_trained_model(model_name)

    # Node probabilities for training sample events
    result_probs = model.predict(np.array(X_train))
    result_classes = model.predict_classes(np.array(X_train))

    # Node probabilities for testing sample events
    result_probs_test = model.predict(np.array(X_test))
    result_classes_test = model.predict_classes(np.array(X_test))

    # Store model in file
    model_output_name = os.path.join(output_directory,'model.h5')
    model.save(model_output_name)
    weights_output_name = os.path.join(output_directory,'model_weights.h5')
    model.save_weights(weights_output_name)
    model_json = model.to_json()
    model_json_name = os.path.join(output_directory,'model_serialised.json')
    with open(model_json_name,'w') as json_file:
        json_file.write(model_json)
    model.summary()
    model_schematic_name = os.path.join(output_directory,'model_schematic.png')
    #plot_model(model, to_file=model_schematic_name, show_shapes=True, show_layer_names=True)

    print('================')
    print('Training event labels: ', len(Y_train))
    print('Training event probs', len(result_probs))
    print('Training event weights: ', len(train_weights))
    print('Testing events: ', len(Y_test))
    print('Testing event probs', len(result_probs_test))
    print('Testing event weights: ', len(test_weights))
    print('================')

    # Initialise output directory.
    Plotter.plots_directory = plots_dir
    Plotter.output_directory = output_directory

    Plotter.ROC(model, X_test, Y_test, X_train, Y_train)
    Plotter.save_plots(dir=plots_dir, filename='ROC.png')
    Plotter.save_plots(dir=plots_dir, filename='ROC.pdf')

main()
