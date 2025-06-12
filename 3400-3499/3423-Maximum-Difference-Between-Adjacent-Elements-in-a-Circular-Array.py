from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_distance = 0
        for i in range(n):
            max_distance = max(max_distance, abs(nums[i] - nums[i - 1]))

        return max_distance
