class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['.' for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == n - 1:
                    grid[i][j] = '.'
                else:
                    grid[i][j] = '#'

        return [''.join(row) for row in grid]
