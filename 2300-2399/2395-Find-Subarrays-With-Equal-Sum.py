from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum_indices = {}
        for i in range(len(nums) - 1):
            current_sum = nums[i] + nums[i + 1]
            if current_sum in sum_indices:
                for idx in sum_indices[current_sum]:
                    if idx != i:
                        return True
                sum_indices[current_sum].append(i)
            else:
                sum_indices[current_sum] = [i]
        return False