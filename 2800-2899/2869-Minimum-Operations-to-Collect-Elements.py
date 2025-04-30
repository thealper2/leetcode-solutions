from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = set()
        n = len(nums)
        i = n - 1

        while len(s) < k:
            if nums[i] <= k:
                s.add(nums[i])

            i -= 1

        return n - i - 1