from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                if count == 1:
                    return False

                count += 1
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
        
        return True
