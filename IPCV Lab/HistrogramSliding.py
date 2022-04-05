
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt 
histogram = np.zeros([256,1], dtype=int);
img = cv.imread('Images/lena.jpg',0)
img_right_sliding = img + 50
img_left_sliding = img - 50
"""
The parameters are:

    images: source image of type uint8 or float32. it should be given in as a list, ie, [gray_img].
    channels: it is also given in as a list []. It the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0],[1] or [2] to calculate histogram of blue,green or red channel, respectively.
    mask: mask image. To find histogram of full image, it is set as None. However, if we want to get histogram of specific region of image, we should create a mask image for that and give it as mask.
    histSize: this represents our BIN count. Need to be given in []. For full scale, we pass [256].
    ranges: Normally, it is [0,256].

"""
histr = cv.calcHist([img],[0],None,[256],[0,256])
histr_right_sliding = cv.calcHist([img_right_sliding],[0],None,[256],[0,256])
histr_left_sliding = cv.calcHist([img_left_sliding],[0],None,[256],[0,256])
# show the plotting graph of an image 
figure,axes= plt.subplots(nrows=1, ncols=3)

plt.subplot(131)
plt.plot(histr)
plt.title('Normal Hitrogram')
plt.xlabel('Intensity level')
plt.ylabel('Intensity level frequency')

plt.subplot(132)
plt.plot(histr_left_sliding)
plt.title('Left slided hitrogram')
plt.xlabel('Intensity level')

plt.subplot(133)
plt.plot(histr_right_sliding)
plt.title('Right slided hitrogram')
plt.xlabel('Intensity level')
#figure.tight_layout(pad=1.0)
plt.show() 