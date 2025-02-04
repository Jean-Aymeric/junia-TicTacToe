from enum import Enum


class Score(Enum):
    WIN = 1
    LOOSE = -1
    DRAW = 0
    GAME_IN_PROGRESS = 2
