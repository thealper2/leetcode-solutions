from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def mod_pow(x, n):
            result = 1
            x %= 1337
            while n:
                if n & 1:
                    result = (result * x) % 1337

                x = (x ** 2) % 1337
                n //= 2

            return result

        res = 1
        for d in b:
            res = (mod_pow(res, 10) * mod_pow(a, d)) % 1337

        return res
