class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            t = ""
            for i in range(len(s) - 1):
                d1 = int(s[i])
                d2 = int(s[i + 1])
                t += str((d1 + d2) % 10)
            
            s = t

        return s[0] == s[1]