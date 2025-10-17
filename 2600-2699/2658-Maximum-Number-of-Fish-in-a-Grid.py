from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        max_fish = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    fish_count = 0
                    stack = [(i, j)]
                    grid[i][j] *= -1
                    
                    while stack:
                        r, c = stack.pop()
                        fish_count += abs(grid[r][c])
                        
                        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                stack.append((nr, nc))
                                grid[nr][nc] *= -1
                    
                    max_fish = max(max_fish, fish_count)
        
        return max_fish
