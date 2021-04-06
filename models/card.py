from .constants import card_characters, possible_suits, possible_ranks, card_values

class Card():
    def __init__(self, suit:str, rank:str):
        if suit not in possible_suits:
            raise AttributeError(f"Suit must be in {possible_suits}")
        if rank not in possible_ranks:
            raise AttributeError(f"Suit must be in {possible_ranks}")
        self.suit = suit
        self.rank = rank
        self.char = card_characters[suit][rank]
        self.value = card_values[rank]
        
    
    def demote(self):
        """ demotes aces value to 1 """
        if self.rank != "A":
            raise TypeError("Card must be an Ace")
        else:
            self.value = 1
        
    
        
        

if __name__ == "__main__":
    card = Card("spades", "10")
    print(card.value)