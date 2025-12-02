from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = 0
        for truck in 'MPG':
            travel_time = 0
            for i in range(len(garbage)):
                if i > 0:
                    travel_time += travel[i - 1]

                if truck in garbage[i]:
                    total += garbage[i].count(truck)
                    total += travel_time
                    travel_time = 0

        return total
