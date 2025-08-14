from typing import List


class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = float('inf')
        max_idx = float('-inf')

        for i in range(n):
            if self.is_prime(nums[i]):
                min_idx = min(min_idx, i)
                max_idx = max(max_idx, i)

        return abs(max_idx - min_idx)
