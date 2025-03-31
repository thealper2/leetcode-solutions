class Solution:
    def count_set_bits(self, num: int) -> int:
        count = 0
        while num:
            count += num & 1
            num >>= 1

        return count

    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False

        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        result = 0

        for num in range(left, right + 1):
            count = self.count_set_bits(num)

            if self.is_prime(count):
                result += 1

        return result
