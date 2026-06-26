class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = 0
        square_sum = 0
        i = 0

        while 10**i <= n:
            d = n // 10**i % 10
            digit_sum += d
            square_sum += d ** 2 
            i += 1

        return square_sum - digit_sum >= 50
