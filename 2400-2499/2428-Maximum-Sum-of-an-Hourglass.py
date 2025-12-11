from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_sum = float('-inf')
        for i in range(n - 2):
            for j in range(m - 2):
                total = (
                    grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + 
                    grid[i + 1][j + 1] +
                    grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                )

                max_sum = max(max_sum, total)

        return max_sum
