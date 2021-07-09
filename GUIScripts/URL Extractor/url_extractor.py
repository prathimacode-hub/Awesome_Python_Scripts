
# URL EXTRACTOR

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import re
from itertools import chain

'''

\b is used for word boundary to delimit the URL and the rest of the text
(?:https?://)? to match http:// or https// if present
(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6}) to match standard url (that might start with www. (lets call it STANDARD_URL)
(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?) to match standard Ipv4 (lets call it IPv4)
to match the IPv6 URLs: (?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])) (lets call it IPv6)
to match the port part (lets call it PORT) if present: (?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])
to match the (?:/[\w\.-]*)*/?) target object part of the url (html file, jpg,...) (lets call it RESSOURCE_PATH)

'''

# created main window
window = Tk()
window.geometry("1000x700")
window.title("URL Extractor")

# extracting url -------------------------
def extract_url():
    input_text = str(text_enter.get("1.0", "end-1c"))
    regex = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"

    matches = re.findall(regex, input_text)
    res = ""
    for ele in matches:
        res = res + str(ele) + "\n"
    # print(res)
    mbox.showinfo("Extracted URL", "Extracted URL from text :\n\n" + res)

# ------------------------------------------

# extracting domain name --------------------------
httpurl_re = re.compile('https?://[A-Za-z0-9-.]+')

def valid_label(label):
    return re.match('[a-z0-9]([a-z0-9-]*[a-z0-9])?', label)

def parse_domain(potential):
    domain = potential.lower().split('/')[-1]
    labels = domain.split('.')
    if not labels[-1]:
        labels.pop()
    if labels and all(valid_label(l) for l in labels):
        if re.match('ww((w?[0-9])|w)', labels[0]):
            labels = labels[1:]
        if len(labels) >= 2:
            return '.'.join(labels)

def get_domains(s):
    for potential in httpurl_re.findall(s):
        domain = parse_domain(potential)
        if domain:
            yield domain

def extract_domain():
    input_text = str(text_enter.get("1.0", "end-1c"))
    # print(input_text)
    res_list = input_text.splitlines()
    # print(res_list)
    res = '\n'.join(sorted(set(chain(*[get_domains(l) for l in res_list]))))
    # print('\n'.join(sorted(set(chain(*[get_domains(l) for l in res_list])))))
    mbox.showinfo("Extracted Domain", "Extracted Domain from text :\n\n" + res)

# ----------------------------------------------------------------

# top label
start1 = tk.Label(text = "URL EXTRACTOR", font=("Arial", 50), fg="magenta") # same way bg
start1.place(x = 200, y = 10)

# top second label
enter_label = Label(window, text="Enter Your text and Extract URLs and Domains...", font=("Arial", 30),fg="brown")
enter_label.place(x=70,y=100)

# created text area
text_enter = tk.Text(window, height=18, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_enter.place(x=50, y=150)

# created extract domain button
domainb = Button(window, text="EXTRACT DOMAIN",command=extract_domain,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
domainb.place(x =50 , y =600 )

# created extract url button
extractb = Button(window, text="EXTRACT URL",command=extract_url,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
extractb.place(x =380 , y =600 )

# function for clearing the text area
def clear_text():
    text_enter.delete("1.0","end")

# created a clear button
clearb = Button(window, text="CLEAR",command=clear_text,font=("Arial", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
clearb.place(x =660 , y =600 )


# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()
# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =850 , y =600 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()