from typing import Self

from Grid import Grid


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

    def generateChildren(self, playerSymbol: str, opponentSymbol: str) -> None:
        possibleChoices = self.__grid.getPossibleChoices(playerSymbol)
        for possibleChoice in possibleChoices:
            childGrid = Grid(self.__grid)
            childGrid.setTileXY(possibleChoice[0], possibleChoice[1], playerSymbol)
            child = Node(childGrid)
            self.addChild(child)
