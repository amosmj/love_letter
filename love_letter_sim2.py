'''
Implementation of the popular card game Love Letters.
DISCLAIMER: This work is for practicing purposes only.
'''
import random
import itertools
from deck import Deck
from player import Player



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
        return len([player for player in self.players if player.eliminated == False]) > 1

    def take_turn(self):
        player = next(self.turn_order)
        player.protected = False # effect of a previously played Handmaid expires
        print("START TURN", player.name)
        if player.eliminated is False:
            player.draw_a_card(self.deck)
            player.play_card()
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

def main():
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

if  __name__ == '__main__':
    main()
