from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = []
        
        for i in range(m):
            if i % 2 == 0:
                result.extend(grid[i][::2])
            else:
                result.extend(grid[i][::-1][n%2::2])
        
        return result
