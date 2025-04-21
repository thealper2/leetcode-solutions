from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        r = 0
        for i in range(n):
            if i <= k:
                r += min(tickets[i], tickets[k])
            else:
                r += min(tickets[i], tickets[k] - 1)

        return r