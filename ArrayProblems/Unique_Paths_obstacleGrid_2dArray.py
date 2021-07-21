from typing import List

'''A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.'''


class Solution:
    unique_path = 0

    def isBothOpen(self, i, j, row, column, obstacleGrid):
        if i + 1 < row and obstacleGrid[i + 1][j] == 0 and j + 1 < column and obstacleGrid[i][j + 1] == 0:
            return True
        return False

    def isRightOpen(self, i, j, row, column, obstacleGrid):
        if j + 1 < column and obstacleGrid[i][j + 1] == 0:
            return True
        return False

    def isDownOpen(self, i, j, row, column, obstacleGrid):
        if i + 1 < row and obstacleGrid[i + 1][j] == 0:
            return True
        return False

    def checkReachFinal(self, i, j, row, column, obstacleGrid):
        if i == row - 1 and j == column - 1:
            self.unique_path += 1
        elif self.isBothOpen(i, j, row, column, obstacleGrid):
            self.checkReachFinal(i, j + 1, row, column, obstacleGrid)
            self.checkReachFinal(i + 1, j, row, column, obstacleGrid)

        elif self.isRightOpen(i, j, row, column, obstacleGrid):
            self.checkReachFinal(i, j + 1, row, column, obstacleGrid)

        elif self.isDownOpen(i, j, row, column, obstacleGrid):
            self.checkReachFinal(i + 1, j, row, column, obstacleGrid)

        else:
            pass
        return self.unique_path

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        column = len(obstacleGrid[0])
        row = len(obstacleGrid)
        results = self.checkReachFinal(0, 0, row, column, obstacleGrid)
        return results
