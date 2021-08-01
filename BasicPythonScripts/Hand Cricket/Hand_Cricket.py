import random #Imported random Library
print("------------------------------------------INSTRUCTIONS------------------------------------------ \n1. Choose ODD or EVEN \n2. Enter your input for Toss between 1 to 10 \n3. If you win the toss, Opt Bat or Ball \n4. If Number matches then it's OUT \n------------------------------------------------------------------------------------------------")

def playagain(): #Playagain
    print("------------------------------------------------------------------------------------------------ \n1. Enter \"Yes\" to Play again. \n2. Enter \"No\" to Exit. \n------------------------------------------------------------------------------------------------ ")
    PLAYAGAIN = input('Play Again..?: ')
    if PLAYAGAIN.upper() == 'YES':
        main()
    elif PLAYAGAIN.upper() == 'NO':
        print("------------------------------------------------------------------------------------------------ \nThanks for playing..!! \nSee you soon.. \n-------------------------------------------------------------------------------------------------")
        exit()
    else:
        print('------Invalid input------\n-----Please try again-----')

        playagain()


def main():#Start of the game

    def firstbatting(): #If user or AI won Toss and opted to bat first
        print("You\'re all set Bat now..")
        score = 0
        while (True):

            AI = random.randint(1, 10)
            MINE = int(input("Bat: ")) #User Batting Runs Input
            if MINE > 10:
                print('----- INVALID INPUT ------ \n----- GAME RESTARTING -----')
                toss()
            print("AI Bowls: ", AI) #AI Bowling Input
            score = score + MINE #Score Count

            if (AI == MINE): #Out
                print("Out!!!..Your Innings comes to an end..")
                print("Score: ", score)
                break

        print('AI require ', score + 1, 'runs to win..!!') #Target
        print('AI is ready to chase down the target..!!') 
        ai_score = 0
        while (True):

            AI = random.randint(1, 10) 
            MINE = int(input("Bowl: "))#User Bowling input
            if MINE > 10:
                print('----- INVALID INPUT ------ \n----- GAME RESTARTING -----')
                toss()
            print("AI Bats: ", AI) #AI Batting Input
            ai_score = ai_score + AI
            if ai_score > score:
                print("AI Score", ai_score)
                print('Hard Luck Buddy, YOU LOSE..!! AI sealed the WIN with great knock') 
                break
            if (AI == MINE):
                print("Gone...!! You dismissed AI...Out...!!")
                print("AI Score: ", ai_score)
                if score > ai_score:
                    print('Superb Victory..Won by ', ((score)-(ai_score)), 'runs, Congratulations..!!')
                else:
                    print('----- MATCH TIED -----')
                break

    def secondbatting():  #If user or AI won Toss and opted to bowl first
        print('AI is ready to start the innings..!!')
        ai_score = 0
        while (True):

            AI = random.randint(1, 10)
            MINE = int(input("Bowl: ")) #User Bowling Input
            if MINE > 10:
                print('----- INVALID INPUT ------ \n----- GAME RESTARTING -----')
                toss()
            print("AI Bats: ", AI) #AI Batting
            ai_score = ai_score + AI

            if (AI == MINE): #Out
                print("Gone...!! You dismissed AI...Out...!!")
                print("AI Score: ", ai_score)
                break

        print('AI is ready to bowl, Most exciting match coming soon.. ALL THE BEST...')
        score = 0
        while (True):

            AI = random.randint(1, 10)
            MINE = int(input("Bat: ")) #User Batting Input
            if MINE > 10:
                print('----- INVALID INPUT ------ \n----- GAME RESTARTING -----')
                toss()
            print("AI Bowls: ", AI)
            score = score + MINE
            if ai_score < score:
                print("Score", score)
                print('OMG..!! You Win..What a win that  is..!! Chased down the target perfectly..Unbelievable knock..')
                break
            if (AI == MINE):
                print("Gone...!! AI dismissed you...Out...!!")
                print("Score", score)
                if ai_score > score:
                    print('Hard Luck Buddy..!! AI sealed the win by',(ai_score - score)  ,'runs...A spectacular performance..')
                else:
                    print('----- TIE MATCH -----')
                break

    def toss():
        TOSS = input('Toss time..What you want \"ODD or EVEN \": ')
        My_input = int(input('Please, Enter any number between 1 to 10: '))
        if My_input > 10:
            print('----- INVALID INPUT ------ \n----- GAME RESTARTING -----')
            toss()
        AI_input = random.randint(1, 10)
        print('Input of AI: ', AI_input)
        if TOSS.upper() == 'EVEN':
            if ((My_input + AI_input) % 2) == 0: #User Toss even
                print('Great..!!, You won the Toss..What you wanna choose ?')
                YOURTOSS = input('BAT or BALL:')
                if YOURTOSS.upper() == 'BAT':
                    firstbatting()
                elif YOURTOSS.upper() == 'BOWL':
                    secondbatting()
                else:
                    print('----- INVALID INPUT ------ \n----- GAME RESTARTING -----') #Invalid
                    toss()
            else:
                AITOSS = random.choice(['bat', 'bowl'])
                if AITOSS == 'bat':
                    print('AI opted Bat first..')
                    secondbatting()
                elif AITOSS == 'bowl':
                    print('AI opted Bowl first..')
                    firstbatting()
        elif TOSS.upper() == 'ODD': 
            if ((My_input + AI_input) % 2) == 0: 
                AITOSS = random.choice(['bat', 'bowl'])
                if AITOSS == 'bat':
                    print('AI opted Bat first..')
                    secondbatting()
                elif AITOSS == 'bowl':
                    print('AI opted Bowl first..')
                    firstbatting()

            else:
                print('Great..!!, You won the Toss..What you wanna choose ?')
                YOURTOSS = input('BAT or BOWL: ')
                if YOURTOSS.upper() == 'BAT':
                    firstbatting()
                elif YOURTOSS.upper() == 'BOWL':
                    secondbatting()
                else:
                    print('----- INVALID INPUT ------ \n----- GAME RESTARTING -----')
                    toss()
        else:
            print('----- INVALID INPUT ------ \n----- GAME RESTARTING -----')
            toss()

    toss()
    playagain()

main()
