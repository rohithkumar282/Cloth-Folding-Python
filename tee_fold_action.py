#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon
from shapely.geometry import LineString, Point
from numpy import linalg as la
from fold_geometry import *

if __name__ == "__main__":

    # T-Shirt
    bottom_left = (5,1)
    left_armpit = (5,11)
    left_sleeve_bottom = (3,9)
    left_sleeve_top = (1,11)
    left_shoulder_top = (5,15)
    left_collar = (7,16.8)
    spine_top = (11,16)
    right_collar = (15,16.8)
    right_shoulder_top = (17,15)
    right_sleeve_top = (21,11)
    right_sleeve_bottom = (19,9)
    right_armpit = (17,11)
    bottom_right = (17,1)
    # joining all coordinates
    tee_raw = [bottom_left,left_armpit,left_sleeve_bottom,left_sleeve_top,left_shoulder_top,left_collar,spine_top
               ,right_collar,right_shoulder_top,right_sleeve_top,right_sleeve_bottom,right_armpit,bottom_right]
    #converting into a closed geometry 
    tee = Polygon(tee_raw)

    # example of folding
    fig= plt.figure(1, figsize=(5,5), dpi=90)
    ax = fig.add_subplot(111)

    x,y = tee.exterior.xy
    ax.plot(x, y, color='blue', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
    plt.xlim(-10,30)
    plt.ylim(0,20)
    plt.show()

grasp_points1=[0,20,16.9,16.9]
grasp_points2=[8.9,8.9,0,30]
grasp_points3=[5,5]
grasp_points4=[0,20]
#fold_lines
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
x,y = tee.exterior.xy
ax.plot(x, y, color='blue', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.plot(grasp_points1[:2],grasp_points2[:2],'r-')
ax.plot(grasp_points1[2:5],grasp_points2[2:5],'r-')
ax.plot(grasp_points3[:],grasp_points4[:],'r-')
ax.set_title('Fold Lines')

plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()
#first_fold
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
fold = fold_geometry()
#fold_lines and polygon coordinates sent to fold_geometry.py
folded_raw = fold.fold(tee_raw,[(5.9,125),(5.5,30)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('T-Shirt')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()

t_raw=[]
i=0
#acquiring coordinates after first fold to perform second fold on it
for i in range(len(folded.exterior.xy[0])):
    t_raw.append((folded.exterior.xy[0][i],folded.exterior.xy[1][i]))
#second_fold    
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
#fold lines and coordinates of polygon
folded_raw = fold.fold(t_raw,[(16.9,0),(16.5,30)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('T-Shirt')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()

t1_raw=[]
i=0
#acquiring coordinates after second fold to perform third fold on it
for i in range(len(folded.exterior.xy[0])):
    t1_raw.append((folded.exterior.xy[0][i],folded.exterior.xy[1][i]))
#third fold
fig= plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
#fold lines and coordinates of polygon
folded_raw = fold.fold(t1_raw,[(0,8.9),(20,8.9)])
folded = Polygon(folded_raw)
x,y = folded.exterior.xy
ax.plot(x, y, color='green', alpha=0.7,linewidth=2, solid_capstyle='round', zorder=2)
ax.set_title('T-Shirt')
plt.xlim(-10,30)
plt.ylim(0,20)
plt.show()


# In[ ]:




