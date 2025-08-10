from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        result = grid.copy()

        start_row = x
        end_row = min(x + k, n)
        start_col = y
        end_col = min(y + k, m)

        submatrix = [row[start_col:end_col] for row in grid[start_row:end_row]][::-1]

        for i in range(start_row, end_row):
            result[i][start_col:end_col] = submatrix[i - start_row]

        return result
