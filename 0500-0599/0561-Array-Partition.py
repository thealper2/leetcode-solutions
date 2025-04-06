from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        total = 0
        for i in range(0, n, 2):
            total += nums[i]
        
        return total