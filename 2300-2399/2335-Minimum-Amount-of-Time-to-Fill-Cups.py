from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        a, b, c = sorted(amount)
        return c if c >= a + b else (a + b + c + 1) // 2