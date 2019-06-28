# import numpy,matplotlib.pyplot
import numpy as np
import math
# import matplotlib.pyplot as plt

#def loaddata
def loaddata(filename):
    fr=open(filename)

    x=[]
    y=[]
    z=[]
    for line in fr.readlines():

        line=line.strip().split()
        x.append(float(line[1]))
        y.append(float(line[2]))
        z.append(float(line[3]))
    xmat=np.array(x)
    ymat=np.array(y)
    zmat=np.array(z)
    return xmat,ymat,zmat

# show
xmat,ymat,zmat=loaddata('D:\CCbondJ\CCBJ2.txt')

i=0
j=0
CC1=0
CC2=0
CC3=0
while (i<3000):
    j=i+1
    while (j<3000):
        D=math.pow((xmat[i]-xmat[j]),2)+math.pow((ymat[i]-ymat[j]),2)+math.pow((zmat[i]-zmat[j]),2)
        d=math.sqrt(D)
        j= j+1
        if (d>1.54):
          continue
        elif (1.44 < d <=1.54):
           CC1=CC1+1
        elif (1.27<d<=1.44):
           CC2=CC2+1
        elif (d<=1.27):
           CC3=CC3+1
    else:i=i+1

print('CC1=',CC1)
print('CC2=',CC2)
print('CC3=',CC3)