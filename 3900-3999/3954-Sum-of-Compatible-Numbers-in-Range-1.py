class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        total = 0
        for x in range(n - k, n + k + 1):
            if x > 0 and (n & x) == 0:
                total += x

        return total
