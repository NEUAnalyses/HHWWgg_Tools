########################################################################################################################
# Abe Tishelman-Charny
# 17 April 2020
#
# Definitions to be used by Make_Fragments.py
########################################################################################################################

# Check arguments for inconsistencies 
def ArgChecks(args):
    if(not args.NMSSM and not args.EFT):
        print"[Make_Fragments - ERROR]: Need to create either NMSSM or EFT fragments"
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1)     

    if(args.NMSSM and args.EFT):
        print"[Make_Fragments - ERROR]: Need to create either NMSSM or EFT fragments, not both"
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1)   

    if(args.NMSSM and args.gridpacks == ""):
        print"[Make_Fragments - ERROR]: If you want to produce NMSSM fragments, you need to provide a comma separated list of gridpacks"
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1)         

    if(args.NMSSM and args.massPairs==""):
        print"[Make_Fragments - ERROR]: If you want to produce NMSSM fragments, you need to provide a comma separated list of mass points"
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1) 

    if(args.NMSSM) and len(args.massPairs.split(','))%2 != 0:
        print"[Make_Fragments - ERROR]: If you want to produce NMSSM fragments, your mass points must be a multiple of 2 as they are used as pairs"
        print"[Make_Fragments - ERROR]: length of mass pairs:",len(args.massPairs.split(','))
        print"[Make_Fragments - ERROR]: length of mass pairs mod 2:",len(args.massPairs.split(','))%2
        print"[Make_Fragments - ERROR]: Exiting"
        exit(1)         

# Get NMSSM mass pairs from single string of masses 
def GetMassPairs(massPairs,massPairsString):
    onFirst, onSecond = 0, 0
    massPair = []
    for im,mass in enumerate(massPairsString.split(',')):
        if(im == 0 or im%2==0): 
            onFirst, onSecond = 1, 0
        else: 
            onFirst, onSecond = 0, 1
        if(onFirst): 
            massPair = []
            massPair.append(mass)
        if(onSecond): 
            massPair.append(mass)
            massPairs.append(massPair) 
    print'NMSSM massPairs:',massPairs            
    return massPairs 
