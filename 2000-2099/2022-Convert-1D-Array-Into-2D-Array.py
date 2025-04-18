from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n * m != len(original):
            return []
        
        result = [[0] * n for _ in range(m)]
        idx = 0

        for i in range(m):
            for j in range(n):
                result[i][j] = original[idx]
                idx += 1

        return result