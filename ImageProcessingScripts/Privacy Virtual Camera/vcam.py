import cv2
import pyvirtualcam  # For making virtual camera
from pyvirtualcam import PixelFormat
import numpy as np
import mediapipe as mp # Face Mesh

import multiprocessing # Enables python to run 2 processes at same time 
import time 
import speech_recognition as sr # Speech Recognizer
import cvzone as cv

## This function is used to take real time microphone input from user

def takesinput():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    #print(sr.Microphone.list_microphone_names())
    text=""
    with mic as source:

        while True:
            r.adjust_for_ambient_noise(source)  # To avoid taking background noise
            audio = r.listen(source)
            try:
                text=r.recognize_google(audio)
            except:
                pass
                
            #result.value=text
            print(text)  
            fh = open("Utils/words.txt","w+") # Saving Text in words text file (to be retrieved later)
            fh.write(text)
            print(fh.read(),"from takesinput")
            fh.close()
    

def program():
    print(1)
    mp_drawing = mp.solutions.drawing_utils  # For face mesh
    mp_face_mesh = mp.solutions.face_mesh
    face_cascade = cv2.CascadeClassifier(r'C:\Users\tusha\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    camera_no=0
    '''
    try:
        camera_no = int(input("Enter Camera Number : "))
    except:
        pass
    # Set up webcam capture.
    '''
    vcam = cv2.VideoCapture(camera_no) # Change camera no if camera doesn't detect

    if not vcam.isOpened():
        raise RuntimeError('Could not open video source')

    #Settings for virtual camera
    pref_width = 1280
    pref_height = 720
    pref_fps_in = 30
    vcam.set(cv2.CAP_PROP_FRAME_WIDTH, pref_width)
    vcam.set(cv2.CAP_PROP_FRAME_HEIGHT, pref_height)
    vcam.set(cv2.CAP_PROP_FPS, pref_fps_in)

    width = int(vcam.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_in = vcam.get(cv2.CAP_PROP_FPS)
    print(f'Webcam capture started ({width}x{height} @ {fps_in}fps)')  # Prints fps of vcam
    
    
    ###### CUSTOM CHANGES CAN BE MADE HERE #######
    images=['Images/mask1.png','Images/mask2.png','Images/mask3.png','Images/mask4.png']
    mask_img = cv2.imread(images[0],cv2.IMREAD_UNCHANGED) #### Change this Image to any Eye wear of your choice
    colorsavailable=[(255,255,255),(0,255,255),(0,0,255),(255,0,255),(0,0,255),(0,0,0),(100,20,100),(208, 253, 255)]
    chooseColor=colorsavailable[0]
    bgColor=colorsavailable[6]
    ##############################################
    

    fps_out = 20
    with pyvirtualcam.Camera(width, height, fps_out, fmt=PixelFormat.BGR, print_fps=fps_in) as cam:
        print(f'Virtual cam started: {cam.device} ({cam.width}x{cam.height} @ {cam.fps}fps)')
        while True:
            ret, frame = vcam.read()
            faces=face_cascade.detectMultiScale(frame, 1.2, 5, 0, (120, 120), (350, 350)) #Detecting face using face cascade
            if not ret:
                raise RuntimeError('Error fetching frame')

            # Send to virtual cam.
            img = np.zeros((480,640,3), dtype=np.uint8)
            img.fill(255)
            img = np.full((480, 640, 3), bgColor, np.uint8) # Making a plain canvas with specific solid color
            face_mesh = mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            min_detection_confidence=0.5)
            
            results = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) # Landmarks stored here
            drawing_spec = mp_drawing.DrawingSpec(color=chooseColor,thickness=1, circle_radius=0)
            if not results.multi_face_landmarks:
                continue
            for face_landmarks in results.multi_face_landmarks:
              #print('face_landmarks:', face_landmarks)
              mp_drawing.draw_landmarks(
                  image=img,
                  landmark_list=face_landmarks,
                  connections=mp_face_mesh.FACE_CONNECTIONS,
                  landmark_drawing_spec=drawing_spec,
                  connection_drawing_spec=drawing_spec)
              for ids,landmrk in enumerate(face_landmarks.landmark):
                #print(landmrk,ids)
                # 25 is for left eye and 339 is for right eye
                if ids == 25:
                    #cv2.putText(img, str(ids), (int(landmrk.x*640),int(landmrk.y*480)), cv2.FONT_HERSHEY_SIMPLEX,0.1, (255,0,255), 1, cv2.LINE_AA)
                    x1=landmrk.x*640
                    y1=landmrk.y*480
                if ids == 339:
                    x2=landmrk.x*640
                    y2=landmrk.y*480
            
            # getting size of canvas and mask image used
            hf,wf,cf=img.shape
            hb,wb,cb=mask_img.shape
            mask_img=cv2.resize(mask_img, (int(x2-x1)+100, int(y2-y1)+100),interpolation=cv2.INTER_AREA)
            
            #try and except used because it causes error when head is not detected
            
            try:
                img = cv.overlayPNG(img,mask_img,[int(x1)-40,int(y1)-70]) 
            except:
                pass
                    
               
            
            # Retrieve the detected text from takesinput process
            fh = open("Utils/words.txt","r")
            text=fh.read()
            fh.close()
            
            text = "Captions : " + text
            
            # Place it on canvas
            img = cv2.putText(img, str(text), (20,400), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,0,255), 1, cv2.LINE_AA)
            #cv2.imshow("image", img)
            cam.send(img)
            if cv2.waitKey(1) == ord('q'):
                break
        
        
        
        
        

        # Wait until it's time for the next frame.
        cam.sleep_until_next_frame()
# Running 2 processes using multiprocessing    
p1 = multiprocessing.Process(target=takesinput)
p2 = multiprocessing.Process(target=program)        
if __name__ == '__main__':
    
    p1.start() # Starting both process
    p2.start()