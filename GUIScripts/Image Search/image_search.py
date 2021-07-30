
# Image Search

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import filedialog
from PIL import ImageTk, Image
import json
import requests
import webbrowser


# Main Window
frame = Tk()
frame.title('Image Search')
frame.geometry('1000x700')
# frame.configure(bg = "white")


# image on the main window
path = "Images/front.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(frame, image = img1)
panel.place(x = 200, y = 110)

# starting label
start1 = Label(frame, text='IMAGE SEARCH', font=("Arial", 55,"underline"),fg="magenta")
start1.place(x=200,y=10)

def start_fun():
    frame.destroy()

# creating an exit button
prevB = Button(frame, text='START', command=start_fun, font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 100, y = 580)

# defined exit_win function, to show a exit dialog box when tried to exit
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        frame.destroy()

# creating an exit button
prevB = Button(frame, text='EXIT', command=exit_win, font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
prevB.place(x = 750, y = 580)

# this is done to show the exit dialog box when tried to exit from the main window, using the top-roght close button of titlebar
frame.protocol("WM_DELETE_WINDOW", exit_win)
frame.mainloop()

#created main window
window = Tk()
window.geometry("1000x700")
window.title("Image Search")

# defined variable
global count, emig
# global bright, con
# global frp, tname  # list of paths
frp = []
tname = []
con = 1
bright = 0
panelA = None

# function defined to get the path of the image selected
def getpath(path):
    a = path.split(r'/')
    # print(a)
    fname = a[-1]
    l = len(fname)
    location = path[:-l]
    return location

# function defined to get the folder name from which image is selected
def getfoldername(path):
    a = path.split(r'/')
    # print(a)
    name = a[-1]
    return name

# function defined to get the file name of image is selected
def getfilename(path):
    a = path.split(r'/')
    fname = a[-1]
    a = fname.split('.')
    a = a[0]
    return a

# function defined to open the image file
def openfilename():
    filename = filedialog.askopenfilename(title='"pen')
    return filename

# function defined to open the selected image
def open_img():
    global x, panelA
    global count, eimg, location, filename
    count = 0
    x = openfilename()
    img = Image.open(x)
    eimg = img
    img = ImageTk.PhotoImage(img)
    temp = x
    location = getpath(temp)
    filename = getfilename(temp)
    # print(x)
    if panelA is None:
        panelA = Label(image=img)
        panelA.image = img
        panelA.pack(side="left", padx=50, pady=10)
    else:
        panelA.configure(image=img)
        panelA.image = img

# Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

# function defined to search an image
def search_fun():
    global x
    searchUrl = 'https://yandex.com/images/search'
    files = {'upfile': ('blob', open(x, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json',
              'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url = searchUrl + '?' + query_string
    # print(img_search_url)
    path_text.delete("1.0", "end")
    path_text.insert(END, img_search_url)
    callback(img_search_url)


# top label
start1 = tk.Label(text = "IMAGE SEARCH", font=("Arial", 50, "underline"), fg="magenta") # same way bg
start1.place(x = 200, y = 10)

# original image label
start1 = tk.Label(text = "Selected Image\nwill preview here...", font=("Arial", 40), fg="magenta") # same way bg
start1.place(x =80, y = 250)

# choose button created
chooseb = Button(window, text="SELECT",command=open_img,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
chooseb.place(x =745 , y =150 )

# Encrypt button created
enb = Button(window, text="SEARCH",command=search_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
enb.place(x =740 , y =300 )

# original image label
start1 = tk.Label(text = "URL Generated", font=("Arial", 30), fg="green") # same way bg
start1.place(x =80, y = 560)

path_text = tk.Text(window, height=1, width=37, font=("Arial", 30), bg="light yellow", fg="orange",borderwidth=2, relief="solid")
path_text.place(x=80, y = 610)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =772 , y =450 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()