from tkinter import *
from speedtest import Speedtest

#Function for checking the speed
def update_text():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    speed_test.get_servers([])
    ping=speed_test.results.ping
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps")
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps")
    ping_label.config(text="Ping - " + str(ping) + "ms")

root = Tk()
#Title Of Application
root.title("Internet Speed Tracker")
#Dimension of application window
root.geometry('350x350')
root.resizable(0,0)
root.config(bg="cyan")
font1=("Times",14,"bold")
font2=("Times",12,"bold","italic")

#Added the logo to application
l=PhotoImage(file="Media/SpeedTest Logo.gif")
root.iconphoto(False,l)

#Functions for HoverButton
def on_enterbutton(r):
    button.config(background="light blue",foreground="black")

def on_leavebutton(r):
    button.config(background="SystemButtonFace",foreground="black")

button = Button(root, text="Get Speed", width=30,command=update_text)
button.pack(padx=20,pady=20)

button.bind('<Enter>',on_enterbutton)
button.bind('<Leave>',on_leavebutton)

labelA=Label(root,text="Click the button to check speed!!",bg="cyan",font=font2,padx=5,pady=5)
labelA.pack()
labelB=Label(root,text="Checking the speed takes time..Please wait..",bg="cyan",font=font2,padx=10,pady=10)
labelB.pack()
down_label = Label(root, text="",bg="cyan",padx=20,pady=20,font=font1)
down_label.pack()
up_label = Label(root, text="",bg="cyan",padx=20,pady=20,font=font1)
up_label.pack()
ping_label=Label(root,text="",bg="cyan",padx=20,pady=20,font=font1)
ping_label.pack()

root.mainloop()