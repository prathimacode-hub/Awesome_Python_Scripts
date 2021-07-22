import tkinter as tk
import numpy as np
import cv2
from PIL import Image, ImageTk
import face_recognition
from Utils import Blocking
from PIL import ImageTk as itk
from win32api import GetSystemMetrics
from gtts import gTTS
from io import BytesIO
import playsound
import os
import winsound

bg = "Images/bg.jpg"
bgmusic = 'Images/bluedanube.wav'

customizeOrNot = input("Press \'Y\' or \'y\' if you wish to customize background music and wallpaper \n")
if customizeOrNot.lower() == 'y':
    bg = "Images/"+input("Enter filename of wallpaper : ")
    bgmusic = "Images/"+input("Enter filename of music file (WAV only) : ")

name=input("Please Enter First Name Entered During Registration:  ")
#if name+"png" in 



length=""


try:
    img = face_recognition.load_image_file(f'Utils/faceRegister/{name}.png')
    #Blocking.blockinput()
except:
    print("Incorrect User Name")
    exit()
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
faceLoc = face_recognition.face_locations(img)[0]
encodeImg = face_recognition.face_encodings(img)[0]
cv2.rectangle(img,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)


def quit():
        root.destroy()
        
root=tk.Tk()
#root.config(background="#FFFFFF")


image=Image.open(bg)
image = image.resize((GetSystemMetrics(0), GetSystemMetrics(1)), Image.ANTIALIAS)
bg = itk.PhotoImage(image)
label1 = tk.Label(root, image = bg)
label1.place(x = 0, y = 0)


root.grid_columnconfigure(0, weight=1)
root.attributes('-fullscreen', True)
button = tk.Button(root, text = 'Quit', command=quit)
#button.grid(row=1,column=0,padx=10,pady=2)
imageFrame = tk.Frame(root, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

l = tk.Label(root, text = "Processing... Screen is now Locked. You can't Access Keyboard or Mouse")
l.config(font =("Courier", 14))
l.grid(row=2, column=0, padx=10, pady=2)

l2 = tk.Label(root, text = length)
l2.config(font =("Sitka Text", 30))
l2.config(bg = "#270057", fg='white')
l2.grid(row=3, column=0, padx=10, pady=30)

lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

final_answer=""
final_answer_list=[]
counter=0
counter2=0

flagNoone = 0
flagWrong = 0
flagCorrect = 0

def show_frame():
    Blocking.blockinput()
    _, imgTest = cap.read()
    imgTest = cv2.flip(imgTest, 1)
    imgTest = cv2.resize(imgTest, (0, 0), fx = 0.5, fy = 0.5)
    cv2image = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, detect)
        
def detect():
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

    try:
        #Blocking.blockinput()
        faceLocTest = face_recognition.face_locations(imgTest)[0]
        encodeTest = face_recognition.face_encodings(imgTest)[0]
        cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
        #results = face_recognition.compare_faces([encodeImg],encodeTest)
        faceDis = face_recognition.face_distance([encodeImg],encodeTest)
        #print(results,faceDis)
        cv2.putText(imgTest,f'{faceDis[0]}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        if faceDis[0]<=0.4:
            flagNoone = 0
            flagWrong = 0
            winsound.PlaySound(None, winsound.SND_FILENAME)
            #print(faceDis[0])
            #print(faceDis[0]<=0.4)
            final_answer=True
            final_answer_list.append(final_answer)
            counter2=counter2+1
            l2.config(text=f'{counter2} test passed ✔')
            
            if flagCorrect == 0:
                msg = "Stay Still. Minimum 8 Cases should pass"
                myobj = gTTS(text=msg, lang='en', slow = 'False')
                
                try:
                    os.remove('msg.mp4')
                except Exception as e:
                    print(e)
                
                myobj.save('msg.mp4')
                playsound.playsound('msg.mp4')
                os.remove('msg.mp4')
                flagCorrect = 1
        else:
            final_answer=False
            final_answer_list.append(final_answer)
            #counter2=0
            l2.config(text="❌Wrong Person❌")
            winsound.PlaySound(None, winsound.SND_FILENAME)
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
                flagWrong = 1
            
            
            
    except Exception as e:
        #Blocking.blockinput()
        
        l2.config(text="❖ No one is in front of the Screen. Screen is Locked ❖")
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
            winsound.PlaySound(bgmusic, winsound.SND_ALIAS | winsound.SND_ASYNC)
            flagNoone=1
        
        
    finally:
        #Blocking.blockinput()
        
        length = len(final_answer_list)
        
        #pass
        #cv2.imshow('Test',imgTest)
        #cv2.imshow('Original',img)
        #print(final_answer)
        print(final_answer_list)
        
        if len(final_answer_list)>10:
        
            for ele in final_answer_list:
                if ele==True:
                    counter=counter+1
            if counter/len(final_answer_list) >0.8:
                print("Accuracy",counter/len(final_answer_list))
                Blocking.unblockinput()
                quit()
            else:
                print(counter/len(final_answer_list))
                final_answer_list=[]
                counter=0
                counter2=0
          



show_frame()
root.mainloop()

