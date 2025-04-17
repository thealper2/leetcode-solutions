class Solution:
    def splitNum(self, num: int) -> int:
        if num == 0:
            return 0
        
        digit_counts = [0] * 10
        temp = num
        while temp > 0:
            digit = temp % 10
            digit_counts[digit] += 1
            temp = temp // 10
        
        num1 = 0
        num2 = 0
        turn = 0
        
        for digit in range(10):
            while digit_counts[digit] > 0:
                if turn == 0:
                    num1 = num1 * 10 + digit
                else:
                    num2 = num2 * 10 + digit
                
                digit_counts[digit] -= 1
                turn ^= 1
        
        return num1 + num2