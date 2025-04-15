from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        r = set()
        for s, e in nums:
            r |= set(range(s, e + 1))

        return len(r)