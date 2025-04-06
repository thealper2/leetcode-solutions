from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        operations = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                diff = nums[i-1] - nums[i] + 1
                operations += diff
                nums[i] += diff
        
        return operations