from enum import Enum

# State explanation:
# The board is represented using 18 bits (2 bits per cell) of an integer.
# The first 9 bits represent the X player (player 0), the next 9 bits represent the O player (player 1).
# Each cell is represented by a number from 0 to 8, where 0 is the top left cell and 8 is the bottom right cell.
# -------------
# | 0 | 1 | 2 |
# -------------
# | 3 | 4 | 5 |
# -------------
# | 6 | 7 | 8 |
# -------------

# The state is represented as an 18-bit integer in the following way:
# |-----------------------------------|-----------------------------------|
# |             Player O              |             Player X              |
# |-----------------------------------|-----------------------------------|
# | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
# |-----------------------------------|-----------------------------------|


class GameResult(Enum):
    ONGOING = 0
    X_WINS  = 1
    O_WINS  = 2
    DRAW    = 3


class Board():
    def __init__(self):
        self.state = 0

    def apply_move(self, position: int, player: int) -> GameResult:
        self.state |= ((1 << position) << (player * 9))
        return self.get_result()

    def get_result(self) -> GameResult:
        if \
            self.state & 7 == 7 or self.state & 56 == 56 or self.state & 448 == 448 or \
            self.state & 73 == 73 or self.state & 146 == 146 or self.state & 292 == 292 or \
            self.state & 84 == 84 or self.state & 273 == 273:
            return GameResult.X_WINS
        if \
            self.state & 3584 == 3584 or self.state & 28672 == 28672 or self.state & 229376 == 229376 or \
            self.state & 37376 == 37376 or self.state & 74752 == 74752 or self.state & 149504 == 149504 or \
            self.state & 43008 == 43008 or self.state & 139776 == 139776:
            return GameResult.O_WINS
        if ((self.state | (self.state >> 9)) & 511) == 511:
            return GameResult.DRAW
        return GameResult.ONGOING

    def get_valid_moves(self) -> int:
        return ((self.state | (self.state >> 9)) & 511) ^ 511

    def position_is_empty(self, position: int) -> bool:
        return self.state & (1 << position) == 0 and self.state & (1 << (position + 9)) == 0

    def position_contains_player(self, position: int, player: int) -> bool:
        return self.state & ((1 << position) << (player * 9)) != 0

    def get_position(self, position: int) -> int:
        if self.state & (1 << position): return 0
        if self.state & (1 << (position + 9)): return 1
        return 2

    def __str__(self) -> str:
        state_list = []
        for position in range(9):
            position_state = self.get_position(position)
            if position_state == 0: state_list.append("X")
            elif position_state == 1: state_list.append("O")
            else: state_list.append(" ")
        s = "-------------\n"
        s += f"| {state_list[0]} | {state_list[1]} | {state_list[2]} |\n"
        s += "-------------\n"
        s += f"| {state_list[3]} | {state_list[4]} | {state_list[5]} |\n"
        s += "-------------\n"
        s += f"| {state_list[6]} | {state_list[7]} | {state_list[8]} |\n"
        s += "-------------\n"
        return s

    def __repr__(self) -> str:
        return self.__str__()

