#!/usr/bin/env python
# coding: utf-8

# In[3]:


from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon
from shapely.geometry import LineString, Point
from numpy import linalg as la
from fold_geometry import *

if __name__ == "__main__":


    # Pant
    left_leg_right = (4,1)
    left_leg_left = (1,1.2)
    top_left = (2,18)
    top_right = (10,18)
    right_leg_right = (11,1.2)
    right_leg_left = (8,1)
    crotch = (6,14)
    # joining all coordinates
    pant_raw = [left_leg_right,left_leg_left,top_left,top_right,right_leg_right,right_leg_left,crotch]
    #converting into a closed geometry 
    pant = Polygon(pant_raw)


    # example of folding
    fig= plt.figure(1, figsize=(5,5), dpi=90)
    ax = fig.add_subplot(111)

    x,y = pant.exterior.xy
    ax.plot(x, y, color='blue', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
    plt.xlim(-10,30)
    plt.ylim(0,20)
    plt.show()

grasp_points1=[-4,15,-4,15,6.1,6.1]
grasp_points2=[9.5,9.5,13.4,13.4,0,20]
#fold lines
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
x,y = pant.exterior.xy
ax.plot(x, y, color='blue', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.plot(grasp_points1[:2],grasp_points2[:2],'r-')
ax.plot(grasp_points1[2:4],grasp_points2[2:4],'r-')
ax.plot(grasp_points1[4:],grasp_points2[4:],'r-')
ax.set_title('Fold Lines')

plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()
#first fold
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
fold = fold_geometry()
#fold_lines and polygon coordinates sent to fold_geometry.py
folded_raw = fold.fold(pant_raw,[(6.1,125),(6.1,30)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('Pant')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()


pant1_raw=[]
i=0
#acquiring coordinates after first fold to perform second fold on it
for i in range(len(folded.exterior.xy[0])):
    pant1_raw.append((folded.exterior.xy[0][i],folded.exterior.xy[1][i]))
#second_fold   
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
#fold lines and coordinates of polygon
folded_raw = fold.fold(pant1_raw,[(0,9.5),(20,9.5)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('Pant')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()

pant2_raw=[]
i=0
#acquiring coordinates after second fold to perform third fold on it
for i in range(len(folded.exterior.xy[0])):
    pant2_raw.append((folded.exterior.xy[0][i],folded.exterior.xy[1][i]))
#third fold
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
#fold lines and coordinates of polygon
folded_raw = fold.fold(pant2_raw,[(0,13.4),(20,13.4)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('Pant')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()


# In[18]:


fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
fold = fold_geometry()
folded_raw = fold.fold(pant_raw,[(6.1,125),(6.1,30)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('Pant')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()


# In[19]:


pant1_raw=[]
i=0
for i in range(len(folded.exterior.xy[0])):
    pant1_raw.append((folded.exterior.xy[0][i],folded.exterior.xy[1][i]))
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
folded_raw = fold.fold(pant1_raw,[(0,9.5),(20,9.5)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('Pant')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()


# In[20]:


pant2_raw=[]
i=0
for i in range(len(folded.exterior.xy[0])):
    pant2_raw.append((folded.exterior.xy[0][i],folded.exterior.xy[1][i]))
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
folded_raw = fold.fold(pant2_raw,[(0,13.4),(20,13.4)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('Pant')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()


# In[22]:


grasp_points1=[-4,15,-4,15,6.1,6.1]
grasp_points2=[9.5,9.5,13.4,13.4,0,20]

fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
x,y = pant.exterior.xy
ax.plot(x, y, color='blue', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.plot(grasp_points1[:2],grasp_points2[:2],'r-')
ax.plot(grasp_points1[2:4],grasp_points2[2:4],'r-')
ax.plot(grasp_points1[4:],grasp_points2[4:],'r-')
ax.set_title('Fold Lines')

plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()


# In[ ]:




