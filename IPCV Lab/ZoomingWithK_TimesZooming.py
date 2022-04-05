#Program for Image Zooming using "Pixel Replication Method"
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 
#operator list
op_list = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y}
# read a image using imread 
img = cv.imread('Images\lena.jpg',0).astype(float)
#img = img.astype(np.uint32)
#img = np.array([[15,30,15],[30,15,30]])
k=int(input('Enter replication factor: '))
def zooming(img, f):
    m,n = img.shape
    #Counter for Row and Column replication
    x=0 
    y=0 
    z_c=k*(n-1)+1
    row_wise_zoomed_img = np.zeros([m, z_c]).astype(float)
    #Loop for reading row and
    #Row replication
    for i in range(0, m):
        #Loop for reading column 
        for j in range(0, n-1):
            op = np.round(np.abs(img[i,j]- img[i,j+1])/k)
            #Column replication
            for t in range(0, k):
                if t == 0:
                    row_wise_zoomed_img[x,y] = img[i,j]
                    inserted_value = img[i,j]
                    if img[i,j] <= img[i,j+1]:
                        operator = '+'
                    else:
                        operator = '-'
                else:
                    inserted_value =op_list[operator](inserted_value,op)
                    row_wise_zoomed_img[x,y] = inserted_value
                y=y+1
                if t == k-1:
                    row_wise_zoomed_img[x,y] = img[i,j+1]
            op = 0
        y=0
        x=x+1
    return row_wise_zoomed_img

#print(zooming(img,f))
row_wise_zoomed_img = zooming(img,k)
tp_row_wise_zoomed_img = zooming(np.transpose(row_wise_zoomed_img),k)
col_wise_zoomed_img = np.transpose(tp_row_wise_zoomed_img).astype(int)
#print(col_wise_zoomed_img)

plt.figure
plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(col_wise_zoomed_img)
