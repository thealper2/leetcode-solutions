from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = arr[-1] + k + 1

        for i in range(1, n):
            if k == 0:
                return i

            if i not in arr:
                k -= 1

        return n