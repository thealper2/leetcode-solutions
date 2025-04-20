from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = 0

        while l <= r:
            if l == r:
                result += nums[l]
            else:
                result += int(str(nums[l]) + str(nums[r]))

            l += 1
            r -= 1

        return result
