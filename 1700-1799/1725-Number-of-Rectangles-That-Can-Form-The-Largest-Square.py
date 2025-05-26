from typing import List
from collections import defaultdict


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = defaultdict(int)
        max_len = 0

        for rectangle in rectangles:
            t = min(rectangle)
            count[t] += 1
            if t > max_len:
                max_len = t

        return count[max_len]