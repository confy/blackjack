GREEN = (53,101,77)
import pygame
class MainView:
    def __init__(self, window):
        self._window = window
        
    def display(self):
        self._window.fill(GREEN)
        pygame.display.flip()
        
        
