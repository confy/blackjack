import pygame
from pygame.sprite import Sprite
from constants import card_characters, possible_suits, possible_ranks, card_values, CARD_SIZE, WHITE


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
        
    def demote(self):
        """ demotes aces value to 1 """
        if self.rank != "A":
            raise TypeError("Card must be an Ace")
        else:
            self.value = 1
            
    def update(self):
        surface = pygame.Surface(CARD_SIZE)
        card_filename = f"assets/sprites/card{self.suit.capitalize()}{self.rank}.png"
        card_image = pygame.image.load(card_filename).convert_alpha()
        surface.blit(card_image,(0, 0))
        self.image = surface
        self.rect = self.image.get_rect()


if __name__ == "__main__":
    card = Card("spades", "10")
    print(card.value)
