#!/usr/bin/env python

"""
This is my attempt at building and OOP Love Letter Simulator
Apologies to AEG who created and sell Love Letter and it's many variants
It is not my intention that this should replace buying a physical copy of
Love Letter for anyone. Instead I am doing this to improve my coding skills
and to try and test my theory that Love Letter is very nearly random
"""
import random
import itertools


class Card:
    '''  NOTE: we should really make this class an abstract base class, but I'm
    skipping that step for the moment.  JHA 1/16/18 '''

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return "{:8}:\t{}".format(self.name, self.power)

    def action(self):
        print("do {} action".format(self.name))
        pass

    # allows me to print a list of cards and have them be pretty
    __repr__ = __str__


class Guard(Card):
    '''When this card is played, its player designates another player
    and names a type of card. If that player's hand matches the type
    of card specified, that player is eliminated from the round.
    However, Guard cannot be named as the type of card.'''

    def __init__(self):
        super().__init__("Guard", 1)

    # def action(self):
        # print("do guard action")


class Priest(Card):
    '''When this card is played, its player is allowed to see another
    player's hand.'''

    def __init__(self):
        super().__init__("Priest", 2)

    def action(self):
        print("do priest action")


class Baron(Card):
    '''When this card is played, its player will choose another
    player and privately compare hands. The player with the lower-
    strength hand is eliminated from the round.'''

    def __init__(self):
        super().__init__("Baron", 3)

    def action(self):
        print("do baron action")


class Handmaid(Card):
    '''When this card is played, the player cannot be affected by any
    other player's card until the next turn.'''

    def __init__(self):
        super().__init__("Handmaid", 4)

    def action(self):
        print("do Handmaid action")


class Prince(Card):
    '''When this card played, its player can choose any player (including
    themselves) to discard their hand and draw a new one. If that player
    discards the Princess, they are eliminated.'''

    def __init__(self):
        super().__init__("Prince", 5)

    def action(self):
        print("do Prince action")


class King(Card):
    '''When this card is played, its player trades hands with any other player.'''

    def __init__(self):
        super().__init__("King", 6)

    def action(self):
        print("do King action")


class Countess(Card):
    '''If a player holds both this card and either the King or Prince card,
    this card must be played immediately.'''

    def __init__(self):
        super().__init__("Countess", 7)

    def action(self):
        print("do Countess action")


class Princess(Card):
    '''If a player plays this card for any reason, they are eliminated from the round.'''

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
        drawn_card = self.game_deck[len(self.game_deck) - 1]
        self.game_deck.pop(len(self.game_deck) - 1)
        # print(self.game_deck)
        # print("You drew a {}".format(drawn_card))
        return drawn_card


class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []
        self.protected = False
        self.eliminated = False
        print("{} is a player".format(id))

    def draw_a_card(self, deck):
        self.hand.append(deck.draw_a_card())
        self.check_hand()
        print("{} holds {}".format(self.id, self.hand))

    def check_hand(self):
        # specifically designed to deal with the Countess
        for card in self.hand:
            if isinstance(card, Countess):
                # print(self.hand)
                for c in self.hand:
                    if isinstance(c, King) or isinstance(c, Prince):
                        print("have to discard and end turn")
                        self.hand.remove(card)

    def play_card(card_name, target_name=""):
        pass
        # I think playing a card is a player action that invokes
        # a card object. Many cards need a target but not all
        # I'm guessing I could do it better than the empty string
        # I have above but that's what I have now

    def compare_card(target):
        pass
        # discard Baron
        # compare cards and determine who is eliminated
        # eliminate player


class Game:
    def __init__(self, players):
        self.over = False
        self.start_player = random.choice(players)
        # This varies turn order and makes it easier to loop through
        # the players sequentially. I still have it in the back of
        # my head that I eventually will add multiplayer support
        random.shuffle(players)
        self.turn_order = itertools.cycle(players)


print("Welcome to Love Letter Simulator")
# this following section works if a human actually
# wants to key in everything
# commenting out because I don't want to do that
# most of the time
'''
player_count = input("how many players? ")
players = []
for player in range(int(player_count)):
    player_name = input("input player name: ")
    players.append(Player(player_name))
'''
# This next line does all of the stuff above but just
# forces the players to be Alice and Bod
players = [Player("Alice")]
players.append(Player("Bob"))

# create a game object
# create the deck and randomize it
game = Game(players)
game_deck = Deck()
# print(game_deck)
for player in players:
    player.draw_a_card(game_deck)
for player in game.turn_order:
    if player.eliminated is False:
        if len(player.hand) is 0:  # deal with Prince
            player.draw_a_card(game_deck)
        player.draw_a_card(game_deck)
        if len(player.hand) is 2:  # deal with Countess
            # player logic here
            player.hand.pop(0)
        # test for game over conditions
        #  Deck empty
        if len(game_deck.game_deck) == 0:
            game.over = True
        #  all players but one eliminated
    if game.over is True:
        break


print("The Game is Over")
