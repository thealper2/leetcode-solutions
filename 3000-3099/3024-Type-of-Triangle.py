from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums

        if not (a + b > c and a + c > b and b + c > a):
            return "none"

        nums = set(nums)
        n = len(nums)

        if n == 1:
            return "equilateral"
        elif n == 2:
            return "isosceles"
        elif n == 3:
            return "scalene"