from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        
        if m == 0 or n == 0:
            return True
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        
        return True