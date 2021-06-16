import tkinter
from tkinter.constants import END
from tkinter.font import names
import random
from tkinter import Label, messagebox
from typing import Text
#import tkMessageBox 

#list of categories and words in each list
fruits =["apple","pineapple","orange","mango","banana","cherry"]
countries =["india", "australia","england","germany","austria","indonesia","japan","singapore"]
superheroes = ["batman","batwoman","catwoman","hawkeye","supergirl","thor","flash"]
vegetables = ["tomato","potato","brinjal","onion","mushroom"]
sco = 0
score_txt ="Score:- "+str(sco)

#This function is called when the user presses the exit button
def destroy_fn():
    #this will show a pop up window
    messagebox.showinfo("EXIT MESSAGE","Thank you for playing the game")
    #this is used to destroy window and exit game
    gamewindow.destroy()

#This function is called when the user presses the next word button
def next_word(cat):
        global word
        jword =""
        cat = cat.lower()
        #print("catloer is ",cat)
        #word = cat[random.randrange(0,len(cat))]
        #jumble = random.sample(word,len(word))
        #for i in jumble:
         #   jword += i
        #print("inside next word")
        #choosing a random word from the chossen category
        if(cat == "fruits"):
            word = random.choice(fruits)
        elif(cat =="countries"):
            word = random.choice(countries)
        elif(cat == "superheroes"):
            word = random.choice(superheroes)
        elif(cat == "vegetables"):
            word = random.choice(vegetables)
        #print("word is ",word)
        #jumble the letters of the word
        jumble = random.sample(word,len(word))
        #converting the lsit to string
        for i in jumble:
            jword += i

        #print("jword is ",jword)
        #displaying the word
        word_label.configure(text = jword)
        #deleting the existing text in the text box
        get_input.delete(0, END)
        #print("end of next word")
        #deleting the ans shown 
        ans_space.configure(text ="")
    
#this function is called when the user presses the answer key
def showans():
    global word
    #showing the answer
    ans_space.configure(text = word)

#This function is called when the user presses the submit button
def check_word(cat):
    #guess = get_input.get().lower()
    global sco,word 
    #print("word is ", word)
    #print("inside check eord")
    #user_input = get_input.get()
    #storing the user input
    guess = get_input.get().lower()
    #print(user_word)
    #checking if the guessed word is right
    if(guess == word):
        #print("correct")
        #shoeing a po up mesage if guess is right        
        messagebox.showinfo("CORRECT ANS", "CONGRATULATIONS!!!!!! you found the right word")
        #displaying the next word
        next_word(cat)
        # jword =""
        # cat = cat.lower()
        # #print("catloer is ",cat)
        # #word = cat[random.randrange(0,len(cat))]
        # #jumble = random.sample(word,len(word))
        # #for i in jumble:
        #  #   jword += i
        # if(cat == "fruits"):
        #     word = random.choice(fruits)
        # elif(cat =="countries"):
        #     word = random.choice(countries)
        # elif(cat == "superheroes"):
        #     word = random.choice(superheroes)
        # elif(cat == "vegetables"):
        #     word = random.choice(vegetables)
        # print("word is ",word)
        # jumble = random.sample(word,len(word))
        # for i in jumble:
        #     jword += i

        # print("jword is ",jword)
        # word_label.configure(text = jword)
        # get_input.delete(0, END)
        #deleting the ans shown 
        ans_space.configure(text ="")
        return
    else:
        #pop up box for wrong message
        messagebox.showinfo("WRONG ANS", "Please try again")
        #print("Wrong")
        #deleting thw prv user input
        get_input.delete(0, END)


        

#this fn is used to create the game window
def game(cat,jword):
    #print("hello")
    global word
    #print("word is ",word)
    #print("jumbled word is",jword)
    #destroying the intro window
    root.destroy()
    global gamewindow 
    #creating the game window
    gamewindow = tkinter.Tk()
    gamewindow.geometry("600x600+600+200")
    gamewindow.title(cat)
    gamewindow.configure(bg="light blue")
    global score 
    
    global word_label
    #diplaying the word
    word_label = tkinter.Label(
        gamewindow,
        text=jword,
        pady=10,
        bg="light blue",
        fg="#000000",
        font="Titillium  50 bold"
    )
    word_label.pack()
    global get_input
    answer = tkinter.StringVar() 
    # displaying the input box
    get_input = tkinter.Entry(
         font="none 26 bold",
         borderwidth=10,
         justify='center',
         textvariable= answer
     )
    get_input.pack()
    #user_word = get_input.get().upper()
    #guess = get_input.get().lower()
    #print(user_word)
    #displaying submit buutton whixh calls check word
    submit = tkinter.Button(
                gamewindow,
                text="SUBMIT",
                width=18,
                borderwidth=8,
                font=("", 18),
                fg="#000000",
                bg="light green",
                #cursor="hand2",
                command=lambda:check_word(cat)
        )
    submit.pack(pady=(10,20))

    #displaying answer button which calls showans fn
    ans = tkinter.Button(
                gamewindow,
                text="ANSWER",
                width=18,
                borderwidth=8,
                font=("", 18),
                fg="#000000",
                bg="light green",
                #cursor="hand2",
                command=lambda: showans(),
        )
    ans.pack(pady=(10,20))
    
    #displaying next word button which calls nextword fn
    nextWord = tkinter.Button(
                gamewindow,
                text="NEXT WORD",
                width=18,
                borderwidth=8,
                font=("", 18),
                fg="#000000",
                bg="light green",
                #cursor="hand2",-
                command=lambda:next_word(cat)
        )
    nextWord.pack(pady=(10,20))

    #displaing exxit button which calls destroy fn
    exit_btn = tkinter.Button(
                gamewindow,
                text="EXIT",
                width=18,
                borderwidth=8,
                font=("", 18),
                fg="#000000",
                bg="light green",
                #cursor="hand2",
                command=lambda:destroy_fn()
        )
    exit_btn.pack(pady=(10,20))


    global ans_space
    #shows the ans when needed initaaly it doesn not display anything
    ans_space = tkinter.Label(
        gamewindow,
        text="",
        pady=10,
        bg="light blue",
        fg="#000000",
        font="Courier 15 bold"
    )
    ans_space.pack()
    
    gamewindow.mainloop()

#this fn is used to find a random word from the choosen category and jumble it and then call the game fn
def start_game(args):
    global word 
    jword =""
    #print(args)
    if(args == 1):
        word = random.choice(fruits)
        jumble = random.sample(word,len(word))
        for i in jumble:
            jword += i
     #   print(word,jword)
        game("FRUITS",jword)
    elif(args == 2):
        word = random.choice(countries)
        jumble = random.sample(word,len(word))
        for i in jumble:
            jword += i
      #  print(word,jumble)
        game("COUNTRIES",jword)
    elif(args == 3):
        word = random.choice(superheroes)
        jumble = random.sample(word,len(word))
        for i in jumble:
            jword += i
       # print(word,jumble)
        game("SUPERHEROES",jword)
    elif(args == 4):
        word = random.choice(vegetables)
        jumble = random.sample(word,len(word))
        for i in jumble:
            jword += i
        #print(word,jumble)
        game("VEGETABLES",jword)


#this fn is to show the options to the user
def disp_option():
    #print("hi")
    #destroying all the elements which were previously displayed
    start_btn.destroy()
    label.destroy()
    #Displaying fruits button
    sel_btn1 = tkinter.Button(
            root,
            text="Fruits",
            width=30,
            borderwidth=10,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(1),
        )
    #Displaying countries button    
    sel_btn2 = tkinter.Button(
            root,
            text="Countries",
            width=30,
            borderwidth=10,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(2),
        )
    #Displaying superheores button    
    sel_btn3 = tkinter.Button(
            root,
            text="Superheroes",
            width=30,
            borderwidth=10,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(3),
        )
        #Displaying vegetables button
    sel_btn4 = tkinter.Button(
            root,
            text="Vegetables",
            width=30,
            borderwidth=10,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(4),
        )
    #alliging the buttons
    sel_btn1.grid(row=0, column=100, pady=(10, 0), padx=450 )
    sel_btn2.grid(row=2, column=100, pady=(10, 0), padx=450 )
    sel_btn3.grid(row=4, column=100, pady=(10, 0), padx=450 )
    sel_btn4.grid(row=6, column=100, pady=(10, 0), padx=450 )
    

        
#creating the start window
root = tkinter.Tk()
root.geometry("600x600+600+200")
root.title("JUMBLED WORDS GUESSING GAME")
root.configure(bg="#856ff8")
label = tkinter.Label(root,font='times 35',text= "WELCOME TO JUMBLED WORDS GUESSING GAME ",bg= "#856ff8")#.place(x=30,y=60)
label.pack(pady =(150,0))#pady=30,ipady=150,ipadx=10)

#name = tkinter.StringVar()
#e1 = tkinter.Entry(root,textvariable=name)
#e1.pack(ipady=0,ipadx= 0 )
#print(name)
#displying the start button which when clicked will call the disp_option fn
start_btn = tkinter.Button(
        root,
        text="Start",
        width=30,
        borderwidth=10,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        cursor="hand2",
        command=disp_option,
    )
start_btn.pack(pady=(50, 20))

    
root.mainloop()