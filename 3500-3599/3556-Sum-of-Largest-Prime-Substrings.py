class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        n = len(s)
        primes = set()
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                num_str = s[i:j]
                if len(num_str) > 1 and num_str[0] == '0':
                    continue
                
                num = int(num_str)
                if num < 2:
                    continue

                is_prime = True
                for k in range(2, int(num**0.5) + 1):
                    if num % k == 0:
                        is_prime = False
                        break
                
                if is_prime:
                    primes.add(num)
        
        if not primes:
            return 0

        primes = sorted(primes)
        return sum(primes[-3:])
