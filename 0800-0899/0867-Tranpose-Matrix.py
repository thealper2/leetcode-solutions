from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        transposed = []
        for j in range(cols):
            new_row = []
            for i in range(rows):
                new_row.append(matrix[i][j])

            transposed.append(new_row)

        return transposed