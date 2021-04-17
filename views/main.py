import pygame
from constants import (BANK_TXT_OFFSET, BET_OFFSET, HIT_OFFSET, POT_TXT_OFFSET,
                       STAND_OFFSET, WHITE)
from models import Player

from .bet_input import BetInputView
from .button import Bet, Hit, Stand
from .deck import DeckView


class MainView:
    def __init__(self, window):
        self._window = window
        self._bet_button = Bet().get_button_image()
        self._hit_button = Hit().get_button_image()
        self._stand_button = Stand().get_button_image()
        self._bet_input = BetInputView()
        self._deck = DeckView()
        self._font = pygame.font.SysFont("arial", 36, bold=True)
        self._background = pygame.image.load('assets/greenfelt.png')
        
        pygame.mixer.init()
        # Song is Freddie Freeloader - Miles Davis
        pygame.mixer.music.load("assets/freddie.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def display(self, bet_str, player_bal, hand_pot):
        self._window.blit(self._background, (0, 0))
        self._window.blit(self._bet_button, BET_OFFSET)
        self._window.blit(self._hit_button, HIT_OFFSET)
        self._window.blit(self._stand_button, STAND_OFFSET)
        self._bet_input.display(self._window, bet_str)
        self._deck.draw(self._window)
        if hasattr(self, 'player'):
            # Only display hands if they exist
            self.player.update()
            self.player.draw(self._window)

            self.dealer.update()
            self.dealer.draw(self._window)
        self._window.blit(self.create_text(
            f"You have ${int(player_bal)}"), BANK_TXT_OFFSET)
        self._window.blit(self.create_text(
            f"Current pot is ${int(hand_pot)}"), POT_TXT_OFFSET)

        pygame.display.flip()

    def attach_hands(self, player: Player, dealer: Player):
        self.player = player
        self.dealer = dealer

    def create_text(self, text):
        return self._font.render(text, 1, WHITE)

    def has_clicked_bet(self, pos):
        """ Returns true if the bet button has been clicked """
        return bool(self._bet_button.get_rect(topleft=BET_OFFSET).collidepoint(pos))

    def has_clicked_hit(self, pos):
        """ Returns true if the hit button has been clicked """
        return bool(self._hit_button.get_rect(topleft=HIT_OFFSET).collidepoint(pos))

    def has_clicked_stand(self, pos):
        """ Returns true if the stand button has been clicked """
        return bool(self._stand_button.get_rect(topleft=STAND_OFFSET).collidepoint(pos))
