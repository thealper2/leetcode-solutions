from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        total = 0
        n = len(nums)

        for i in range(n):
            l = i - k
            r = i + k
            good = True

            if l >= 0 and nums[i] <= nums[l]:
                good = False

            if r < n and nums[i] <= nums[r]:
                good = False

            if good:
                total += nums[i]

        return total