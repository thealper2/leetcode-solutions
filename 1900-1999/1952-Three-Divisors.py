import math


class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        
        root = math.isqrt(n)
        if root * root != n:
            return False
        
        if root < 2:
            return False

        for i in range(2, math.isqrt(root) + 1):
            if root % i == 0:
                return False

        return True