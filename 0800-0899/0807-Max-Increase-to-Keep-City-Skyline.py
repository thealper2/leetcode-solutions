from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(n)) for j in range(n)]
        
        total = 0
        for i in range(n):
            for j in range(n):
                total += min(row_max[i], col_max[j]) - grid[i][j]
                
        return total
