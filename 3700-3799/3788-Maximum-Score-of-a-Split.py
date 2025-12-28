from typing import List


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        prefix_sum = 0
        max_score = float('-inf')
        for i in range(n - 1):
            prefix_sum += nums[i]
            score = prefix_sum - suffix_min[i + 1]
            max_score = max(max_score, score)

        return max_score
