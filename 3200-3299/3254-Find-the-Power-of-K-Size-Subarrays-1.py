from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n - k + 1):
            sub = nums[i:i+k]
            sorted_sub = sorted(sub)
            
            if (sub == sorted_sub and 
                sorted_sub[-1] - sorted_sub[0] == k - 1 and 
                len(set(sub)) == k):
                result.append(max(sub))
            else:
                result.append(-1)
        
        return result
