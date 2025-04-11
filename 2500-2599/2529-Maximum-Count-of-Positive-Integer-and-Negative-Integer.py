from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p, n = 0, 0
        for num in nums:
            if num < 0:
                n += 1
            elif num > 0:
                p += 1

        return max(n, p)