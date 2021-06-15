import cv2
import matplotlib.pyplot as plt
img = cv2.imread('flower.jpg') #reading the input images

cv2.imshow("Original Image",img)
edges = cv2.Canny(img,100,150)#detecting edges of the images using canny() edge algorithm
cv2.imshow("Canny Edge detection",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
