from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row in matrix:
            if len(set(row)) != n:
                return False
            
        transposed = list(zip(*matrix))
        for col in transposed:
            if len(set(col)) != n:
                return False
            
        return True