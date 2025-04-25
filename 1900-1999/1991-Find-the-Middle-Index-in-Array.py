from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        idx = -1
        n = len(nums)

        for i in range(n):
            if sum(nums[:i]) == sum(nums[i+1:]):
                idx = i
                break

        return idx