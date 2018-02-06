#!/usr/bin/env python

"""
Class to hold the deck - spitting this out allows us to use alternate
'fixed' decks for testing.
"""
import random
import itertools
from cards import Guard,Priest,Baron,Handmaid,Prince,King,Countess,Princess 

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
            result += "\t{0}\n".format(card)
        return result

    def __len__(self):
        return len(self.game_deck)

    # I've debated if this is a deck action or a player action
    # I've settled on deck for now but could see this going the other way
    def draw_a_card(self):
        drawn_card = self.game_deck[len(self.game_deck) - 1]
        self.game_deck.pop(len(self.game_deck) - 1)
        # print(self.game_deck)
        # print("You drew a {}".format(drawn_card))
        return drawn_card
