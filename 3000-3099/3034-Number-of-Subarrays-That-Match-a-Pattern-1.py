from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        k = len(pattern) + 1
        result = 0
        
        for i in range(n - k + 1):
            sub = nums[i:i + k]
            is_valid = True
            for j in range(k - 1):
                if pattern[j] == 1 and sub[j + 1] <= sub[j]:
                    is_valid = False
                    break
                elif pattern[j] == 0 and sub[j + 1] != sub[j]:
                    is_valid = False
                    break
                elif pattern[j] == -1 and sub[j + 1] >= sub[j]:
                    is_valid = False
                    break
            if is_valid:
                result += 1
        
        return result
