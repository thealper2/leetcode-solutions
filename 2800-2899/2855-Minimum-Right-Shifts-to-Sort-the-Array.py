from typing import List


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        decreases = 0
        pivot = 0
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                decreases += 1
                pivot = (i + 1) % n
        
        if decreases > 1:
            return -1
        
        if decreases == 0:
            return 0
        
        rotated = nums[pivot:] + nums[:pivot]
        for i in range(n - 1):
            if rotated[i] > rotated[i + 1]:
                return -1
        
        return (n - pivot) % n
