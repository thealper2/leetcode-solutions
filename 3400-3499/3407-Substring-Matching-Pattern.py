class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        for c in p:
            if c != '*' and c not in s:
                return False

        n = len(s)
        for i in range(n):
            for j in range(i, n):
                t = p.replace('*', s[i:j])
                if t in s:
                    return True

        return False
