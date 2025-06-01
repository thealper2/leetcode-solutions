from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    continue
                    
                for k in range(j + 1, n):
                    if nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1
                        
        return count