from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        init_min = min(nums)
        init_max = max(nums)
        if init_max - init_min <= 2 * k:
            return 0
        
        new_max = init_max - k
        new_min = init_min + k
        return new_max - new_min