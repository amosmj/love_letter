#!/usr/bin/env python

"""
This is a supporting module of love_letter_sim2 providing class description of the cards
"""
class Card:
    '''  NOTE: we should really make this class an abstract base class, but I'm
    skipping that step for the moment.  JHA 1/16/18 '''

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return "{:8}:\t{}".format(self.name, self.power)

    def action(self, player, other_card_in_hand):
        ''' Mike - this is the thought I had, but it's not playing out as
        cleanly as I would have hoped.  THe part of this whole thing that I
        don't have in my head is "how does the player decide which card to play
        against which other player AND which guess to make".  One interesting
        thought: I'm used to C++ where ALL overridden functions in subclasses
        need to have the same parameters (unless you do something special).
        It seems the action method on each card could be unique.  The player
        already will need to know which card she is playing and therefore
        can send the proper parameters (i.e. Guard will take (player, guess)
        while priest will just take player.)  The return values might need
        to be different as well.  Priest will return card value, others  will
        return ???
        '''
        # print("do {} action".format(self.name))
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

    def action(self, player, other_card_in_hand):
        print("do guard action")


class Priest(Card):
    '''When this card is played, its player is allowed to see another
    player's hand.'''

    def __init__(self):
        super().__init__("Priest", 2)

    def action(self, player, other_card_in_hand):
        print("do priest action")


class Baron(Card):
    '''When this card is played, its player will choose another
    player and privately compare hands. The player with the lower-
    strength hand is eliminated from the round.'''

    def __init__(self):
        super().__init__("Baron", 3)

    def action(self, player, other_card_in_hand):
        print("do baron action")
        #compare cards and eliminate one player unless its a draw

class Handmaid(Card):
    '''When this card is played, the player cannot be affected by any
    other player's card until the next turn.'''

    def __init__(self):
        super().__init__("Handmaid", 4)

    def action(self, player, other_card_in_hand):
        player.protected = True
        print("do Handmaid action")


class Prince(Card):
    '''When this card played, its player can choose any player (including
    themselves) to discard their hand and draw a new one. If that player
    discards the Princess, they are eliminated.'''

    def __init__(self):
        super().__init__("Prince", 5)

    def action(self, player, other_card_in_hand):
        print("do Prince action")


class King(Card):
    '''When this card is played, its player trades hands with any other
    player.'''

    def __init__(self):
        super().__init__("King", 6)

    def action(self, player, other_card_in_hand):
        print("do King action")


class Countess(Card):
    '''If a player holds both this card and either the King or Prince card,
    this card must be played immediately.'''

    def __init__(self):
        super().__init__("Countess", 7)

    def action(self, player, other_card_in_hand):
        print("do Countess action")


class Princess(Card):
    '''If a player plays this card for any reason, they are eliminated from the
    round.'''

    def __init__(self):
        super().__init__("Princess", 8)

    def action(self, player, other_card_in_hand):
        print("do Princess action")
