from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(nums) % 3