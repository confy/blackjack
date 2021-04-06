import random
from .card import Card


class Hand():
    def __init__(self, cards=[]):
        self._cards = cards
    
    def add_card(self, card):
        """ Adds cards to the hand """
        if not isinstance(card, Card):
            raise AttributeError("Only cards can be added")
        self._cards.append(card)
    
    def get_random_card(self):
        """ gets random card, removes it and returns"""
        rand_id = random.randint(0, len(self._cards))
        return self._cards.pop(rand_id)
        
        
    @property
    def value(self):
        """ Returns the total value of the hand """