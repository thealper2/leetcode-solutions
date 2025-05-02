class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0
        
        binary_n = []
        binary_k = []

        while n >= 1 or k >= 1:
            binary_n.append(n % 2)
            n //= 2

            binary_k.append(k % 2)
            k //= 2
        
        count = 0
        for a, b in zip(binary_n, binary_k):
            if a == 1 and b == 0:
                count += 1
            elif a == 0 and b == 1:
                return -1

        return count