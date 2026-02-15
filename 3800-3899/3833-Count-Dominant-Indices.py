from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        dominant = 0
        for i in range(n - 1):
            total -= nums[i]
            avg = total / (n - i - 1)
            if nums[i] > avg:
                dominant += 1

        return dominant
