from views import HandDoneView
from .base import PygameController


class HandDoneController(PygameController):
    def __init__(self, message: str, profit: int):
        self._view = HandDoneView(message, profit)

    def run(self, window):
        self._view.display(window)
        self._run_loop()
