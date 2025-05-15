from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = -1
        total = 0
        
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
            total += num
        
        expected_sum = n * (n + 1) // 2
        missing = expected_sum - (total - duplicate)
        
        return [duplicate, missing]
