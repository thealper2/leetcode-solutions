from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops:
            a = min(op[0] for op in ops)
            b = min(op[1] for op in ops)
            return a * b

        return m * n