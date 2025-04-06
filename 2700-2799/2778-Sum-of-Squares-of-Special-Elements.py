from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                count += nums[i - 1] * nums[i - 1]

        return count