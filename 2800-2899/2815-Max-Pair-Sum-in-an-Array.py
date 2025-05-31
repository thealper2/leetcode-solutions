from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        digit_groups = {}
        
        for num in nums:
            if num == 0:
                max_digit = 0
            else:
                temp = abs(num)
                max_digit = 0
                while temp > 0:
                    digit = temp % 10
                    if digit > max_digit:
                        max_digit = digit
                    temp //= 10
            
            if max_digit in digit_groups:
                digit_groups[max_digit].append(num)
            else:
                digit_groups[max_digit] = [num]
        
        max_total = -1
        
        for digit, numbers in digit_groups.items():
            if len(numbers) >= 2:
                numbers.sort(reverse=True)
                current_sum = numbers[0] + numbers[1]
                if current_sum > max_total:
                    max_total = current_sum
        
        return max_total