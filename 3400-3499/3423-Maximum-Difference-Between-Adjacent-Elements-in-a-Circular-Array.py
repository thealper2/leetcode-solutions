from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = 0
        for i in range(n):
            curr = nums[i]
            next_num = nums[(i + 1) % n]
            diff = abs(curr - next_num)
            if diff > max_diff:
                max_diff = diff

        return max_diff