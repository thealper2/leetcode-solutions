from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] - nums[j]) * nums[k] > max_val:
                        max_val = (nums[i] - nums[j]) * nums[k]

        return max_val