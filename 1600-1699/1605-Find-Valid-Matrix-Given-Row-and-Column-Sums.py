from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                min_val = min(rowSum[i], colSum[j])
                matrix[i][j] = min_val
                rowSum[i] -= min_val
                colSum[j] -= min_val
        
        return matrix
