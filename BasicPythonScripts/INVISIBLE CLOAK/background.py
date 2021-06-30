import cv2

cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,back=cap.read()

    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(6)== ord('s'):
            cv2.imwrite('image.jpg',back)
            break

cap.release()
cv2.destroyAllWindows()

        
