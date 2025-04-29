from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        result = float('inf')
        n = len(nums)
        found = False

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        found = True
                        s = nums[i] + nums[j] + nums[k]
                        if s < result:
                            result = s

        return result if found else -1
        