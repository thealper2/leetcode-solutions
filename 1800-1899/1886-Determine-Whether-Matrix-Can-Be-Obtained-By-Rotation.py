from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True

            mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]) - 1, -1, -1)]

        return False