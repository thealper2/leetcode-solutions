class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = num // 10
            c = num % 10
            num = s + c

        return num
