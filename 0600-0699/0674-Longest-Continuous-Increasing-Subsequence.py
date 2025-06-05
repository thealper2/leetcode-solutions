from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 1
        max_longest = 1

        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                longest += 1
                if longest > max_longest:
                    max_longest = longest

            else:
                longest = 1

        return max_longest
