'''
Simple Implementation of Player object.
'''
from cards import Guard, Priest, Baron, Handmaid, Prince, King, Countess, Princess, InvalidActionError


class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []
        self.protected = False
        self.eliminated = False
        # print("{} is a player".format(id))

    def draw_a_card(self, deck):
        self.hand.append(deck.draw_a_card())
        print("{} ({})holds {}".format(self.id, self.eliminated, self.hand))

    def discard_card(self,card):
        if card in self.hand:
            self.hand.remove(card)
        else:
            # report a card that cannot be discarded. For now no action taken.
            pass

    def play_card(self,played_card = None,other_player = None):
        if not played_card:
            played_card = self.hand[0]
        if not other_player:
            other_player = self
        if played_card in [Prince(),King()] and Countess() in self.hand:
            self.discard_card(Countess())
            played_card = Countess()
        else:
            try:
                played_card.action(other_player)
            except InvalidActionError as error:
                print('Ivalid Action: ' + error.errorMessage)
        print("{0} played {1}".format(self.id, played_card))
        self.discard_card(played_card)

    def __str__(self):
        return  "{0} holds {1}".format(self.id, ' and '.join(map(str,self.hand)))

