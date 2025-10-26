class Solution:
    def removeZeros(self, n: int) -> int:
        result = []
        i = 0
        while 10**i <= n:
            d = n // 10**i % 10
            if d != 0:
                result.append(str(d))

            i += 1

        return int(''.join(result[::-1]))
