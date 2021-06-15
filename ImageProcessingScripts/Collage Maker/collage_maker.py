#import PIL and numpy
from PIL import Image
import numpy as np

#open images by providing path of images 

img1= Image.open(r"D:/Python/Img1.jpg.jpg")
img2= Image.open(r"D:/Python/Img2.jpg.jpg")

#create arrays of above images 

img1_array = np.array(img1)
img2_array = np.array(img2)

#================collage of 2 images==============
#arrange arrays of two images in a single row 

imgg = np.hstack([img1_array, img2_array])

#create image of imgg array

finalimg = Image.fromarray(imgg)

#provide the path with name for finalimg where you want to save it 

finalimg.save(r"D:/Python.jpg")
print("Image saved")

