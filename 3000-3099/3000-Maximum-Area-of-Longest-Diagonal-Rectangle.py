import math
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal_sq = -1
        max_area = 0
        
        for length, width in dimensions:
            diagonal_sq = length ** 2 + width ** 2
            area = length * width
            
            if diagonal_sq > max_diagonal_sq:
                max_diagonal_sq = diagonal_sq
                max_area = area
                
            elif diagonal_sq == max_diagonal_sq and area > max_area:
                max_area = area
                
        return max_area