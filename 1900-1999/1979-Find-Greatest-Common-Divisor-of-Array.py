from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)

        if b % a == 0:
            return a
        
        for i in range(a, 1, -1):
            if a % i == 0 and b % i == 0:
                return i

        return 1