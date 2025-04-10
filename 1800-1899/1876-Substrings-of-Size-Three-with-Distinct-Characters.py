class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s) - 2):
            sub = s[i:i+3]
            l = set(sub)
            if len(l) == 3:
                c += 1

        return c