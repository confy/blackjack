import pygame

from constants import WINDOW_SIZE, HAND_DONE_COLOR, HAND_DONE_MSG_RECT, HAND_DONE_TXT_OFFSET, WHITE


class HandDoneView:
    """ Displays a message when the hand is done: BUST, LOSS, WIN etc.
        Altered from Tims LevelDoneView. thx
    """

    def __init__(self, message: str, profit:int):
        self._message = message
        self._profit = profit
    
    def display(self, window):
        surface = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)

        surface.fill((0, 0, 0, 50))
        window.blit(surface, (0,0))
        
        pygame.draw.rect(window, HAND_DONE_COLOR, HAND_DONE_MSG_RECT)
        font = pygame.font.SysFont("arial", 48, bold=True)
        profit_str = self._profit
        if self._profit >= 0:
            profit_str = f"+{profit_str}"
        text = font.render(f"{self._message} | Profit: {profit_str}", True, WHITE)
        window.blit(text, HAND_DONE_TXT_OFFSET)
        pygame.display.flip()