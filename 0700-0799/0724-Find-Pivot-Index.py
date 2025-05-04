from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, sum(nums)
        
        for i in range(n):
            r -= nums[i]
            if l == r:
                return i
            
            l += nums[i]

        return -1