from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        result = []
        z_c = 0
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                z_c += 1
        result.extend([0] * z_c)
        return result