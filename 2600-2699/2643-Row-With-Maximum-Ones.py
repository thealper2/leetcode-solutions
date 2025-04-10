from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx = 0
        c = 0

        for i in range(len(mat)):
            s = sum(mat[i])
            if s > c:
                idx = i
                c = s

        return [idx, c]