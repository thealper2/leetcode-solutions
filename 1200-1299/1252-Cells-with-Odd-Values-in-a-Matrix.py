from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        r = [0] * m
        c = [0] * n
        
        for ri, ci in indices:
            r[ri] += 1
            c[ci] += 1
        
        count = 0
        for i in range(m):
            for j in range(n):
                if (r[i] + c[j]) % 2 != 0:
                    count += 1
                    
        return count