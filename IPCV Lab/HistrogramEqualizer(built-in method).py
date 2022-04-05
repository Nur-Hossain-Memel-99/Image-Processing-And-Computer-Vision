# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:28:39 2020

@author: Arifur Rahaman
"""
import cv2 as cv
from matplotlib import pyplot as plt 
# read a image using imread 
img = cv.imread('Images\lena.jpg',0)
# creating a Histograms Equalization 
# of a image using cv2.equalizeHist() 
equ = cv.equalizeHist(img) 
# stacking images side-by-side 
#res = np.hstack((img, equ)) 
plt.figure(1)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(equ)

plt.figure(2)
plt.subplot(121)
hist = cv.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.title('Histogram')

plt.subplot(122)
hist_eq = cv.calcHist([equ],[0],None,[256],[0,256])
plt.plot(hist_eq)
plt.title('Histogram Equalizer')
