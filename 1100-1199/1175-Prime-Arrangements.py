import math

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        def is_prime(num):
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
            return True

        prime_count = 0
        for num in range(1, n + 1):
            if is_prime(num):
                prime_count += 1
        non_prime_count = n - prime_count
        return (math.factorial(prime_count) * math.factorial(non_prime_count)) % MOD