from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        inside = []

        for query in queries:
            xj, yj, rj = query
            count = 0

            for point in points:
                xi, yi = point
                distance = (xi - xj) ** 2 + (yi - yj) ** 2
                if distance <= rj ** 2:
                    count += 1

            inside.append(count)

        return inside
