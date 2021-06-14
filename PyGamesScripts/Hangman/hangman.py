import random
name = input("Enter your name ")
print("Welcome ",name)
again = "yes"
#words in each category
fruits =["apple","pineapple","orange","mango","banana","cherry"]
countries =["india", "australia","england","germany","austria","indonesia","japan","singapore"]
superheroes = ["batman","batwoman","catwoman","hawkeye","supergirl","thor","flash"]
vegetables = ["tomato","potato","brinjal","onion","mushroom"]
#various stages
stages = [
"""
\t--------
\t|
\t|
\t|
\t|""",
"""
\t--------
\t|      |
\t|
\t|
\t|""",
"""
\t--------
\t|      |
\t|      O
\t|
\t|""",
"""
\t--------
\t|      |
\t|      O
\t|     /
\t|""",

"""
\t--------
\t|      |
\t|      O
\t|     /|
\t|""",

"""
\t--------
\t|      |
\t|      O
\t|     /|\\
\t|""",

"""
\t--------
\t|      |
\t|      O
\t|     /|\\
\t|     /""",

"""
\t--------
\t|      |
\t|      O
\t|     /|\\
\t|     / \\ """,

]
           
        
while(again == "yes"):
    z=-1
    print("Lets play hangman ")
        #choosing a category
    print("\n\t\tCATEGORIES\n1.Fruits\n2.Countries\n3.Superheroes\n4.vegetables\n")
    n = int(input("Enter the category u want "))
        #chosing a rondom word from the choosen category
    if(n ==1):
        word = random.choice(fruits)
    elif(n ==2):
        word = random.choice(countries)
    elif(n==3):
        word = random.choice(superheroes)
    elif(n==4):
        word = random.choice(vegetables)
        #printing the word with blank spaces so that user can know the number of letters
    for i in word:
        print("_",end=" ")
        # having guess for storing all the right guesses alone and all_guess for storing all guesses from user
    guess =" "
    all_guess =" "
    #getting a letter from user
    ch = input("\n\nEnter the guessed character ");
#int n = len(word)
    chance = 8
    while (chance>0):
                   #wrong is  a varibale used to check if word is fully found or not
        wrong = 0
        #printing the word with all right guesses made by the user
        for i in word:
            if (i == ch or i in guess):
                print(i,end=" ")
            else:
                print("_",end=" ")
                wrong+=1
        #checking if the word is fully found
        if( wrong == 0):
            print("\n\nCONGRATULATIONS!! YOU WIN !!! YOU FOUND THE WORD")
            break
         #checking if the letter is in the word and user has guessed that letter for the 1st time
        if(ch in word and ch not in guess):
            print("\nGood attempt ",ch," is in the word ")
            guess +=ch
            #showing the hangamn image if the user had made even 1 wrong guess before
            if(z>=0):
                print (stages[z])
        #checking if the letter is already guessed
        elif (ch in all_guess):
            print("\nYou have already guessed ",ch )
         #checking if it is a wrong guess and incrementing the hangman image to next stage and decrementing the chances
        elif (ch not in word):
            print("\n",ch," not in the given word try again ")
            z+=1
            print(stages[z])
            chance-=1
            print("\nYou still have ",chance," chances ")
         #loosing condition
        if( chance <1):
            print("\n\nSorry. YOU LOOSE!!!")
            print("The Word is ", word)
            break
        all_guess +=ch
        #getting the guessed cahr from  user
        ch = input("\n\nEnter the guessed character ");
            #checking if user wants to play again
    again = input("Do you want to play again ")
    
    
            
