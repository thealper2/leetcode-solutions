from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        trusted_by = [0] * (n + 1)
        trusts_someone = [False] * (n + 1)
        
        for a, b in trust:
            trusts_someone[a] = True
            trusted_by[b] += 1
        
        for i in range(1, n + 1):
            if trusted_by[i] == n - 1 and not trusts_someone[i]:
                return i
        
        return -1
