# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 20:07:22 2020

@author: Arifur Rahaman
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 
histogram = np.zeros([256,1], dtype=int)
img = cv.imread('Images/lena.jpg',0) 
#size = img.shape
#rows, cols = size[0], size[1]
rows, cols = img.shape
for i in np.arange(0, rows):
    for j in np.arange(0,cols):
        histogram[img[i,j]]= histogram[img[i,j]] + 1

figure,axes= plt.subplots(nrows=1, ncols=2)
plt.subplot(121)
plt.imshow(img)
plt.title('Lena Image')

plt.subplot(122)
plt.plot(histogram)
plt.title('Image hitogram')
plt.xlabel('Intensity or color level')
plt.ylabel('Frequency')
plt.show() 