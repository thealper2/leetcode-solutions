from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        result = [0] * n
        result[0] = cost[0]
        for i in range(1, n):
            result[i] = min(result[i - 1], cost[i])

        return result