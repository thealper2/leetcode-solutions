from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        result = [0] * n
        for j in range(n):
            max_len = 0
            for i in range(m):
                num = grid[i][j]
                if num < 0:
                    length = len(str(abs(num))) + 1
                else:
                    length = len(str(num))

                if length > max_len:
                    max_len = length
            result[j] = max_len

        return result