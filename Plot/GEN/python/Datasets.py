##############################################################
# Abe Tishelman-Charny                                       #
# 25 July 2020                                               #
#                                                            #
# The purpose of this module is to define datasets.          #
#                                                            #
#####:wq
#########################################################

def GetDatasets(DatasetBatch):

    productionLocation = "/eos/cms/store/group/phys_higgs/resonant_HH/RunII/MicroAOD/HHWWggSignal"
    MasterDatasetDict = {
        "Resonant": {
            "X250":"%s/ggF_X250_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_140109/0000/"%(productionLocation),
            "X260":"%s/ggF_X260_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200009/0000/"%(productionLocation),
            "X270":"%s/ggF_X270_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200029/0000/"%(productionLocation),
            "X280":"%s/ggF_X280_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200047/0000/"%(productionLocation),
            "X300":"%s/ggF_X300_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200105/0000/"%(productionLocation),
            "X320":"%s/ggF_X320_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200124/0000/"%(productionLocation),
            "X350":"%s/ggF_X350_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200141/0000/"%(productionLocation),
            "X400":"%s/ggF_X400_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200200/0000/"%(productionLocation),
            "X450":"%s/ggF_X450_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200218/0000/"%(productionLocation),
            "X500":"%s/ggF_X500_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200235/0000/"%(productionLocation),        
            "X550":"%s/ggF_X550_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200252/0000/"%(productionLocation),
            "X600":"%s/ggF_X600_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200310/0000/"%(productionLocation),
            "X650":"%s/ggF_X650_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200329/0000/"%(productionLocation),
            "X700":"%s/ggF_X700_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200347/0000/"%(productionLocation),
            "X750":"%s/ggF_X750_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200406/0000/"%(productionLocation),
            "X800":"%s/ggF_X800_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200425/0000/"%(productionLocation),
            "X850":"%s/ggF_X850_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200442/0000/"%(productionLocation),
            "X900":"%s/ggF_X900_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200500/0000/"%(productionLocation),
            "X1000":"%s/ggF_X1000_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200519/0000/"%(productionLocation)
        },

        "ZZgg-Check":{
	     "ZZgg" : "%s/Phase_II/ZZgg/"%(productionLocation)
        },

        "Resonant-Short": {
            "X250":"%s/ggF_X250_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_140109/0000/"%(productionLocation),
            "X850":"%s/ggF_X850_HHWWgg_qqlnu/HHWWgg_v2-7_100000events_GEN-SIM/200616_200442/0000/"%(productionLocation)
        },        

        "VBF-Resonant1":{
            "X250-2-4-2":"%s/VBFToBulkGravitonToHH_X250_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck_100000events_GEN/200731_110730/0000/"%(productionLocation),
            # "X250-2-6-0":"%s/VBFToBulkGravitonToHH-2-6-0_X250_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-0_100000events_GEN/200731_112003/0000/"%(productionLocation),
            # "X850-2-4-2":"%s/VBFToBulkGravitonToHH-2-4-2_X850_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-4-2_100000events_GEN/200731_112734/0000/"%(productionLocation),
            # "X850-2-6-0":"%s/VBFToBulkGravitonToHH-2-6-0_X850_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-0_100000events_GEN/200731_112838/0000/"%(productionLocation)
        },

        "VBF-Resonant2":{
            # "X250-2-4-2":"%s/VBFToBulkGravitonToHH_X250_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck_100000events_GEN/200731_110730/0000/"%(productionLocation),
            # "X250-2-6-0":"%s/VBFToBulkGravitonToHH-2-6-0_X250_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-0_100000events_GEN/200731_112003/0000/"%(productionLocation),
            "X850-2-4-2":"%s/VBFToBulkGravitonToHH-2-4-2_X850_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-4-2_100000events_GEN/200731_112734/0000/"%(productionLocation),
            # "X850-2-6-0":"%s/VBFToBulkGravitonToHH-2-6-0_X850_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-0_100000events_GEN/200731_112838/0000/"%(productionLocation)
        },

        "VBF-Resonant3":{
            # "X250-2-4-2":"%s/VBFToBulkGravitonToHH_X250_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck_100000events_GEN/200731_110730/0000/"%(productionLocation),
            # "X250-2-6-0":"%s/VBFToBulkGravitonToHH-2-6-0_X250_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-0_100000events_GEN/200731_112003/0000/"%(productionLocation),
            # "X850-2-4-2":"%s/VBFToBulkGravitonToHH-2-4-2_X850_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-4-2_100000events_GEN/200731_112734/0000/"%(productionLocation),
            "X850-2-6-0":"%s/VBFToBulkGravitonToHH-2-6-0_X850_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-0_100000events_GEN/200731_112838/0000/"%(productionLocation)
        }, 
        "VBF-Resonant4":{
            # "X250-2-4-2":"%s/VBFToBulkGravitonToHH_X250_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck_100000events_GEN/200731_110730/0000/"%(productionLocation),
            "X250-2-6-0":"%s/VBFToBulkGravitonToHH-2-6-0_X250_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-0_100000events_GEN/200731_112003/0000/"%(productionLocation),
            # "X850-2-4-2":"%s/VBFToBulkGravitonToHH-2-4-2_X850_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-4-2_100000events_GEN/200731_112734/0000/"%(productionLocation),
            # "X850-2-6-0":"%s/VBFToBulkGravitonToHH-2-6-0_X850_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-0_100000events_GEN/200731_112838/0000/"%(productionLocation)
        },                        

        "Non-Resonant": {
            "qqlnuSM_2016":"%s/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_GEN-SIM/200716_113925/0000/"%(productionLocation),
            "qqlnuSM_2017":"%s/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2017_100000events_GEN-SIM/200714_172049/0000/"%(productionLocation),
            "qqlnuSM_2018":"%s/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2018_100000events_GEN-SIM/200720_160816/0000/"%(productionLocation)
        },
        "Non-Resonant-2016": {
            "qqlnuSM_2016":"%s/GluGluToHHTo_WWgg_qqlnu_nodeSM/HHWWgg_SM2016_100000events_GEN-SIM/200716_113925/0000/"%(productionLocation)
        },        
        "VBF-Resonant-2-6-5_1":{
            "X250-2-6-5":"%s/VBFToBulkGravitonToHH-2-6-5_X250_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-5_100000events_GEN/200922_134239/0000/"%(productionLocation),
            # "X850-2-6-5":"%s/VBFToBulkGravitonToHH-2-6-5_X850_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-5_100000events_GEN/200922_194132/0000/"%(productionLocation)
        },
        "VBF-Resonant-2-6-5_2":{
            # "X250-2-6-5":"%s/VBFToBulkGravitonToHH-2-6-5_X250_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-5_100000events_GEN/200922_134239/0000/"%(productionLocation),
            "X850-2-6-5":"%s/VBFToBulkGravitonToHH-2-6-5_X850_HHWWgg_qqlnu/HHWWgg_VBF-MG-VersionCheck-2-6-5_100000events_GEN/200922_194132/0000/"%(productionLocation)
        },
        ##-- MadGraph 2.6.5 
        "HHWWgg-VBF-nonres-SM":{ 
            "SM-NonRes":"%s/WWgg_qqlnu_nodeSM_100000events/HHWWgg-SM-NonRes-VBF_GEN-SIM/200928_054428/0000/"%(productionLocation)
        },   

        ##-- Phase II private LHE / GEN 
        "PhaseIIHHWWgg-GF-nonres-SM":{ 
            "SM-NonRes":"%s/Phase_II/Private_LHEGEN/"%(productionLocation)
        }           

    }

    if DatasetBatch not in MasterDatasetDict:
        print "Can't find DatasetBatch: %s"%(DatasetBatch)
        print "Exiting"
        exit(1)  

    else: Datasets = MasterDatasetDict[DatasetBatch]    

    return Datasets 
