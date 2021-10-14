#Friends Madlib Game
def madlib():
    
    #Defining Blanks that the user has to enter
    
    Adj1=input("Adjective = ")
    Adj2=input("Adjective = ")
    Adj3=input("Adjective = ")
    Adj4=input("Adjective = ")
    verb1=input("Verb in continuous tense = ")
    verb2=input("Verb in past tense = ")
    verb4=input("Verb in continuous tense = ")
    FamousPersonality=input("FamousPersonality = ")
    
    print("The F.r.i.e.n.d.s Template")       #heading of the story template
    print()
 

    #MADLIB STORY
    madlib=f""" Monica {verb2} some {Adj1} dishes for the Thanksgiving dinner, while joey was super {Adj2} for the
               dinner Rachel thought of ways to avoid it as she had some {Adj3} plans with {FamousPersonality}. 
               Ross meanwhile was {verb1} on some dinosaur stuff. and chandler and phoebe were {verb4} inorder 
               to help Monica. well, that very moment came a {Adj4} voice saying "OHH! My God" I bet you know 
               whose it was ? ;)"""

    print(madlib)
    print() 
