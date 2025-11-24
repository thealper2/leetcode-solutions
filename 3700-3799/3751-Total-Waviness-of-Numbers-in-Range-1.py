class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for num in range(num1, num2 + 1):
            digits = str(num)
            n = len(digits)
            if n < 3:
                continue

            for i in range(1, n - 1):
                if digits[i] > digits[i - 1] and digits[i] > digits[i + 1]:
                    total += 1

                elif digits[i] < digits[i - 1] and digits[i] < digits[i + 1]:
                    total += 1

        return total
