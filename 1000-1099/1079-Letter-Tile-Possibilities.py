from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        unique_sequences = set()
        n = len(tiles)
        
        for length in range(1, n + 1):
            for perm in permutations(tiles, length):
                unique_sequences.add(perm)
                
        return len(unique_sequences)
