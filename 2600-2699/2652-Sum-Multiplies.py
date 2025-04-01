class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for num in range(1, n + 1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                total += num
        return total