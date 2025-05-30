import math
from math import gcd
from functools import reduce
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def compute_gcd(list_numbers):
            return reduce(lambda x, y: gcd(x, y), list_numbers)

        def compute_lcm(list_numbers):
            return reduce(lambda x, y: x * y // gcd(x, y), list_numbers)

        max_len = 0
        n = len(nums)
        for i in range(n):
            current_prod = 1
            current_gcd = nums[i]
            current_lcm = nums[i]
            for j in range(i, n):
                current_prod *= nums[j]
                current_gcd = gcd(current_gcd, nums[j])
                current_lcm = current_lcm * nums[j] // gcd(current_lcm, nums[j])
                if current_prod == current_gcd * current_lcm:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
        return max_len
