#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon
from shapely.geometry import LineString, Point
from numpy import linalg as la
from fold_geometry import *

if __name__ == "__main__":
    # Towel
    bottom_left = (1,1)
    top_left = (1,7)
    top_right = (12,7)
    bottom_right = (12,1)
    # joining all coordinates
    towel_raw = [bottom_left,top_left,top_right,bottom_right]
    #converting into a closed geometry 
    towel = Polygon(towel_raw)

    # example of folding
    fig= plt.figure(1, figsize=(5,5), dpi=90)
    ax = fig.add_subplot(111)

    x,y = towel.exterior.xy
    ax.plot(x, y, color='blue', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
    plt.xlim(-10,30)
    plt.ylim(0,20)
    plt.show()
    
grasp_points1=[-2,15,6.4,6.4]
grasp_points2=[4,4,0,12]
#fold_lines
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
x,y = towel.exterior.xy
ax.plot(x, y, color='blue', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.plot(grasp_points1[:2],grasp_points2[:2],'r-')
ax.plot(grasp_points1[2:],grasp_points2[2:],'r-')
ax.set_title('Fold Lines')

plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()
#first fold
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
fold = fold_geometry()
#send fold lines and coordinates of polygon
folded_raw = fold.fold(towel_raw,[(6.4,0),(6.4,10)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('Towel')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()

towel1_raw=[]
i=0
#acquiring coordinates after first fold to perform second fold on it
for i in range(len(folded.exterior.xy[0])):
    towel1_raw.append((folded.exterior.xy[0][i],folded.exterior.xy[1][i]))
#second fold
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
folded_raw = fold.fold(towel1_raw,[(0,4),(20,4)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('Towel')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()


# In[ ]:




