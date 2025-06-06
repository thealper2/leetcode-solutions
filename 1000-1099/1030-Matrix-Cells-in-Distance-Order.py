from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cells = [(r, c) for r in range(rows) for c in range(cols)]
        cells.sort(key=lambda x: (abs(x[0] - rCenter) + abs(x[1] - cCenter), x[0], x[1]))
        return [list(cell) for cell in cells]
