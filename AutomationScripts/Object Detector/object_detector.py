# used to detect the object and draw the rectangle
import cv2

# used to take the image path as input from the terminal
import sys

# reads the two images from the paths specified in the terminal
obj_img = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
search_img = cv2.imread(sys.argv[2], cv2.IMREAD_COLOR)

# gets the width of the image with the object to detect
obj_w = obj_img.shape[1]
# gets the height of the image with the object to detect
obj_h = obj_img.shape[0]

# uses the matchTemplate() function of cv2 to find the object in the image
result = cv2.matchTemplate(obj_img, search_img, cv2.TM_CCOEFF)
# finds the positions and probability values of the areas with the highest
# and lowest probability of being the object that needs to be detected
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# top left corner of the rectangle drawn
top_left = max_loc
# bottom right corner of the rectangle drawn
bottom_right = (top_left[0] + obj_w, top_left[1] + obj_h)

# draws the rectangle where the object is
cv2.rectangle(
    search_img,
    top_left,
    bottom_right,
    color=(0, 255, 0),
    thickness=2,
    lineType=cv2.LINE_4,
)

# shows the image with the rectangle around the object
cv2.imshow("Result", search_img)
# keeps the window open till a key is pressed
cv2.waitKey()