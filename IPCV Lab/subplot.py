from matplotlib import pyplot as plt
import cv2 as cv
img = cv.imread("Images/lena.jpg")
cv.imwrite("Images/lena_test.jpg",img)
plt.subplot(131)
plt.imshow(img)
plt.subplot(132)
plt.imshow(cv.imread("Images/lena.jpg",0))
plt.subplot(133)
