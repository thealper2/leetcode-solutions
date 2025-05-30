from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        n = len(s)
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                if count[s[i]] == int(s[i]) and count[s[i + 1]] == int(s[i + 1]):
                    return s[i] + s[i + 1]

        return ''
