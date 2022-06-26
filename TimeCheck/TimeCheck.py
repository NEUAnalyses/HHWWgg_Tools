import time 
from matplotlib import pyplot as plt 
maxStatements = 100000

nIfs = []
dts = []

nIfs_CheckTwo = []
dts_CheckTwo = [] 

for Nstatements in range(1,maxStatements+1):
  initialTime = time.time()
  for N in range(1,Nstatements+1):
   if(1 and (1 and 1 and 1)): pass 
  finalTime = time.time()
  dt = finalTime - initialTime 
  #print"dt=",dt 
  nIfs.append(Nstatements)
  dts.append(dt)

plt.plot(nIfs,dts, label = "One Condition")
plt.xlabel("N if statements")
plt.ylabel("Time [s]")
"""
for Nstatements in range(1,maxStatements+1):
  initialTime = time.time()
  for N in range(1,Nstatements+1):
    if(1 and (1 and 1 and 1)): pass 
  finalTime = time.time()
  dt = finalTime - initialTime 
  #nIfs_CheckTwo
  dts_CheckTwo.append(dt)
"""
#plt.plot(nIfs,dts_CheckTwo,label="Two Conditions")
#plt.legend()
plt.savefig("dtVsif.png")
