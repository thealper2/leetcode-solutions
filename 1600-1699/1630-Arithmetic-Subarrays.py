from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        
        for i, j in zip(l, r):
            sub = nums[i:j+1]
            sub.sort()
            n = len(sub)
            is_arithmetic = True
            
            if n > 1:
                diff = sub[1] - sub[0]
                for k in range(2, n):
                    if sub[k] - sub[k-1] != diff:
                        is_arithmetic = False
                        break
            
            result.append(is_arithmetic)
        
        return result