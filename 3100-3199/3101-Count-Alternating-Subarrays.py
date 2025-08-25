from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        count = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                count += 1
            else:
                total += count * (count + 1) // 2
                count = 1

        total += count * (count + 1) // 2
        return total
