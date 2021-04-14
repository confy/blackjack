CARD_CHARACTERS = {
    "clubs": {
        "A": "🃑",
        "2": "🃒",
        "3": "🃓",
        "4": "🃔",
        "5": "🃕",
        "6": "🃖",
        "7": "🃗",
        "8": "🃘",
        "9": "🃙",
        "10": "🃚",
        "J": "🃛",
        "Q": "🃝",
        "K": "🃞",
    },
    "diamonds": {
        "A": "🃁",
        "2": "🃂",
        "3": "🃃",
        "4": "🃄",
        "5": "🃅",
        "6": "🃆",
        "7": "🃇",
        "8": "🃈",
        "9": "🃉",
        "10": "🃊",
        "J": "🃋",
        "Q": "🃍",
        "K": "🃎",
    },
    "hearts": {
        "A": "🂱",
        "2": "🂲",
        "3": "🂳",
        "4": "🂴",
        "5": "🂵",
        "6": "🂶",
        "7": "🂷",
        "8": "🂸",
        "9": "🂹",
        "10": "🂺",
        "J": "🂻",
        "Q": "🂽",
        "K": "🂾",
    },
    "spades": {
        "A": "🂡",
        "2": "🂢",
        "3": "🂣",
        "4": "🂤",
        "5": "🂥",
        "6": "🂦",
        "7": "🂧",
        "8": "🂨",
        "9": "🂩",
        "10": "🂪",
        "J": "🂫",
        "Q": "🂭",
        "K": "🂮",
    }
}
CARD_VALUES = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
               "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
POSSIBLE_SUITS = ["clubs", "diamonds", "hearts", "spades"]
POSSIBLE_RANKS = ["A", "2", "3", "4", "5",
                  "6", "7", "8", "9", "10", "J", "Q", "K"]


WHITE = (255, 255, 255)
# GREEN = (53, 101, 77)
GREEN = (82, 152, 72)
BLUE = (16, 61, 135)
RED = (192, 17, 26)
YELLOW = (232, 200, 51)

WINDOW_SIZE = (1000, 800)
CARD_SIZE = (140, 190)
CARD_SPACING = 20
DEALER_OFFSET = (CARD_SPACING, CARD_SPACING)
PLAYER_OFFSET = (WINDOW_SIZE[1] - CARD_SIZE[1] - CARD_SPACING, CARD_SPACING)

DECK_SPACING = (125, 300)


BET_TXT_OFFSET = (400, 235)
BET_OFFSET = (400, 315)
HIT_OFFSET = (400, 395)
STAND_OFFSET = (400, 475)
BANK_TXT_OFFSET = (660, 332)
POT_TXT_OFFSET = (660, 392)


HAND_DONE_COLOR = (10, 50, 10)
HAND_DONE_MSG_RECT = (250, 300, 500, 200)
HAND_DONE_TXT_OFFSET = (320, 370)
