from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        count = 0
        for idx in range(len(nums)):
            temp = []
            i = idx
            while idx >= 1:
                temp.append(idx % 2)
                idx //= 2

            if sum(temp) == k:
                count += nums[i]

        return count