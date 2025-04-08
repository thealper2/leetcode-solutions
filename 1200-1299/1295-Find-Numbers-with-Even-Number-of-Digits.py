from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        r = 0
        for x in nums:
            x = str(x)
            if len(x) % 2 == 0:
                r += 1
        return r