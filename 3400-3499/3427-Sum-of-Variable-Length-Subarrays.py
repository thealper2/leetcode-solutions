from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        for i in range(n):
            start = max(0, i - nums[i])
            subarray_sum = sum(nums[start:i+1])
            total_sum += subarray_sum
        return total_sum