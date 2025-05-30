from collections import Counter


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2 * k:
            return False
        
        if k == 1:
            return True
        
        def is_strictly_increasing(sub):
            for i in range(len(sub)-1):
                if sub[i] >= sub[i+1]:
                    return False
            return True
        
        for i in range(n - 2*k + 1):
            first = nums[i:i+k]
            second = nums[i+k:i+2*k]
            if is_strictly_increasing(first) and is_strictly_increasing(second):
                return True
        
        return False
