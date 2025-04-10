class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        c = 0
        while num1 != 0 and num2 != 0:
            if num1 < num2:
                c += num2 // num1
                num2 = num2 % num1
            elif num2 < num1:
                c += num1 // num2
                num1 = num1 % num2
            else:
                num1 = 0
                num2 = 0
                c += 1
        return c