# import image from pillow module
from PIL import Image

# user input of the jpg image path
jpg_path = input("Enter the path of the .jpg image : ")

# opening jpg image
im1 = Image.open(jpg_path)

# user input of png image path
png_path = input("Enter the folder where .png image should be saved : ")

# user input of png file name to be saved
png_name=input("Enter the name by which the .png image should be saved: ")

# saving as png image
im1.save(png_path+"\ "+png_name+".png")
