import matplotlib.pyplot as plt 
#import matplotlib.ticker as ticker
import pandas as pd 
import csv



tudfarben = {"blau":"#005AA9","hellblau":"#0083CC","tuerkis":"#009D81","gruen":"#99C000","gruengelb":"#C9D400","gelb":"#FDCA00","orange":"#F5A300","orangerot":"#EC6500","rot":"#E6001A","lila":"#A60084","lilablau":"#721085"}
myfiles = ["av_numberofblobs_35.txt", "av_numberofblobs_50.txt", "av_numberofblobs_75.txt", "av_numberofblobs_100.txt"]
alldata = []
for myfile in myfiles:
     data = pd.read_csv(myfile, sep = "\s\s\s\s\s\s", header=None, names = ["x","y","eb"])
     x = data["x"]
     y = data["y"]
     eb = data["eb"]
     alldata.append((x,y,eb))
#plt.plot(*alldata[0][:2],label="quench 35", color=tudfarben["rot"]) # nur die ersten beiden (also x und y, kein eb)     
#plt.errorbar(*alldata[0],label="quench 35")
plt.errorbar(*alldata[1],label="quench 50", color=tudfarben["lila"])
plt.errorbar(*alldata[2],label="quench 75", color=tudfarben["orange"])
plt.errorbar(*alldata[3],label="quench 100", color=tudfarben["gruen"])

plt.legend(shadow=True)
plt.xlabel('timestep')
plt.ylabel('beads per bridge')
#plt.show()
#plt.figure()
plt.savefig('numberofblobs_witheb.png')

plt.close()


plt.errorbar(*alldata[1][:2],label="quench 50", color=tudfarben["lila"])
plt.errorbar(*alldata[2][:2],label="quench 75", color=tudfarben["orange"])
plt.errorbar(*alldata[3][:2],label="quench 100", color=tudfarben["gruen"])

plt.legend(shadow=True)
plt.xlabel('timestep')
plt.ylabel('number of blobs')

plt.savefig('numberofblobs.png')

plt.close()

plt.errorbar(*alldata[1],label="quench 50", color=tudfarben["lila"])

plt.legend(shadow=True)
plt.xlabel('timestep')
plt.ylabel('number of blobs')

plt.savefig('numberofblobs_50.png')

plt.close()



plt.errorbar(*alldata[2],label="quench 75", color=tudfarben["orange"])

plt.legend(shadow=True)
plt.xlabel('timestep')
plt.ylabel('number of blobs')

plt.savefig('numberofblobs_75.png')

plt.close()




plt.errorbar(*alldata[3],label="quench 100", color=tudfarben["gruen"])

plt.legend(shadow=True)
plt.xlabel('timestep')
plt.ylabel('number of blobs')

plt.savefig('numberofblobs_100.png')

plt.close()


