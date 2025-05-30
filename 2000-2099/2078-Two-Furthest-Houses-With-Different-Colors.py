from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_dist = 0
        first_color = colors[0]
        last_color = colors[-1]

        for i in range(n):
            if colors[i] != last_color:
                max_dist = max(max_dist, n - 1 - i)
                break
                
        for i in range(n - 1, -1, -1):
            if colors[i] != first_color:
                max_dist = max(max_dist, i)
                break

        return max_dist
