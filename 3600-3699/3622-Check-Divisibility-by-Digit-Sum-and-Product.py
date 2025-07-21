class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_product = 1
        digit_sum = 0
        i = 0

        while 10 ** i <= n:
            d = n // 10 ** i % 10
            digit_product *= d
            digit_sum += d
            i += 1

        total = digit_sum + digit_product
        return n % total == 0
