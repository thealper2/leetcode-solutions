class Solution:
    def maxSumOfSquares(self, num: int, sum_: int) -> str:
        if sum_ > 9 * num or sum_ < 0:
            return ""

        result = ['0'] * num
        remaining_sum = sum_

        for i in range(num):
            digit = min(9, remaining_sum)
            result[i] = str(digit)
            remaining_sum -= digit

        if remaining_sum > 0:
            return ''

        return ''.join(result)
