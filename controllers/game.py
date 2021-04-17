import os
from datetime import datetime

import pygame
from constants import WINDOW_SIZE
from models import Deck, Player
from views import MainView

from .base import PygameController
from .bet_input import BetInputController
from .hand_done import HandDoneController
from .post import post_hand

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


class GameController(PygameController):
    """ Main Game controller that spawns all controllers and views """

    def __init__(self):
        """ Initialize Game Controller """
        pygame.init()
        self._window = pygame.display.set_mode(WINDOW_SIZE)
        self.logo = pygame.image.load("assets/spades-32.png")
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Blackjack")

        self._view = MainView(self._window)
        self._bet_input = BetInputController()
        self._bet_input.run(self._view._window)

        self.deck = Deck(2)
        self.bet_curr_input = []
        self.hand_ongoing = False
        self.hand_pot = 0
        self.player_bal = 1000000

    def run(self):
        """ Main game loop"""

        while True:
            self.bet_str = ''.join(self.bet_curr_input)
            self._view.display(self.bet_str, self.player_bal, self.hand_pot)
            event = self._run_loop()
            if isinstance(event, int):
                # if int event is keyboard input
                self.bet_curr_input = self._bet_input.run(
                    self._view._window, event, self.bet_curr_input)

            if isinstance(event, tuple):
                # if tuple it is mouse position
                if self._view.has_clicked_bet(event) and not self.hand_ongoing:
                    self.bet()
                    self.reset_bet()
                    self.new_hand()

                elif self._view.has_clicked_hit(event) and self.hand_ongoing:
                    self.hit()

                elif self._view.has_clicked_stand(event) and self.hand_ongoing:
                    self.stand()

    def reset_bet(self):
        """ Resets the bet input text """
        self.bet_str = ''
        self.bet_curr_input = []

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
        if len(self.deck._cards) < 1:
            self.deck = Deck(2)
        new_card = self.deck.get_random_card()
        if player == "player":
            self.player_hand.add_card(new_card)
            if self.player_hand.value > 21 and self.player_hand.soft:
                self.player_hand.demote_first_ace()
        elif player == "dealer":
            self.dealer_hand.add_card(new_card)
            if self.dealer_hand.value > 21 and self.dealer_hand.soft:
                self.dealer_hand.demote_first_ace()
        else:
            raise ValueError("Invalid Player")
        self._view.attach_hands(self.player_hand, self.dealer_hand)

    def deal_dealer(self):
        """ Deals to the dealer until their hand is 17 or over """
        while self.dealer_hand.value < 17:
            self.deal('dealer')

    def bet(self):
        """ Runs when bet button is pressed, starts the hand, adds to the pot, deals a new hand"""
        self.hand_ongoing = True
        self.betAmount = 0 if self.bet_str == '' else int(self.bet_str)
        # bet cannot be more than players balance
        self.betAmount = min(self.betAmount, self.player_bal)
        self.hand_pot = self.betAmount * 2
        self.player_bal -= self.betAmount

    def hit(self):
        """ Runs when hit button is pressed """
        self.deal('player')
        if self.player_hand.value > 21:
            post_hand(self.serialize(-1))
            self.hand_ongoing = False
            profit = -self.hand_pot / 2
            self.hand_pot = 0
            hand_done_msg = 'Bust'
            self._view.display(self.bet_str, self.player_bal, self.hand_pot)

        if self.hand_ongoing == False:
            HandDoneController(hand_done_msg, profit).run(self._view._window)

        elif self.player_hand.value == 21:
            post_hand(self.serialize(1))
            self.hand_ongoing = False
            self.deal_dealer()
            result = self.check_winner()
            self._view.display(self.bet_str, self.player_bal, self.hand_pot)
            self.act_on_result(result)

    def stand(self):
        """ Runs when the Stand Button is clicked """
        self.hand_ongoing = False
        self.deal_dealer()
        self._view.display(self.bet_str, self.player_bal, self.hand_pot)
        result = self.check_winner()
        post_hand(self.serialize(result))
        self.act_on_result(result)

    def check_winner(self) -> int:
        """ Checks the winner of the hand """
        if self.dealer_hand.value > 21:
            return 1

        if self.dealer_hand.value == self.player_hand.value:
            # push back
            return 0
        elif self.dealer_hand.value > self.player_hand.value:
            # loss
            return -1
        elif self.dealer_hand.value < self.player_hand.value:
            # win
            return 1
        else:
            # ???
            return "You broke the universe"

    def act_on_result(self, result):
        """ Takes a win, loss or draw result and does the appropriate things"""
        if result == 1:
            # win
            profit = self.hand_pot
            self.player_bal += profit
            hand_done_msg = 'Win'

        elif result == 0:
            profit = self.hand_pot / 2
            self.player_bal += profit
            hand_done_msg = 'Draw'

        elif result == -1:
            profit = -self.hand_pot / 2
            hand_done_msg = 'Loss'

        HandDoneController(hand_done_msg, profit).run(self._view._window)

        self.hand_pot = 0

    def serialize(self, result):
        """ Takes a snapshot of the results of the round and serializes """
        date = datetime.now()
        if result == 1:
            result_str = "Win"
        elif result == 0:
            result_str = "Draw"
        elif result == -1:
            result_str = "Loss"

        return {
            "player_hand": self.player_hand.serialize(),
            "dealer_hand": self.dealer_hand.serialize(),
            "hand_pot": self.hand_pot,
            "player_bal": self.player_bal,
            "date": date.strftime('%Y-%m-%d-%H:%M:%S'),
            "result": result_str
        }
