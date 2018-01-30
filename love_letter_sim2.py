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
from love_letter_cards import Guard,Priest,Baron,Handmaid,Prince,King,Countess,Princess 

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


class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []
        self.protected = False
        self.eliminated = False
        # print("{} is a player".format(id))

    def draw_a_card(self, deck):
        self.hand.append(deck.draw_a_card())
        self.check_hand()
        print("{} ({})holds {}".format(self.id, self.eliminated, self.hand))

    def check_hand(self):
        # specifically designed to deal with the Countess
        for card in self.hand:
            if isinstance(card, Countess):
                # print(self.hand)
                for c in self.hand:
                    if isinstance(c, King) or isinstance(c, Prince):
                        print("have to discard and end turn")
                        # JHA - we have to do something different here.
                        self.hand.remove(card)

    def play_card(self,other_player = None):
        # MA - I think playing a card is a player action that invokes
        # a card object. Many cards need a target but not all
        # I'm guessing I could do it better than the empty string
        # I have above but that's what I have now
        # JHA - I think the player object should be the one deciding which
        # card to play.  Therefore shouldn't need the params

        # for now, just removing first card
        played_card = self.hand[0]
        played_card.action(self,other_player)
        print("{0} played {1}".format(self.id, played_card))
        self.hand.pop(0)

    def __str__(self):
        if len(self.hand) == 1:
            return "{0} holds {1}".format(self.id, self.hand[0])
        else:
            return "{0} holds {1} and {2}".format(self.id, self.hand[0],
                                                  self.hand[1])


class Game:
    def __init__(self, *args):
        # initialze deck
        self.deck = Deck()

        # initialize players
        self.players = list()
        for arg in args:
            player = Player(arg)
            player.draw_a_card(self.deck)
            self.players.append(player)
        self.start_player = random.choice(self.players)

        random.shuffle(self.players)
        self.turn_order = itertools.cycle(self.players)

    def more_than_one_player(self):
        # JHA - I suspect there's a fancier way to do this
        foundFirst = False
        for player in self.players:
            if not player.eliminated:
                if foundFirst:
                    return True  # found second active player
                foundFirst = True
        return False

    def take_turn(self):
        player = next(self.turn_order)
        print("START TURN", player.id)
        if player.eliminated is False:
            # JHA - seems to me that the action a prince would have would be
            # to call 'discard()' on other player.  That player would be
            # responsible for playing card, and if princess: elminated =
            # True, else draw_card()
            if len(player.hand) is 0:  # deal with Prince
                player.draw_a_card(self.deck)
            player.draw_a_card(self.deck)
            # integers.  You're getting away with it due to the odd way that
            # Python treats ints < 256
            # if len(player.hand) is 2:  # deal with Countess
            # you dealt with countess when you drew the card?
            # player logic here
            # player.hand.pop(0)
        # test for game over conditions: only one player or deck empty
        return self.more_than_one_player() and len(self.deck) > 0

    def __str__(self):
        retval = "Players:\n"
        for player in self.players:
            retval += "\t{}\n".format(player)
        retval += "Deck:\n{}".format(self.deck)
        return retval

    def __repr__(self):
        ''' JHA probably should do something better than this '''
        return self.__str__()


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
# forces the players to be a fixed set
newGame = Game("Alice", "Bob", "Carol")
print(newGame)

while newGame.take_turn():
    print(newGame)

print("The Game is Over")
