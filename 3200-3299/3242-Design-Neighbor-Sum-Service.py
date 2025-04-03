from typing import List


class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.value_to_pos = {}
        for i in range(self.n):
            for j in range(self.n):
                self.value_to_pos[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        if value not in self.value_to_pos:
            return 0
        
        i, j = self.value_to_pos[value]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total = 0

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                total += self.grid[ni][nj]

            return total

    def diagonalSum(self, value: int) -> int:
        if value not in self.value_to_pos:
            return 0
        
        i, j = self.value_to_pos[value]
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        total = 0

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.n:
                total += self.grid[ni][nj]

        return total