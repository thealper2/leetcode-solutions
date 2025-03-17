class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = []
        while n >= 1:
            result.append(n % 2)
            n //= 2

        return sum(result) == 1
