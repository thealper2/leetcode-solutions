class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        if x < 0:
            x = abs(x)
            is_neg = True
        
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10
        
        if is_neg:
            reversed_num = -reversed_num
        
        if reversed_num < -2 ** 31 or reversed_num > 2 ** 31 - 1:
            return 0
        
        return reversed_num