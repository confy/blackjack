import pygame
from constants import (BET_OFFSET, BET_TXT_OFFSET, GREEN, HIT_OFFSET,
                       STAND_OFFSET)
from models import Player

from .bet_input import BetInputView
from .button import Bet, Hit, Stand


class MainView:
    def __init__(self, window):
        self._window = window
        self._bet_button = Bet().get_button_image()
        self._hit_button = Hit().get_button_image()
        self._stand_button = Stand().get_button_image()
        self._bet_input = BetInputView()

    def display(self, bet_str):
        self._window.fill(GREEN)
        self._window.blit(self._bet_button, BET_OFFSET)
        self._window.blit(self._hit_button, HIT_OFFSET)
        self._window.blit(self._stand_button, STAND_OFFSET)
        self._bet_input.display(self._window, bet_str)
        self.player.update()
        self.player.draw(self._window)

        self.dealer.update()
        self.dealer.draw(self._window)

        pygame.display.flip()

    def attach_hands(self, player: Player, dealer: Player):
        self.player = player
        self.dealer = dealer

    def has_clicked_bet(self, pos):
        """ Returns true if the bet button has been clicked """
        return bool(self._bet_button.get_rect().collidepoint(pos))

    def has_clicked_hit(self, pos):
        """ Returns true if the hit button has been clicked """
        return bool(self._hit_button.get_rect().collidepoint(pos))

    def has_clicked_stand(self, pos):
        """ Returns true if the stand button has been clicked """
        return bool(self._stand_button.get_rect().collidepoint(pos))
