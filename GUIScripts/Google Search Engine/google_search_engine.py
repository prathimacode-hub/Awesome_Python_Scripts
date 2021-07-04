
# Google Search Engine

# imported necessary libraries
from tkinter import *                                                   
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
from googlesearch import search


# created main window
root = tk.Tk()
root.title("Google Search Engine")
root.geometry("1000x700")
root.iconbitmap('Images/google_icon.ico')

# created a callback function to open linked web browser
def callback(url):
    webbrowser.open_new_tab(url)

# function defined to search any things in this google search engine
def search_query():
    query = text.get("1.0","end-1c")
    s = search(query, tld="co.in", num=10, stop=1, pause=2)
    for j in s:
        print(webbrowser.open(j))



# label to create top blask strip
l1 = Label(root,bg="black",width=500,height=2)
l1.grid(sticky="w")

# app logo added
apps_logo = ImageTk.PhotoImage(Image.open('Images/apps.jpg'))
apps_logo_lbl = Label(root, image = apps_logo,borderwidth=0)
apps_logo_lbl.place(x=13,y=11)
apps_lbl = Label(root,text="Apps",bg="black",fg="white",cursor="hand2")
apps_lbl.place(x=30,y=10)
apps_lbl.bind("<Button-1>",lambda e: callback("https://about.google/intl/en/products/"))


# google drive drive logo added
drive_logo = ImageTk.PhotoImage(Image.open('Images/Google drive.png'))
drive_logo_lbl = Label(root, image = drive_logo,borderwidth=0)
drive_logo_lbl.place(x=85,y=8)
drive_lbl = Label(root,text="Google Drive",bg="black",fg="white",cursor="hand2")
drive_lbl.place(x=110,y=10)
drive_lbl.bind("<Button-1>",lambda e: callback("https://drive.google.com/drive/u/0/my-drive"))


#youtube logo added
yt_logo = ImageTk.PhotoImage(Image.open('Images/youtube.png'))
yt_logo_lbl = Label(root, image = yt_logo,borderwidth=0)
yt_logo_lbl.place(x=210,y=8)
yt_lbl =  Label(root,text="YouTube",bg="black",fg="white",cursor="hand2")
yt_lbl.place(x=240,y=10)
yt_lbl.bind("<Button-1>",lambda e: callback("https://www.youtube.com/"))


# gmail logo added
gmail_logo = ImageTk.PhotoImage(Image.open('Images/gmail.jpg'))
gmail_logo_lbl = Label(root, image = gmail_logo,borderwidth=0)
gmail_logo_lbl.place(x=315,y=8)
gmail_lbl =  Label(root,text="Gmail",bg="black",fg="white",cursor="hand2")
gmail_lbl.place(x=340,y=10)
gmail_lbl.bind("<Button-1>",lambda e: callback("https://mail.google.com/mail/"))


# right gmail link
g_word = Label(root,text="Gmail",cursor="hand2")
g_word.place(x=810,y=55)
g_word.bind("<Button-1>",lambda e: callback("https://mail.google.com/mail/"))

# right images link
i_word = Label(root,text="Images",cursor="hand2")
i_word.place(x=850,y=55)
i_word.bind("<Button-1>",lambda e: callback("https://www.google.co.in/imghp?hl=en&tab=wi&ogbl"))

# created signin button
signinb = Button(root,text="sign in",font=('roboto',10,'bold'),bg="#4583EC",fg="white",cursor="hand2")
signinb.place(x=920,y=50)
signinb.bind("<Button-1>",lambda e: callback("https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAlAmgQ&flowName=GlifWebSignIn&flowEntry=AddSession"))


# google big logo added
g_logo = ImageTk.PhotoImage(Image.open('Images/google logo.png'))
l2 = Label(root, image = g_logo)
l2.place(x=350,y=190)


# search entry box added
text = Text(root,width=90,height=2,relief=RIDGE,font=('roboto',10,'bold'),borderwidth=2)
text.place(x=170,y=300)

# search button added
search1 = Button(root, text="Google Search",relief=RIDGE,font=('arial',10),bg="#F3F3F3",fg="#222222",cursor="hand2",command=search_query)
search1.place(x=350,y=360)


# Lucky Button added
lucky = Button(root, text="i' m Felling Lucky",relief=RIDGE,font=('arial',10),bg="#F3F3F3",fg="#222222",cursor="hand2")
lucky.place(x=500,y=360)
lucky.bind("<Button-1>",lambda e: callback("https://www.google.com/doodles"))


# different language offered label
offered = Label(root,text="Google offered in:")
offered.place(x=240,y=410)
lang = Label(root,text="हिन्दी বাংলা తెలుగు मराठी தமிழ் ગુજરાતી ಕನ್ನಡ മലയാളം ਪੰਜਾਬੀ",fg="blue")
lang.place(x=350,y=410)

# About label
about_lbl = Label(root,text="About",cursor="hand2")
about_lbl.place(x=50,y=650)
about_lbl.bind("<Button-1>",lambda e: callback("https://about.google/?utm_source=google-IN&utm_medium=referral&utm_campaign=hp-footer&fg=1"))

# advertising label
ad_lbl = Label(root,text="Advertising",cursor="hand2")
ad_lbl.place(x=100,y=650)
ad_lbl.bind("<Button-1>",lambda e: callback("https://ads.google.com/intl/en_in/home/?subid=ww-ww-et-g-awa-a-g_hpafoot1_1!o2&utm_source=google.com&utm_medium=referral&utm_campaign=google_hpafooter&fg=1"))

# business label
business_lbl = Label(root,text="Business",cursor="hand2")
business_lbl.place(x=180,y=650)
business_lbl.bind("<Button-1>",lambda e: callback("https://www.google.com/intl/en_in/business/"))

# how search works label
search_work_lbl = Label(root,text="How Search works",cursor="hand2")
search_work_lbl.place(x=250,y=650)
search_work_lbl.bind("<Button-1>",lambda e: callback("https://www.google.com/search/howsearchworks/?fg=1"))

# privacy label
privacy_lbl = Label(root,text="Privacy",cursor="hand2")
privacy_lbl.place(x=850,y=650)
privacy_lbl.bind("<Button-1>",lambda e: callback("https://policies.google.com/privacy?hl=en-IN&fg=1"))

# terms label
terms_lbl = Label(root,text="Terms",cursor="hand2")
terms_lbl.place(x=900,y=650)
terms_lbl.bind("<Button-1>",lambda e: callback("https://policies.google.com/terms?hl=en-IN&fg=1"))

root.mainloop()