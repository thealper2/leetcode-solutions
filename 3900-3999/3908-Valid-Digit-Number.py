class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        i = 0
        is_in = False
        while 10**i <= n:
            d = n // 10**i % 10
            i += 1
            if d == x:
                is_in = True

        return is_in and d != x