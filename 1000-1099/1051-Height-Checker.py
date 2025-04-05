from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != s[i]:
                count += 1

        return count