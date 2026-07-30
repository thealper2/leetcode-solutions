class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > 9 * n:
            return -1

        if s == 0:
            return 0

        result = []
        remaining = s

        for i in range(n):
            for digit in range(9, -1, -1):
                if remaining - digit >= 0 and remaining - digit <= 9 * (n - i - 1):
                    result.append(str(digit))
                    remaining -= digit
                    break

        return int(''.join(result))
        
