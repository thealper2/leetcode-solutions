from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)

        for x, y in queries:
            diff[x] += 1
            if y + 1 < n:
                diff[y + 1] -= 1

        curr = 0
        for i in range(n):
            curr += diff[i]
            if nums[i] > curr:
                return False

        return True
