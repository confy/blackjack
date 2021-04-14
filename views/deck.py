from constants import DECK_SPACING
from models import CardBack
from pygame.sprite import Group


class DeckView(Group):
    """ View for the dummy deck in the middle of the screen """

    def __init__(self):
        super().__init__()
        for _ in range(12):
            self.add(CardBack())
        self.update()

        for i, sprite in enumerate(self.sprites()):
            # make 3d by slight offset
            sprite.rect.x += DECK_SPACING[0] + 3*i
            sprite.rect.y += DECK_SPACING[1] - 1*i
