from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_types = len(set(candyType))
        max_allowed = len(candyType) // 2
        return min(unique_types, max_allowed)