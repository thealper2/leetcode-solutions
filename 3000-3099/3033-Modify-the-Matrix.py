from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        answer = [row[:] for row in matrix]

        col_max = [-float('inf')] * n
        for j in range(n):
            for i in range(m):
                if matrix[i][j] > col_max[j]:
                    col_max[j] = matrix[i][j]

        for i in range(m):
            for j in range(n):
                if answer[i][j] == -1:
                    answer[i][j] = col_max[j]

        return answer