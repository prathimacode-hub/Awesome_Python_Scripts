import cv2
import numpy as np
import glob  # To access images
import pyautogui  # Taking screenshots
import os
import shutil # Delete Folders with contents
import tkinter #GUI
from tkinter import * 
import shortuuid #Unique File Name
from PIL import ImageTk, Image

# For Displaying Live Feed
cv2.namedWindow("Rec..", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Rec..", 480, 270)

## Constants, Please change according to your PC
DIRECTORY_NAME = "Images"
PARENT_DIR = "D:/React_apps/Privacy Virtual Cam/Screen Recorder - Copy"
PATH = os.path.join(PARENT_DIR,DIRECTORY_NAME)

# If Images folder present then remove it else say no errors
try:
    shutil.rmtree(PATH)
except Exception as e:
    print("No errors")
# Make Images Directory    
os.mkdir(PATH)
current_Image = None

# Counter for file names
i=0

#This variable acts as toggle to make application run or stop
running = False

#Functions to carry out toggle
def on_stop():
   global running
   running = False
def on_start():
   global running
   running = True

#Function that keeps running in tkinter mainloop
def program():
    
    # If running is true i.e. User has pressed Rec button the recording will take place else pause
    if running:
        global i, current_Image    
        #image = pyscreenshot.grab(backend="mss", childprocess=False)
        image=pyautogui.screenshot() # Taking Screenshot
        frame=np.array(image) # Making it suitable for cv2
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('Rec..', frame) # Display
        image.save(f"Images/Images{i}.jpg") # Save in Images folder that is created above
        
        # This is working but I've commented because it becomes drastically slow to display inside tkinter window
        #current_Image = ImageTk.PhotoImage(Image.open(f"Images/Images{i}.jpg").resize((100,100)))  #Image.fromarray
        #current_Image = ImageTk.PhotoImage(Image.fromarray(frame).resize((1366,768)))
        #recordLive.configure(image=current_Image)
        #print(current_Image)
        
        i=i+1
    wintk.after(1, program) # Loop
    #if cv2.waitKey(1) == ord('q'):
    #    break
        

    
wintk = tkinter.Tk()  # Make tkinter window
wintk.geometry('350x100')
wintk.title('Screen Recorder')
backimg = ImageTk.PhotoImage(Image.open("Image/backgrd.png").resize((347,97))) # Background metallic Image
backgrd = tkinter.Label(image=backimg)
backgrd.place(x=0,y=0)
#current_Image = ImageTk.PhotoImage(Image.open(r"Images0.jpg"))

# All button Created and Placed with respective images
recButton = ImageTk.PhotoImage(Image.open("Image/recButton.png").resize((50,50)))
start = Button(wintk, text="Record", command=on_start, image = recButton)
start.place(x=10,y=10)

pauseButton = ImageTk.PhotoImage(Image.open("Image/pause.png").resize((50,50)))
stop = Button(wintk, text="Pause", command=on_stop, image = pauseButton)
stop.place(x=150,y=10)

endButton = ImageTk.PhotoImage(Image.open("Image/end.png").resize((50,50)))
endProg = Button(wintk, text="End & Save", command=wintk.destroy, image = endButton)
endProg.place(x=290,y=10)

footer = tkinter.Label(wintk, text="Screen Recorder")
footer.place(x=130,y=80)

#recordLive = tkinter.Label(wintk,text="Tushar")#, image=current_Image)
#recordLive.place(x=200,y=200)


# To loop program function
wintk.after(1, program)
wintk.mainloop()

# Empty array to store images
img_array=[]
files = glob.glob('D:/React_apps/Privacy Virtual Cam/Screen Recorder - Copy/Images/*.jpg') # Accessing all jpg images in given path
files.sort(key=os.path.getmtime) # This is important to sort them according to date and time

# Reading all the files in cv2 format with dimentions and storing them in array
for filename in files:
    #print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
print("All Files Compiled Successfully")
    
filename = 'vid' + str(shortuuid.uuid()) + ".avi"     
# After getting all files traverse the array and stitch the images into one video 
out = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
# Delete Images Folder
shutil.rmtree(PATH)

