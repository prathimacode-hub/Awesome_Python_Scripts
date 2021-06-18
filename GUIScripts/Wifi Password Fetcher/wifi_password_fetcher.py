from tkinter import *
import subprocess
import pyperclip
#making the gui for script
root = Tk()
root.geometry("600x600")
pass_details = StringVar()
myList = []

#function for fetching password and using the funtion of subprocess library
def see_wifi_pass():
    global myList
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
            '\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            myList.append(i)
            myList.append("--")
            myList.append(results[0])
            myList.append("|")
        except IndexError:
            myList.append(i)
            myList.append("--")
            myList.append("")

#showing the password
def show_wifi_pass():
    pass_details.set(myList)

#copying to clipboard using pyperclip library
def copytoclipboard():
    password = pass_details.get()
    pyperclip.copy(password)

#final layout for gui and printing all things
Label(root, text="Getting all the Wifi passwords from your device", font="calibri 20 bold").pack()
Button(root, text="Initiate Process Now", command=see_wifi_pass).pack(pady=10)
Button(root, text="Show wifi pass details", command=show_wifi_pass).pack(pady=10)
Entry(root, textvariable=pass_details, width=80).pack(pady=10)
Button(root, text="Copy to clipbord", command=copytoclipboard).pack(pady=10)

root.mainloop()

