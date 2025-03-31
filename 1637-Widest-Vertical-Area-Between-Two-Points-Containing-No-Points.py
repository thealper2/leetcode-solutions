from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coords = sorted([point[0] for point in points])
        
        max_width = 0
        for i in range(1, len(x_coords)):
            width = x_coords[i] - x_coords[i-1]
            if width > max_width:
                max_width = width
        
        return max_width