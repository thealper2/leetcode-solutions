from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        min_ = min(nums)
        max_ = max(nums)
        
        count = 0
        for num in nums:
            if num > min_ and num < max_:
                count += 1
        
        return count