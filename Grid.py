from typing import Self

from Score import Score

EMPTY = " "
SIZE = 3


class Grid:
    __tiles: list[list[str]]

    def __init__(self, grid: Self = None):
        if grid is not None:
            self.__tiles = [[tile for tile in row] for row in grid.__tiles]
        else:
            self.__tiles = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]

    def getTileXY(self, x: int, y: int) -> str:
        return self.__tiles[x][y]

    def setTileXY(self, x: int, y: int, value: str) -> None:
        self.__tiles[x][y] = value

    def __str__(self) -> str:
        result = ""
        for row in self.__tiles:
            result += "+---" * SIZE + "+\n"
            result += "|"
            for tile in row:
                result += f" {tile} |"
            result += "\n"
        result += "+---" * SIZE + "+\n"
        return result

    def getScore(self, playerSymbol: str, opponentSymbol: str) -> Score:
        if self.__isSymbolInARow(playerSymbol):
            return Score.WIN
        if self.__isSymbolInARow(opponentSymbol):
            return Score.LOOSE
        if self.__isFull():
            return Score.DRAW
        return Score.GAME_IN_PROGRESS

    def __isSymbolInARow(self, symbol: str) -> bool:
        for row in self.__tiles:
            if all([tile == symbol for tile in row]):
                return True
        for column in range(SIZE):
            if all([self.__tiles[row][column] == symbol for row in range(SIZE)]):
                return True
        if all([self.__tiles[i][i] == symbol for i in range(SIZE)]):
            return True
        if all([self.__tiles[i][SIZE - i - 1] == symbol for i in range(SIZE)]):
            return True
        return False

    def __isFull(self):
        for row in self.__tiles:
            for tile in row:
                if tile == EMPTY:
                    return False
        return True

    def getPossibleChoices(self, symbol: str) -> list[tuple[int, int]]:
        winChoice = self.__getWinChoice(symbol)
        if winChoice is not None:
            return [winChoice]
        return [(x, y) for x in range(SIZE) for y in range(SIZE) if self.__tiles[x][y] == EMPTY]

    def __getWinChoice(self, symbol: str):
        for x in range(SIZE):
            for y in range(SIZE):
                if self.__tiles[x][y] == EMPTY:
                    self.__tiles[x][y] = symbol
                    if self.__isSymbolInARow(symbol):
                        self.__tiles[x][y] = EMPTY
                        return x, y
                    self.__tiles[x][y] = EMPTY
        return None
