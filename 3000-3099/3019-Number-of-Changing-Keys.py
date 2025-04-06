class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        count = 0

        for c in range(1, n):
            if abs(ord(s[c]) - ord(s[c - 1])) != 32 and (s[c] != s[c - 1]):
                count += 1

        return count