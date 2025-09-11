from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1

        result = 0
        for v in freq.values():
            if v % 2 == 0:
                result += 2
            else:
                result += 1

        return result
