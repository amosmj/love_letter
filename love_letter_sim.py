"""
Love Letter is a card game that came out from AEG some years ago
https://en.wikipedia.org/wiki/Love_Letter_(card_game)

I've played tens of games and probably hundreds of hands. It's light
and fun but I've never been able to shake the idea that the game is 
little better than a coin flip.

The purpose of this program is to create a script that lets players
play the game with some documentation of outcomes so that I can later 
analyze trends and outcomes

Finally, I hope to leave adequate hooks in place to hook a machine
learning tool up at to and simulte thousands of plays


Rules: https://web.archive.org/web/20160518034814/http://www.alderac.com/tempest/files/2012/09/Love_Letter_Rules_Final.pdf
"""

# my first pass at this will be extremely crude. I think I need to use
# classes to do this right but I've never done that

#import pandas as pd
import itertools
import random
import collections


# This is the deck layout. I have it here partially for my reference but 
# I also hope to make it functonal in the code
# name_of_card : card_power, qty_of_card, "card description"
the_deck = {"Guard": [1, 5, "When this card is played, its player designates" , 
                "another player and names a type of card. If that player's" ,
                "hand matches the type of card specified, that player is" , 
                "eliminated from the round. However, Guard cannot be named" ,
                "as the type of card"] ,
            "Priest" : [2, 2, "When this card is played, its player is allowed"
                "to see another player's hand"] ,
            "Baron": [3, 2, "When this card is played, its player will choose" ,
                "another player and privately compare hands. The player with the",
                "lower-strength hand is eliminated from the round."] ,
            "Handmaid" : [4, 2, "When this card is played, the player cannot be" ,
                "affected by any other player's card until the next turn"] ,
            "Prince" : [5, 2, "When this card played, its player can choose any player",
                "(including themselves) to discard their hand and draw a new one. If" ,
                "that player discards the Princess, they are eliminated"] ,
            "King" : [6, 1, "When this card is played, its player trades hands with" ,
                "any other player"] ,
            "Countess" : [7, 1, "If a player holds both this card and either the King" ,
                "or Prince card, this card must be played immediately."] ,
            "Princess" : [8 , 1, "If a player plays this card for any reason, they are" ,
                "eliminated from the round"]
            }

# Public knowledge will be. aplace for putting discarded cards
# in a human or AI game, this is reviewble by any player at any time
public_knowledge = []

# Active player will use and integer to identify a player who is "going"
# will refernce either a list or dictionary of players
active_player = 0

# until I figure out how to do this as a list of classes, I think
# I will need to lean on a dictionary to store info and a list to 
# call that info in an ordered manner
# dict should contain player_name: [player, hand]
# future additons are "knowledge of other players"
# AI or human (and any other things I come up with)
players = {}
player_order = []

### forcing players for now
players["Alice"] = None
players["Bob"] = None
player_order = random.shuffle(list(players.keys()))
print(players)

# I originally designed this, thinking I might try to play against it
# at some point but right now that is not my primary concern
# as such this is really only about half finished
def get_players():
    random_names = ["Bender", "Hal", "Alice", "Chip", "Joanna", "Johnny"]

    valid_player_count = False
    while valid_player_count == False:
        player_count = int(input("how many humans are playing?"))
        if 0 <= player_count <= 4:
            robot_count = int(input("how many bots are playing"))
            if 0 <= robot_count <= 4:
                if 2 <= robot_count + player_count <= 4:
                    valid_player_count = True
                else:
                    player_count = 0
                    robot_count = 0
                    print("your total number of humans and bots needs to be between 2 and 4")
        else:
            print("{} players passed to compare to {}".format(player_count, list(range(0,5))))
        players = []
        for player in range(player_count + robot_count):
            for human_player in range(player_count):
                player_name  = input("Please enter your name, it must be unique to other names used")
                while player_name in players:
                    player_name = input("I'm sorry but that appears to be a duplicate name, try again:")
                players.append(player_name)
            for player in range(robot_count):
                player_name = randome.randint(0, len(random_names)-1)
                while player_name in players:
                    player_name = randome.randint(0, len(random_names)-1)
                players.append(player_name)
                print( "{} has been assigned to your game".format(player_name))
    return players

# This builds the deck of the right number and distribution of cards then randomizes it into a list
# the result of this is meant to be handled from the front (0) to the back (len()-1)
# a number of cards are removed based on the number of players, this is done here too
def prepare_to_play(player_count):
    game_deck = []
    for card_type, details in the_deck.items():
        for card in ([card_type] * details[1]):
            game_deck.append(card)
    random.shuffle(game_deck)
    if player_count == 2:
        game_deck.pop()
        game_deck.pop()
        game_deck.pop()
    game_deck.pop()
    return(game_deck)


def give_player_card(game_deck,player):
    card = game_deck[0]
    game_deck.pop()
    return card

def discard_card(card):
    # this will end up being the real workhorse of this thing, coming back to it
    # I think that I have seen code for a using a dictionary as a case statement but
    # I'm not sure where I saw it or how to implement it
    # https://www.pydanny.com/why-doesnt-python-have-switch-case.html
    return False

def Guard():
    # guess a card number, if the player has it, they lose
    # can not guess Guard
    guess = 1
    guessable = game_deck.sort()
    while guess == 1:
        guess = range(len(game_deck))
    return guess

def Priest():
    # allows player to know another players card
    return False

def Baron():
    # compare cards, lower number loses
    return False

def Handmaid():
    # player is protected from other cards until next turn
    # not yet sure how I will handle this
    return False

def Prince():
    # Choose a player to discard their card
    # may inlcude player of card
    return False

def King():
    # when played, active player trades cards with another player
    return False

def Countess():
    # if the player holds this card and either the King or Prince, then
    # the player must discrd the Countess
    return False

def Princess():
    # if a player discards this card for any reason, they are out of the game
    return False



print(prepare_to_play(len(players)))