from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        n = len(nums)

        for k in range(l, min(n + 1, r + 1)):
            window_sum = sum(nums[:k])
            if window_sum > 0 and window_sum < min_sum:
                min_sum = window_sum

            for i in range(1, n - k + 1):
                window_sum = window_sum - nums[i - 1] + nums[i + k - 1]
                if window_sum > 0 and window_sum < min_sum:
                    min_sum = window_sum
        
        return min_sum if min_sum != float('inf') else -1
