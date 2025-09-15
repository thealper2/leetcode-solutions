from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        set_nums = sorted(set_nums, reverse=True)
        return set_nums[:k]
