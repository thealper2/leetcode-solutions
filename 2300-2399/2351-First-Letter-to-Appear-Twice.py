class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
                if d[c] == 2:
                    return c
                
        return ""