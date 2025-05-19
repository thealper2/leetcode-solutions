class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"

        while len(s) < k:
            for c in s:
                next_ord = ord(c) + 1
                if next_ord > 122:
                    next_ord = 97

                s += chr(next_ord)

        return s[k - 1]