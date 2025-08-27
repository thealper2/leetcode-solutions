from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        min_row_flips = 0
        for i in range(m):
            l, r = 0, n - 1
            while l < r:
                if grid[i][l] != grid[i][r]:
                    min_row_flips += 1

                l += 1
                r -= 1

        min_col_flips = 0
        for j in range(n):
            t, b = 0, m - 1
            while t < b:
                if grid[t][j] != grid[b][j]:
                    min_col_flips += 1

                t += 1
                b -= 1

        return min(min_row_flips, min_col_flips)
