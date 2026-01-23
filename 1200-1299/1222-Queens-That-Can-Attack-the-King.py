from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = {(x, y) for x, y in queens}
        kx, ky = king
        result = []
        
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        
        for dx, dy in directions:
            x, y = kx, ky
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if 0 <= x < 8 and 0 <= y < 8:
                    if (x, y) in queen_set:
                        result.append([x, y])
                        break
                else:
                    break
        
        return result
