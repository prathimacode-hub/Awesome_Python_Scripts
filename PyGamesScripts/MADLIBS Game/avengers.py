#Avengers Madlib Game
def madlib():
    
    #Defining Blanks to be filled by user
    
    Adj1=input("Adjective = ")
    Adj2=input("Adjective = ")
    Adj3=input("Adjective = ")
    verb1=input("Verb in present tense = ")
    verb4=input("Verb in continuous tense = ")
    FamousPersonality1=input("FamousPersonality = ")
    FamousPersonality2=input("FamousPersonality = ")

    print("The Avengers Template")  #Heading of the story template
    print()


    #MADLIB STORY
    madlib=f""" And with the snap of the finger, everything started to {verb1} back. Hulk aka Bruce Banner was thrown back by the recoiling
                power of the gauntlet. Spiderman aka {Adj1} Peter thrived back to life and started blabbering about his time in that quantum of
                time with {FamousPersonality1}, Tony aka Iron man was happily in tears listening to this little boy he had been missing all these
                five years. Ah! but Thanos equivalent to our {FamousPersonality2} was still standing alive with all his {Adj2} plans in action with 
                his daughter Nebula (from the past). And to the rescue came our {Adj3} Captain Marvel and the troops of Waganda {verb4} and fighting 
                the warship of Thanos!! """


    
    print(madlib)
    print()
