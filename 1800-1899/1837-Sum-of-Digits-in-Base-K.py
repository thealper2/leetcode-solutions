class Solution:
    def sumBase(self, n: int, k: int) -> int:
        s = []

        while n > 0:
            r = n % k
            if r >= 10:
                r = 65 + r - 10
                
            s.append(r)
            n = n // k

        return sum(s)