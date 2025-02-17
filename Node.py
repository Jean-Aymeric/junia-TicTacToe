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
        result = 1
        for child in self.__children:
            result += child.countChildren()
        return result

    @property
    def Grid(self) -> Grid:
        return self.__grid

    @property
    def Children(self) -> list[Self]:
        return self.__children

    def generateChildren(self, playerSymbol: str, opponentSymbol: str, playerTurn: bool) -> None:
        score = self.Grid.getScore(playerSymbol, opponentSymbol)
        if score == Score.GAME_IN_PROGRESS:
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

    def getGrade(self) -> (int, int, int):
        score = self.__grid.getScore("X", "O")
        if score == Score.WIN:
            return 1, 0, 0
        if score == Score.LOOSE:
            return 0, 1, 0
        if score == Score.DRAW:
            return 0, 0, 1
        win, loose, draw = 0, 0, 0
        for child in self.__children:
            result = child.getGrade()
            win += result[0]
            loose += result[1]
            draw += result[2]
        return win, loose, draw

    def getMaxGrid(self) -> Grid:
        maxGrade = 0
        maxGrid = None
        for child in self.__children:
            grade = child.getGrade()
            if self.rateGrade(grade) > maxGrade:
                maxGrade = self.rateGrade(grade)
                maxGrid = child.Grid
        return maxGrid

    def rateGrade(self, grade: (int, int, int)) -> float:
        return (2 * grade[0] - 2 * grade[1] - grade[2]) / (grade[0] + grade[1] + grade[2])
