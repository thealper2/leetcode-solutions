from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(n):
            d = set()
            for j in range(i, n):
                d.add(nums[j])
                total += len(d) ** 2
        return total