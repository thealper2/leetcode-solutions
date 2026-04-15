class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        total = 0

        for num in nums:
            i = 0
            while 10**i <= num:
                d = num // 10**i % 10
                if d == digit:
                    total += 1

                i += 1

        return total
