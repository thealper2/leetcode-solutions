class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last_occurrence = -1
        n = len(number)
        
        for i in range(n):
            if number[i] == digit:
                last_occurrence = i
                if i < n - 1 and number[i + 1] > digit:
                    return number[:i] + number[i + 1:]

        return number[:last_occurrence] + number[last_occurrence + 1:]