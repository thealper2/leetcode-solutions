class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        is_dividend_neg = 1
        is_divisor_neg = 1

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        if dividend < 0:
            is_dividend_neg = -1
            dividend = -dividend

        if divisor < 0:
            is_divisor_neg = -1
            divisor = -divisor

        while dividend >= divisor:
            temp_divisor = divisor
            temp_count = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                temp_count <<= 1

            dividend -= temp_divisor
            count += temp_count

        result = count * is_divisor_neg * is_dividend_neg
        
        if result < -2 ** 31:
            return -2 ** 31
            
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        
        return result