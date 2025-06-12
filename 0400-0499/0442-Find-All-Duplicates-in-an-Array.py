from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                duplicates.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
        
        return duplicates
