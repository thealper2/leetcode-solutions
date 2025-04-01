from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        count = 0

        for num in nums:
            if num in d:
                count += d[num]
                d[num] += 1
            else:
                d[num] = 1

        return count