# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 2019

@author: cotengineer
"""


import math
#import numpy as np
from mpl_toolkits.mplot3d import Axes3D  
# Axes3D import has side effects, it enables using projection='3d' in add_subplot
import matplotlib.pyplot as plt
import pylab
#from matplotlib import cm


x = [0,0]
maxG = 0
bestX = [0,0]
xx = []
yy = []
zz = []

while (x[1] < 10):  
    
    x[0] = 0
    while (x[0] < 10):
            
        if (x[0]*x[1] >= 0.75) and (x[0]+x[1] <= 15) and (x[0] < 10) and (x[0] > 0) and (x[1] > 0) and (x[1] < 10):
        
            G = abs(((math.cos(x[0]))**4 + (math.cos(x[1])**4) - 2 * (math.cos(x[0])**2) *
                    (math.cos(x[1])**2))/(math.sqrt((1*x[0]**2)+(2*x[1]**2))))
            if G > maxG:
                maxG = G
                bestX = [x[0],x[1]]   
        else:
            G = 0
        
        xx.append(x[0])
        yy.append(x[1])
        zz.append(G)        
        
        x[0] += 0.1
        
    x[1] += 0.1
         
print("Maximum Value:",maxG,'\n',"Corresponding X",bestX)

#3D Plot
fig = pylab.figure()
ax = Axes3D(fig)

ax.plot_trisurf(xx, yy, zz, cmap='jet')

ax.view_init(30, 240)
ax.set_xlabel('X_1')
ax.set_ylabel('X_2')
ax.set_zlabel('G(x)')
plt.show()

"""
Color map types:
Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, spectral_r, spring, spring_r, summer, summer_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r

"""
