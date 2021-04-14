from constants import CARD_SIZE, CARD_SPACING, DEALER_OFFSET, PLAYER_OFFSET
from pygame.sprite import Group

from .card import Card


class Player(Group):
    """ Class for player and dealer hands """

    def __init__(self, name: str, money: int):
        super().__init__()
        self._cards = []
        self._name = name
        self._money = money

    def add_card(self, card) -> None:
        """ Adds cards to the hand """
        if not isinstance(card, Card):
            raise AttributeError("Only cards can be added")
        self._cards.append(card)
        self.add(card)

    def demote_first_ace(self) -> None:
        """ demotes the first ace in the hand"""
        for card in self._cards:
            if card.rank == 'A' and card.value == 11:
                card.demote()
                return

    @property
    def soft(self) -> bool:
        """ returns true if the hand is 'soft' (meaning it has an ace with value 11)"""
        return any(card.rank == 'A' and card.value == 11 for card in self._cards)

    @property
    def value(self) -> int:
        """ Returns the total value of the hand """
        return sum(card.value for card in self._cards)

    def update(self):
        super().update()
        for i, sprite in enumerate(self.sprites()):
            sprite.rect.x = i * (CARD_SIZE[0]+5) + CARD_SPACING
            if self._name == 'player':
                sprite.rect.y = PLAYER_OFFSET[0]
            elif self._name == 'dealer':
                sprite.rect.y = CARD_SPACING

    def serialize(self) -> str:
        """ Returns a unicode representation of the hand for web api"""
        output = ' '.join(card.char for card in self._cards)
        output += " = " + str(self.value)
        return output
