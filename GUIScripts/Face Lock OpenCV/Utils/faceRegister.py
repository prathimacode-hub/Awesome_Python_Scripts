import cv2
import copy
cap = cv2.VideoCapture(0)

name=input("Please Enter Your First Name :   ")
while(True):
    ret,frame = cap.read()
    frame1=copy.deepcopy(frame)
    frame1 = cv2.putText(frame1, 'Press \'k\' to click photo', (200,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 3, cv2.LINE_AA)
    cv2.imshow('img1',frame1)
    if cv2.waitKey(1) & 0xFF == ord('k'):
        cv2.imwrite('faceRegister/%s.png'%name,frame)
        cv2.destroyAllWindows()
        break

cap.release()