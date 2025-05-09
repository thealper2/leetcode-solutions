class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        moves = 0
        idx = 0

        while idx < n:
            if s[idx] == 'X':
                moves += 1
                idx += 3
            else:
                idx += 1

        return moves