#Program for Image Zooming using "Pixel Replication Method"
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 
# read a image using imread 
img = cv.imread('Images\lena.jpg',0)
#img = cv.imread('Images\lena.jpg',0).astype(np.uint32)
img = img.astype(np.uint32)
#img = np.array([[3, 4, 5, 6],[5, 6, 9, 16],[9, 100, 9, 24]])
def zooming(img):
    m,n = img.shape
    #Counter for Row and Column replication
    x=0 
    y=0 
    #for zero order hold zooming factor is fixed to twice
    f = 2
    z_r = m*f-1
    z_c = n*f-1
    row_wise_zoomed_img = np.zeros([m, z_c], dtype=int)
    for i in range(0, m):
        #Loop for reading column 
        for j in range(0, n):
            #Adding row wise column values
            for t in range(0, f):
                if t :
                    if y > z_c-1: break
                    row_wise_zoomed_img[x,y] = int((img[i,j] + img[i, j+1])/2)
                else:
                    if x > z_r-1: break
                    row_wise_zoomed_img[x,y] = img[i,j]
                y=y+1;
        y=0
        x=x+1
    return row_wise_zoomed_img

row_wise_zoomed_img = zooming(img)
tp_row_wise_zoomed_img = zooming(np.transpose(row_wise_zoomed_img))
col_wise_zoomed_img = np.transpose(tp_row_wise_zoomed_img)
#print(col_wise_zoomed_img)

plt.figure
plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(col_wise_zoomed_img)

