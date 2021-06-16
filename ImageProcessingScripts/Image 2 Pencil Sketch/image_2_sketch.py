import cv2
image=cv2.imread('Image 2 Pencil Sketch/Images/Captain_america.jpg') #  loads an image from the specified file
grey_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # convert an image from one color space to another
invert=cv2.bitwise_not(grey_img) # helps in masking of the image
blur=cv2.GaussianBlur(invert,(21,21),0) # sharp edges in images are smoothed while minimizing too much blurring
invertedblur=cv2.bitwise_not(blur)
sketch=cv2.divide(grey_img,invertedblur,scale=256.0)
cv2.imwrite("sketch.png",sketch) # converted image is saved as mentioned name
