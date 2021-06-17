#importimg the librabies
import cv2
import numpy as np

#adding the required elements
frameWidth = 1000
frameHeight = 1000
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

#adding the colorcodes
colorsofme = [[5, 107, 0, 19, 255, 255],  # orange
            [90, 48, 0, 118, 255, 255]]  # blue
[133, 56, 0, 159, 156, 255],  # purple
[57, 76, 0, 100, 255, 255],  # green

#adding color values
values = [[255, 153, 0],  # BGR
                 [0, 0, 0],
                 [255, 153, 153],
                 [0, 153, 0]]

myPoints = []  # [x , y , colorId ]

#let the screen find the colors
def findColor(img, colorsofme, values):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    
    for color in colorsofme:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 15, values[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        
        #let us return the result of cv2.imshow(str(color[0]),mask) 
    return newPoints


def getContours(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            
            #let us find the cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

#result
def drawOnCanvas(myPoints, values):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]),
                   10, values[point[2]], cv2.FILLED)

#running a while loop.
        
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, colorsofme, values)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, values)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

#let us destroy all the windows
cv2.destroyAllWindows()
