
# Highlight Selected Part of Text

import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox


window = Tk()
window.geometry("1000x700")
window.title("Highlight Selected Part of Text")


class highlight_fun(tk.Frame):
    def __init__(self, parent, *args, **kwargs):

        hightlightb = Button(window, text="HIGHLIGHT",command=self.highlight_text,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
        hightlightb.place(x =100 , y =610 )

        unhightlightb = Button(window, text="UN HIGHLIGHT", command=self.unhightlight_text, font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
        unhightlightb.place(x=320, y=610)

        clearb = Button(window, text="CLEAR", command=self.clear_text, font=("Arial", 20),bg="light green", fg="blue", borderwidth=3, relief="raised")
        clearb.place(x=600, y=610)

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.text = tk.Text(self,height=17, width=70, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
        self.text.pack(fill="both", expand=True)

        self.text.tag_configure("start", background="green", foreground="red")

    def highlight_text(self):
        try:
            self.text.tag_add("start", "sel.first", "sel.last")
        except tk.TclError:
            pass

    def unhightlight_text(self):
        self.text.tag_remove("start", "1.0", 'end')

    def clear_text(self):
        self.text.delete('1.0', END)

# top label
start1 = tk.Label(text = "HIGHLIGHT SELECTED TEXT", font=("Arial", 50), fg="magenta",underline=0) # same way bg
start1.place(x = 50, y = 10)

note1 = tk.Label(text = "Enter Any Paragraph in Text Area, select any text and click on HIGHLIGHT Button.\nAnd to un-highlight the highlighted text, click on UN HIGHLIGHT button.\nTo clear the entered text, click on CLEAR button.", font=("Arial", 18), fg="brown") # same way bg
note1.place(x = 50, y = 510)

# highlight_text(window).pack(expand=1, fill="both")
highlight_fun(window).place(x = 100, y = 100)

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =780 , y =610 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()