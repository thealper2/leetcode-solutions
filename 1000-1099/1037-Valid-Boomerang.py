from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        c1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        c2 = (points[2][0] - points[0][0], points[2][1] - points[0][1])
        return (c1[0] * c2[1] - c1[1] * c2[0]) != 0