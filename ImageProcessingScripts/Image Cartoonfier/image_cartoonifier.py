import cv2


#fetching the image
img =cv2.imread("image.jpg")
#giving the color changes
gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
gray=cv2.medianBlur(gray,9)
edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,13,6)
color=cv2.bilateralFilter(img,9,250,250)
cartoon=cv2.bitwise_and(color,color,mask=edges)

#showing the output image
cv2.imshow("output cartoonified image",cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()