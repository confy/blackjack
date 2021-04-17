import pygame
from constants import (CARD_CHARACTERS, CARD_SIZE, CARD_VALUES, POSSIBLE_RANKS,
                       POSSIBLE_SUITS, WHITE)
from pygame.sprite import Sprite


class Card(Sprite):
    def __init__(self, suit: str, rank: str):
        """ Init one card """
        super().__init__()
        if suit not in POSSIBLE_SUITS:
            raise AttributeError(f"Suit must be in {POSSIBLE_SUITS}")
        if rank not in POSSIBLE_RANKS:
            raise AttributeError(f"Suit must be in {POSSIBLE_RANKS}")
        self.suit = suit
        self.rank = rank
        self.value = CARD_VALUES[rank]
        self.char = CARD_CHARACTERS[suit][rank]

    def demote(self):
        """ demotes aces value to 1 """
        if self.rank != "A":
            raise TypeError("Card must be an Ace")
        else:
            self.value = 1

    def update(self):
        """ Gets the card image and creates a card surface """
        surface = pygame.Surface(CARD_SIZE, pygame.SRCALPHA)
        card_filename = f"assets/sprites/card{self.suit.capitalize()}{self.rank}.png"
        card_image = pygame.image.load(card_filename)
        surface.blit(card_image, (0, 0))
        self.image = pygame.Surface.convert_alpha(surface)
        self.rect = self.image.get_rect()


class CardBack(Sprite):
    """ Class for the card backs, used in the deck display """

    def __init__(self):
        """ Init Card Back """
        super().__init__()

    def update(self):
        """ Gets the card image and creates a card surface """

        surface = pygame.Surface(CARD_SIZE, pygame.SRCALPHA)
        card_filename = f"assets/sprites/cardBack.png"
        card_image = pygame.image.load(card_filename).convert_alpha()
        surface.blit(card_image, (0, 0))
        self.image = surface
        self.rect = self.image.get_rect()
