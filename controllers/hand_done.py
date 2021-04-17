from views import HandDoneView

from .base import PygameController


class HandDoneController(PygameController):
    """ Displays whenever the hand finishes """

    def __init__(self, message: str, profit: int):
        """ Init hand done Controller """
        self._view = HandDoneView(message, profit)

    def run(self, window):
        """ Display the hand done view and wait for input to finish """
        self._view.display(window)
        self._run_loop()
