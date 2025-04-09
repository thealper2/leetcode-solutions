class Solution:
    def minLength(self, s: str) -> int:
        f = True
        while f:
            if "AB" in s:
                s = s.replace('AB', '')

            elif "CD" in s:
                s = s.replace('CD', '')

            else:
                f = False

        return len(s)