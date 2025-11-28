from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            count = 0
            for j in range(i, n):
                if nums[j] == target:
                    count += 1

                if count > (j - i + 1) // 2:
                    total += 1
        
        return total
