from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        positive_nums = [num for num in nums if num > 0]
        
        if not positive_nums:
            return max(nums)
        
        return sum(positive_nums)
