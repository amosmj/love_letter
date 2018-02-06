'''
Simple Implementation of Player object.
'''
from cards import Guard, Priest, Baron, Handmaid, Prince, King, Countess, Princess


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
        return  "{0} holds {1}".format(self.id, ' and '.join(map(str,self.hand)))

