class Solution:
    def hammingWeight(self, n: int) -> int:
        result = []
        while n >= 1:
            result.append(n % 2)
            n //= 2

        return sum(result)