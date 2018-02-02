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
import cards
import deck
import player


class Game:
    def __init__(self, *args):
        # initialze deck
        self.deck = deck.Deck()

        # initialize players
        self.players = list()
        for arg in args:
            this_player = player.Player(arg, self.deck)
            self.players.append(this_player)

        random.shuffle(self.players)
        self.turn_order = itertools.cycle(self.players)

        # have the players draw their first cards in the proper order - need 
        # to do this after shuffling the players
        for this_player in self.players:
            this_player.draw_a_card()

        # set up the deck
        # note about next steps: per game rules, with 2 players you discard
        # four cards blindly with more than 2 players you discard only one card
        if len(self.players) == 2:
            print("Only two players - removing four cards from deck!")
            self._add_card_to_blind()
            self._add_card_to_blind()
            self._add_card_to_blind()
        self._add_card_to_blind()

    def _add_card_to_blind(self):
        card = self.deck.draw_a_card()
        print("Added {} to blind".format(card.name))

    def more_than_one_player(self):
        # JHA - I suspect there's a fancier way to do this
        foundFirst = False
        for this_player in self.players:
            if not this_player.eliminated:
                if foundFirst:
                    return True  # found second active player
                foundFirst = True
        return False

    def take_turn(self):
        this_player = next(self.turn_order)
        # JHA - TODO - this is unprotecting the player too late
        player.protected = False # effect of a previously played Handmaid expires
        if not this_player.eliminated:
            print("START TURN", this_player.id)
            this_player.draw_a_card()
            this_player.play_card(self.players)
        # test for game over conditions: only one player or deck empty
        return self.more_than_one_player() and len(self.deck) > 0

    def __str__(self):
        retval = "Players:\n"
        for this_player in self.players:
            retval += "\t{}\n".format(this_player)
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
    for this_player in range(int(player_count)):
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


if __name__ == '__main__':
    main()
