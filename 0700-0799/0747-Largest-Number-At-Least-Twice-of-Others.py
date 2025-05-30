from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m1 = max(nums)
        idx = nums.index(m1)
        nums.remove(m1)
        m2 = max(nums)
        if m1 >= m2 * 2:
            return idx

        return -1
