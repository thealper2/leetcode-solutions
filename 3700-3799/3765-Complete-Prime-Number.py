class Solution:
    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False

        return True

    def completePrime(self, num: int) -> bool:
        s = str(num)
        n = len(s)
        for i in range(1, n + 1):
            prefix = int(s[:i])
            suffix = int(s[n - i:])

            if not self.is_prime(prefix) or not self.is_prime(suffix):
                return False

        return True
