card_characters = {
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
card_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
possible_suits = ["clubs", "diamonds", "hearts", "spades"]
possible_ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


WHITE = (255, 255, 255)
GREEN = (53,101,77)
BLUE = (16, 61, 135)
RED = (192, 17, 26)
YELLOW = (232, 200, 51)

WINDOW_SIZE = (1000, 800)
CARD_SIZE = (140, 190)
CARD_SPACING = 20
DEALER_OFFSET = (CARD_SPACING, CARD_SPACING)
PLAYER_OFFSET = (WINDOW_SIZE[1] - CARD_SIZE[1] - CARD_SPACING ,CARD_SPACING)

BET_TXT_OFFSET = (0,0)
BET_OFFSET = (800,300)
HIT_OFFSET = (800,380)
STAND_OFFSET = (800,460)



LEVEL_DONE_COLOR = (10, 50, 10)
LEVEL_DONE_MSG_RECT = (250, 300, 500, 200)
LEVEL_DONE_TXT_OFFSET = (320, 370)