import win32com.shell.shell as shell
import os
import sys
import ctypes
import time
from datetime import datetime as dt
from tkinter import *
from tkinter import messagebox

#Create tkinter root/GUI
root = Tk()
root.title("Website Blocker by Rutuj Runwal")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.geometry("600x300")
ASADMIN = 'asadmin'
# Host's Path - All the website info that is to be blocked is saved here
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
# localhost's IP
redirect = "127.0.0.1"
website_list = []


def AddWebsite():
    site = Input.get()   # Get the site-input given by the user and check if it is 
    print("You Entered: "+site)
    if("www" not in site or "." not in site):
        messagebox.showinfo(
            "Invalid Website", "Make sure the site is of this format 'www.google.com' `")
    else:
        website_list.append(site)
        print(website_list)

# Function to check for admin access 
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def Block():
    if is_admin():
        while True:
            # Time of your work
            if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
                print("Access Denied")
                with open(hosts_path, 'r+') as file:
                    content = file.read()
                    for website in website_list:
                        if website in content:
                            pass
                        else:
                            # Mapping hostnames to your localhost IP address
                            file.write(redirect + " " + website + "\n")
            else:
                with open(hosts_path, 'r+') as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)
                    # Removing hostnames from host file
                    file.truncate()

                print("Access Granted")
            time.sleep(5)
    else:
        # Retry getting admin access to modify hosts file
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        if is_admin():
            while True:
                # Time of your work
                if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
                    print("Access Denied")
                    with open(hosts_path, 'r+') as file:
                        content = file.read()
                        for website in website_list:
                            if website in content:
                                pass
                            else:
                                # mapping hostnames to your localhost IP address
                                file.write(redirect + " " + website + "\n")
                else:
                    with open(hosts_path, 'r+') as file:
                        content = file.readlines()
                        file.seek(0)
                        for line in content:
                            if not any(website in line for website in website_list):
                                file.write(line)
                        # removing hostnames from host file
                        file.truncate()

                    print("Access Granted")
                time.sleep(5)

# The BlockSites function is used to handle no. of sites to block
def BlockSites():
    if(len(website_list) == 1):
        Val = messagebox.askquestion("", "You are about to block 1 website.Are you sure you dont want to add more?")
        if Val == "yes": #If user says "yes" , block the site provided
            print("Blocking One Site...")
            Block()
        else:
            messagebox.showinfo("", "Add more sites and then press Block-Sites when you are ready")
    if(len(website_list) == 0):
        #If the website_list is zero it means the user has not added any site to block
        messagebox.showinfo("No sites to block","Please add sites to block first!")
    else:
        #If the sites are >1 block them directly
        print("Ready to block "+str(len(website_list)) + " sites")
        Block()


if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    try:
        # Try running the code with admin access
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
        messagebox.showinfo("Welcome", "Welcome to Website Blocker v1.0.Add Websites to block,Once you are done click on Block-Sites to get started!")
        MyLabel = Label(root, text="Enter Website to Block:")
        MyLabel.grid(row=0, column=0)
        Input = Entry(root, width=60, borderwidth=3)
        Input.insert(0, "Please REMOVE this text and enter website address.")
        Input.grid(row=0, column=2)
        MyBtn = Button(root, text="Add Website",command=AddWebsite).grid(row=1, column=2)
        MyBtn2 = Button(root, text="Block-Sites",command=BlockSites).grid(row=3, column=2)
        root.mainloop()
    except(Exception):
        # Show an error when admin access is denied
        messagebox.showerror(
            "ERR:Admin Denied", "Admin rights are required for the script to work")
