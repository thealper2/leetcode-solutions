from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []

        while nums:
            m = min(nums)
            l = max(nums)

            averages.append((m + l) / 2)

            nums.remove(m)
            nums.remove(l)

        return min(averages)