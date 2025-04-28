from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    s = nums[i] + nums[j] + nums[k]
                    for d in range(k + 1, n):
                        if nums[d] == s:
                            count += 1

        return count