from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        result = nums.pop(0)
        result += min(nums)
        nums.remove(min(nums))
        result += min(nums)
        return result