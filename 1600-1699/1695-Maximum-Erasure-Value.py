from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0 
        current_sum = 0
        seen = set()
        l = 0

        for r in range(n):
            while nums[r] in seen:
                seen.remove(nums[l])
                current_sum -= nums[l]
                l += 1

            seen.add(nums[r])
            current_sum += nums[r]
            max_sum = max(max_sum, current_sum)

        return max_sum
