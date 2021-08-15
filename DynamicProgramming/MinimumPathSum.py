"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        height = len(grid)
        for i in range(height):
            for j in range(length):
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    smallest = min(grid[i][j-1], grid[i-1][j])
                    grid[i][j] += smallest
        return grid[-1][-1]