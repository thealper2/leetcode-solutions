class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        rev_n = int(str(n)[::-1])
        l, r = min(rev_n, n), max(rev_n, n)

        if r < 2:
            return 0

        is_prime = [True] * (r + 1)
        is_prime[0] = is_prime[1] = False

        i = 2
        while i * i <= r:
            if is_prime[i]:
                for j in range(i * i, r + 1, i):
                    is_prime[j] = False

            i += 1

        total = 0
        for num in range(l, r + 1):
            if is_prime[num]:
                total += num

        return total