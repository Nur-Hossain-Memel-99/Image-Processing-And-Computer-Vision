import cv2 
import matplotlib.pyplot as plt
# Loading the image 
image = cv2.imread('Images\lena.jpg', 1) 
'''
cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
src	[required] source/input image
dsize	[required] desired size for the output image
fx	[optional] scale factor along the horizontal axis
fy	[optional] scale factor along the vertical axis
interpolation	[optional] flag that takes one of the following methods. INTER_NEAREST – a nearest-neighbor interpolation INTER_LINEAR – a bilinear interpolation (used by default) INTER_AREA – resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method. INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood INTER_LANCZOS4 – a Lanczos interpolation over 8×8 pixel neighborhood
'''
half = cv2.resize(image, (0, 0), fx =.5, fy =.5)
#bigger = cv2.resize(image, (1050, 1610),fx =.5, fy =.5) 
bigger = cv2.resize(image, (1000, 1000)) 
stretch_near = cv2.resize(image, (780, 540), interpolation = cv2.INTER_NEAREST) 
Titles =["Original", "Half", "Bigger", "Interpolation Nearest"] 
images =[image, half, bigger, stretch_near] 
#count = len(images)
count = 4

for i in range(count): #0,1,2,3
	plt.subplot(2, 2, i + 1) 
	plt.title(Titles[i]) 
	plt.imshow(images[i]) 

plt.show() 
