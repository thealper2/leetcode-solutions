class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        num = 0
        is_neg = 1
        is_first = True
        digits_started = False

        for i in range(n):
            if s[i] == ' ' and not digits_started:
                continue
                
            elif s[i] == '-' and is_first:
                is_neg = -1
                is_first = False
                digits_started = True
                
            elif s[i] == '+' and is_first:
                is_first = False
                digits_started = True
                
            elif s[i].isdigit():
                num = num * 10 + int(s[i])
                is_first = False
                digits_started = True
                
            else:
                break

        num *= is_neg
        num = max(-2**31, min(num, 2**31 - 1))
        return num