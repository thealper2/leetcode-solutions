from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        total = 0
        n = len(cost)
        for i in range(n):
            if i % 3 != 2:
                total += cost[i]

        return total