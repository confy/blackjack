import pygame
from constants import WINDOW_SIZE
from models import Deck, Player
from views import MainView

from .base import PygameController
from .bet_input import BetInputController
from .hand_done import HandDoneController


class GameController(PygameController):
    def __init__(self):
        pygame.init()
        # self.turn = "player"
        self._window = pygame.display.set_mode(WINDOW_SIZE)
        self.logo = pygame.image.load("assets/spades-32.png")
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Blackjack - Adrian Mc")
        pygame.mixer.init()
        # Song is Freddie Freeloader - Miles Davis
        # pygame.mixer.music.load("assets/freddie.mp3")
        # pygame.mixer.music.set_volume(0.2)
        # pygame.mixer.music.play()
        self._view = MainView(self._window)
        self._bet_input = BetInputController()
        self.deck = Deck(2)

    def run(self):

        running = True
        self.new_hand()
        self._bet_input.run(self._view._window)
        curr_bet = []
        while running:
            bet_str = ''.join(curr_bet)
            self._view.display(bet_str)
            event = self._run_loop()
            print(event)
            if isinstance(event, int):
                curr_bet = self._bet_input.run(
                    self._view._window, event, curr_bet)

            if isinstance(event, tuple):
                pass
                # if tuple it is mouse position

    def new_hand(self):
        """ Creates a hand for each player and dealer and deals """
        self.player_hand = Player("player")
        self.dealer_hand = Player("dealer")
        for _ in range(2):
            self.deal("player")
        self.deal("dealer")
        self._view.attach_hands(self.player_hand, self.dealer_hand)

    def deal(self, player: str) -> None:
        """ Deals the player or dealer one card from deck """
        new_card = self.deck.get_random_card()
        if player == "player":
            self.player_hand.add_card(new_card)
        elif player == "dealer":
            self.dealer_hand.add_card(new_card)
        else:
            raise ValueError("Invalid Player")
        self._view.attach_hands(self.player_hand, self.dealer_hand)

    def check_winner(self) -> str:
        """ Checks the winner of the hand """
        if self.dealer_hand.value == self.player_hand.value:
            return "Push Back"
        elif self.dealer_hand.value > self.player_hand.value:
            return "Loss!"
        elif self.dealer_hand.value < self.player_hand.value:
            return "Winner!"
        else:
            return "You broke the universe"

    def next_turn(self, player_action: str):
        if player_action == "hit":
            self.deal("player")
            if self.player_hand.value > 21:
                if self.player_hand.soft:
                    self.player_hand.demote_first_ace()
                    return
                else:
                    return "Bust"
        elif player_action == "stand":
            if self.dealer_hand.value < 17:
                self.deal("dealer")


def deal(hand, deck) -> None:
    """ Deals the player or dealer one card from deck """
    new_card = deck.get_random_card()
    hand.add_card(new_card)


if __name__ == "__main__":
    game = GameController()
