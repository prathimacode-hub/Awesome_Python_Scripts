#NOTE: The dataset reference was taken from https://github.com/YoniChechik/AI_is_Math
#CREATOR- https://github.com/theshredbox

#LOAD THE DATSET IMAGES
import sys
import subprocess
    subprocess.call("apt-get install subversion".split())
    subprocess.call("svn export https://github.com/YoniChechik/AI_is_Math/trunk/c_07_camera_calibration/images".split())

#IMPORT ALL THE EQUIRED PACKAGES


import numpy as np
import cv2
from glob import glob
import matplotlib.pyplot as plt

#GET IMAGES FROM THE SESSION STORAGE AND DEFINE THEIR SIZE

square_size = 2.88
img_mask = "./images/*.jpeg"
pattern_size = (9, 6)

figsize = (20, 20)
# DEFINE THE DIMENSIONS OF THE CHESSBOARD AND-

# 1.  Create vector to store vectors of 3D points for each chessboard image.
# 2.  Create vector to store vectors of 2D points for each chessboard image.

img_names = glob(img_mask)
num_images = len(img_names)

pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
pattern_points *= square_size

obj_points = []
img_points = []
h, w = cv2.imread(img_names[0]).shape[:2]

#LOAD THE IMAGES AND APPLY LOOP ON THE SET OF IMAGES
#IF A DESIRED NUMBER OF CORNERS ARE FOUND IN THE IMAGE, REFINE THE PIXEL COORDINATES FOR THOSE IMAGES AND DISPLAY THEM ON THE CHESSBOARD

plt.figure(figsize=figsize)

for i, fn in enumerate(img_names):
    print("loading images %s" % fn)
    imgBGR = cv2.imread(fn)

    if imgBGR is None:
        print("Failed to load", fn)
        continue

    imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(imgRGB, cv2.COLOR_RGB2GRAY)

    assert w == img.shape[1] and h == img.shape[0], f"size: {img.shape[1]} x {img.shape[0]}"
    found, corners = cv2.findChessboardCorners(img, pattern_size)


    if not found:
        print("chessboard not found")
        continue

    if i < 12:
        img_w_corners = cv2.drawChessboardCorners(imgRGB, pattern_size, corners, found)
        plt.subplot(4, 3, i + 1)
        plt.imshow(img_w_corners)

    print(f"{fn}... OK")
    img_points.append(corners.reshape(-1, 2))
    obj_points.append(pattern_points)


plt.show()

#CALCULATE THE CAMERA DISTORTION


rms, camera_matrix, dist_coefs, _rvecs, _tvecs = cv2.calibrateCamera(obj_points, img_points, (w, h), None, None)

print("\nRMS:", rms)
print("camera matrix:\n", camera_matrix)
print("distortion coefficients: ", dist_coefs.ravel())


#UNDISTORT THE IMAGE FROM THE CALCULATED CALIBERATION


plt.figure(figsize=figsize)
for i, fn in enumerate(img_names):

    imgBGR = cv2.imread(fn)
    imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

    dst = cv2.undistort(imgRGB, camera_matrix, dist_coefs)

    if i < 12:
        plt.subplot(4, 3, i + 1)
        plt.imshow(dst)

plt.show()
print("ABOVE ARE THE UNDISTORED IMAGES")


