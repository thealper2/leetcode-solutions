from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        n = len(points)
        
        for i in range(n - 2):
            x1, y1 = points[i]
            for j in range(i+1, n-1):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    current_area = abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
                    if (current_area > max_area):
                        max_area = current_area
            
        return max_area