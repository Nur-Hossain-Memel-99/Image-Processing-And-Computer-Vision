# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:34:36 2021

@author: Arifur Rahaman
"""
import cv2 as cv
img = cv.imread("Images\lena.jpg",0)
#Image size caculation formula
#ImageSize = rows*colms*bpp
rows = img.shape[0]
colms = img.shape[1]
bpp = 8
ImageSize = rows*colms*bpp
print("image size is ", ImageSize, "bits")

