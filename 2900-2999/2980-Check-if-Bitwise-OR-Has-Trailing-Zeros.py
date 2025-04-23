from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        c = 0
        for num in nums:
            if num % 2 == 0:
                c += 1

        return c >= 2