from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        p = 0
        while 10**p <= n:
            d = (10 ** p) * (n // 10**p % 10)
            if d != 0:
                result.append(d)
    
            p += 1

        return result[::-1]
