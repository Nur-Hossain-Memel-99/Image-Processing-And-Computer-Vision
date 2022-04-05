import cv2 as cv
import numpy as np
#read an rgb image
# get gray image using second parameter as 0
#gray_image = cv.imread ("Images\lena.jpg", 0)
rgb_image = cv.imread ("Images\lena.jpg")
size = rgb_image.shape
rows = size[0]
cols = size[1]
rgb_image = rgb_image.astype(np.uint32)
grey_image_using_average_method = np.zeros([rows, cols], dtype = int)
grey_image_using_formula = np.zeros([rows, cols], dtype = int)
for x in range(rows):
    for y in range(cols):
        grey_image_using_average_method[x, y] = int((rgb_image[x,y,0] + rgb_image[x,y,1]+ rgb_image[x,y,2])/3)
        grey_image_using_formula[x, y] = int(0.3*rgb_image[x,y,0] + 0.59*rgb_image[x,y,1] + 0.11*rgb_image[x,y,2])

cv.imwrite("Images\lena_gray_grey_image_using_average_method.jpg", grey_image_using_average_method)
cv.imwrite("Images\lena_gray_using_formula.jpg", grey_image_using_formula)
cv.imshow("RGB Image", rgb_image.astype(np.uint8)) 
cv.imshow("Using Average", grey_image_using_average_method.astype(np.uint8))
cv.imshow("Using Formula", grey_image_using_formula.astype(np.uint8)) 
cv.waitKey(0)