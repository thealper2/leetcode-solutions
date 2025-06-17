from collections import defaultdict
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        count_A = defaultdict(int)
        count_B = defaultdict(int)
        common = 0
        result = []
        
        for i in range(n):
            count_A[A[i]] += 1
            if count_A[A[i]] == 1 and count_B[A[i]] >= 1:
                common += 1
            elif count_A[A[i]] == 2 and count_B[A[i]] >= 1:
                common += 1
            
            count_B[B[i]] += 1
            if count_B[B[i]] == 1 and count_A[B[i]] >= 1:
                common += 1
            elif count_B[B[i]] == 2 and count_A[B[i]] >= 1:
                common += 1
            
            result.append(common)
        
        return result
