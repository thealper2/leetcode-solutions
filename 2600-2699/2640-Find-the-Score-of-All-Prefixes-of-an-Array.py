from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        total = 0
        max_so_far = 0

        for i in range(n):
            max_so_far = max(max_so_far, nums[i])
            total += nums[i] + max_so_far
            result[i] = total
        
        return result
