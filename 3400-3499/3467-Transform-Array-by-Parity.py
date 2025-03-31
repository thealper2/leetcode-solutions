from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        count_0 = sum(1 for num in nums if num % 2 == 0)
        return [0] * count_0 + [1] * (len(nums) - count_0)