from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        total = 0
        length = 1

        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                length += 1
            else:
                total += length * (length + 1) // 2
                length = 1

        total += length * (length + 1) // 2
        return total
