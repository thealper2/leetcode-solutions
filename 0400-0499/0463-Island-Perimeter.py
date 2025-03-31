from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result += 4

                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        result -= 2

                    if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                        result -= 2

        return result
