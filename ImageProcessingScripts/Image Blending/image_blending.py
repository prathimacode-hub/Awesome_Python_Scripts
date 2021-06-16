import cv2 
import numpy as np

#reading input images
img1=cv2.imread('apple.jpg')
img2=cv2.imread('orange.jpg')

#resizing the image 
img1=cv2.resize(img1,(img2.shape[1],img2.shape[0]))

#concatenating two inputimages
img = np.hstack((img1,img2))
cv2.imshow("Original Image",img)

#blending the image
blended_img=cv2.addWeighted(img1,0.45,img2,0.55,0)

#displaying final output
cv2.imshow("Blended Image",blended_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
