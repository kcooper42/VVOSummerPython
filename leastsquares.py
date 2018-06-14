#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 13:30:02 2018

@author: kecooper
"""

def leastsquares(dx,dy):
    ## summation of x, y, xy, x^2 and computation of least squares
    sx2=0
    sxy=0
    sx=0
    sy=0
    for i in range(len(dx)):
        sx+=dx[i]
        sy+=dy[i]
        sxy+=dx[i]*dy[i]
        sx2+=dx[i]**2
    N=float(len(dx))
    m=((N*sxy)-(sx*sy))/((N*sx2-(sx)**2))
    b=((sy*sx2)-(sx*sxy))/((N*sx2)-(sx)**2)
    return m, b

dx=[]
dy=[]
dr=[]
for line in open('/Users/kecooper/Documents/python/data.csv','r').readlines():
    if 'P' in line:
        continue
    vals=line.strip().split(',')
    dx+=[float(vals[0])]
    dy+=[float(vals[1])]
    dr+=[float(vals[2])]
    ## reads and extracts avlues from cvs data file of cephieds
print(leastsquares(dx,dy))

import matplotlib.pyplot as plt
kwargs={'color':'white','linestyle':'none','marker':'o','markeredgecolor':'red','label':'Data'}
m,b = leastsquares(dx,dy)
mx=[float(i) for i in range(50)]
my=[m*mxi+b for mxi in mx]
## mx and my are model x and y for y=mx+b
plt.plot(dx,dy,**kwargs)
plt.plot(mx,my,'--k',label='y=mx+b')
plt.xlabel('logP')
plt.ylabel('Mw')
plt.xlim(0,1.6)
plt.ylim(-4,-9)
plt.legend()
plt.show()



