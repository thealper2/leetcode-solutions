from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        e = o = 0
        i = 0
        while n > 0:
            d = n % 2
            n //= 2
            if d == 1:
                if i % 2 == 0:
                    e += 1
                else:
                    o += 1

            i += 1

        return [e, o]