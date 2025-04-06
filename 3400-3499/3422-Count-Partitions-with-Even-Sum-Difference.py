from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(1, n):
            left = sum(nums[:i])
            right = sum(nums[i:])
            diff = left - right
            if diff % 2 == 0:
                count += 1

        return count