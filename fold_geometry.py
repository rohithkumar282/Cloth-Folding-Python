#!/usr/bin/env python
# coding: utf-8

# In[1]:


from shapely.geometry import LineString, Point
from numpy import linalg as la

class fold_geometry:
    def __init__(self):
        return

    def is_dynamic(self, pt, fold_line):
        x0, y0 = fold_line[0]
        x1, y1 = fold_line[1]
        x2, y2 = pt
        val = (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)
        if val < 0:
            return True
        else:
            return False
    #perform folding
    def reflect(self, pt, fold_line):
        x0, y0 = fold_line[0]
        x1, y1 = fold_line[1]
        x2, y2 = pt
        # reflecting over y-axis
        if x1-x0 == 0:
            x2 = x1-(x2-x1)
        else:
            slope = (y1-y0)/(x1-x0)
            intercept = y1-slope * x1
            d = (x2 + (y2 - intercept) * slope)/(1 + slope ** 2)
            x2 = 2*d - x2
            y2 = 2*d*slope - y2 + 2*intercept

        return (x2,y2)

    # recieves shape of object, and 2 point define a line
    def fold(self, shape, fold_line):
        folded = []
        fold_l = LineString(fold_line)
        print(fold_l)
        for i in range(len(shape)):
            if i == len(shape)-1:
                temp = LineString([shape[i],shape[0]])
            else:
                temp = LineString([shape[i],shape[i+1]])

            if self.is_dynamic(shape[i], fold_line):
                folded.append(self.reflect(shape[i], fold_line))
            else:
                folded.append(shape[i])

            if isinstance(fold_l.intersection(temp), Point):
                folded.append(list(fold_l.intersection(temp).coords)[0])
        return folded


# In[ ]:




