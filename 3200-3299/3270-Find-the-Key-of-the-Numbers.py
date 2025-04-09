class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        result = 0
        i = 0
        while num1 > 0 and num2 > 0 and num3 > 0:
            t = min(num1 % 10, num2 % 10, num3 % 10)
            result += (10 ** i) * t
            num1 //= 10
            num2 //= 10
            num3 //= 10
            i += 1

        return result