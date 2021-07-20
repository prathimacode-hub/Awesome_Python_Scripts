# importing required libraries after installing
from tkinter import *
from pytube import YouTube

# creating tkinter object
root = Tk()
# setting dimensions for the GUI application
root.geometry('500x300')
# application cannot be resized
root.resizable(0, 0)
# setting background color to the application
root.configure(bg='yellow')
# setting title of the application
root.title("Youtube Video Downloader")
Label(root, text='Youtube Video Downloader',
      font='arial 20 bold', bg='yellow').pack()

# placeholder to enter link of the youtube video to be downloaded
link = StringVar()
Label(root, text='Paste Link Here:', font='arial 15 bold',
      bg='yellow').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(
    x=32, y=90, height=30)


# function to download video
def Downloader():
    # url of the video
    url = YouTube(str(link.get()))
    video = url.streams.first()
    # download function
    video.download()
    # message to be displayed as "DOWNLOADED" after downloading the video
    Label(root, text='DOWNLOADED', font='arial 15 bold',
          bg='red', fg='white').place(x=180, y=210)


# Download button
Button(root, text='DOWNLOAD', font='arial 15 bold', bg='black', fg='white',
       padx=2, command=Downloader).place(x=180, y=150)

# Running infinite loop of the tkinter object until the user exits the application
root.mainloop()
