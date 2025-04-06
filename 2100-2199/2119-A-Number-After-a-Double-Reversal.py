class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverse_number(n: int):
            reversed_num = 0
            while n > 0:
                digit = n % 10
                reversed_num = reversed_num * 10 + digit
                n = n // 10
            return reversed_num
        
        reversed1 = reverse_number(num)
        reversed2 = reverse_number(reversed1)
        return reversed2 == num