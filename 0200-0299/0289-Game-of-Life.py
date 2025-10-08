from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        
        def count_live_neighbors(r, c):
            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] in (1, 2):
                        live_neighbors += 1
            return live_neighbors
        
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2
                else:
                    if live_neighbors == 3:
                        board[r][c] = 3
        
        for r in range(rows):
            for c in range(cols):
                board[r][c] %= 2
