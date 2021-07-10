
# IP Address Extractor-Validator

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from PIL import Image, ImageTk
import re
import sys



# created main window
window = Tk()
window.geometry("1000x700")
window.title("IP Address Extractor-Validator")



# extracting IP Addresses
def go_extract():
    # created extract window
    window_extract = Tk()
    window_extract.geometry("1000x700")
    window_extract.title("Extract IP Address")

    # function to ectract ip address
    def extract_IP_address():
        input_text = str(text_enter.get("1.0", "end-1c"))

        # declaring the regex pattern for IP addresses
        ipPattern = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        findIP = re.findall(ipPattern, input_text)

        s = ""
        for i in findIP:
            s = s + i
            s = s + "\n"

        if len(findIP)>0:
            mbox.showinfo("Extracted IP Address", "Total Count  :  " + str(len(findIP)) + "\n\nExtracted IP Address :\n" + s)
        else:
            mbox.showinfo("Extracted IP Address", "No IP Address Extracted.")


    # top label
    start1 = tk.Label(window_extract,text="EXTRACT IP ADDRESS", font=("Arial", 50), fg="magenta")  # same way bg
    start1.place(x=120, y=10)

    # top second label
    enter_label = Label(window_extract, text="Enter Your text and Extract IP Address...", font=("Arial", 30), fg="brown")
    enter_label.place(x=130, y=100)

    # created text area
    text_enter = tk.Text(window_extract, height=18, width=80, font=("Arial", 15), bg="light yellow", fg="brown", borderwidth=3,relief="solid")
    text_enter.place(x=50, y=150)

    # created extract button
    extractb = Button(window_extract, text="EXTRACT", command=extract_IP_address, font=("Arial", 25), bg="light green",fg="blue", borderwidth=3, relief="raised")
    extractb.place(x=150, y=600)

    # function for clearing text area
    def clear_text():
        text_enter.delete("1.0","end")

    # created clear button
    clearb = Button(window_extract, text="CLEAR", command=clear_text, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
    clearb.place(x=650, y=600)


def go_validate():
    # created validate window
    window_validate = Tk()
    window_validate.geometry("1000x700")
    window_validate.title("Validate IP Address")

    def check(ip):
        if '.' in ip:
            # ipv4
            ip = ip.split('.')
            if len(ip) != 4:
                return False
            for n in ip:
                try:
                    n = int(n)
                except:
                    return False
                else:
                    if n > 255 or n < 0:
                        return False
            return 4
        elif ':' in ip:
            # ipv4
            ip = ip.split(':')
            if len(ip) != 8:
                return False
            for n in ip:
                for c in n:
                    if (c not in map(str, range(10)) and
                            c not in map(lambda x: chr(x), range(ord('a'), ord('f') + 1))):
                        return False
            return 6
        else:
            return False

    # function for checking validity of IP address
    def validate_IP_address():
        ip = str(ip_entry.get())
        res = check(ip)
        if res == False:
            mbox.showinfo("Validity Details", "The entered IP Address\n[ " + ip + " ] is NOT VALID.")
        elif res == 4:
            mbox.showinfo("Validity Details", "The entered IP Address\n[ " + ip + " ] is VALID\n\nAnd type is IPv4.")
        elif res == 6:
            mbox.showinfo("Validity Details", "The entered IP Address\n[ " + ip + " ] is VALID\n\nAnd type is IPv6.")
        else:
            mbox.showinfo("Validity Details", "The entered IP Address\n[ " + ip + " ] is VALID\n\nAnd type is UFO.")

    # top label
    start1 = tk.Label(window_validate,text="Validate IP Address", font=("Arial", 50), fg="magenta")  # same way bg
    start1.place(x=200, y=10)

    # top second label
    enter_label = Label(window_validate, text="Enter Your IP Address and see validity...", font=("Arial", 30),fg="brown")
    enter_label.place(x=130, y=150)

    # label for IP Address
    ip_lbl = tk.Label(window_validate,text="IP Address :  ", font=("Arial", 30), fg="brown")  # same way bg
    ip_lbl.place(x=100, y=300)

    # Entry Box
    ip_entry = Entry(window_validate, font=("Arial", 25), fg='brown', bg="light yellow", borderwidth=3, width=30)
    ip_entry.place(x=330, y=300)

    # created extract domain button
    validateb = Button(window_validate, text="VALIDATE", command=validate_IP_address, font=("Arial", 25),bg="light green", fg="blue", borderwidth=3, relief="raised")
    validateb.place(x=150, y=500)

    # function for clearing the entry
    def clear_entry():
        ip_entry.delete(0,END)

    # created clear button
    clearb = Button(window_validate, text="CLEAR", command=clear_entry, font=("Arial", 25), bg="orange", fg="blue",borderwidth=3, relief="raised")
    clearb.place(x=650, y=500)

# function for start button
def start_fun():
    # new frame defined
    f1 = Frame(window, width=1000, height=700)
    f1.propagate(0)
    f1.pack(side='top')

    # for adding images
    c1 = Canvas(f1, width=1000, height=700, bg="white")  # blue
    c1.pack()
    p1 = PhotoImage(file="Images/one.gif")
    c1.create_image(0, -10, image=p1, anchor="nw")
    w1 = Canvas(window)
    w1.p1 = p1

    # for adding extract label
    extract_lbl = Label(f1, text='Want to Extract Add. ...', font=("Arial", 40), fg="brown", bg = "white")
    extract_lbl.place(x=400, y=120)

    # created go here button
    gohere1b = Button(f1, text="GO HERE", command=go_extract, font=("Arial", 25), bg="light green", fg="blue", borderwidth=3, relief="raised")
    gohere1b.place(x = 540, y=200)

    # for adding validate label
    validate_lbl = Label(f1, text='Want to Check Validity...', font=("Arial", 40), fg="brown", bg="white")
    validate_lbl.place(x=400, y=420)

    # created go here button
    gohere2b = Button(f1, text="GO HERE", command=go_validate, font=("Arial", 25), bg="light green",fg="blue", borderwidth=3, relief="raised")
    gohere2b.place(x=540, y=500)

# function defined for showing details
def details_fun():
    mbox.showinfo("IP Address Details", "\tAn Internet Protocol address (IP address) is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.\n\n\tAn IP address serves two main functions: host or network interface identification and location addressing.\n\n\tInternet Protocol version 4 (IPv4) defines an IP address as a 32-bit number. However, because of the growth of the Internet and the depletion of available IPv4 addresses, a new version of IP (IPv6), using 128 bits for the IP address, was standardized in 1998.\n\n\tIP addresses are written and displayed in human-readable notations, such as 172.16.254.1 in IPv4, and 2001:db8:0:1234:0:567:8:1 in IPv6. ")


# top label
start1 = tk.Label(text = "IP Address Extractor-Validator", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 50, y = 10)

# image on the main window
path = "Images/front_ip.jpg"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img1)
panel.place(x = 120, y = 130)

# created start button
startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x =90 , y =600 )

# created details button
detailsb = Button(window, text="DETAILS",command=details_fun,font=("Arial", 25), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
detailsb.place(x =420 , y =600 )

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =800 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()