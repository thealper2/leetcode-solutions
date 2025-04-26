from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = sum(apple)
        capacity.sort(reverse=True)
        count = 0

        for c in capacity:
            count += 1
            n -= c
            if n <= 0:
                break

        return count