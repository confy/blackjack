from .card import Card

class Hand():
    """ Class for player and dealer hands """
    def __init__(self, cards=[]):
        self._cards = cards
    
    def add_card(self, card):
        """ Adds cards to the hand """
        if not isinstance(card, Card):
            raise AttributeError("Only cards can be added")
        self._cards.append(card)
        
    def demote_first_ace(self):
        """ demotes the first ace in the hand"""
        for card in self._cards:
            if card.rank == 'A':
                card.demote()
                return
        
    @property
    def soft(self):
        """ returns true if the hand is 'soft' (meaning it has an ace with value 11)"""
        return any(card.rank == 'A' and card.value == 11 for card in self._cards)
    
    @property
    def value(self):
        """ Returns the total value of the hand """
        return sum(card.value for card in self._cards)