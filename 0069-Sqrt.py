class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        x1 = x / 2
        while True:
            x2 = (x1 + x / x1) / 2
            if x1 == x2:
                break

            x1 = x2

        return int(x1)
