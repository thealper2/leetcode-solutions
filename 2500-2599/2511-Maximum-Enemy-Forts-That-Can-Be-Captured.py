from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_forts = 0
        n = len(forts)

        for i in range(n):
            if forts[i] == 1 or forts[i] == -1:
                for j in range(i + 1, n):
                    if forts[j] == 1 or forts[j] == -1:
                        if forts[i] != forts[j]:
                            valid = True
                            for k in range(i + 1, j):
                                if forts[k] != 0:
                                    valid = False
                                    break
                            
                            if valid:
                                max_forts = max(max_forts, j - i - 1)
                        
                        break
        return max_forts