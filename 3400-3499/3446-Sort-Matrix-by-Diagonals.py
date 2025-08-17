from collections import defaultdict
from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)

        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])

        for d in diagonals:
            if d >= 0:
                diagonals[d].sort(reverse=True)
            else:
                diagonals[d].sort()

        for i in range(n):
            for j in range(n):
                grid[i][j] = diagonals[i - j].pop(0)
                
        return grid
