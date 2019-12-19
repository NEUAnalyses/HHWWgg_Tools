# Abe Tishelman-Charny
# 5 December 2019 
# The purpose of this module is to create an MC_Configs.json file to run with . main.sh

outputName = 'MC_Configs.json'

MC_Configs = '['

masses = [260, 270, 280, 300, 320, 350, 400, 500, 550, 600, 650, 700, 800, 850, 900, 1000]

for im,mass in enumerate(masses):

    MC_Configs_Entry = '''
    {
        "step"      : "GEN-SIM",
        "events"    : 100000,
        "jobs_jobsize"      : 200,
        "fragment_directory"  : "ggF_X{mass}_WWgg_qqlnugg",
        "pileup"              : "wPU" 
    }'''

    MC_Configs_Entry = MC_Configs_Entry.replace("{mass}",str(mass))
    MC_Configs += MC_Configs_Entry

    if im is not len(masses)-1: MC_Configs += ','
    else: continue 

MC_Configs += ']'

with open(outputName, "w") as output:
    output.write(MC_Configs)