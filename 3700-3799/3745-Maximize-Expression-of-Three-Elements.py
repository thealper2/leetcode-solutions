from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        a = b = float('-inf')
        c = float('inf')

        for num in nums:
            if num > a:
                b = a
                a = num

            elif num > b:
                b = num

            if num < c:
                c = num

        return a + b - c
