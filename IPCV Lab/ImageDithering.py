import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 

def UnifDither(img, A, thr = 128):
     rows, cols = img.shape
     noise = (np.random.rand(rows, cols ) - 0.5)*A
     img_n = np.float16(img) + noise
     return img_n > thr

img = cv.imread('Images\lena.jpg',0)
plt.figure(1)
plt.subplot(121)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(122)
plt.imshow(img > 128)
plt.title('After threshold')

figure,axes= plt.subplots(nrows=1, ncols=3)
#plt.figure(2)
plt.subplot(131)
plt.imshow(UnifDither(img,16))
plt.title('After Dithering(A=16)')
plt.subplot(132);
plt.imshow(UnifDither(img,64));
plt.title('After Dithering(A=64)')
plt.subplot(133);
plt.imshow(UnifDither(img,128));
plt.title('After Dithering(A=128)')
figure.tight_layout(pad=1.0)