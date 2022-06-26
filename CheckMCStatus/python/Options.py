import argparse 

def GetOptions():
    parser = argparse.ArgumentParser()

    ##-- Misc
    parser.add_argument('--outLoc', type=str, default="", help="Output location for plots", required=False)
    parser.add_argument('--PhysicsType', type=str, default="Non-Resonant", help="Physics type to get processes. Ex: 'Non-Resonant'", required=False)
    parser.add_argument('--oneDataset', action="store_true", default=False, help="Only run on one dataset for brevity and testing", required=False)

    args = parser.parse_args()
    return args