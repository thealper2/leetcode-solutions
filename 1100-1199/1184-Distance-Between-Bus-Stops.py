from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a = min(start, destination)
        b = max(start, destination)

        c1 = sum(distance[a:b])
        c2 = sum(distance) - c1
        return min(c1, c2)
