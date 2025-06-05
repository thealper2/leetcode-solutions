from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        max_sum = 0
        min_sub = []

        for num in nums:
            max_sum += num
            min_sub.append(num)

            if total - max_sum < max_sum:
                return min_sub

        return min_sub
