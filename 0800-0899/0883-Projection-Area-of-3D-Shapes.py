from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy_area = 0
        yz_area = 0
        zx_area = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    xy_area += 1
        
        for j in range(n):
            max_col = 0
            for i in range(n):
                if grid[i][j] > max_col:
                    max_col = grid[i][j]
            yz_area += max_col
        
        for i in range(n):
            max_row = max(grid[i])
            zx_area += max_row
        
        return xy_area + yz_area + zx_area