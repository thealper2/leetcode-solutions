from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        while n > k:
            nums.remove(min(nums))
            n -= 1

        return nums