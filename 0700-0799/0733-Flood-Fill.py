from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        m, n = len(image), len(image[0])
        original_color = image[sr][sc]
        stack = [(sr, sc)]
        
        while stack:
            r, c = stack.pop()
            if 0 <= r < m and 0 <= c < n and image[r][c] == original_color:
                image[r][c] = color
                if r > 0:
                    stack.append((r - 1, c))
                if r < m - 1:
                    stack.append((r + 1, c))
                if c > 0:
                    stack.append((r, c - 1))
                if c < n - 1:
                    stack.append((r, c + 1))
        
        return image