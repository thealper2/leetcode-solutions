from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        current_inc = 1
        current_dec = 1
        best_inc = 1
        best_dec = 1

        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                current_inc += 1
                current_dec = 1
            elif nums[i] > nums[i + 1]:
                current_dec += 1
                current_inc = 1
            elif nums[i] == nums[i + 1]:
                current_inc = 1
                current_dec = 1

            best_inc = max(current_inc, best_inc)
            best_dec = max(current_dec, best_dec)

        return max(best_inc, best_dec)