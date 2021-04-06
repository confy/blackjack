from .constants import card_characters, possible_suits, possible_ranks, card_values

class Card():
    def __init__(self, suit:str, rank:str):
        if suit not in possible_suits:
            raise AttributeError(f"Suit must be in {possible_suits}")
        if rank not in possible_ranks:
            raise AttributeError(f"Suit must be in {possible_ranks}")
        self._suit = suit
        self._rank = rank
        self._char = card_characters[suit][rank]
        self._value = card_values[rank]
        
        
    @property
    def suit(self):
        """ Getter for the suit """
        return self._suit
    
    @property
    def rank(self):
        """ Getter for the rank """
        return self._rank
    
    @property
    def char(self):
        """ getter for the card character string"""
        return self._char
    
    @property
    def value(self):
        """ getter for value """
        return self._value
    
    def demote(self):
        """ demotes aces value to 1 """
        if self._rank != "A":
            raise TypeError("Card must be an Ace")
        else:
            self._value = 1
        
    
        
        

if __name__ == "__main__":
    card = Card("spades", "10")
    print(card.value)