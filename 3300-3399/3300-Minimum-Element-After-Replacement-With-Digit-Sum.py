from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        minimum = float('inf')
        for num in nums:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10

            if s < minimum:
                minimum = s

        return minimum