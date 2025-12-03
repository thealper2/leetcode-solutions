from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_sum = 0
        for i in range(n // 2):
            max_sum = max(max_sum, nums[i] + nums[n - i - 1])

        return max_sum
