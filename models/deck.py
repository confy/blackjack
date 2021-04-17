import random

from constants import POSSIBLE_RANKS, POSSIBLE_SUITS

from .card import Card


class Deck():
    """ Class for the dealer deck """

    def __init__(self, number_of_decks: int):
        """ Init the deck of cards """
        self._cards = []
        for _ in range(number_of_decks):
            for suit in POSSIBLE_SUITS:
                for rank in POSSIBLE_RANKS:
                    self._cards.append(Card(suit, rank))

    def get_random_card(self):
        """ gets random card, removes it and returns"""
        length = len(self._cards) - 1
        rand_id = random.randint(0, length)
        return self._cards.pop(rand_id)
