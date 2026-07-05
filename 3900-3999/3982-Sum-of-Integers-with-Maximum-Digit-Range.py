class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_digit_range = 0
        max_sum = 0
        for num in nums:
            digits = [int(d) for d in str(num)]
            max_digit, min_digit = max(digits), min(digits)
            digit_range = max_digit - min_digit
            if digit_range > max_digit_range:
                max_digit_range = digit_range
                max_sum = num
            elif digit_range == max_digit_range:
                max_sum += num

        return max_sum
