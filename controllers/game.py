import pygame
from .base import PygameController
from models import Deck, Hand

from views import MainView

class GameController(PygameController):
    def __init__(self):
        pygame.init()
        # self.turn = "player"
        self._window = pygame.display.set_mode((800, 600))
        self._view = MainView(self._window)
        self.deck = Deck(2)
        
        
    def run(self):
        
        running = True
        self.new_hand()
        while running:
            self._view.display()
            
            mouse_pos = self._run_loop()
            
            if mouse_pos is False:
                running = False
                continue
            
            
            
    def new_hand(self):
        """ Creates a hand for each player and dealer and deals """
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        for _ in range(2):
             self.deal("player")
        self.deal("dealer")
        
    def deal(self, player:str) -> None:
        """ Deals the player or dealer one card from deck """
        new_card = self.deck.get_random_card()
        if player == "player":
            self.player_hand.add_card(new_card)
        elif player == "dealer":
            self.dealer_hand.add_card(new_card)
        else:
            raise ValueError("Invalid Player")
    def check_winner(self) -> str:
        """ Checks the winner of the hand """
        if self.dealer_hand.value == self.player_hand.value:
            return "Push Back"
        elif self.dealer_hand.value > self.player_hand.value:
            return "Loss"
        elif self.dealer_hand.value < self.player_hand.value:
            return "Winner"
        else:
            return "You broke the universe"
        
    def next_turn(self, player_action:str):
        if player_action == "hit":
            self.deal("player")
            if self.player_hand.value > 21:
                if self.player_hand.soft:
                    self.player_hand.demote_first_ace()
                    return
                else:
                    return "Bust"
        elif player_action == "stand":
            if self.dealer_hand.value < 17:
                self.deal("dealer")
                
                
def deal(hand, deck) -> None:
        """ Deals the player or dealer one card from deck """
        new_card = deck.get_random_card()
        hand.add_card(new_card)

if __name__ == "__main__":
    game = GameController()