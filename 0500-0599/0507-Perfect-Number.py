import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        sum_divisors = 1
        sqrt_num = int(math.sqrt(num)) + 1

        for i in range(2, sqrt_num):
            if num % i == 0:
                sum_divisors += i
                corresponding_divisor = num // i
                if corresponding_divisor != i:
                    sum_divisors += corresponding_divisor

        return sum_divisors == num