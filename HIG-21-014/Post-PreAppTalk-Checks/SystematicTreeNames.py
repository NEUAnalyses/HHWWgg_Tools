"""
11 November 2021
Abraham Tishelman-Charny 

The purpose of this python module is to define the systematic labels used for HIG-21-014 as defined originally in flashgg.
"""

def GetSystLabels(year):

    systLabels = []

    # Different names per year 
    listOfSources_2016 = [
                            "Absolute",
                            "Absolute2016",
                            "BBEC1",
                            "BBEC12016",
                            "EC2",
                            "EC22016",
                            "FlavorQCD",
                            "HF",
                            "HF2016",
                            "RelativeBal",
                            "RelativeSample2016"
                            ]

    listOfSources_2017 = [
                    "Absolute",
                    "Absolute2017",
                    "BBEC1",
                    "BBEC12017",
                    "EC2",
                    "EC22017",
                    "FlavorQCD",
                    "HF",
                    "HF2017",
                    "RelativeBal",
                    "RelativeSample2017"
                    ]

    listOfSources_2018 = [
                    "Absolute",
                    "Absolute2018",
                    "BBEC1",
                    "BBEC12018",
                    "EC2",
                    "EC22018",
                    "FlavorQCD",
                    "HF",
                    "HF2018",
                    "RelativeBal",
                    "RelativeSample2018"
                    ]   


    for direction in ["Up","Down"]:

        ##-- Photons 
        systLabels.append("MvaShift%s01sigma"%direction)
        systLabels.append("SigmaEOverEShift%s01sigma"%direction)
        systLabels.append("MaterialCentralBarrel%s01sigma"%direction)
        systLabels.append("MaterialOuterBarrel%s01sigma"%direction)
        systLabels.append("MaterialForward%s01sigma"%direction)
        systLabels.append("FNUFEB%s01sigma"%direction)
        systLabels.append("FNUFEE%s01sigma"%direction)
        systLabels.append("MCScaleGain6EB%s01sigma"%direction)
        systLabels.append("MCScaleGain1EB%s01sigma"%direction)

        ##-- Jets 
        systLabels.append("JEC%s01sigma" % direction)
        systLabels.append("JER%s01sigma" % direction)           
        systLabels.append("PUJIDShift%s01sigma" % direction)

        ##-- Different reduced JEC names for different years
        if(year == '2016'):
            for sourceName in listOfSources_2016:
                systLabels.append("JEC%s%s01sigma" % (str(sourceName),direction))
        elif(year == '2017'):
            for sourceName in listOfSources_2017:
                systLabels.append("JEC%s%s01sigma" % (str(sourceName),direction))  
        elif(year == '2018'):
            for sourceName in listOfSources_2018:
                systLabels.append("JEC%s%s01sigma" % (str(sourceName),direction))  

        ##-- HEM Systematic only in 2018 
        if(year == '2018'):
            systLabels.append("JetHEM%s01sigma" % (direction))

        ##-- MET 
        systLabels.append("metJecUncertainty%s01sigma" % direction)
        systLabels.append("metJerUncertainty%s01sigma" % direction)
        systLabels.append("metPhoUncertainty%s01sigma" % direction)
        systLabels.append("metUncUncertainty%s01sigma" % direction)   

        for r9 in ["HighR9","LowR9"]:
            for region in ["EB","EE"]:
                systLabels.append("ShowerShape%s%s%s01sigma"%(r9,region,direction))
                systLabels.append("MCScale%s%s%s01sigma" % (r9,region,direction))
                for var in ["Rho","Phi"]:
                    systLabels.append("MCSmear%s%s%s%s01sigma" % (r9,region,var,direction))

    return systLabels 