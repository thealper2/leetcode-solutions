from typing import List


class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        grid = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]

        def fill(x, y, current_size, start_val):
            if current_size == 1:
                grid[x][y] = start_val
                return

            half = current_size // 2
            # Top-right
            fill(x, y + half, half, start_val)
            # Bottom-right
            fill(x + half, y + half, half, start_val + half * half)
            # Bottom-left
            fill(x + half, y, half, start_val + 2 * half * half)
            # Top-left
            fill(x, y, half, start_val + 3 * half * half)

        fill(0, 0, 2 ** n, 0)
        return grid
