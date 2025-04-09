class Solution:
    def minimizedStringLength(self, s: str) -> int:
        r = []
        for c in s:
            if c not in r:
                r.append(c)

        return len(r)