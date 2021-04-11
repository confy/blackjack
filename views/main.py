import pygame
from models import GREEN, Player

class MainView:
    def __init__(self, window):
        self._window = window
        
    def attach_hands(self, player:Player, dealer:Player):
        self.player = player
        self.dealer = dealer
    def display(self):
        self._window.fill(GREEN)
        self.player.update()
        self.dealer.update()
        self.player.draw(self._window)
        self.dealer.draw(self._window)
        pygame.display.flip()
        
        
