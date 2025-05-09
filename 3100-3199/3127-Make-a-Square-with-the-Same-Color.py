from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for x in range(2):
            for y in range(2):
                temp = [
                    grid[x][y],
                    grid[x+1][y],
                    grid[x][y+1],
                    grid[x+1][y+1]
                ]

                count = {'B': 0, 'W': 0}
                for color in temp:
                    count[color] += 1

                if count['B'] >= 3 or count['W'] >= 3:
                    return True
                
        return False