class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digits = 0
        t = x
        while t > 0:
            digits += t % 10
            t //= 10

        if x % digits == 0:
            return digits
        else:
            return -1