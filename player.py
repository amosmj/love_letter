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

    def play_card(self,played_card = None,other_player = None):
        if not played_card:
            played_card = self.hand[0]
        if not other_player:
            other_player = self
        try:
            played_card.action(other_player)
        except InvalidActionError as error:
            print('Ivalid Action: ' + error.errorMessage)
        print("{0} played {1}".format(self.id, played_card))
        self.hand.pop(self.hand.index(played_card))

    def __str__(self):
        return  "{0} holds {1}".format(self.id, ' and '.join(map(str,self.hand)))

