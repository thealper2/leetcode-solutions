class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        result = 0
        idx = 0
        while n >= 1:
            d = n % 2
            print(d)
            n //= 2
            result += (2 ** idx) * (1 - d)
            idx += 1

        return result