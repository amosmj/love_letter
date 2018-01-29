'''
The deck is exactly what it sounds like, a deck of cards
See Card.py to understand the cards themselves
The Deck class primarily prepares the deck for the game
'''
# note for someone with more experience than me
# this file doesn't pass my linter
# it is looking for the cards and random
# not sure if this is critica
# MA
import card
import random


class Deck:
    def __init__(self, player_count=2):
        card_counts = [
            (card.Guard, 5),
            (card.Priest, 2),
            (card.Baron, 2),
            (card.Handmaid, 2),
            (card.Prince, 2),
            (card.King, 1),
            (card.Countess, 1),
            (card.Princess, 1),
        ]
        self.player_count = player_count
        self.game_deck = []
        for card_type, count in card_counts:
            for card.card in ([card_type()] * count):
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
        for c in self.game_deck:
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
