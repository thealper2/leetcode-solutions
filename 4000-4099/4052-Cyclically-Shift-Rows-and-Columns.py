class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        shifted = []
        for i in range(n):
            k = rowShift[i] % n
            shifted.append(grid[i][k:] + grid[i][:k])

        result = [[0] * n for _ in range(n)]
        for j in range(n):
            k = colShift[j] % n
            for i in range(n):
                result[(i - k + n) % n][j] = shifted[i][j]

        return result