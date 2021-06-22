################################################
#           AIR CANVAS PROJECT
###############################################


import cv2
import numpy as np

#### global ####
x, y, k = 200, 200, -1

cap = cv2.VideoCapture(0)  # input video stream


# func def #########################
def take_inp(event, x1, y1, flag, param):
    global x, y, k
    if event == cv2.EVENT_LBUTTONDOWN:  # indicates that the left mouse button is pressed.
        x = x1
        y = y1
        k = 1


# The function namedWindow creates a window that can be used as a placeholder for images and trackbars. Created
# windows are referred to by their names.
cv2.namedWindow("enter_point")
cv2.setMouseCallback("enter_point", take_inp)  # Callback function for mouse events

# taking input point ######################
while True:

    _, inp_img = cap.read()
    inp_img = cv2.flip(inp_img, 1)  # flips a 2D array around vertical, horizontal, or both axes
    gray_inp_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)  # this method is used to convert an image from one
    # color space to another

    cv2.imshow("enter_point", inp_img)

    # waitKey() is a keyboard binding function. Its argument is the time in milliseconds. 0 – wait indefinitely cv2. destroyAllWindows() simply destroys all the windows we created. To destroy any specific window
    if k == 1 or cv2.waitKey(30) == 27:
        cv2.destroyAllWindows()
        break

##############################################
stp = 0
########## opical flow starts here ###########


old_pts = np.array([[x, y]], dtype=np.float32).reshape(-1, 1, 2)

mask = np.zeros_like(inp_img)

while True:
    _, new_inp_img = cap.read()
    new_inp_img = cv2.flip(new_inp_img, 1)  # flips a 2D array around vertical, horizontal, or both axes
    new_gray = cv2.cvtColor(new_inp_img, cv2.COLOR_BGR2GRAY)  # this method is used to convert an image from one
    new_pts, status, err = cv2.calcOpticalFlowPyrLK(gray_inp_img,
                                                    new_gray,
                                                    old_pts,
                                                    None, maxLevel=1,
                                                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                                                              15,
                                                              0.08))  # alcOpticalFlowPyrLK function that calculate the flow between to image and allow to track the movement of an object.

    for i, j in zip(old_pts, new_pts):
        x, y = j.ravel()
        a, b = i.ravel()
        if cv2.waitKey(2) & 0xff == ord('q'):  # waitKey() is a keyboard binding function.
            stp = 1

        elif cv2.waitKey(2) & 0xff == ord('w'):
            stp = 0

        elif cv2.waitKey(2) == ord('n'):
            mask = np.zeros_like(new_inp_img)

        if stp == 0:
            mask = cv2.line(mask, (a, b), (x, y), (0, 0, 255), 6)  # we use this method to draw a line, you need to
            # pass starting and ending coordinates of line.

        cv2.circle(new_inp_img, (x, y), 6, (0, 255, 0), -1)  # we use this method to draw a circle

    new_inp_img = cv2.addWeighted(mask, 0.3, new_inp_img, 0.7, 0)  # Calculates the weighted sum of two arrays.
    cv2.putText(mask, "'q' to gap 'w' - start 'n' - clear", (10, 50),
                # cv2.putText() method is used to draw a text string on any image.
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))
    cv2.imshow("ouput", new_inp_img)  # cv2.imshow() method is used to display an image in a window
    cv2.imshow("result", mask)

    gray_inp_img = new_gray.copy()  # copy() method is used to clone an image
    old_pts = new_pts.reshape(-1, 1,
                              2)  # Many times we need to resize the image i.e. either shrink it or scale up to meet the size requirements

    if cv2.waitKey(1) & 0xff == 27:  # waitKey() is a keyboard binding function.
        break

#### thank you for this vi

cv2.destroyAllWindows()  # destroys all the windows we created
cap.release()  # Closes video file or capturing device.
