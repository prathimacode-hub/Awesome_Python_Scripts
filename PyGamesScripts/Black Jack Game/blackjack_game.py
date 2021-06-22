import random
import art   ## importing logo from that






print (art.logo)

is_start=False
print("Welcome to Blackjack Game")
if input("Do you want to start the game?'y' for yes 'n'for no: " ) =='y':
        is_start=True
        
else:
    
    is_start=False    
    
while is_start:

    def deal_card():                          ## this function will choose random card
        cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]      ## list of cards
        return random.choice(cards)                     

    def calculate_score(cards):                    ## it will calculate score
        if sum(cards)==21 and len(cards)==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)        
        return sum(cards)

    def compare (user_score,computer_score):       ## this is to comapre user and computer score
        if user_score==computer_score:
            return "Draw!"
        elif computer_score==0:
            return "Lose!opponent has Blackjack"
        elif user_score>21:
            return "You went over. You loose!"
        elif user_score>computer_score:
            return "You won!"
        else:
            return "You won!" 



    user_cards=[deal_card(),deal_card()]           ## first initialization of user cards 
    computer_cards=[deal_card(),deal_card()]       # and computer cards which will contain two cards at first
    is_game_over=False                             # boolean it will decide when game will stop
    
    while not is_game_over:                         # until when is_game_over will be false the game will continue 

        user_score=calculate_score(user_cards)                     #keeping user score
        computer_score=calculate_score(computer_cards)            # and computer score in a variable
        print(f" Your cards: {user_cards}, current score: {user_score}") 
        print(f"First card of computer: {computer_cards[0]}")
        if user_score==0 or user_score>21 or computer_score==0:          # at this condition we will like to exit our game
            is_game_over=True
        else:
            print("You want to draw another card?")
            user_choice=input("Type 'y' to draw and 'n'to pass: ")            ## asking user to continue or not
            if user_choice=='y':
                user_cards.append(deal_card())                           ## adding new card to list
            else:
                is_game_over=True                                      
        
    while computer_score!=0 and computer_score<17:                     ## computer will continue according to condition
        computer_cards.append(deal_card())                                
        computer_score=calculate_score(computer_cards)               ##calculating computer score

    print(f" Your final hand: {user_cards}, final score: {user_score}")
    print(f" Your final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score,computer_score))
    if input("Do you want to play another game?'y' for yes 'n'for no: " ) =='y':
        is_start=True
    else:
        is_start=False    
    
