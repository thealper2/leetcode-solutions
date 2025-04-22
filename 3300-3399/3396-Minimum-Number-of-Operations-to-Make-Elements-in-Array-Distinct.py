from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(set(nums)) == len(nums):
            return 0
        
        c = 0
        while nums:
            if len(set(nums)) == len(nums):
                return c

            remove_count = min(3, len(nums))
            nums = nums[remove_count:]
            c += 1
        
        return c