from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        flattened = []
        for row in grid:
            flattened.extend(row)
        
        freq = {}
        a = -1
        for num in flattened:
            if num in freq:
                a = num
            freq[num] = freq.get(num, 0) + 1
        
        total_numbers = n * n
        b = -1
        for num in range(1, total_numbers + 1):
            if num not in freq:
                b = num
                break
        
        return [a, b]