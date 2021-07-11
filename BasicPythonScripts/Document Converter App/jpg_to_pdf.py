# import image from pillow module
from PIL import Image

# user input of the jpg image path
jpg_path = input("Enter the path of the .jpg image : ")

# opening jpg image
im1 = Image.open(jpg_path)

# user input of pdf file path
pdf_path = input("Enter the folder where pdf file should be saved : ")

# user input of pdf file name to be saved
pdf_name=input("Enter the name by which the pdf file should be saved: ")

# saving as png image
im1.save(pdf_path+"\ "+pdf_name+".pdf")
