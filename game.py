'''
The game class manages game flow and some
mehanical rules that should not be left up
to the player
'''
import deck
import player
import random
import itertools


class Game:
    def __init__(self, *args):
        # initialze deck
        self.deck = deck.Deck()

        # initialize players
        self.players = list()
        for arg in args:
            p = player.Player(arg)
            p.draw_a_card(self.deck)
            self.players.append(player)
        self.start_player = random.choice(self.players)

        random.shuffle(self.players)
        self.turn_order = itertools.cycle(self.players)

    def more_than_one_player(self):
        # JHA - I suspect there's a fancier way to do this
        foundFirst = False
        for p in self.players:
            if not p.eliminated:
                if foundFirst:
                    return True  # found second active player
                foundFirst = True
        return False

    def take_turn(self):
        p = next(self.turn_order)
        print("START TURN", p.id)
        if p.eliminated is False:
            # JHA - seems to me that the action a prince would have would be
            # to call 'discard()' on other player.  That player would be
            # responsible for playing card, and if princess: elminated =
            # True, else draw_card()
            if len(p.hand) is 0:  # deal with Prince
                p.draw_a_card(self.deck)
            p.draw_a_card(self.deck)
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
        for p in self.players:
            retval += "\t{}\n".format(player)
        retval += "Deck:\n{}".format(self.deck)
        return retval

    def __repr__(self):
        ''' JHA probably should do something better than this '''
        return self.__str__()
