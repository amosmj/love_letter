#!/usr/bin/env python

"""
Class to hold the deck - splitting this out allows us to use alternate 
'fixed' decks for testing.
"""
import random
import itertools
import cards
import player


class Deck:
    def __init__(self, player_count=2):
        card_counts = [
            (cards.Guard, 5),
            (cards.Priest, 2),
            (cards.Baron, 2),
            (cards.Handmaid, 2),
            (cards.Prince, 2),
            (cards.King, 1),
            (cards.Countess, 1),
            (cards.Princess, 1),
        ]
        self.player_count = player_count
        self.game_deck = []

        '''
        self.game_deck.append(cards.Guard())
        self.game_deck.append(cards.Guard())
        self.game_deck.append(cards.Guard())
        self.game_deck.append(cards.Guard())
        self.game_deck.append(cards.Guard())
        self.game_deck.append(cards.Priest())
        self.game_deck.append(cards.Priest())
        self.game_deck.append(cards.Baron())
        self.game_deck.append(cards.Baron())
        self.game_deck.append(cards.Handmaid())
        self.game_deck.append(cards.Handmaid())
        self.game_deck.append(cards.Prince())
        self.game_deck.append(cards.Prince())
        self.game_deck.append(cards.King())
        self.game_deck.append(cards.Countess())
        self.game_deck.append(cards.Princess())
        '''

        self.game_deck.append(cards.Priest())
        self.game_deck.append(cards.Countess())
        self.game_deck.append(cards.Prince())

        self.game_deck.append(cards.Guard())
        self.game_deck.append(cards.Handmaid())
        self.game_deck.append(cards.Princess())
        self.game_deck.append(cards.King())
        # self.game_deck.append(cards.Priest())
        # self.game_deck.append(cards.Priest())
        # self.game_deck.append(cards.Baron())
        # self.game_deck.append(cards.Handmaid())
        # self.game_deck.append(cards.Handmaid())
        # self.game_deck.append(cards.Prince())
        # self.game_deck.append(cards.King())
        # self.game_deck.append(cards.Countess())
        # self.game_deck.append(cards.Princess())


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


class FairDeck:
    ''' Need to do some testing with 'fixed' decks.  THis is the good one '''
    def __init__(self, player_count=2):
        card_counts = [
            (cards.Guard, 5),
            (cards.Priest, 2),
            (cards.Baron, 2),
            (cards.Handmaid, 2),
            (cards.Prince, 2),
            (cards.King, 1),
            (cards.Countess, 1),
            (cards.Princess, 1),
        ]
        self.player_count = player_count
        self.game_deck = []
        for card_type, count in card_counts:
            for card in ([card_type()] * count):
                self.game_deck.append(card)
        random.shuffle(self.game_deck)

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
