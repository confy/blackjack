import pygame
from models import Player
from constants import GREEN, STAND_OFFSET, HIT_OFFSET, BET_OFFSET, BET_TXT_OFFSET
from .button import Hit, Stand, Bet


class MainView:
    def __init__(self, window):
        self._window = window
        self._bet_button = Bet().get_button_image()
        self._hit_button = Hit().get_button_image()
        self._stand_button = Stand().get_button_image()
        
        
    def attach_hands(self, player:Player, dealer:Player):
        self.player = player
        self.dealer = dealer
        
        
    def display(self):
        self._window.fill(GREEN)
        self._window.blit(self._bet_button, BET_OFFSET)
        self._window.blit(self._hit_button, HIT_OFFSET)
        self._window.blit(self._stand_button, STAND_OFFSET)
        
        self.player.update()
        self.player.draw(self._window)
        
        self.dealer.update()
        self.dealer.draw(self._window)
        
        pygame.display.flip()
        
        
