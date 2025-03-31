class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        h = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0 or h:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            total = digit1 + digit2 + h
            h = total // 10
            result.append(str(total % 10))
            i -= 1
            j -= 1

        return "".join(result[::-1])
