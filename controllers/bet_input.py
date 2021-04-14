from pygame.locals import K_BACKSPACE
from views import BetInputView


class BetInputController:
    """ Controller for the BetInput Text box """

    def __init__(self):
        self._view = BetInputView()

    def run(self, window, key=0, curr_bet=[]):
        if key == K_BACKSPACE:
            curr_bet = curr_bet[0:-1]
        elif key <= 127:
            char = chr(key)
            if char.isnumeric():
                curr_bet.append(chr(key))
        self._view.display(window, "$" + ''.join(curr_bet))
        return curr_bet
