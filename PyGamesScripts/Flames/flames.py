from tkinter import *


def clear_all():
    Ply1_field.delete(0, END)
    Ply2_field.delete(0, END)
    Status_field.delete(0, END)

    #NOw, let's focus the set field of player 1 
    Ply1_field.focus_set()

def status():
    p1 = Ply1_field.get()
    p2 = Ply2_field.get()
    p1 = p1.replace(" ", "")
    p2 = p2.replace(" ", "")
    p1 = list(p1)
    p2 = list(p2)

    Status_field.insert(10, result_flame(p1, p2))


def result_flame(x, y):
    for i in x[:]:
        if i in y:
            x.remove(i)
            y.remove(i)
    count = len(x) + len(y)
    result = ["Love", "Friends", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if (split_index >= 0):
            right = result[split_index + 1:]
            left = result[:split_index]
            result = right + left
        else:
            result = result[:len(result) - 1]
    return result


if __name__ == "__main__":
   #creating a GUI 
    root = Tk()
    #NOW, SET THE BG COLOR
    root.configure(background='#82EEFD')
    # LET'S SET THE CONFIGURATION
    root.geometry("350x125")
    # SET THE NAME OF WINDOW
    root.title("Let's try once")
    # ply 1 name: label
    label1 = Label(root, text="Name 1 ", fg='white', bg='#0000cd')
    # ply 2 name: label
    label2 = Label(root, text="Name 2 ", fg='white', bg='#0000cd')
    # relation status
    label3 = Label(root, text="Relationship Status", fg='black', bg='#82EEFD')
    # grid method is used for placing
    
    label1.grid(row=1, column=0, sticky="E")
    label2.grid(row=2, column=0, sticky="E")
    label3.grid(row=4, column=0, sticky="E")
    # Create a text entry box
   
    Ply1_field = Entry(root)
    Ply2_field = Entry(root)
    Status_field = Entry(root)
    # grid method is used for placing the widgets at respective positions
   
    Ply1_field.grid(row=1, column=1, ipadx="50")
    Ply2_field.grid(row=2, column=1, ipadx="50")
    Status_field.grid(row=4, column=1, ipadx="50")
   #creating a submit button
    button1 = Button(root,
                     text="Flame",
                     bg="#007fff",
                     fg="white",
                     command=status)

    # Creating a Clear Button
  
    button2 = Button(root,
                     text="Clear",
                     bg="#007fff",
                     fg="white",
                     command=clear_all)

    # grid method is used for placing the widgets at respective positions
   
    button1.grid(row=3, column=1)
    button2.grid(row=5, column=1)
#let's repeat
    root.mainloop()
