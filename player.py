'''
Player object represents each player and does much of the
heavy lifting for how cards work. The player plays a card,
discards it and so on.
The player object includes the player's hand as well
as an Eliminated flag for when the player is out of the game
'''

import card


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
        print("{} ({})holds {}".format(self.id, self.eliminated, self.hand))

    def check_hand(self):
        # specifically designed to deal with the Countess
        for carde in self.hand:
            if isinstance(carde, card.Countess):
                # print(self.hand)
                for c in self.hand:
                    if isinstance(c, card.King) or isinstance(c, card.Prince):
                        print("have to discard and end turn")
                        # JHA - we have to do something different here.
                        self.hand.remove(card)

    def play_card(self):
        # MA - I think playing a card is a player action that invokes
        # a card object. Many cards need a target but not all
        # I'm guessing I could do it better than the empty string
        # I have above but that's what I have now
        # JHA - I think the player object should be the one deciding which
        # card to play.  Therefore shouldn't need the params

        # for now, just removing first card
        played_card = self.hand[0]
        print("{0} played {1}".format(self.id, played_card))
        self.hand.pop(0)

    def compare_card(target):
        pass
        # discard Baron
        # compare cards and determine who is eliminated
        # eliminate player

    def __str__(self):
        if len(self.hand) == 1:
            return "{0} holds {1}".format(self.id, self.hand[0])
        else:
            return "{0} holds {1} and {2}".format(self.id, self.hand[0],
                                                  self.hand[1])
