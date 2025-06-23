from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] in row:
                    return False
                elif board[i][j] != '.':
                    row.add(board[i][j])

        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] in col:
                    return False
                elif board[j][i] != '.':
                    col.add(board[j][i])

        starts = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]

        for i, j in starts:
            sub = set()
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    item = board[r][c]
                    if board[r][c] in sub:
                        return False
                    elif board[r][c] != '.':
                        sub.add(board[r][c])
        
        return True