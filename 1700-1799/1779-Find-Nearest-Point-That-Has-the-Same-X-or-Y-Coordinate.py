from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        result_index = -1
        
        for index, point in enumerate(points):
            a, b = point
            if a == x or b == y:
                distance = abs(x - a) + abs(y - b)
                if distance < min_distance:
                    min_distance = distance
                    result_index = index
                        
        return result_index