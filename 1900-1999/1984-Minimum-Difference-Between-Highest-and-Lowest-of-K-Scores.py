from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        n = len(nums)
        nums.sort()

        min_diff = float('inf')
        for i in range(n - k + 1):
            diff = abs(nums[i] - nums[i + k - 1])
            min_diff = min(min_diff, diff)

        return min_diff