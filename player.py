'''
Simple Implementation of Player object.
'''
from cards import Guard, Priest, Baron, Handmaid, Prince, King, Countess, Princess, InvalidActionError


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.protected = False
        self.eliminated = False
        # print("{} is a player".format(id))

    def draw_a_card(self, deck):
        self.hand.append(deck.draw_a_card())
        print("{} ({})holds {}".format(self.name, self.eliminated, self.hand))

    def discard_card(self,card = None):
        if not card:
            card = self.hand[0]
        if card in self.hand:
            self.hand.remove(card)
            if card.power == 8: # discarding the Princess eliminates the player
                self.eliminated = True
                print("Player ",self.name, " got eliminated by discarding the princess")
        else:
            # report a card that cannot be discarded. For now no action taken.
            pass

    def play_card(self,played_card = None,other_player = None):
        if not played_card:
            played_card = self.hand[0]
        if not other_player or played_card.power == 4: # handmaid action cannot be applied on other player
            other_player = self
        if played_card in [Prince(),King()] and Countess() in self.hand:
            self.discard_card(Countess())
        elif other_player.protected:
            print("Action cannot be used as other player is protected by the Handmaid")
            pass
        else:
            try:
                self.discard_card(played_card)
                played_card.action(other_player)
            except InvalidActionError as error:
                print('Ivalid Action: ' + error.errorMessage)
                self.hand.append(played_card) # return the wrongly played card to hand.
        print("{0} played {1}".format(self.name, played_card))

    def __str__(self):
        return  "{0} holds {1}".format(self.name, ' and '.join(map(str,self.hand)))

