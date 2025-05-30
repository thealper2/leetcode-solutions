from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k and digits[i] != 0 and digits[k] % 2 == 0:
                        number = digits[i] * 100 + digits[j] * 10 + digits[k]
                        numbers.add(number)
        return len(numbers)
