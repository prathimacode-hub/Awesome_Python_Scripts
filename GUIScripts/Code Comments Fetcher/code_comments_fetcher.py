# Code Comments Fetcher

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import re

# created main window
window = Tk()
window.geometry("1000x700")
window.title("Code Comments Fetcher")


# extracting url -------------------------
def fetch_comments():
    global detected_language
    input_text = str(text_enter.get("1.0", "end-1c"))
    if re.search(r'public static void main\(String args\[\]\)|System\.out\.println|import java\..+?;', input_text):
        detected_language = 'Java'
    elif re.search(r'#include<stdio.h>', input_text):
        detected_language = 'C'
    elif re.search(r'#include<iostream.h>', input_text):
        detected_language = 'C++'
    elif re.search(r'using System;', input_text):
        detected_language = 'C#'
    elif re.search(r'<!DOCTYPE html>', input_text):
        detected_language = 'HTML'
    elif re.search(r'<html>', input_text):
        detected_language = 'HTML'
    elif re.search(r'fun ', input_text):
        detected_language = 'Kotlin'
    elif re.search(r'<script>', input_text):
        detected_language = 'JavaScript'
    else:
        detected_language = 'Python'

    comments = ""
    res_list = (input_text.rstrip().split('\n'))

    if(detected_language == "Python"):
        mul = False
        for line in res_list:
            # print (line)
            if mul:
                # print(mul)
                texts1 = line.strip().split("'''")
                if len(texts1) == 2:
                    # print("%s*/" % texts1[0])
                    comments = comments + texts1[0] + "'''\n\n"
                    mul = False
                else:
                    comments = comments + texts1[0]
                    # print(texts1[0])
            else:
                # print(mul)
                texts = line.strip().split("'''")
                if len(texts) == 2:
                    comments = comments + "'''" + texts[1] + "\n\n"
                    # print("//%s" % texts[1])

                # ----------------- python single ---------
                texts = line.strip().split("#")
                if len(texts) == 2:
                    comments = comments + "#" + texts[1] + "\n\n"
                    # print("//%s" % texts[1])
                # -------------------------------------

                else:
                    texts2 = line.strip().split("'''")
                    if len(texts2) == 2:
                        texts3 = texts2[1].split("'''")
                        if len(texts3) == 2:
                            comments = comments + "'''" + texts3[0] + "'''\n\n"
                            # print("/*%s*/" % texts3[0])
                        else:
                            comments = comments + "'''" + texts2[1] + "\n\n"
                            # print("/*%s" % texts2[1])
                            mul = True
    elif(detected_language=="HTML" or detected_language=="JavaScript"):
        mul = False
        for line in res_list:
            # print (line)
            if mul:
                # -------------------- html -----------
                texts1 = line.strip().split("-->")
                if len(texts1) == 2:
                    # print("%s*/" % texts1[0])
                    comments = comments + texts1[0] + "-->\n\n"
                    mul = False
                else:
                    comments = comments + texts1[0]
                    # print(texts1[0])
                # -------------------------------------
            else:
                # print(mul)
                texts = line.strip().split("<!--")
                if len(texts) == 2:
                    comments = comments + "<!--" + texts[1] + "\n\n"
                    # print("//%s" % texts[1])

                else:
                    # ----------------------------html -------------
                    texts2 = line.strip().split("<!--")
                    if len(texts2) == 2:
                        texts3 = texts2[1].split("-->")
                        if len(texts3) == 2:
                            comments = comments + "<!--" + texts3[0] + "-->\n\n"
                            # print("/*%s*/" % texts3[0])
                        else:
                            comments = comments + "-->" + texts2[1] + "\n\n"
                            # print("/*%s" % texts2[1])
                            mul = True
                    # ---------------------------------------------
    else:
        mul = False
        for line in res_list:
            # print (line)
            if mul:
                # print(mul)
                texts1 = line.strip().split("*/")
                if len(texts1) == 2:
                    # print("%s*/" % texts1[0])
                    comments = comments + texts1[0] + "*/\n\n"
                    mul = False
                else:
                    comments = comments + texts1[0]
                    # print(texts1[0])
            else:
                # print(mul)
                texts = line.strip().split("//")
                if len(texts) == 2:
                    comments = comments + "//" + texts[1] + "\n\n"
                    # print("//%s" % texts[1])

                else:
                    texts2 = line.strip().split("/*")
                    if len(texts2) == 2:
                        texts3 = texts2[1].split("*/")
                        if len(texts3) == 2:
                            comments = comments + "/*" + texts3[0] + "*/\n\n"
                            # print("/*%s*/" % texts3[0])
                        else:
                            comments = comments + "/*" + texts2[1] + "\n\n"
                            # print("/*%s" % texts2[1])
                            mul = True

    mbox.showinfo("Comments Fetch", "Language  :  " + detected_language + "\n\nComments  :\n\n" + comments)


def lang_support():
    mbox.showinfo("Supported Programming Language", "Supported Programming Language :\n\nC\nC++\nJava\nPython\nHTML\nKolin\nJavaScript\nC#")


# top label
start1 = tk.Label(text="Code Comments Fetcher", font=("Arial", 50), fg="magenta")  # same way bg
start1.place(x=110, y=10)

# top second label
enter_label = Label(window, text="Write code snippets and fetch comments...", font=("Arial", 30), fg="brown")
enter_label.place(x=110, y=100)

# created text area
text_enter = tk.Text(window, height=18, width=80, font=("Arial", 15), bg="light yellow", fg="brown", borderwidth=3,relief="solid")
text_enter.place(x=50, y=150)

# created Language button
domainb = Button(window, text="LANG. SUPPORT", command=lang_support, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
domainb.place(x=50, y=600)

# created FETCH COMMENTS button
extractb = Button(window, text="FETCH COMMENTS", command=fetch_comments, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
extractb.place(x=330, y=600)


# function for clearing the text area
def clear_text():
    text_enter.delete("1.0", "end")


# created a clear button
clearb = Button(window, text="CLEAR", command=clear_text, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3,relief="raised")
clearb.place(x=660, y=600)


# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()


# created exit button
exitb = Button(window, text="EXIT", command=exit_win, font=("Arial", 20), bg="red", fg="blue", borderwidth=3,relief="raised")
exitb.place(x=850, y=600)

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
