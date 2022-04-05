#Program for Image Zooming using "Pixel Replication Method"
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 
# read a image using imread 
img = cv.imread('Images\lena.jpg',0)
#img = np.array([[5,6],[7,8]])
m,n = img.shape
#Counter for Row and Column replication
x=0 
y=0 
#enter zooming factor f
f = int(input('Enter replication factor: '))
zoomed_img = np.zeros([m*f,n*f], dtype=int)
# =============================================================================
# [5,6]
# [7,8]
# =============================================================================
#Loop for reading row and
for i in range(0, m):
    #Row replication
    for t in range(0, f):
        #Loop for reading column 
        for j in range(0, n):
            #Column replication
            for t in range(0, f):
                zoomed_img[x,y] = img[i,j]
                y=y+1;
        y=0
        x=x+1
#print(zoomed_img)

plt.figure
plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(zoomed_img)
