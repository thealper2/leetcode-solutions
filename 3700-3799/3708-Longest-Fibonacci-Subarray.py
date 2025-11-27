from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        max_len = 2
        length = 2

        for i in range(2, n):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                length += 1
            else:
                length = 2

            max_len = max(max_len, length)

        return max_len
