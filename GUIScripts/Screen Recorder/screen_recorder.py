import pyautogui #imported pyautogy library
import cv2 #imported open cv library
import numpy as np #imported numpy library

resolution = (1920, 1080)#video resolution
codec = cv2.VideoWriter_fourcc(*"XVID")#video codec
filename = "Recording.avi"#name of Output file
fps = 60.0#frame rate
out = cv2.VideoWriter(filename, codec, fps, resolution)#VideoWriter object created
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)#Empty window
cv2.resizeWindow("Live", 480, 270)#window resize

while True:

    img = pyautogui.screenshot()# Takes screenshot
    frame = np.array(img)# Convert the screenshot to a numpy array
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)# Convert it from BGR(Blue, Green, Red) to RGB(Red, Green, Blue)
    out.write(frame)#output file    
    cv2.imshow('Live', frame)#Display the recording content on screen
    if cv2.waitKey(1) == ord('q'): #click q to Stop recording
        break

out.release()# Release the Video writer

cv2.destroyAllWindows()# Destroy all windows
