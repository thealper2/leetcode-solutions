from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = set()
        l, r = 0, len(nums) - 1
        nums.sort()

        while l < r:
            min_value = nums[l]
            max_value = nums[r]

            averages.add((min_value + max_value) / 2)

            l += 1
            r -= 1

        return len(averages)