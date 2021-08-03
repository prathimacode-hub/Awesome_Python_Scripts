
# Adding Frames to Video

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
from moviepy.editor import *


# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Adding Frames to Video") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "ADD MORE FRAMES\nTO VIDEO", font=("Arial", 55,"underline"), fg="magenta") # same way bg
start1.place(x = 125, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =150 , y =580 )

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 90, y = 210)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =730 , y = 580 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Adding Frames to Video") # title given is "DICTIONARY"
window1.geometry('1000x700')

# function to select file
def open_video():
    global video_name
    video_name = filedialog.askopenfilename(title="Select Video")
    # print(filename)
    path_video.delete("1.0", "end")
    path_video.insert(END, video_name)

# function to select file
def open_images():
    global filename, image_names
    filename = filedialog.askopenfilenames(title="Select Images")
    # print(len(filename))
    path_images.delete("1.0", "end")
    image_names = ""
    for i in filename:
        # print(i)
        image_names = image_names + i + "\n"
    path_images.insert(END, image_names)

# function to add frames
def add_frames():
    global video_name, image_names, before_cnt, after_cnt, filename
    path_list = []
    before_cnt = 0
    after_cnt = 0

    # converting videos to images --------------------------------
    # Read the video from specified path
    cam = cv2.VideoCapture(video_name)
    # print(cam.get(cv2.CAP_PROP_FPS))
    # info1.config(text="Frame Rate  :  " + str(cam.get(cv2.CAP_PROP_FPS)))
    x = int(cam.get(cv2.CAP_PROP_FPS))
    try:
        # creating a folder named data
        if not os.path.exists('Video Images'):
            os.makedirs('Video Images')
    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')
    # frame
    currentframe = 0
    x2 = 0
    while (True):
        # reading from frame
        ret, frame = cam.read()
        if ret:
            if currentframe % x == 0:
                # if video is still left continue creating images
                x1 = int(currentframe / x)
                name = './Video Images/frame' + str(x1) + '.jpg'
                # print(x1, end = " ")
                before_cnt = before_cnt + 1
                path_list.append(name)
                #         print ('Creating...' + name)
                # writing the extracted images
                cv2.imwrite(name, frame)


            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    #     ret,frame = cam.read()
    # info2.config(text="No. of frame/Images  :  " + str(x2))
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()

    # print(len(path_list))
    # for i in path_list:
    #     print(i)

    for i in filename:
        path_list.append(i)

    after_cnt = len(filename) + before_cnt
    ic_list = []
    for i in range(after_cnt):
        ic_list.append(ImageClip(path_list[i]).set_duration(1))
    video = concatenate(ic_list, method="compose")
    video.write_videofile('slide_show.mp4', fps=24)
    mbox.showinfo("Success", "Frames added to selected video successfully!")

# function to show original video
def orig_video():
    global video_name

    sourceo = cv2.VideoCapture(video_name)
    # running the loop
    while True:
        # extracting the frames
        ret1, img1 = sourceo.read()
        # displaying the video
        cv2.imshow("Original Video", img1)
        # exiting the loop
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

# function to show new video
def new_video():
    global video_name

    sourcen = cv2.VideoCapture('slide_show.mp4')
    # running the loop
    while True:
        # extracting the frames
        ret1, img2 = sourcen.read()
        # displaying the video
        cv2.imshow("New Video with additional frames", img2)
        # exiting the loop
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

# function defined to get the frame count info
def frame_cnt():
    global before_cnt, after_cnt
    mbox.showinfo("Frame Count Info", "Frame Count before addition of new frame in video  :  " + str(before_cnt) + "\n\nFrame Count after addition of nre frame in video  :  " + str(after_cnt))


# top label
start1 = tk.Label(text = "ADD MORE FRAMES TO VIDEO", font=("Arial", 45, "underline"), fg="magenta") # same way bg
start1.place(x = 50, y = 10)

lbl2 = tk.Label(text="Select Video", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=100)

# Select Button
selectb=Button(window1, text="SELECT",command=open_video,  font=("Arial", 17), bg = "light green", fg = "blue")
selectb.place(x = 790, y = 100)

path_video = tk.Text(window1, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_video.place(x=80, y = 150)

lbl2 = tk.Label(text="Select Frames to add", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=220)

# Select Button
selectb=Button(window1, text="SELECT",command=open_images,  font=("Arial", 17), bg = "light green", fg = "blue")
selectb.place(x = 790, y = 220)

path_images = tk.Text(window1, height=4, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_images.place(x=80, y = 270)

# original Button
selectb=Button(window1, text="ORIGINAL VIDEO",command=orig_video,  font=("Arial", 25), bg = "orange", fg = "blue")
selectb.place(x = 80, y = 500)

# new Button
selectb=Button(window1, text="NEW VIDEO",command=new_video,  font=("Arial", 25), bg = "orange", fg = "blue")
selectb.place(x = 680, y = 500)

# add frames Button
selectb=Button(window1, text="ADD FRAMES",command=add_frames,  font=("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x = 100, y = 580)

# frame count Button
getb=Button(window1, text="FRAME CNT.",command=frame_cnt,  font=("Arial", 25), bg = "yellow", fg = "blue")
getb.place(x = 410, y = 540)

# function defined for exiting
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# Get Images Button
getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 740, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

