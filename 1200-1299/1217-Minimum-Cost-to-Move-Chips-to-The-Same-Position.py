from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        e = 0
        o = 0
        for p in position:
            if p % 2 == 0:
                e += 1
            else:
                o += 1

        return min(e, o)