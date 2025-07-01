from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    stack = [(i, j, 0, set())]
                    while stack:
                        x, y, k, visited = stack.pop()
                        if k == len(word):
                            return True
                        
                        if x < 0 or x >= rows or y < 0 or y >= cols or (x, y) in visited or board[x][y] != word[k]:
                            continue

                        visited.add((x, y))
                        stack.append((x + 1, y, k + 1, visited.copy()))
                        stack.append((x - 1, y, k + 1, visited.copy()))
                        stack.append((x, y + 1, k + 1, visited.copy()))
                        stack.append((x, y - 1, k + 1, visited.copy()))
                        
        return False
