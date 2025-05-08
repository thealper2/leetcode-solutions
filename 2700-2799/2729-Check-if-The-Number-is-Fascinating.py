class Solution:
    def isFascinating(self, n: int) -> bool:
        word = str(n) + str(n * 2) + str(n * 3)
        if '0' in word:
            return False

        digits = {}
        sum_digits = 0
        for c in word:
            if c not in digits:
                digits[c] = 1
                sum_digits += int(c)
            else:
                return False
        
        return sum_digits == 45