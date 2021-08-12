import os 
for d in os.listdir("crab_projects"):
  COMMAND = "crab status -d crab_projects/%s"%(d)
  print"*****************************************"
  print(COMMAND)
  print"*****************************************"
  os.system(COMMAND)
