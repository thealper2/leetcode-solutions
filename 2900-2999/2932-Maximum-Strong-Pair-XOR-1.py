from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        m = 0
        for i in range(n):
            for j in range(i, n):
                x = nums[i]
                y = nums[j]
                if abs(x - y) <= min(x, y):
                    c = x ^ y
                    if m < c:
                        m = c

        return m