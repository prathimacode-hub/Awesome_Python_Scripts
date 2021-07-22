
# Video Property Fetcher

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from videoprops import get_video_properties
from videoprops import get_audio_properties
from moviepy.editor import VideoFileClip


# Main Window & Configuration
window = tk.Tk() # created a tkinter gui window frame
window.title("Video Property Fetcher") # title given is "DICTIONARY"
window.geometry('1000x700')

# top label
start1 = tk.Label(text = "VIDEO PROPERTY FETCHER", font=("Arial", 50,"underline"), fg="magenta") # same way bg
start1.place(x = 30, y = 10)

def start_fun():
    window.destroy()

# start button created
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =130 , y =580 )

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 80, y = 150)

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
window1.title("Video Property Fetcher")
window1.geometry('1000x700')

# function to open file
def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select file")
    # print(filename)
    path_text.delete("1.0", "end")
    path_text.insert(END, filename)

# function to get video properties
def video_fun():
    global filename
    props = get_video_properties(filename)
    clip = VideoFileClip(filename)
    mbox.showinfo("Video Properties", "Video Properties :\n\n1.)  Codec  :  " + str(props['codec_name']) + "\n\n2.)  Resolution  :  " + str(str(props['width']) + " x " + str(props['height'])) + "\n\n3.)  Aspect ratio  :  " + str(props['display_aspect_ratio']) + "\n\n4.)  Frame rate  :  " + str(props['avg_frame_rate']) + "\n\n5.)  Duration  :  " + str(clip.duration) + " sec")

# function to get audio properties
def audio_fun():
    global filename
    props1 = get_audio_properties(filename)
    mbox.showinfo("Audio Properties", "Audio Properties :\n\n1.)  Codec  :  " + str(props1['codec_name']) + "\n\n2.)  Channels  :  " + str(props1['channels']) + "\n\n3.)  Sample rate  :  " + str(props1['sample_rate']))


# top label
start1 = tk.Label(text = "VIDEO PROPERTY FETCHER", font=("Arial", 50, "underline"), fg="magenta") # same way bg
start1.place(x = 30, y = 10)

lbl1 = tk.Label(text="Select any video &\nget video & audio properties...", font=("Arial", 40),fg="green")  # same way bg
lbl1.place(x=140, y=120)

lbl2 = tk.Label(text="Selected Video", font=("Arial", 30),fg="brown")  # same way bg
lbl2.place(x=80, y=280)

path_text = tk.Text(window1, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text.place(x=80, y = 330)

# Select Button
selectb=Button(window1, text="SELECT",command=open_file,  font=("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x = 120, y = 580)

# video property Button
getb=Button(window1, text="VIDEO PROPERTY",command=video_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
getb.place(x = 80, y = 450)

# audio property Button
getb=Button(window1, text="AUDIO PROPERTY",command=audio_fun,  font=("Arial", 25), bg = "orange", fg = "blue")
getb.place(x = 580, y = 450)

# function for exiting
def exit_win1():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window1.destroy()

# Get Images Button
getb=Button(window1, text="EXIT",command=exit_win1,  font=("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 750, y = 580)

window1.protocol("WM_DELETE_WINDOW", exit_win1)
window1.mainloop()

