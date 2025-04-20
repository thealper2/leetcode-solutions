from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank_dict = {v: i + 1 for i, v in enumerate(sorted_unique)}
        return [rank_dict[num] for num in arr]