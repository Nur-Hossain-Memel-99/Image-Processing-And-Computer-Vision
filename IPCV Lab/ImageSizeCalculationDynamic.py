'''
import imghdr
import easygui
import sys
file = easygui.fileopenbox(msg="Choose JPG file to convert",
                           default="*.jpg")
#print(imghdr.what(file)==None)

if imghdr.what(file) == None:
    print("No image detected")
    sys.exit()
elif imghdr.what(file) == 'jpg' or 'jpeg':
    print(file)
#print(file)
'''

'''
Needed Modules: cv2,Tk,fildialog,imghdr,matplotlib.pyplot
Drawbacks:
    1. I can take image input for given type only(".png .jfif .jpg .jpeg")
    2. Can determine image type for png and jpeg only.
    3. If we select multiple image then the convertion tuple to string didn't work
'''
# open_file = filedialog.askopenfilenames(filetypes=[("File type", "Image's .extesnions spearated by space")])
# In this example I'll be opening dialog box to select only images with (.jpg, .jpeg, .png, .jfif) extensions.
from tkinter import Tk, filedialog
root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
# Open dialog box to select images with certain extensions.
open_file = filedialog.askopenfilenames(filetypes=[("Image Files", ".png .jfif .jpg .jpeg")]) # returns a tuple with opened file's complete path
#print(open_file[0])
#Convert the tuple into string
path = ''
for item in open_file:
    #print(item)
    path = path + item

#Now we read the image that we selected earlier
import cv2 as cv
image = cv.imread(path)
#print(image.shape)

#Display the image into plots
import matplotlib.pyplot as plt
#plt.subplot(1,1,1)
plt.title("Main Image")
plt.imshow(image)
plt.show()

#Determine the type of an image
import imghdr
print('The Image type is ',imghdr.what(path,h=None))