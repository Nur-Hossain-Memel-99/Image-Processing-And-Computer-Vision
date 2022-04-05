import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 
# read a image using imread 
img = cv.imread('Images\lena.jpg',0)

def SumArrayValues(PMF, level):
    sum = 0;
    for i in np.arange(0,level+1):
        sum = sum + PMF[i]
    return sum

levels = 256
gray_levels = np.arange(0,levels)
histogram = np.zeros([levels,1], dtype=int)
#step 1
#Read an image
img = cv.imread('Images/lena.jpg',0)
#step 2
# Calculate histogram of input image
rows, cols = img.shape
for i in np.arange(0, rows):
    for j in np.arange(0,cols):
        histogram[img[i,j]]= histogram[img[i,j]] + 1
#step 3
#Calculate PMF with the help of histogram array
resolution = rows*cols # Total number of pixels
histogram_PMF = histogram / resolution
#step 4
#Calculate CDF with help of histogram_PMF array
histogram_CDF = np.zeros([levels,1], dtype=float)
for level in np.arange(0, levels):
    histogram_CDF[level] = SumArrayValues(histogram_PMF, level)
#step 5 
# Generate new CDF levels
histogram_CDF_Levels = np.round(histogram_CDF*(levels-1))
#step 6 
# Update original image array im according to new CDF levels
he_img = img
for i in np.arange(0,levels):
    if histogram_CDF_Levels[i] != i:
        for x in np.arange(0,rows):
            for y in np.arange(0,cols):
                if he_img[x,y] == i:
                    he_img[x,y] = histogram_CDF_Levels[i]

# Calculate histogram of new image
he_histogram = np.zeros([levels,1], dtype=int)
rows, cols = he_img.shape
for i in np.arange(0, rows):
    for j in np.arange(0,cols):
        he_histogram[he_img[i,j]]= he_histogram[he_img[i,j]] + 1

plt.figure(1)
plt.subplot(121)
plt.plot(histogram)
plt.title('Image Histogram')
plt.subplot(122)
plt.plot(he_histogram)
plt.title('Histogram Equalization')


plt.figure(2)
plt.subplot(121)
plt.title('Histogram')
plt.imshow(img)
plt.subplot(122)
plt.imshow(he_img)
plt.title('Histogram Equalizer')
