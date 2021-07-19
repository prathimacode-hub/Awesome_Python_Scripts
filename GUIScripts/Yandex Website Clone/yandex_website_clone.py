
# Yandex Website Clone

# imported necessary libraries
from tkinter import *                                                   
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
from googlesearch import search

# -----------------------------------------------------------------------------------------------

class Keypad(tk.Frame):

    cells = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['!', '@', '#', '$', '%', '&', '*', '/', '\'', '.', ',', ';', ':', '?', '<', '>','😀','😋','😂','🌞','🌴','🍕','🏳', '♻', '✔', '👍'],
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.target = None
        self.memory = ''

        for y, row in enumerate(self.cells):
            for x, item in enumerate(row):
                b = tk.Button(self, text=item, command=lambda text=item:self.append(text),font=("Arial", 14), bg = "white", fg = "black", borderwidth=3, relief="raised")
                b.grid(row=y, column=x, sticky='news')

        x = tk.Button(self, text='Space', command=self.space,font=("Arial", 14), bg = "white", fg = "black", borderwidth=3, relief="raised")
        x.grid(row=0, column=10, columnspan='4', sticky='news')

        x = tk.Button(self, text='tab', command=self.tab,font=("Arial", 14), bg = "white", fg = "black", borderwidth=3, relief="raised")
        x.grid(row=0, column=14, columnspan='3', sticky='news')

        x = tk.Button(self, text='Backspace', command=self.backspace,font=("Arial", 14), bg = "white", fg = "black", borderwidth=3, relief="raised")
        x.grid(row=0, column=17,columnspan='3', sticky='news')

        x = tk.Button(self, text='Clear', command=self.clear,font=("Arial", 14), bg = "white", fg = "black", borderwidth=3, relief="raised")
        x.grid(row=0, column=20, columnspan='3',  sticky='news')

        x = tk.Button(self, text='Hide', command=self.hide,font=("Arial", 14), bg = "white", fg = "black", borderwidth=3, relief="raised")
        x.grid(row=0, column=23, columnspan='3', sticky='news')


    def get(self):
        if self.target:
            return self.target.get()

    def append(self, text):
        if self.target:
            self.target.insert('end', text)

    def clear(self):
        if self.target:
            self.target.delete(0, END)

    def backspace(self):
        if self.target:
            text = self.get()
            text = text[:-1]
            self.clear()
            self.append(text)

    def space(self):
        if self.target:
            text = self.get()
            text = text + " "
            self.clear()
            self.append(text)

    def tab(self): # 5 spaces
        if self.target:
            text = self.get()
            text = text + "     "
            self.clear()
            self.append(text)

    def copy(self):
        #TODO: copy to clipboad
        if self.target:
            self.memory = self.get()
            self.label['text'] = 'memory: ' + self.memory
            print(self.memory)

    def paste(self):
        #TODO: copy from clipboad
        if self.target:
            self.append(self.memory)

    def show(self, entry):
        self.target = entry

        self.place(relx=0.5, rely=0.65, anchor='c')

    def hide(self):
        self.target = None

        self.place_forget()

#-------------------------------------------------------

# created main window
root = tk.Tk()
root.title("Yandex Website Clone")
root.geometry("1200x700")
root.iconbitmap('Images/yandex_icon.ico')
root.configure(bg = "white")

# image on the main window
path = "Images/front.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(root, image = img1)
panel.place(x = 300, y = 170)

# image on the main window
path1 = "Images/yandex.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img2 = ImageTk.PhotoImage(Image.open(path1))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel1 = tk.Label(root, image = img2)
panel1.place(x = 150, y = 300)

# created a callback function to open linked web browser
def callback(url):
    webbrowser.open_new_tab(url)

# en link
g_word = Label(root,text="EN",cursor="hand2", bg = "white")
g_word.place(x=1050,y=10)
g_word.bind("<Button-1>",lambda e: callback("https://mail.google.com/mail/"))

# login link
g_word = Label(root,text="Log in",cursor="hand2", bg = "white")
g_word.place(x=1100,y=10)
g_word.bind("<Button-1>",lambda e: callback("https://mail.yandex.com/"))

# image link
g_word = Label(root,text="Images",cursor="hand2", bg = "white")
g_word.place(x=315,y=240)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.com/images/"))

# video link
g_word = Label(root,text="Video",cursor="hand2", bg = "white")
g_word.place(x=410,y=240)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.com/video/search?text=video"))

# mail link
g_word = Label(root,text="Mail",cursor="hand2", bg = "white")
g_word.place(x=507,y=240)
g_word.bind("<Button-1>",lambda e: callback("https://mail.yandex.com/"))

# maps link
g_word = Label(root,text="Maps",cursor="hand2", bg = "white")
g_word.place(x=600,y=240)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.com/maps/?ll=10.854186%2C49.182076&z=4"))

# translte link
g_word = Label(root,text="AppMetrica",cursor="hand2", bg = "white")
g_word.place(x=675,y=240)
g_word.bind("<Button-1>",lambda e: callback("https://appmetrica.yandex.com/about"))

# browser link
g_word = Label(root,text="Translate",cursor="hand2", bg = "white")
g_word.place(x=777,y=240)
g_word.bind("<Button-1>",lambda e: callback("https://translate.yandex.com/"))

# browser link
g_word = Label(root,text="Browser",cursor="hand2", bg = "white")
g_word.place(x=870,y=240)
g_word.bind("<Button-1>",lambda e: callback("https://browser.yandex.com/?from=morda_icon_yandex_com&banerid=3401000000"))

firstclick1 = True
def on_entry_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick1
    if firstclick1:  # if this is the first time they clicked it
        firstclick1 = False
        search_entry.delete(0, "end")  # delete all the text in the entry

# Search Entry Box
search_entry = Entry(root, font=("Arial", 25,"italic"), fg='black', bg="white", borderwidth=3, width=35)
search_entry.insert(0, 'Finds everything')
search_entry.bind('<FocusIn>', on_entry_click)
search_entry.place(x=300, y=302)

def search_fun():
    query = search_entry.get()
    s = search(query, tld="co.in", num=10, stop=1, pause=2)
    for j in s:
        print(webbrowser.open(j))

keypad = Keypad(root)

# created reset button
keypadb = Button(root, text="⌨",command=lambda:keypad.show(search_entry),font=("Arial", 15), bg = "orange", fg = "black", borderwidth=3, relief="raised",cursor="hand2")
keypadb.place(x =950 , y =303 )

# created reset button
searchb = Button(root, text="SEARCH",command=search_fun,font=("Arial", 15), bg = "orange", fg = "black", borderwidth=3, relief="raised",cursor="hand2")
searchb.place(x =1010 , y =303 )

# browser link
g_word = Label(root,text="Yandex in",font = ("Arial", 12,"bold"), bg = "white")
g_word.place(x=230,y=580)

# browser link
g_word = Label(root,text="Russia",font = ("Arial", 12),cursor="hand2", bg = "white")
g_word.place(x=350,y=580)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.ru/"))

# browser link
g_word = Label(root,text="Ukraine",font = ("Arial", 12),cursor="hand2", bg = "white")
g_word.place(x=440,y=580)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.ua/"))

# browser link
g_word = Label(root,text="Belarus",font = ("Arial", 12),cursor="hand2", bg = "white")
g_word.place(x=540,y=580)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.by/"))

# browser link
g_word = Label(root,text="Kazakhstan",font = ("Arial", 12),cursor="hand2", bg = "white")
g_word.place(x=640,y=580)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.kz/"))

# browser link
g_word = Label(root,text="Uzbekistan",font = ("Arial", 12),cursor="hand2", bg = "white")
g_word.place(x=760,y=580)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.uz/"))

# browser link
g_word = Label(root,text="Turkey",font = ("Arial", 12),cursor="hand2", bg = "white")
g_word.place(x=870,y=580)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.com.tr/"))

# browser link
g_word = Label(root,text="Technologies",font = ( 12),cursor="hand2", bg = "white")
g_word.place(x=150,y=650)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.com/dev/"))

# browser link
g_word = Label(root,text="About Yandex",font = ( 10),cursor="hand2", bg = "white")
g_word.place(x=270,y=650)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.com/company/"))

# browser link
g_word = Label(root,text="Terms of Service",font = ( 10),cursor="hand2", bg = "white")
g_word.place(x=400,y=650)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.com/legal/termsofservice/"))

# browser link
g_word = Label(root,text="Privacy Policy",font = ( 10),cursor="hand2", bg = "white")
g_word.place(x=550,y=650)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.com/legal/confidential/?lang=en"))

# browser link
g_word = Label(root,text="Contact Us",font = ( 10),cursor="hand2", bg = "white")
g_word.place(x=680,y=650)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.com/support/common/"))

# browser link
g_word = Label(root,text="Copyright Notice",font = ( 10),cursor="hand2", bg = "white")
g_word.place(x=790,y=650)
g_word.bind("<Button-1>",lambda e: callback("https://yandex.com/support/copyright-complaint/"))

# browser link
g_word = Label(root,text="© Yandex",font = ( 10), bg = "white")
g_word.place(x=950,y=650)

# # created a callback function to open linked web browser
# def callback(url):
#     webbrowser.open_new_tab(url)
#
# # function defined to search any things in this google search engine
# def search_query():
#     query = text.get("1.0","end-1c")
#     s = search(query, tld="co.in", num=10, stop=1, pause=2)
#     for j in s:
#         print(webbrowser.open(j))
#
#
#
# # label to create top blask strip
# l1 = Label(root,bg="black",width=500,height=2)
# l1.grid(sticky="w")
#
# # app logo added
# apps_logo = ImageTk.PhotoImage(Image.open('Images/apps.jpg'))
# apps_logo_lbl = Label(root, image = apps_logo,borderwidth=0)
# apps_logo_lbl.place(x=13,y=11)
# apps_lbl = Label(root,text="Apps",bg="black",fg="white",cursor="hand2")
# apps_lbl.place(x=30,y=10)
# apps_lbl.bind("<Button-1>",lambda e: callback("https://about.google/intl/en/products/"))
#
#
# # google drive drive logo added
# drive_logo = ImageTk.PhotoImage(Image.open('Images/Google drive.png'))
# drive_logo_lbl = Label(root, image = drive_logo,borderwidth=0)
# drive_logo_lbl.place(x=85,y=8)
# drive_lbl = Label(root,text="Google Drive",bg="black",fg="white",cursor="hand2")
# drive_lbl.place(x=110,y=10)
# drive_lbl.bind("<Button-1>",lambda e: callback("https://drive.google.com/drive/u/0/my-drive"))
#
#
# #youtube logo added
# yt_logo = ImageTk.PhotoImage(Image.open('Images/youtube.png'))
# yt_logo_lbl = Label(root, image = yt_logo,borderwidth=0)
# yt_logo_lbl.place(x=210,y=8)
# yt_lbl =  Label(root,text="YouTube",bg="black",fg="white",cursor="hand2")
# yt_lbl.place(x=240,y=10)
# yt_lbl.bind("<Button-1>",lambda e: callback("https://www.youtube.com/"))
#
#
# # gmail logo added
# gmail_logo = ImageTk.PhotoImage(Image.open('Images/gmail.jpg'))
# gmail_logo_lbl = Label(root, image = gmail_logo,borderwidth=0)
# gmail_logo_lbl.place(x=315,y=8)
# gmail_lbl =  Label(root,text="Gmail",bg="black",fg="white",cursor="hand2")
# gmail_lbl.place(x=340,y=10)
# gmail_lbl.bind("<Button-1>",lambda e: callback("https://mail.google.com/mail/"))
#
#
# # right gmail link
# g_word = Label(root,text="Gmail",cursor="hand2")
# g_word.place(x=810,y=55)
# g_word.bind("<Button-1>",lambda e: callback("https://mail.google.com/mail/"))
#
# # right images link
# i_word = Label(root,text="Images",cursor="hand2")
# i_word.place(x=850,y=55)
# i_word.bind("<Button-1>",lambda e: callback("https://www.google.co.in/imghp?hl=en&tab=wi&ogbl"))
#
# # created signin button
# signinb = Button(root,text="sign in",font=('roboto',10,'bold'),bg="#4583EC",fg="white",cursor="hand2")
# signinb.place(x=920,y=50)
# signinb.bind("<Button-1>",lambda e: callback("https://accounts.google.com/signin/v2/identifier?hl=en&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAlAmgQ&flowName=GlifWebSignIn&flowEntry=AddSession"))
#
#
# # google big logo added
# g_logo = ImageTk.PhotoImage(Image.open('Images/google logo.png'))
# l2 = Label(root, image = g_logo)
# l2.place(x=350,y=190)
#
#
# # search entry box added
# text = Text(root,width=90,height=2,relief=RIDGE,font=('roboto',10,'bold'),borderwidth=2)
# text.place(x=170,y=300)
#
# # search button added
# search1 = Button(root, text="Google Search",relief=RIDGE,font=('arial',10),bg="#F3F3F3",fg="#222222",cursor="hand2",command=search_query)
# search1.place(x=350,y=360)
#
#
# # Lucky Button added
# lucky = Button(root, text="i' m Felling Lucky",relief=RIDGE,font=('arial',10),bg="#F3F3F3",fg="#222222",cursor="hand2")
# lucky.place(x=500,y=360)
# lucky.bind("<Button-1>",lambda e: callback("https://www.google.com/doodles"))
#
#
# # different language offered label
# offered = Label(root,text="Google offered in:")
# offered.place(x=240,y=410)
# lang = Label(root,text="हिन्दी বাংলা తెలుగు मराठी தமிழ் ગુજરાતી ಕನ್ನಡ മലയാളം ਪੰਜਾਬੀ",fg="blue")
# lang.place(x=350,y=410)
#
# # About label
# about_lbl = Label(root,text="About",cursor="hand2")
# about_lbl.place(x=50,y=650)
# about_lbl.bind("<Button-1>",lambda e: callback("https://about.google/?utm_source=google-IN&utm_medium=referral&utm_campaign=hp-footer&fg=1"))
#
# # advertising label
# ad_lbl = Label(root,text="Advertising",cursor="hand2")
# ad_lbl.place(x=100,y=650)
# ad_lbl.bind("<Button-1>",lambda e: callback("https://ads.google.com/intl/en_in/home/?subid=ww-ww-et-g-awa-a-g_hpafoot1_1!o2&utm_source=google.com&utm_medium=referral&utm_campaign=google_hpafooter&fg=1"))
#
# # business label
# business_lbl = Label(root,text="Business",cursor="hand2")
# business_lbl.place(x=180,y=650)
# business_lbl.bind("<Button-1>",lambda e: callback("https://www.google.com/intl/en_in/business/"))
#
# # how search works label
# search_work_lbl = Label(root,text="How Search works",cursor="hand2")
# search_work_lbl.place(x=250,y=650)
# search_work_lbl.bind("<Button-1>",lambda e: callback("https://www.google.com/search/howsearchworks/?fg=1"))
#
# # privacy label
# privacy_lbl = Label(root,text="Privacy",cursor="hand2")
# privacy_lbl.place(x=850,y=650)
# privacy_lbl.bind("<Button-1>",lambda e: callback("https://policies.google.com/privacy?hl=en-IN&fg=1"))
#
# # terms label
# terms_lbl = Label(root,text="Terms",cursor="hand2")
# terms_lbl.place(x=900,y=650)
# terms_lbl.bind("<Button-1>",lambda e: callback("https://policies.google.com/terms?hl=en-IN&fg=1"))

root.mainloop()