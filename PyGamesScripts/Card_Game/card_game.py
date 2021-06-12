import random

suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
#Values are assigned to make the comparison easier. A dictionary has been used.
values={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#Object oriented programming is used.
#Various classes are created.

#card class

class Card():

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

#deck class

class Deck():
    def __init__(self):
       #Create a list to store all the cards of the deck
        self.allcards = [] 
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit,rank))
                
    def shuffle(self):
        #Shuffle the deck using "random" which was imported
        random.shuffle(self.allcards)
        
    def deal_one(self):
        #Deal one card from the deck
        return self.allcards.pop()
    
#player class

class Player():
    def __init__(self,name):
        #define the player 
        self.name = name
        self.allcards = [] 
        
    def remove_one(self):
        #Remove one card
        return self.allcards.pop(0)
    
    def add_cards(self,new_cards):
        #add cards
        if type(new_cards) == type([]):
            self.allcards.extend(new_cards)
        else:
            self.allcards.append(new_cards)
    
    
    def __str__(self):
        #Returns the number of cards the player has
        return f'Player {self.name} has {len(self.allcards)} cards.'

#Main logic of the game

#First define the names of both players
player_one=Player("player1")
player_two=Player("player2")

#Now, create a deck and shuffle it
new_deck=Deck()
new_deck.shuffle()

#divide the cards equally amongst both the players (a deck has 52 cards)
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

import pdb

game_on=True

print("Welcome!!")

round_num = 0
while game_on:
    
    round_num += 1
    #print the round number to keep track.
    print(f"Round {round_num}")
    
   
    if len(player_one.allcards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.allcards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    #check for a condition where both the players have an equal value on their card
    #This condition is called war
    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:

           
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            
            
            at_war = False
        
      
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            
            at_war = False

        else:
            print('WAR!')
            
            if len(player_one.allcards) < 5: #It can be any number other than 5 as well, depends on game rules.
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.allcards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player Two Loses!")
                game_on = False
                break
           
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

        
        
    



