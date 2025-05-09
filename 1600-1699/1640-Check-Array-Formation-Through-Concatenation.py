from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        piece_map = { piece[0]: piece for piece in pieces }

        result = []
        for num in arr:
            result += piece_map.get(num, [])

        return result == arr
