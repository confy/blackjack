import pygame.font
from constants import WHITE, RED, BLUE, YELLOW
class Button:
    """ Root class for buttons """
    def __init__(self):
        self.button_text = str()
        self.button_color = tuple()
        self.txt_offset = 25

        
    def get_button_image(self):
        """ Creates a surface for the button and returns """
        font = pygame.font.SysFont("arial", 40, bold=True)
        dimensions = font.size(self.button_text)
        text = font.render(self.button_text, True, WHITE)
        surface = pygame.Surface((200, dimensions[1] + 10))
        surface.fill(self.button_color)
        surface.blit(text, (self.txt_offset, 5))
        
        return surface


class Hit(Button):
    def __init__(self):
        super().__init__()
        self.button_text = "Hit"
        self.button_color = BLUE
   
        
class Stand(Button):
    def __init__(self):
        super().__init__()
        self.button_text = "Stand"
        self.button_color = RED


class Bet(Button):
    def __init__(self):
        super().__init__()
        self.button_text = "Bet"
        self.button_color = YELLOW


