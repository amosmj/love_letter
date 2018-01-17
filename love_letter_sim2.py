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
    '''  NOTE: we should really make this class an abstract base class, but I'm
    skipping that step for the moment.  JHA 1/16/18 '''
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return "{:8}:\t{}".format(self.name, self.power)

    def action(self):
        ''' This is what will be called when the player plays this card. '''
        pass


class Guard(Card):
    def __init__(self):
        super().__init__("Guard", 1)

    def action(self):
        print("do guard action")


class Priest(Card):
    def __init__(self):
        super().__init__("Priest", 2)

    def action(self):
        print("do priest action")


class Baron(Card):
    def __init__(self):
        super().__init__("Baron", 3)

    def action(self):
        print("do baron action")


class Handmaid(Card):
    def __init__(self):
        super().__init__("Handmaid", 4)

    def action(self):
        print("do Handmaid action")


class Prince(Card):
    def __init__(self):
        super().__init__("Prince", 5)

    def action(self):
        print("do Prince action")


class King(Card):
    def __init__(self):
        super().__init__("King", 6)

    def action(self):
        print("do King action")


class Countess(Card):
    def __init__(self):
        super().__init__("Countess", 7)

    def action(self):
        print("do Countess action")


class Princess(Card):
    def __init__(self):
        super().__init__("Princess", 8)

    def action(self):
        print("do Princess action")


class Deck:
    def __init__(self, player_count=2):
        card_counts = [
            (Guard, 5),
            (Priest, 2),
            (Baron, 2),
            (Handmaid, 2),
            (Prince, 2),
            (King, 1),
            (Countess, 1),
            (Princess, 1),
        ]
        self.player_count = player_count
        self.game_deck = []
        for card_type, count in card_counts:
            for card in ([card_type()] * count):
                self.game_deck.append(card)
        random.shuffle(self.game_deck)
        # note about next steps: per game rules, with 2 players you discard
        # four cards blindly with more than 2 players you discard only one card
        if player_count == 2:
            self.game_deck.pop()
            self.game_deck.pop()
            self.game_deck.pop()
        self.game_deck.pop()

    def __str__(self):
        result = ""
        for card in self.game_deck:
            result += str(card) + "\n"
        return result

    # I've debated if this is a deck action or a player action
    # I've settled on deck for now but could see this going the other way
    def draw_a_card(self):
        drawn_card = self.game_deck[0]
        self.game_deck.pop()
        print("You drew a {}".format(drawn_card))
        return drawn_card


class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []
        self.protected = False
        self.turn = False  # JHA - not sure what turn is for?
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
print(game_deck)
# game_deck.draw_a_card()
# playerOne.draw_a_card(game_deck)
# playerTwo.draw_a_card(game_deck)
# while not newGame.over:
# print("yep, it's a loop")
# newGame.over = True

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
