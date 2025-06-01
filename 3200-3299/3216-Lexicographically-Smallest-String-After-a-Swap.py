class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(map(int, s))
        n = len(s)
        for i in range(n - 1):
            if s[i] % 2 == s[i + 1] % 2 and s[i] > s[i + 1]:
                s[i], s[i + 1] = s[i + 1], s[i]
                break

        return ''.join(map(str, s))