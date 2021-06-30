import cv2
import numpy as np
cap=cv2.VideoCapture(0)
back=cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame=cap.read()

    if ret:
        #conversion of RGB to HSV
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #cv2.imshow('image.jpg',hsv)
        red=np.uint8([[[0,0,255]]])
        hsv_yellow=cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        #print(hsv_red)
        l_red=np.array([0,100,100])
        u_red=np.array([10,255,255])

        mask=cv2.inRange(hsv, l_red, u_red)
        #cv2.imshow("mask",mask)
        part1=cv2.bitwise_and(back,back,mask=mask)
        #cv2.imshow('part2',part1)
        mask=cv2.bitwise_not(mask)

        part2=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("cloak",part1+part2)
        if cv2.waitKey(5)==ord('s'):
            break

cap.release()
cap.destroyAllWindows()

