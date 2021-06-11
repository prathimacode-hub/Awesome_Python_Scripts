import random
name = input("Enter your name ")
print("Welcome ",name)
again = "yes"
fruits =["apple","pineapple","orange","mango","banana","cherry"]
countries =["india", "australia","england","germany","austria","indonesia","japan","singapore"]
superheroes = ["batman","batwoman","catwoman","hawkeye","supergirl","thor","flash"]
vegetables = ["tomato","potato","brinjal","onion","mushroom"]
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
    print("\n\t\tCATEGORIES\n1.Fruits\n2.Countries\n3.Superheroes\n4.vegetables\n")
    n = int(input("Enter the category u want "))
    
    if(n ==1):
        word = random.choice(fruits)
    elif(n ==2):
        word = random.choice(countries)
    elif(n==3):
        word = random.choice(superheroes)
    elif(n==4):
        word = random.choice(vegetables)
    for i in word:
        print("_",end=" ")
    guess =" "
    all_guess =" "
    ch = input("\n\nEnter the guessed character ");
#int n = len(word)
    chance = 8
    while (chance>0):
        wrong = 0
        for i in word:
            if (i == ch or i in guess):
                print(i,end=" ")
            else:
                print("_",end=" ")
                wrong+=1
        if( wrong == 0):
            print("\n\nCONGRATULATIONS!! YOU WIN !!! YOU FOUND THE WORD")
            break
        if(ch in word and ch not in guess):
            print("\nGood attempt ",ch," is in the word ")
            guess +=ch
            if(z>=0):
                print (stages[z])
        elif (ch in all_guess):
            print("\nYou have already guessed ",ch )
        elif (ch not in word):
            print("\n",ch," not in the given word try again ")
            z+=1
            print(stages[z])
            chance-=1
            print("\nYou still have ",chance," chances ")
        if( chance <1):
            print("\n\nSorry. YOU LOOSE!!!")
            print("The Word is ", word)
            break
        all_guess +=ch
        ch = input("\n\nEnter the guessed character ");
    again = input("Do you want to play again ")
    
    
            
