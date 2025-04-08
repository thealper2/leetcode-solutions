from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0
        while grid and grid[0]:
            t = []
            for r in grid:
                m = max(r)
                t.append(m)
                r.remove(m)

            print(t)
            result += max(t)

        return result
