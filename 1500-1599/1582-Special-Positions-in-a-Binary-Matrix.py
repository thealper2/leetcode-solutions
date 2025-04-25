from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        row_sums = [sum(row) for row in mat]
        col_sums = [0] * cols

        for i in range(rows):
            for j in range(cols):
                col_sums[j] += mat[i][j]

        special_count = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    special_count += 1

        return special_count