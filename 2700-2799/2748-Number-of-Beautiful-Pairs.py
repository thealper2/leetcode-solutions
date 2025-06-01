from typing import List
from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            temp = nums[i]
            first_digit = 0
            while temp > 0:
                first_digit = temp % 10
                temp //= 10

            for j in range(i + 1, n):
                last_digit = nums[j] % 10

                if gcd(first_digit, last_digit) == 1:
                    count += 1

        return count