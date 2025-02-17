from typing import Self

from Grid import Grid
from Score import Score


class Node:
    __grid: Grid
    __children: list[Self]

    def __init__(self, grid: Grid = None):
        if grid is None:
            self.__grid = Grid()
        else:
            self.__grid = grid
        self.__children = []

    def addChild(self, child: Self) -> None:
        if child == self:
            return
        self.__children.append(child)

    def countChildren(self) -> int:
        return len(self.__children)

    @property
    def Grid(self) -> Grid:
        return self.__grid

    @property
    def Children(self) -> list[Self]:
        return self.__children

    def generateChildren(self, playerSymbol: str, opponentSymbol: str, playerTurn: bool) -> None:
        if playerTurn:
            symbol = playerSymbol
        else:
            symbol = opponentSymbol
        possibleChoices = self.__grid.getPossibleChoices(symbol)
        for possibleChoice in possibleChoices:
            childGrid = Grid(self.__grid)
            childGrid.setTileXY(possibleChoice[0], possibleChoice[1], symbol)
            child = Node(childGrid)
            self.addChild(child)
            child.generateChildren(playerSymbol, opponentSymbol, not playerTurn)

    def __str__(self) -> str:
        result = str(self.__grid)
        score = self.__grid.getScore("X", "O")
        if score == Score.WIN:
            result += "X wins!\n"
        if score == Score.LOOSE:
            result += "X looses!\n"
        if score == Score.DRAW:
            result += "DRAW!\n"

        for child in self.__children:
            result += str(child)
        return result
