from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(n - 1, i, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
            
            if nums[i] == target:
                result.append(i)

        return result