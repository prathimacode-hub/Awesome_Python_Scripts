import tkinter as tk
import random
# timer function
def timerFunc():
    global boolean
    global timer_value
    global timer
    global entry_box
    global entry_box_value
    if(boolean==True):
        if(timer_value>0):
            timer_value -= 1
            timer.config(text=timer_value)
            timer.after(1000,timerFunc)
            if(timer_value==0):
                entry_box.config(state=tk.DISABLED)
                entry_box_value.set("Game Over!!")
                boolean = False
            
# start button function
def startFunc():
    global boolean
    global  colors
    global  word_color
    global  word
    boolean = True
    colors = ["Red", "Blue", "Green", "Pink", "Black",
              "Yellow", "Orange", "White", "Purple", "Brown"]
    start_btn.config(state=tk.DISABLED)
    changeColor()
    timerFunc()

    
# change the color of word
def changeColor():
    global  colors
    global  word_color
    global  word
    global word_lbl
    global word_color_list
    global user_score
    word = random.choice(colors)
    word_color = random.choice(colors)
    word_color_list.append(word_color)
    word_lbl.config(text=word)
    word_lbl.config(fg=word_color)
    if user_score >= 1:
        if word_color_list[user_score-1] != word_color:
            word_lbl.config(bg=word_color_list[user_score-1])
        else:
            word_lbl.config(bg="Grey")


# increment score if input is correct
def check(event):
    global score
    global user_score
    if(entry_box.get().lower()==word_color.lower()):
        entry_box_value.set("")
        user_score += 1
        score.config(text=user_score)
        changeColor()

# reset the game
def resetGame():
    global boolean
    global score
    global timer
    global word_lbl
    global user_score
    global timer_value
    global word
    global entry_box
    global entry_box_value
    user_score = 0
    score.config(text = user_score)

    timer_value =  30
    timer.config(text = timer_value)

    word = ""
    word_lbl.config(text = word)

    entry_box_value.set("")
    entry_box.config(state=tk.NORMAL)
    start_btn.config(state=tk.NORMAL)

    boolean = False

# global variables
user_score = 0
timer_value = 30
colors = ""
word = ""
word_color = ""
word_color_list = []
boolean = ""
# Setup window
root = tk.Tk()
root.title("Color Game - Mudit Choudhary")
root.geometry("800x510")


# Heading Label
tk.Label(root, text="Remember type the color of the word, not the word text!!",
         font=("Comic Sans MS", 19), fg="#ff6e6e").pack(pady=(15, 0))

# Frame 1
fr1 = tk.Frame(root)
fr1.pack(pady=(19, 0))

# Your Score label
tk.Label(fr1, text="Your Score : ", font=(
    "Comic Sans MS", 19), fg="#51db74").pack(side=tk.LEFT)
# Show Score label
score = tk.Label(fr1, text=user_score, font=(
    "Comic Sans MS", 19), fg="#fa64e1")
score.pack(side=tk.LEFT)

# Frame 2
fr2 = tk.Frame(root)
fr2.pack()

# Timer label
tk.Label(fr2, text="Time left : ", font=("Comic Sans MS", 19),
         fg="#9b5bf0").pack(side=tk.LEFT, pady=(15, 0))
# Show timer label
timer = tk.Label(fr2, text=timer_value,
                 font=("Comic Sans MS", 19), fg="#e0ca48")
timer.pack(side=tk.LEFT, pady=(15, 0))

# Frame 3
fr3 = tk.Frame(root)
fr3.pack(pady=(19, 0))

# Word label
word_lbl = tk.Label(fr3, text="", font=("Comic Sans MS", 69))
word_lbl.pack()

# Entry Box
entry_box_value = tk.StringVar()
entry_box_value.set("")
entry_box = tk.Entry(fr3, textvariable=entry_box_value,
                     font=("Comic Sans MS", 19))
entry_box.pack(pady=(10, 0))
# Bind Enter Key With Entry Box
entry_box.bind("<Return>",check)

# Start button
start_btn = tk.Button(fr3, text="Start", font=(
    "Comic Sans MS", 22), fg="#2f5df5", width=8, height=1, bg="#fc8b8b", command=startFunc)
start_btn.pack(side=tk.LEFT, pady=(25, 0), padx=(0, 10))

# Reset button
reset_btn = tk.Button(fr3, text="Reset", font=(
    "Comic Sans MS", 22), fg="#f73b3b", width=8, height=1, bg="#5863f5",command=resetGame)
reset_btn.pack(side=tk.LEFT, pady=(25, 0))

root.mainloop()
