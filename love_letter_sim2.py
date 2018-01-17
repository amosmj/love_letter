#!/usr/bin/env python
# For My Reference
# https://codereview.stackexchange.com/questions/42107/simple-card-game-to-learn-oop
# http://www.samyzaf.com/braude/OOP/PROJECTS/blackjack/blackjack.pdf
# http://code.activestate.com/recipes/578179-war-card-game-simulation/
"""
This is my attempt at building and OOP Love Letter Simulator
Apologies to AEG who created and sell Love Letter and it's many variants
It is not my intention that this should replace buying a physical copy of
Love Letter for anyone. Instead I am doing this to improve my coding skills
and to try and test my theory that Love Letter is very nearly random
"""
import random


class Card:
    def __init__(self, name, power):
        self.name = name
        self.power = power


class Deck:
    # Note: this deck dictionary is left over from a previous attempt.
    #       there is likely a better design to this but I don't know it for
    #       sure
    the_deck = {
        "Guard": [1, 5],
        "Priest": [2, 2],
        "Baron": [3, 2],
        "Handmaid": [4, 2],
        "Prince": [5, 2],
        "King": [6, 1],
        "Countess": [7, 1],
        "Princess": [8, 1],
    }

    # this is likely bad form, possibly will even throw and error but for now
    # I'm placing a function that will be called by the init funtion prior to
    # the __init__ function.
    def prepare_the_deck(self, the_deck, player_count):
        game_deck = []
        for card_type, details in the_deck.items():
            for card in ([card_type] * details[1]):
                game_deck.append(card)
        random.shuffle(game_deck)
        # note about next steps
        # per game rules, with 2 players you discard four cards blindly
        # with more than 2 players you discard only one card
        if player_count == 2:
            game_deck.pop()
            game_deck.pop()
            game_deck.pop()
        game_deck.pop()
        return game_deck

    def __init__(self, the_deck=the_deck, player_count=2):
        self.player_count = player_count
        self.game_deck = self.prepare_the_deck(the_deck, player_count)

    # I've debated if this is a deck action or a player action
    # I've settled on deck for now but could see this going the other way
    def draw_a_card(self):
        drawn_card = self.game_deck[0]
        self.game_deck.pop()
        print("You drew a {}".format(drawn_card))
        return drawn_card

# class Card:
    # def __init__(self):
        # self.names = ["Guard"]
        # self.power = range(1,8)
        # self.qty  = [5,3]
        # self.game_deck = []


class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []
        self.protected = False
        self.turn = False
        print("{} is a player".format(id))

    def draw_a_card(self, deck):
        self.hand.append(deck.draw_a_card())
        # print("{} holds {}".format(self.id,self.hand))


class Game:
    def __init__(self, players):
        self.over = False
        self.start_player = random.choice(players)


print("Welcome to Love Letter Simulator")
playerOne = Player("Alice")
playerTwo = Player("Bob")
# create a game object
# create the deck and randomize it
newGame = Game([playerOne, playerTwo])
game_deck = Deck()
game_deck.draw_a_card()
playerOne.draw_a_card(game_deck)
playerTwo.draw_a_card(game_deck)
while not newGame.over:
    print("yep, it's a loop")
    newGame.over = True

print("The Game is Over")

""" Captain's Log
    I didn't document Day 1 at all but I sat down and started working on this
    to quickly find that I don't know how to code OOP. I abandoned it for a
    function driven version but I couldn't shake the idea that I needed to come
    back to this

    Day 2 01/11/2018 (American Dates Ya'll, apologies)
    I returned to the OOP appraoch with renewed enthusiasm. I posted about it
    here (pay forum)
    https://forum.pythonistacafe.com/t/love-letter-simulator/1320
    I'm looking at this post to try and get the syntax and approach pointed in
    the right direction
    https://codereview.stackexchange.com/questions/42107/
             simple-card-game-to-learn-oop
    https://python.swaroopch.com/oop.html
    http://www.samyzaf.com/braude/OOP/PROJECTS/blackjack/blackjack.pdf
    Thos last two have been the most helpful
    At this time I have a Deck object that I am calling to make a deck and it
    seems to work but when I try to do anything else it breaks I have two
    player objects that I can create but haven't done much else with

    I can currently draw the first card from the deck but it's not actually
    removing it so I need to work on that
"""
