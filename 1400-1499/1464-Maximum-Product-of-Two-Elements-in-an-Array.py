from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float('-inf')
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if (nums[i] - 1) * (nums[j] - 1) > result:
                    result = (nums[i] - 1) * (nums[j] - 1)

        return result