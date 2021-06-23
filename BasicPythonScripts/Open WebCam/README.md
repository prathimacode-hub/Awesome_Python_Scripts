## Description:
- My project works on Opening a WebCam.
- To create a python script which is open webcam we will need to import a **cv2** module.
- OpenCV is a vast library that helps in providing various functions for image and video operations.
- So, the process is something like that the user will run the program and it will open the web cam and after clicking on a button it will shutdown the program.

## Procedure: 
```python
import cv2
```
- First after importing modules.
- Use cv2.VideoCapture() to get a video capture object for the camera.
- Set up an infinite while loop and use the read() method to read the frames using the above created object.
- Use cv2.imshow() method to show the frames in the video.
- Breaks the loop when the user clicks a specific key.
## Sample Output:
![LGM](https://github.com/AmitGupta700/Awesome_Python_Scripts/blob/main/BasicPythonScripts/Open%20WebCam/Images/output.png)

## For any query please contact:
<a href="https://www.linkedin.com/in/amit-gupta-681206191/">LinkedIn</a>
