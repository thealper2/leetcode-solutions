from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n

        k = k % total_elements
        if k == 0:
            return grid
        
        flattened = [num for row in grid for num in row]
        shifted = flattened[-k:] + flattened[:-k]
        result = []

        for i in range(m):
            start = i * n
            end = start + n
            result.append(shifted[start:end])

        return result