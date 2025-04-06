from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            digits = []
            if num == 0:
                digits.append(0)
            else:
                while num > 0:
                    digits.append(num % 10)
                    num = num // 10
                digits = digits[::-1]
                
            result.extend(digits)
        return result