from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) / 2
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        for k, v in d.items():
            if v == n:
                return k