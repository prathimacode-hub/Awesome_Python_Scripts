import tkinter as tk #Used to make GUI and fullscreen lock-screen
import numpy as np
import cv2
from PIL import Image, ImageTk
import face_recognition  #Library Used for Face Recognition
from Utils import Blocking #To Block Keyboard and Mouse Temporarily 
from PIL import ImageTk as itk
from win32api import GetSystemMetrics # To get resolution of monitor
from gtts import gTTS # Text to Speech
from io import BytesIO
import playsound # Play Sound
import os
import winsound # To play background music

bg = "Images/bg.jpg"
bgmusic = 'Images/bluedanube.wav'  # These two are default wallpaper and music

# Asking User whether they wish to use customization
customizeOrNot = input("Press \'Y\' or \'y\' if you wish to customize background music and wallpaper \n")
if customizeOrNot.lower() == 'y':
    bg = "Images/"+input("Enter filename of wallpaper : ")
    bgmusic = "Images/"+input("Enter filename of music file (WAV only) : ")


# This name variable is used to get original picture of user generated using faceRegister module
name=input("Please Enter First Name Entered During Registration:  ")

length=""


# We are using try and except block to make sure that if user enters wrong Name (One that doesn't exists in faceRegister Folder) program is terminated.
try:
    img = face_recognition.load_image_file(f'Utils/faceRegister/{name}.png')
    #Blocking.blockinput()
except:
    print("Incorrect User Name")
    exit()

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  # Loading Orignal Image in img variable
faceLoc = face_recognition.face_locations(img)[0]  # Using Face Recognition library to get face locations
encodeImg = face_recognition.face_encodings(img)[0] # We are then encoding it so that afterwards we can compare
cv2.rectangle(img,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2) # Just to display purple rectangle

# To terminate Tkinter GUI
def quit():
        root.destroy()
        
root=tk.Tk()  # Defining Window
#root.config(background="#FFFFFF")


image=Image.open(bg)  # Background Image
image = image.resize((GetSystemMetrics(0), GetSystemMetrics(1)), Image.ANTIALIAS)  # To get resolution of monitor for wallpaper
bg = itk.PhotoImage(image)
label1 = tk.Label(root, image = bg) # Make A tkinter Label and put the image into that label and place it on origin
label1.place(x = 0, y = 0)


root.grid_columnconfigure(0, weight=1)
root.attributes('-fullscreen', True)  # Make the window fullscreen
button = tk.Button(root, text = 'Quit', command=quit) # Button to close the window (Used during debugging)
#button.grid(row=1,column=0,padx=10,pady=2)
imageFrame = tk.Frame(root, width=600, height=500) # Make a frame to display webcam live capture
imageFrame.grid(row=0, column=0, padx=10, pady=2)  # Put it in topmost section with row no 0

# Just a label at below webcam
l = tk.Label(root, text = "Processing... Screen is now Locked. You can't Access Keyboard or Mouse")
l.config(font =("Courier", 14))
l.grid(row=2, column=0, padx=10, pady=2)

# This Label Show live Status of Whether face is detected or no one is in front of screen or wrong person
l2 = tk.Label(root, text = length)
l2.config(font =("Sitka Text", 30))
l2.config(bg = "#270057", fg='white')
l2.grid(row=3, column=0, padx=10, pady=30)

# For displaying video Capture
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

# These are few global variables that are change during execution 
final_answer="" # Correct or Incorrect Face
final_answer_list=[]  # This stores result of 10 iterations
counter=0 # Counter of no of Trues in above list
counter2=0 # To show number of Tests passed

# These flags are used for sole purpose of voice and background music. These flags make sure that we are not re running the music
flagNoone = 0  # Flag is on when no one is 
flagWrong = 0  # Flag is on when wrong person detected 
flagCorrect = 0 # Flag is on when correct person is detected

# This function is used to show live feed on tkinter window
def show_frame():
    Blocking.blockinput()  # Once reached this step block the keyboard and mouse
    _, imgTest = cap.read() # Just reading the frames from webcam
    imgTest = cv2.flip(imgTest, 1)
    imgTest = cv2.resize(imgTest, (0, 0), fx = 0.5, fy = 0.5)  # Resizing Image to 50%
    cv2image = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGBA) #To RGBA
    img = Image.fromarray(cv2image) # Using PIL to convert it into compatible image
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk # Putting image on the Label 
    lmain.configure(image=imgtk)
    lmain.after(10, detect) # Go to detect Function
     
# Function used to detect the face        
def detect():
    # All global variables
    
    global length, l2, final_answer,final_answer_list, counter, counter2, flagNoone, flagWrong, flagCorrect, bgmusic
    
    #Blocking.blockinput()

    _, imgTest = cap.read()
    imgTest = cv2.flip(imgTest, 1)
    imgTest = cv2.resize(imgTest, (0, 0), fx = 0.5, fy = 0.5)
    cv2image = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    
    # Try and Except to Check if user is in front of screen or not. If not then it will throw exception and we have to catch that
    try:
        #Blocking.blockinput()
        faceLocTest = face_recognition.face_locations(imgTest)[0]  # Getting face locations of webcam Image just like we did before for original Image
        encodeTest = face_recognition.face_encodings(imgTest)[0]  # Encoding it
        cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
        #results = face_recognition.compare_faces([encodeImg],encodeTest)
        faceDis = face_recognition.face_distance([encodeImg],encodeTest)  # This is used to calculate the distance between the original and webcam image
        #print(results,faceDis)
        cv2.putText(imgTest,f'{faceDis[0]}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        if faceDis[0]<=0.4:  # Here we are checking that if distance is less than 0.4 which can be also understood as whether the confidence level of Image being same is greater than 60 % or not (less distance more confidence)
            flagNoone = 0 # We are in Correct Image Detected so flag no one is 0
            flagWrong = 0 # We are in Correct Image Detected so flag wrong one is 0
            winsound.PlaySound(None, winsound.SND_FILENAME) # Don't Play any music (music is only played when no face is detected). We can just play None to mute it.
            #print(faceDis[0])
            #print(faceDis[0]<=0.4)
            final_answer=True # If confidence level is greater than 60% faces match and append the result in list
            final_answer_list.append(final_answer)
            counter2=counter2+1 # We are incrementing it to print value in below line
            l2.config(text=f'{counter2} test passed ✔') # Dynamically change status label on GUI 
            
            if flagCorrect == 0:
                msg = "Stay Still. Minimum 8 Cases should pass" # Message to be spoken by Gtts
                myobj = gTTS(text=msg, lang='en', slow = 'False')
                
                try:
                    os.remove('msg.mp4') # If for any reason this file exists remove it first and if it throws error simply print it
                except Exception as e:
                    print(e)
                
                myobj.save('msg.mp4') # Save audio file
                playsound.playsound('msg.mp4') # Play it
                os.remove('msg.mp4') # remove it
                flagCorrect = 1 # Now setting Flag correct as 1, if flag is not 1 then sound will keep on playing
        # What is confidence is less than 60%
        else:
            final_answer=False # Answer becomes false
            final_answer_list.append(final_answer) # append to global list
            #counter2=0
            l2.config(text="❌Wrong Person❌") # Dynamically change status label on GUI
            winsound.PlaySound(None, winsound.SND_FILENAME) # Same like before dont play music
            flagNoone = 0
            flagCorrect = 0
            
            if flagWrong == 0:
                msg = "Wrong Person Detected"
                myobj = gTTS(text=msg, lang='en', slow = 'False')
                
                try:
                    os.remove('msg.mp4')
                except Exception as e:
                    print(e)
                
                myobj.save('msg.mp4')
                playsound.playsound('msg.mp4')
                os.remove('msg.mp4')
                flagWrong = 1 # Above lines are same like before
            
            
    # Exception occurs when no one is in front of screen since we have no another image to compare        
    except Exception as e:
        #Blocking.blockinput()
        
        l2.config(text="❖ No one is in front of the Screen. Screen is Locked ❖")  # Dynamically change status label on GUI
        #counter2=0
        print(e)
        #msg = "Wrong Person Detected"
        #myobj = gTTS(text=msg, lang='en', slow = 'False')
        #myobj.save('msg.mp4')
        #playsound.playsound('msg.mp4')
        #os.remove('msg.mp4')
        
        flagWrong = 0
        flagCorrect = 0
        
        if flagNoone == 0:
            winsound.PlaySound(bgmusic, winsound.SND_ALIAS | winsound.SND_ASYNC) # Here we are playing music and passing bgmusic as parameter instead of none
            flagNoone=1
        
    # This block runs every time
    finally:
        #Blocking.blockinput()
        
        length = len(final_answer_list)
        
        #pass
        #cv2.imshow('Test',imgTest)
        #cv2.imshow('Original',img)
        #print(final_answer)
        print(final_answer_list)
        # When length of the global answer list becomes greater than 10 do this
        
        if len(final_answer_list)>10:
        
            for ele in final_answer_list: # Check no of Trues in list
                if ele==True:
                    counter=counter+1
            if counter/len(final_answer_list) >0.8: # If its greater than 80 % then Unblock the Keyboard and Mouse and Run Quit function
                print("Accuracy",counter/len(final_answer_list))
                Blocking.unblockinput() # Reenable inputs
                quit()
            else:
                # Else we will simply set counters back to 0 and loop again
                print(counter/len(final_answer_list))
                final_answer_list=[]
                counter=0
                counter2=0
          



show_frame()
root.mainloop() # To Run GUI

