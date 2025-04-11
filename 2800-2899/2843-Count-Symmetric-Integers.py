class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            num_str = str(num)
            length = len(num_str)
            if length % 2 != 0:
                continue

            half = length // 2
            first_half = num_str[:half]
            second_half = num_str[half:]
            sum_first = sum(int(digit) for digit in first_half)
            sum_second = sum(int(digit) for digit in second_half)
            if sum_first == sum_second:
                count += 1
        
        return count
