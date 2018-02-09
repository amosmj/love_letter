#!/usr/bin/env python
"""
Simple implementation for player object.  Always plays first card in list
against first found player.
"""
import cards


class Player:
    def __init__(self, id, deck):
        self.id = id
        self.deck = deck
        self.hand = []
        self.protected = False
        self.eliminated = False
        # print("{} is a player".format(id))

    def draw_a_card(self):
        card = self.deck.draw_a_card()
        print("{} drew {}".format(self.id, card.name))
        self.hand.append(card)

    def check_for_countess(self):
        # specifically designed to deal with the Countess
        for card in self.hand:
            if isinstance(card, cards.Countess):
                for c in self.hand:
                    if isinstance(c, cards.King) or \
                       isinstance(c, cards.Prince):
                        print("Prince/King matched with Countess")
                        self.hand.remove(card)
                        return card
        return None

    def find_first_player(self, players):
        for this_player in players:
            if not this_player.eliminated and \
               this_player is not self and \
               not this_player.protected:
                return this_player
        return None  # should never happen - but let's be safe

    def select_card_and_opponent(self, players):
        ''' Returns a tuple of opponent, card to play, and guess (in the case 
            of a Guard being played) '''
        opponent = self.find_first_player(players)

        played_card = self.check_for_countess()
        if not played_card:
            # for now, just removing first card
            played_card = self.hand[0]
            self.hand.pop(0)

        # for now we're always going to guess that the opponent has a baron
        guess = 3
        return opponent, played_card, guess

    def play_card(self, players):
        opponent, card, guess = self.select_card_and_opponent(players)
        print("{0} played {1} against {2} (guess {3})".format(self.id, 
                                                             card,
                                                             opponent.id,
                                                             guess))
        card.new_action(self, opponent, card, guess)

    def bad_play_card(self, players):

        opponent, card, guess = self.select_card_and_opponent(players)

        # JHA - not wild about this - consider making the action function
        # uniform
        print("{0} played {1}".format(self.id, played_card))
        if played_card.power == 1:
            # Guard
            other_player = self.find_first_player(players)
            played_card.action(other_player, 3)  # always guess baron for now
        elif played_card.power == 2:
            pass  # for now - need to get the place to hold 'knowledge'
        elif played_card.power == 3:
            other_player = self.find_first_player(players)
            if played_card.action(other_player, self.hand[0]):
                self.eliminate()
        elif played_card.power == 4:
            self.protected = True
        elif played_card.power == 5:
            other_player = self.find_first_player(players)
            played_card.action(other_player, self.hand[0])
        elif played_card.power == 6:
            other_player = self.find_first_player(players)
            played_card.action(self, other_player, self.hand[0])
        elif played_card.power == 7:
            played_card.action(self)
        elif played_card.power == 8:
            played_card.action(self)


        # At the end of this turn, if we DID NOT play a handmaid, set the
        # protected flag back off
        self.protected = False

    def eliminate(self):
        print("{} is Eliminated!".format(self.id))
        self.eliminated = True

    def is_card(self, guess):
        assert(len(self.hand) == 1)
        if self.hand[0].power == guess:
            self.eliminate()

    def get_card(self):
        return self.hand.pop()

    def set_card(self, card):
        self.hand.append(card)

    def compare_card(self, target):
        ''' Compare the passed-in card with our card.   Return true if our 
        card is higher than the passed-in card.  Eliminates this player if it is
        lower. '''
        print("In compare card.  mine:", self.hand[0])
        print("In compare card.  mine:", target)
        if self.hand[0].power > target.power:
            return True  # they lose!
        elif self.hand[0].power < target.power:
            self.eliminate()

        # return False if they're equal or we are eliminated
        return False

    def discard(self):
        card = self.hand.pop()
        print("{}: Forced discard of {}".format(self.id, card.name))
        if isinstance(card, cards.Princess):
            self.eliminate()
        else:
            # JHA TODO - need a discard pile for each player!
            self.draw_a_card()

    def __str__(self):
        prefix = ""
        if self.eliminated:
            prefix = "ELIM "
        if len(self.hand) == 0:
            return "{0}{1} holds no cards".format(prefix, self.id)
        elif len(self.hand) == 1:
            return "{0}{1} holds {2}".format(prefix, self.id, self.hand[0])
        else:
            return "{0}{1} holds {2} and {3}".format(prefix, self.id, self.hand[0],
                                                  self.hand[1])
