from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        valid_moves = 0
        cumulative_sum = 0
        total_sum = sum(nums)
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                if cumulative_sum * 2 == total_sum:
                    valid_moves += 2

                elif abs(cumulative_sum * 2 - total_sum) == 1:
                    valid_moves += 1

            cumulative_sum += nums[i]

        return valid_moves
