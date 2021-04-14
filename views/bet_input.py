import pygame
from constants import BET_TXT_OFFSET, GREEN, WHITE


class BetInputView:
    def __init__(self):
        self.font = pygame.font.SysFont("arial", 40, bold=True)

    def display(self, window, bet_str):
        if bet_str == '':
            bet_str = '0'
        # pygame.draw.rect(
        #     window, GREEN, (BET_TXT_OFFSET[0], BET_TXT_OFFSET[1], 200, 55), 0)
        pygame.draw.rect(
            window, WHITE, (BET_TXT_OFFSET[0], BET_TXT_OFFSET[1], 200, 55), 1)
        window.blit(self.font.render('$' + bet_str, 1, WHITE),
                    (BET_TXT_OFFSET[0]+2, BET_TXT_OFFSET[1]+2))
        pygame.display.flip()
