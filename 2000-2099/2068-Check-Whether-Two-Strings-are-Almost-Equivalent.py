class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq = {}

        for c1, c2 in zip(word1, word2):
            freq[c1] = freq.get(c1, 0) + 1
            freq[c2] = freq.get(c2, 0) - 1

        for v in freq.values():
            if abs(v) > 3:
                return False
            
        return True