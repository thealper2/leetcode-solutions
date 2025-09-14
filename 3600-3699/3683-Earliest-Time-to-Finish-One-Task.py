from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        min_t = float('inf')
        for task in tasks:
            t = task[0] + task[1]
            if t < min_t:
                min_t = t

        return min_t
