from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        min_ = float('inf')
        idx = 0

        while nums != sorted(nums):
            n = len(nums)
            for i in range(n - 1):
                if nums[i] + nums[i + 1] < min_:
                    min_ = nums[i] + nums[i + 1]
                    idx = i

            nums.pop(idx)
            nums[idx] = min_
            
            min_ = float('inf')
            idx = 0
            count += 1

        return count
