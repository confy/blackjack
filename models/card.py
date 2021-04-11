import pygame
from pygame.sprite import Sprite
from .constants import card_characters, possible_suits, possible_ranks, card_values
CARD_SIZE = (140, 190)
WHITE = (255, 255, 255)


class Card(Sprite):
    def __init__(self, suit: str, rank: str):
        super().__init__()
        if suit not in possible_suits:
            raise AttributeError(f"Suit must be in {possible_suits}")
        if rank not in possible_ranks:
            raise AttributeError(f"Suit must be in {possible_ranks}")
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]
        self.char = card_characters[suit][rank]
        self.surface = pygame.Surface(CARD_SIZE)
        self.surface.fill(WHITE)
        card_filename = f"sprites/card{suit.capitalize()}{rank}.png"
        card_image = pygame.image.load(card_filename).convert_alpha()
        self.surface.blit(card_image,(0, 0))

        
    def demote(self):
        """ demotes aces value to 1 """
        if self.rank != "A":
            raise TypeError("Card must be an Ace")
        else:
            self.value = 1


if __name__ == "__main__":
    card = Card("spades", "10")
    print(card.value)
