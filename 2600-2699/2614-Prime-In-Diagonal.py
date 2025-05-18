from typing import List
import math


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
            n = len(nums)
            primes = set()

            for i in range(n):
                a = nums[i][i]
                if a > 1:
                    is_prime = True
                    for j in range(2, int(math.sqrt(a)) + 1):
                        if a % j == 0:
                            is_prime = False
                            break
                    if is_prime:
                        primes.add(a)

                b = nums[i][n - 1 - i]
                if b > 1:
                    is_prime = True
                    for j in range(2, int(math.sqrt(b)) + 1):
                        if b % j == 0:
                            is_prime = False
                            break
                    if is_prime:
                        primes.add(b)

            return max(primes) if primes else 0