import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#Card class
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = value[rank]
    def __str__(self):
        return self.rank+" of "+self.suit

#Deck class
class Deck:
    
    def __init__(self):
        
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                #create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

#Player class
class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards=[]
    
    def remove_one(self):
    	#pop(0) removes the card from the top
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


# Game setup
player_one=Player("One")
player_two = Player("Two")

new_deck=Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
game_on = True

#Play the game
round_number=0
while game_on:
    round_number += 1
    print(f"Round:{round_number}")
    
    #checks if any player is out of cards
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on=False
        break
        
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on=False
        break
        
# start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    
# while at war
    at_war=True
    while at_war:
        if(player_one_cards[-1].value>player_two_cards[-1].value):
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            print(f"Player one won the round{round_number}")
            at_war = False
            
        elif(player_one_cards[-1].value<player_two_cards[-1].value):
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            print(f"Player two won the round{round_number}")
            at_war = False
            
        else:
            print("War!")
            #To end game quickly i chose 8 cards to drawn by each player once they are at war situation
            if len(player_one.all_cards)<8:
                print("Player one unable to declare war")
                print("Player two wins!")
                game_on = False
                break
            elif len(player_two.all_cards)<8:
                print("Player two unable to declare war")
                print("Player one wins!")
                game_on = False
                break
            else:
                for num in range(8):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    



