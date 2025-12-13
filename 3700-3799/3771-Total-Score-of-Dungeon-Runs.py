from typing import List


class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        pref = 0
        seen = [0]
        ans = 0

        for i in range(n):
            pref += damage[i]
            limit = pref - (hp - requirement[i])
            idx = bisect.bisect_left(seen, limit)
            ans += len(seen) - idx
            bisect.insort(seen, pref)

        return ans
