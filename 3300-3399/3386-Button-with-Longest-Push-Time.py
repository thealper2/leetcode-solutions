from collections import defaultdict
from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        max_time = events[0][1]
        max_button = events[0][0]
        n = len(events)

        for i in range(1, n):
            time = events[i][1] - events[i - 1][1]
            if time > max_time or (time == max_time and events[i][0] < max_button):
                max_time = time
                max_button = events[i][0]
        
        return max_button
