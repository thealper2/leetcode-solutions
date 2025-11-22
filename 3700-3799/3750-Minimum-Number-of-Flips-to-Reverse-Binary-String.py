class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        L = len(s)
        flips = 0
        
        for i in range(L // 2):
            if s[i] != s[L - 1 - i]:
                flips += 2
        
        return flips
