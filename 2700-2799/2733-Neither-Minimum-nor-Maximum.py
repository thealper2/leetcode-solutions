from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mi = min(nums)
        ma = max(nums)

        for num in nums:
            if num != mi and num != ma:
                return num
            
        return -1