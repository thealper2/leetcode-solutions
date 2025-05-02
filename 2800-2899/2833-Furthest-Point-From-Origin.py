class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count = moves.count('L')
        r_count = moves.count('R')
        n = len(moves)
        return n - (l_count + r_count) + abs(l_count - r_count)