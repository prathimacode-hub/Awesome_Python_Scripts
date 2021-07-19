import PIL
from PIL import Image

mywidth=3278  #width of the image to be obtained
myheight=4917 #height of the image to be obtained

#opening the image
img=Image.open('cute_dog.jpg')
#resizing the image
img=img.resize((mywidth,myheight),PIL.Image.ANTIALIAS)
#saving the image
img.save('resize.jpg')
