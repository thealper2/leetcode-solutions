from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            x = max(stones)
            stones.remove(x)

            y = max(stones)
            if x == y:
                stones.remove(y)
            elif x != y:
                stones.remove(y)
                stones.append(abs(y - x))

        return stones[0] if len(stones) > 0 else 0