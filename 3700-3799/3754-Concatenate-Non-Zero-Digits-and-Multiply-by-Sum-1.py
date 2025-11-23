class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = []
        i = 0
        while 10**i <= n:
            d = n // 10**i % 10
            if d != 0:
                digits.append(d)
            i += 1

        if not digits:
            return 0

        total = sum(digits)
        new_n = int(''.join(map(str, digits[::-1])))
        return new_n * total
