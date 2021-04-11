from .card import Card
class Hand():
    """ Class for player and dealer hands """
    def __init__(self):
        self._cards = []
    
    def add_card(self, card) -> None:
        """ Adds cards to the hand """
        if not isinstance(card, Card):
            raise AttributeError("Only cards can be added")
        self._cards.append(card)
        
    def demote_first_ace(self) -> None:
        """ demotes the first ace in the hand"""
        for card in self._cards:
            if card.rank == 'A':
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
    
    def serialize(self) -> str:
        """ Returns a readable representation of the hand """
        output = ' '.join(card.char for card in self._cards)
        output += " = " + str(self.value)
        return output
