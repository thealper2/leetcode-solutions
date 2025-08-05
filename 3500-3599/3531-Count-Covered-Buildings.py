from collections import defaultdict
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_map = defaultdict(list)
        col_map = defaultdict(list)

        for x, y in buildings:
            row_map[y].append(x)
            col_map[x].append(y)

        for y in row_map:
            row_map[y].sort()
            
        for x in col_map:
            col_map[x].sort()

        covered = 0

        for x, y in buildings:
            row = row_map[y]
            col = col_map[x]

            idx_row = bisect.bisect_left(row, x)
            idx_col = bisect.bisect_left(col, y)

            has_left = idx_row > 0
            has_right = idx_row < len(row) - 1
            has_above = idx_col > 0
            has_below = idx_col < len(col) - 1

            if has_left and has_right and has_above and has_below:
                covered += 1

        return covered
