from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0] + nums[1]
        count = 1
        for i in range(2, n - 1, 2):
            if prev == nums[i] + nums[i + 1]:
                count += 1
            else:
                break

        return count