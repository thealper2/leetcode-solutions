from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = []
        n = len(nums)
        for i in range(n - 1):
            if nums[i + 1] - nums[i] > 1:
                for x in range(nums[i] + 1, nums[i + 1]):
                    missing.append(x)

        return missing
