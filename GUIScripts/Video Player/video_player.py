
# Video Player

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import numpy as np
from moviepy.editor import VideoFileClip


# class videoGUI for playing video
class videoGUI:
    # init function defined
    def __init__(self, window):

        self.files = iter(np.arange(1, 10000))
        self.pause1 = 0
        self.downloaded = IntVar()

        self.window = window
        # self.window.title(window_title)

        top_frame = Frame(self.window)
        top_frame.pack(side=TOP, pady=10)

        bottom_frame = Frame(self.window,width=1000, height=100)
        bottom_frame.pack(side=BOTTOM, pady = 10)

        self.lbl1 = tk.Label(self.window, text="File Path : ",font=("Arial",27), fg="brown")  # same way bg
        self.lbl1.place(x=80, y=560)

        # name Entry Box
        self.entry1 = Entry(self.window, font=("Arial", 30), fg='orange', bg="light yellow", borderwidth=3, width=30)
        self.entry1.place(x=265, y=555)

        # for progress bar -----------------
        self.st1 = tk.Label(self.window, font=("Arial", 15), fg="brown")  # same way bg
        self.st1.place(x=70, y=407)

        self.ed1 = tk.Label(self.window, font=("Arial", 15), fg="brown")  # same way bg
        self.ed1.place(x=850, y=407)

        self.progress = ttk.Progressbar(self.window, length=700, orient='horizontal', maximum=5000,variable=self.downloaded, mode='determinate')
        self.progress.place(x=140, y=410)
        # ------------------------------------

        self.lbl1 = tk.Label(self.window, text="Selected Video Will\nAppear & Start Playing Here...", font=("Arial", 30),fg="green")  # same way bg
        self.lbl1.place(x=250, y=440)

        self.pause = False   # Parameter that controls pause button

        self.canvas = Canvas(top_frame)
        self.canvas.pack()

        # Select Button
        self.btn_select=Button(bottom_frame, text="SELECT",width=12, command=self.open_file,  font=("Arial", 20), bg = "light green", fg = "blue")
        self.btn_select.grid(row=0, column=0)

        # Play Button
        self.btn_play=Button(bottom_frame, text="PLAY", width=12, command=self.play_video, font=("Arial", 20), bg = "orange", fg = "blue")
        self.btn_play.grid(row=0, column=1)

        # Pause Button
        self.btn_pause=Button(bottom_frame, text="PAUSE", width=12, command=self.pause_video,font=("Arial", 20), bg = "orange", fg = "blue")
        self.btn_pause.grid(row=0, column=2)

        # Resume Button
        self.btn_resume=Button(bottom_frame, text="RESUME", width=12, command=self.resume_video, font=("Arial", 20), bg = "yellow", fg = "blue")
        self.btn_resume.grid(row=0, column=3)

        self.delay = 15   # ms

        self.window.mainloop()

    # function defined to open the file
    def open_file(self):

        self.pause = False

        self.filename = filedialog.askopenfilename(title="Select file")
        self.clip = VideoFileClip(self.filename)
        self.st1.configure(text="00.00s")
        self.ed1.configure(text=str(self.clip.duration) + "s")
        # print(self.filename)
        self.entry1.delete(0, END)
        self.entry1.insert(0,self.filename)

        # Open the video file
        self.cap = cv2.VideoCapture(self.filename)

        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.canvas.config(width = self.width, height = self.height)
        mbox.showinfo("Status","File Selected successfully, click on PLAY button to play video.")
        self.loading()

    def loading(self):
        global pause
        if not self.pause:
            try:
                self.downloaded.set(next(self.files))  # update the progress bar
                self.window.after(1, self.loading)  # call this function again in 1 millisecond
            except StopIteration:
                mbox.showinfo("Status", "Play Back completed.")
                # the files iterator is exhausted
                # root.destroy()


    # function defined to get the frame
    def get_frame(self):   # get only one frame

        # try:

            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # except:
        #     messagebox.showerror(title='Video file not found', message='Please select a video file.')


    # function defined to play video
    def play_video(self):

        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

        if not self.pause:
            self.window.after(self.delay, self.play_video)
            # self.cnt = self.cnt + 0.01
            # self.st1.configure(text=str(self.cnt))


    # function defined to pause video
    def pause_video(self):
        self.pause = True
        mbox.showinfo("Status","Video Paused, click on RESUME button to resume playing.")

    # function defined to resume playing video
    def resume_video(self):
        self.pause=False
        self.play_video()
        self.loading()

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()


# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Video Player") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "VIDEO  PLAYER", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 240, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =180 , y =600 )

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 120, y = 90)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =700 , y =600 )
window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()

# Main Window & Configuration
window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Video Player") # title given is "DICTIONARY"
window1.geometry('1000x700')

def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()
window1.protocol("WM_DELETE_WINDOW", exit_win1)

videoGUI(window1)