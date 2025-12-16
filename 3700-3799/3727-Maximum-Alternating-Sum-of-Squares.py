from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x, reverse=True, )
        k = (len(nums) + 1) // 2
        a = sum([x ** 2 for x in nums[:k]])
        b = sum([x ** 2 for x in nums[k:]])
        return a - b
