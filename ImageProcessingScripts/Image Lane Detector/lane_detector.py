#Importing the library
import matplotlib.pylab as plt
import cv2
import numpy as np

#Function to find region of interest
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

#Function to draw the line on output image
def draw_the_lines(img, lines):
    img_copy = np.copy(img)
    blank_image = np.zeros((img_copy.shape[0], img_copy.shape[1], 3), np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

#Fetching the image and printing the shape
image = cv2.imread('image/road.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

#setting the region of interest
region_of_interest_vertices = [
    (50, height),
    (width/2.2, height/3),
    (width-240, height)
]

gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#adjusting the threshold value
canny_image = cv2.Canny(gray_image, 20, 100)
cropped_image = region_of_interest(canny_image,
                np.array([region_of_interest_vertices], np.int32),)

lines = cv2.HoughLinesP(cropped_image,
                        rho=2,
                        theta=np.pi/260,
                        threshold=100,
                        lines=np.array([]),
                        minLineLength=100,
                        maxLineGap=50)
image_with_lines = draw_the_lines(image, lines)

plt.imshow(image_with_lines)
plt.show()

cv2.imwrite("Detected_Lane.jpg",image_with_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()

