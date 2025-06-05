from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 1
        while a <= n // 2:
            b = n - a
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]

            a += 1
    
        return [a, n - a]
