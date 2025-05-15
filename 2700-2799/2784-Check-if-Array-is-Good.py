from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        max_num = max(nums)
        if n != max_num + 1:
            return False
        
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1

        if freq[max_num] != 2:
            return False
        
        for i in range(1, max_num):
            if freq[i] != 1:
                return False
            
        return True