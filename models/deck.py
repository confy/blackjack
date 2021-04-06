from .card import Card
from .constants import possible_suits, possible_ranks
import random

class Deck():
    """ Class for the dealer deck """
    def __init__(self, number_of_decks:int):
        self._cards = []
        for _ in range(number_of_decks):
            for suit in possible_suits:
                for rank in possible_ranks:
                    self._cards.append(Card(suit, rank))

    def get_random_card(self):
        """ gets random card, removes it and returns"""
        rand_id = random.randint(0, len(self._cards))
        return self._cards.pop(rand_id)
                    

    