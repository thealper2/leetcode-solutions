class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        result = []
        while n >= 1:
            result.append(n % 3)
            n //= 3

        return sum(result) == 1
