from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = -1
        min_ = float('inf')

        for num in nums:
            if num <= min_:
                min_ = num
            else:
                diff = max(diff, num - min_)

        return diff
