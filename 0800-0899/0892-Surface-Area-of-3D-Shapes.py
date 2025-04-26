from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    total += 2

                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            neighbor = grid[ni][nj]
                        else:
                            neighbor = 0

                        total += max(grid[i][j] - neighbor, 0)
        return total