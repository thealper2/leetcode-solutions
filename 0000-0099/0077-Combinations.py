from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [_ for _ in range(1, n + 1)]
        stack = [(0, [])]
        result = []

        while stack:
            index, current = stack.pop()

            if len(current) == k:
                result.append(current)
                continue

            if index >= len(arr):
                continue

            stack.append((index + 1, current + [arr[index]]))
            stack.append((index + 1, current))

        return result